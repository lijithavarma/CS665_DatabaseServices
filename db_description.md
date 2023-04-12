The database name is employeemanagementsystemdb.
There are 4 tables, employee, user, role and organization tables.
id is the primary key in employee table.
user_id is the foreign key with id of user table.
role_id is the foreign key with id of role table.
department_id is the foreign key with id of organization table.
id is the primary key in user table
id is the primary key in role table
id is the primary key in organization table.

user_id, role_id and department_id is for the 3NF database.
for example:
1, 2 rows in employee table are different with id but user_id is same,
So we can get id of user and get all data from user table