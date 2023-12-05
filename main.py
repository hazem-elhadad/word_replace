import time

from word_replace.replacer import document_generating
from constants import example_obj
from isolated_run import isolate_run

if __name__ == '__main__':
    
    # variables = {        
    #     "file_source": r"E:\\table_hd_ft\\word_replace_service\\templates\\check_List.doc",
    #     "file_destination": r"E:\\table_hd_ft\\word_replace_service\\results\\check_List.docx",
    #     "compress": 1,
    #     "pdf": 1,
    #     "data":{
    #         "DAY_NAME": "SUN",
    #         "LIMIT":'10000',
    #         "YEARS" :"9999999",
    #         "ORR" :"10101010",
    #         "CMTE_CODE" :"xx88yyzz",
    #         "APRVL_DATE":"8/12/1997",
    #         "SIGNERS" :"Hazem + Omar",
    #         "CURR_DATE": "13/11/2023",
    #         "ASSET_DT1" :"HAZEM Elhadad",
    #         "CMPNY_ADDRESS": "6th October",
    #         "CMPNY_SIGNERS": "Pixel",
    #         "CNTRCT_NO": "123",
    #         "CLNT_NAME": "Eng mahmoud",
    #         "LEGAL_ENTITY": "RTest 123",
    #         "TRADE_RG_OFFICE": "TRD RG",
    #         "TRADE_RG_NO": "TRD RG ##",
    #         "TRADE_RG_DATE": "13/11/2023",
    #         "TAX_CARD_NO": "TX CR ##",
    #         "CLNT_ADDRESS": "el nozha",
    #         "CLNT_SIGNERS": "AnasOS20",
    #         "TRNS_DATE": "10/12/2023",
    #         "TRAFFIC_NAME": "Test Traffic Name",
    #         "RVWD": "Test RVWD",
    #         "TAFWEED": "Test TAFWEED",
    #         "ASSET_DESCR1": "example@example.com",
    #         "ASSET_DT1": "03 Jan, 2021",
    #         "PERIOD": "PERIOD test",
    #         "CMPNY_NAME_AR": "تست",
    #         "EXPIRY": "7,000",           
    #     },
    #     "table_data":{
    #         "SOME_DATA": {
    #             "align": "L", # L, R, C, N  
    #             "border": 1, # 1, 0             
    #             "footer": 0, # 1,0               
    #             "header": [
    #                     { 'NAME': 'Asset', 'WIDTH': 100, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': "TOP"}, 
    #                     { 'NAME': 'Cost', 'WIDTH':100, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': "BOTTOM"}],
    #             "data":[  
    #                 [
    #                     { 'VALUE': 'Asset1', 'SORT': 1, 'MERGE_WITH_CELL': 1, 'VALIGN': None, 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset2', 'SORT': 1, 'MERGE_WITH_CELL': 1, 'VALIGN': None, 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset3', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None}
    #                 ],
    #                 [
    #                     { 'VALUE': 'Asset4', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset5', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset6', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset6', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset7', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None}


    #                 ],                    
    #             ]},  
    #         "TABLE_DATA": {
    #             "align": "L", # L, R, C, N  
    #             "border": 0, # 1, 0             
    #             "footer": 0, # 1,0     
    #             "header": [],
    #             "data":[  
    #                 [
    #                     { 'VALUE': 'Asset1', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset2', 'SORT': 1, 'MERGE_WITH_CELL': 2, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                 ],
    #                 [
    #                     { 'VALUE': 'Asset4', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset5', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},
    #                     { 'VALUE': 'Asset6', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': "TOP", 'HALIGN': None, 'PADDING': None},  
    #                 ],                    
    #             ]},   
    #         "ANOTHER_DATA": {
    #             "align": "L", # L, R, C, N  
    #             "border": 0, # 1, 0             
    #             "footer": 0, # 1,0 
    #             "header": [],              
    #             "data":[  
    #                 [
    #                     { 'VALUE': 'Walalal', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': None, 'HALIGN': 'RIGHT', 'PADDING': None},
    #                     { 'VALUE': 'Asset2', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': None, 'HALIGN': 'LEFT', 'PADDING': None},
    #                     { 'VALUE': 'Asset3', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': None, 'HALIGN': 'RIGHT', 'PADDING': None}
    #                 ],
    #                 [
    #                     { 'VALUE': 'Asset4', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': None, 'HALIGN': 'RIGHT', 'PADDING': None},
    #                     { 'VALUE': 'Asset5', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': None, 'HALIGN': 'CENTER', 'PADDING': None},
    #                     { 'VALUE': 'Asset6', 'SORT': 1, 'MERGE_WITH_CELL': 0, 'VALIGN': None, 'HALIGN': 'RIGHT', 'PADDING': None}
    #                 ],                    
    #             ]
    #         },                                             
    #     }}    
        
    start = time.time()     
    document_generating(example_obj)
    end = time.time()    
    print(end - start)