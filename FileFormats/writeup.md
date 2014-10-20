Program 1- Assignment 1
========================

## Conversion:

I choose to use the SQL file to convert to JSON file.

In order to convert it into an JSON i choose to use PHP scripting.

PHP is a server side scripting language which works well with the SQL databases like MySql.
Mysql is a open source database.

create a variable and assign the whole table values to the variable by using command `"select * from table_name"`

After selecting everything from the Sql file we must use the command `"mysql_fetch_object($variable_name)"` to fetch the attributes of the table.

This must be done in a loop and the result that fetch command gets must be sent to encode in JSON using the command `"json_encode($result)"`

Then the output must be sent to a file with an extension of .json


## Compression:


All files compressed size and the percentage of conversion is given below.

| Format		| original      | Gzip        | zip      | Percentage	|
|---------------|---------------|-------------|----------|--------------|
| CSV		    | 484 MB	    | 59 MB       | 59 MB    | 	88%			|
| SQL		    | 467 MB	    | 60 MB       | 60 MB    | 	87%			|
| XML		    | 2.3 GB	    | 75 MB       | 75 MB    | 	97%			|
| YAML	    	| 771 MB	    | 61 MB       | 61 MB    | 	92%			|

By the data from the above table .XML compresses the most with 97%.

