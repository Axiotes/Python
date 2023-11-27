create database lista_telefonica;

use lista_telefonica;

create table lista (
	id int identity(1,1) not null,
	nome varchar(50),
	numero decimal(9),
	primary key(id)
);

select * from lista;