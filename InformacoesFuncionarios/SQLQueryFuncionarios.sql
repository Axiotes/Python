create database funcionarios;

use funcionarios;

create table informacoes(
	id int not null identity(1,1),
	nome varchar(60),
	cpf decimal(11),
	gmail varchar(60),
	funcao varchar(20),
	salario_base decimal(7,2),
	salario_liquido decimal(7,2),
	imposto decimal(6,2),
	inss decimal(6,2),
	primary key(id)
);

select * from informacoes;