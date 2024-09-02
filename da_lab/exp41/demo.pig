-- Define the location of the Python script
python_script = '/piginput/up.py';

-- Load the data from HDFS
data = LOAD '/piginput/sample.txt' USING PigStorage(',') AS (id:int, name:chararray);

-- Use the STREAM operator to process data with the Python script
uppercased_data = FOREACH data GENERATE id, STREAM data THROUGH 'python_script' AS (name:chararray);

-- Dump the results
DUMP uppercased_data;
