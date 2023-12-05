# Description: This file contains all the constants used in the api.

# Single Template query (single file)
query = """
SELECT 
    FilesHd.id AS Id, 
    FilesHd.name AS DestFileName,
    FilesHd.path AS DestFilePath,  
    Tmplt.name AS SrcFileName,
    Tmplt.path AS SrcFilePath,
    Tmplt.gen_pdf AS GenPdf
FROM   
    gb_template_hd Tmplt, 
    gb_template_files_hd FilesHd
WHERE  
    FilesHd.tmplt_id = Tmplt.id
    AND FilesHd.id = :id
"""

# Batch query (multiple files)
batch_query="""
SELECT 
    FilesHd.id AS Id, 
    FilesHd.name AS DestFileName,
    FilesHd.path AS DestFilePath,  
    Tmplt.name AS SrcFileName,
    Tmplt.path AS SrcFilePath,
    Tmplt.gen_pdf AS GenPdf
FROM   
    gb_template_hd Tmplt, 
    gb_template_files_hd FilesHd
WHERE  
    FilesHd.tmplt_id = Tmplt.id        
    AND FilesHd.batch_id = :id
"""

# Data Query (contains keys and values but not tables data)
data_query="""
select 
    field.id FldId,
    field.type Type,
    field.name Name,
    
    fleDt.hd_id FileId, 
    fleDt.id FldDtId,       
    fleDt.fld_val Value, 
    fleDt.copy_from_file_path CopyFromFilePath,
    nvl(fleDt.table_header,1) TableHeader,
    nvl(fleDt.table_border,1) TableBorder,
    nvl(fleDt.table_footer,0) TableFooter,
    
    nvl(fleDt.table_align,'N') tableAlign
from   
    gb_template_dt field, 
    gb_template_files_hd fleHd, 
    gb_template_files_dt fleDt
where  
    field.id = fleDt.fld_id
    and fleHd.id = fleDt.hd_id
    and field.type <> 'M' --exclude tables as we going to fetch them separately
    and to_char(fleHd.id) = :hd_id
order by 
    fleDt.hd_id,fleDt.id        
"""

# Table Query (contains tables data)
table_query="""
select
    dt.id,
    tmplt_dt.name,
    dt.fld_val
from
    gb_template_files_hd hd,
    gb_template_files_dt dt,
    gb_template_dt tmplt_dt
where
    hd.id = dt.hd_id
    and hd.id = :hd_id
    and dt.fld_id = tmplt_dt.id
    and tmplt_dt.type = 'M'       
"""
            
# Table Header Query (contains tables headers)
table_header_query = """
select 
    table_header.*
from   
    gb_files_tables_hd table_header
where  
    table_header.file_dt_id = :file_dt_id       
"""         

# Table Data and footer Query (contains tables data and footer)
table_details_query = """
select 
    table_rows.*
from   
    gb_files_tables_dt table_rows
where  
    table_rows.hd_id = :hd_id       
"""         