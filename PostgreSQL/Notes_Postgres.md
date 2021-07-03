#POSTGRES

- What is PostgreSQL?
    * ORDBMS - Object-Relational Database Management System
    * Open-source
    * Cross-platform
    * Able to add custom functions
    * multi-version concurrency control feature
    * designed to be extensible
    
    
- Query
- Retrieving Data
    * Capabilities of SQL Select 
        - Projection: Takes a subset of columns
        - Selection: Takes a subset of rows
        - Join: Combine tables by some column
    * Concatenation
        - concat() - return string
            - to concatenate string use ['], for table and column names or special sibluls use [`]
            
            SELECT concat(`first_name`,' ',`last_name`) AS 'full_name',
                `job_title` as 'Job Title',
                `id` AS 'No.'
            FROM `employees`;
        - concat_ws() - concatenate with separator
            
            SELECT concat_ws(' ', `first_name`, `last_name`, `job_title`) AS 'full_name',
            `job_title` AS 'Job Title',
            `id` AS 'No.' FROM `employees`;
        
    * Filtering the Selected Rows
        - DISTINCT - eliminate duplicate results
        - WHERE - filter with specific conditions
        - logical operators: = , <= , =>;
    * Other comparing conditions
        - NOT,OR,AND - combined conditions
        - BETWEEN - specify a range
        - IN/NOT IN - to specify a set of values 
             - WHERE `manage_id` IN (109, 3, 16)
        - NULL - means missing value different from 0
    * Sorting
        - ORDER BY
            - ASC
            - DESC
    * Views
        CREATE VIEW `v_hr_result_set` AS
        SELECT
            CONCAT(`first_name`,' ',`last_name`) AS 'Full Name', `salary`
        FROM `employees` ORDER BY `department_id`
        SELECT * FROM `v_hr_result_set`;
    
    
- Writing Data in Tables
    * Inserting Data
        -INSERT INTO
    
    
- Modifying Existing Records
    * Updating Data
        - UPDATE - update, set, where
    * Deleting Data
        - DELETING FROM
            DELETE FROM, WHERE
        - TRUNCATE TABLE - delete all rows from a table
    
- Table Relation
    * JOIN - required min two tables
        - SELECT * FROM table_a
            JOIN table_b ON
                table_b.common_column = table_a.common_column
          
    * JOIN types:
      
        - Inner Join
        - Left Join
        - Right Join
        - Full Join
        - Cross Join
        - Self Join

- pgAdmin4 Demo
    * Create Database using pgAdmin4
    * Open the Query Tool
    
- Lab
    *