-- 1. Create database and switch to it
CREATE database if NOT exists testdb;
Use testdb;
-- 2. Create employees table
create table Employee_v2( 
id int,
EmployeeName varchar(50),
department varchar(50),
salary int
);
-- 3. Insert employee records
insert into Employee_v2 values 
( 101, 'Dinesh', 'Operation', 50000),
( 102, 'Jaffer', 'Operation', 70000),
( 103, 'Mahesh', 'HR', 70000),
( 104, 'Raj', 'HR', 65000),
( 105, 'Roshin', 'HR', 50000),
( 106, 'ram', 'Transport', 50000);
-- 4. Select all records
select * from Employee_v2;
-- 5. Find unique departments
select DISTINCT department from Employee_v2; 
-- 6. Drop old test tables if needed
Drop table if exists base;
Drop table if exists employee_v2;
-- 7. Show all tables in the current DB
show tables ;