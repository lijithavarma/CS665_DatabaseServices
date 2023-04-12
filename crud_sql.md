select * from employee
select * from user
select * from role
select * from organization
insert into employee (user_id, role_id, department_id, status, note, code) values (2, 3, 4, 7, 'employee', 'code')
insert into user (role_id, first_name, last_name, username, email, dob) values (2, 'firstname', 'lastname66', 'fl1990', 'fl1990@gmail.com', '1990/11/20')
insert into role (title, description, type, content) values ("Manager", "executive level", "Executive", "This is another manager")
insert into organization (title, summary, status, content) values ("Organization", "org", 9, "This is organization")
delete from employee where code='code'
delete from user where first_name='firstname'
delete from role where content='This is another manager'
delete from organization where title='Organization'
update user set firstName='David' where firstName='John'