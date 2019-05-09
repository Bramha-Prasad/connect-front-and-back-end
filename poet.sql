create database Poets;

create table Poet_details(u_id varchar(20),passwd varchar(20));

insert into Poet_details values('Bramha','1234@Poet'),('Bittu','54321@write'),('Ivyanka','23343@sdsf');
select *from Poet_details;
drop table Poet_details;