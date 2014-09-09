Program 1- Assignment 1
========================


I choose to use the SQL file to convert to JSON file.

In order to convert it into an JSON i choose to use PHP scripting.

PHP is a server side scripting language which works well with the SQL databases like MySql.
Mysql is a opensource database.

create a variable and assign the whole table values to the variable by using command "select * from table_name"

command "mysql_fetch_object($variable_name)" to fetch the attributes of the table.

This must be done in a loop and the result that fetch command gets must be sent to encode in JSON using the command "json_encode($result)"

Then the output must be sent to a file with an extension of .json
