create database world;
use world;

create table people(
    id int primary key auto_increment,
    name varchar(64) not null,
    gender bool not null,
    location varchar(32)
);

drop table people;

select 
    id,
    name,
    if(gender = false, 'male', 'female') as gender,
    location
from people;

insert into people(name, gender, location)
values ('pranav', false, 'bengaluru');

delete from people where id = 1;

select * from people;