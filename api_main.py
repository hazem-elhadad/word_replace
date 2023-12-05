import os
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
import cx_Oracle
from api_constants import query , data_query, table_query, batch_query, table_header_query, table_details_query


app = Flask(__name__)
CORS(app)


oracle_dir = r"C:\Users\omar\Downloads\instantclient-basic-windows.x64-21.3.0.0.0\instantclient_21_3"
# Init Client
cx_Oracle.init_oracle_client(lib_dir=oracle_dir)

# Connect to the Oracle database
con = cx_Oracle.connect('GBLEASE', 'GBLEASE', '192.168.100.19:1521/DB19C', encoding="UTF8", nencoding="UTF8")
#GBLEASE	GBLEASE@//192.168.100.19:1521/DB19C
                        
# Define the directory where the generated files will be saved
file_dir = "generated_files"

# Ensure the directory exists
os.makedirs(file_dir, exist_ok=True)

@app.route('/', methods=['GET'])
def index():   
    # Return the results
    return redirect('/api/status')

@app.route('/api/status', methods=['GET'])
def get_status():   
    # Return the results
    return jsonify({"status": "success", "message": "api is up and running!!"})    
    

"Generate one file, or patch of files"
@app.route('/api/generate_file/<int:id>/', methods=['GET'])
@app.route('/api/generate_file/<int:id>/<isPatch>/', methods=['GET'])
def generate_file(id, isPatch=False):
    
    # Default main query
    main_query = query
    
    try:
        # Convert isPatch to boolean
        isPatch = isPatch.lower() == 'true' if isinstance(isPatch, str) else bool(isPatch)
        
        # Create a cursor
        cur = con.cursor()                

        # Use the batch query if isPatch is true  
        if isPatch:
            main_query = batch_query

        # Pass the id and isPatch parameters to the query
        # If isPAth is true, then the query will return all files with the same BATCH_ID
        cur.execute(main_query, id=id)
        cur.rowfactory = lambda *args: dict(zip([d[0] for d in cur.description], args)) # Convert cursor to dictionary for easier columns access                
        
        # Fetching all rows if isPatch is true
        files_head_data = cur.fetchall()
        
        if len(files_head_data) == 0:
            return jsonify({"status": "failure", "message": "No files found"})
        
                
        # Loop on songle file or batch files
        for item in files_head_data:
            print(item)
            # This is the final object
            response_obj = {}            
            
            hd_id = item['ID']
            
            
            import os
            
            base_dir = r'C:\Users\omar\Desktop\word replace\LEASE_WEB_FILES_GB\contracts'            
            out_dir = r'C:\Users\omar\Desktop\word replace\results'            

            # os.path.join(base_dir, filename)            
            
            response_obj["file_source"] = os.path.join(base_dir, item["SRCFILENAME"])             
            response_obj["file_destination"] = os.path.join(out_dir, item['DESTFILENAME'])             
            # response_obj["file_source"] = item['SRCFILEPATH']
            # response_obj["file_destination"] = item['DESTFILEPATH']
            response_obj["pdf"] = 1 if item['GENPDF'] == 'Y' else 0
            response_obj["compress"] = 0        
            
            # Get Keys and values except tables data (tables data will be fetched later)
            cur.execute(data_query, hd_id=hd_id)
            
            # Create a redable dictionary from the cursor,and convert Oracle LOBs to redable strings
            cur.rowfactory = lambda *args: {d[0]: args[i].read() if isinstance(args[i], cx_Oracle.LOB) else args[i] for i, d in enumerate(cur.description)}
            
            # Fetch all rows
            file_detail_data = cur.fetchall()
            
            response_obj['data'] = {}
            
            for item in file_detail_data:            
                res = {item["NAME"]: item["VALUE"]}            
                response_obj['data'] ={**response_obj['data'], **res}

            # Start Table        
            cur.execute(table_query, hd_id=hd_id)
            cur.rowfactory = lambda *args: dict(zip([d[0] for d in cur.description], args))# Convert cursor to dictionary for easier columns access                        
            
            # Fetch all rows
            tables = cur.fetchall()
            
            # init table data object that will hold all table data
            response_obj['table_data'] = {}
            print(tables)
            
            for table in tables:
                
                file_dt_id = table['ID']
                
                # init table_data key with empty object
                response_obj['table_data'][table['NAME']] = {}

                response_obj['table_data'][table['NAME']]['align'] = 'C'
                response_obj['table_data'][table['NAME']]['border'] = 1
                response_obj['table_data'][table['NAME']]['footer'] = 1
                header_obj = response_obj['table_data'][table['NAME']]['headers'] = []                
                data_obj = response_obj['table_data'][table['NAME']]['data'] = []
            
                
                # Start Table        
                cur.execute(table_header_query, file_dt_id=file_dt_id)                
                cur.rowfactory = lambda *args: dict(zip([d[0] for d in cur.description], args))
                
                # Fetch all rows
                headers = cur.fetchall()                
          
                for header in headers:
                    header_id = header['ID']
                    header_obj.append(header)
                    
                    # Start Table        
                    cur.execute(table_details_query, hd_id=header_id)                
                    cur.rowfactory = lambda *args: dict(zip([d[0] for d in cur.description], args))                    
                    
                    # Details
                    details = cur.fetchall()                    
                    data_obj.append(details)                                                                
                        
                                                                        
        from word_replace.replacer import document_generating
        document_generating(response_obj)  
        return jsonify({"data": response_obj})
        # return jsonify({"status": "success", "message": "File generated successfully", "data": response_obj})
    except Exception as e:
        print(e)
        return jsonify({"status": "failure", "message": str(e)})
    finally:
        cur.close()        

"Generate Batch of files (1 or more)"
@app.route('/api/generate_batch/<int:id>', methods=['GET'])
def generate_batch(id):
    try:
        # Generate a file with a name based on the provided ID
        file_name = f"file_{id}.txt"
        file_path = os.path.join(file_dir, file_name)

        # Create and write some content to the file (you can customize this)
        with open(file_path, 'w') as file:
            file.write(f"This is the content of file {id}.")

        return jsonify({"status": "success", "message": "File generated successfully"})
    except Exception as e:
        return jsonify({"status": "failure", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
