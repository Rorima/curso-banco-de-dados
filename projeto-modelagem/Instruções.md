# Projeto Completo

Os analistas de sistemas estão desenvolvendo um sistema para uma empresa e foram fazer diversas entrevistas com os funcionários de diversas áreas. Ao final dessa análise de requisitos foi gerado um documento descritivo com o que será necessário para o sistema.

Sua tarefa é naalisar esse documento, extrair as entidades, campos, relacionamentos e gerar o Modelo de Entidade e Relacionamento.

## O projeto

Uma farmácia comercializa vários tipos de produtos (remédios, cosméticos, etc.) Além do tipo, para cada produto são registrados o código, designação, composição, fabricante e preço de venda. Quando um cliente compra pela primeira vez um produto, são registrados os seus dados (nome, endereço, telefone, código postal, localidade e número de contribuinte). Depois de cadastrado, sempre que um cliente compra um determinado produto, é registrado seu código de cliente, os produtos adquiridos, o nome do médico (no caso das receitas médicas), bem como o total da venda. Cada compra é identificada por um número para facilitar as consultas na base de dados.

**Código SQL do projeto**

```sql
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema farmacia
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema farmacia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `farmacia` DEFAULT CHARACTER SET utf8 ;
USE `farmacia` ;

-- -----------------------------------------------------
-- Table `farmacia`.`clientes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`clientes` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `endereco` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `codigo_postal` VARCHAR(45) NOT NULL,
  `localidade` VARCHAR(45) NOT NULL,
  `numero_contribuinte` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`medicos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`medicos` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`medicos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `crm` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`compras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`compras` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`compras` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_cliente` INT NOT NULL,
  `id_medico` INT NOT NULL,
  `data` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_compras_1_idx` (`id_cliente` ASC),
  INDEX `fk_compras_2_idx` (`id_medico` ASC),
  CONSTRAINT `fk_compras_1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `farmacia`.`clientes` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_compras_2`
    FOREIGN KEY (`id_medico`)
    REFERENCES `farmacia`.`medicos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`tipos_produto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`tipos_produto` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`tipos_produto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`fabricantes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`fabricantes` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`fabricantes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`produtos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`produtos` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`produtos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_tipo` INT NOT NULL,
  `id_fabricante` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `designacao` VARCHAR(45) NOT NULL,
  `composicao` VARCHAR(45) NOT NULL,
  `preco_venda` DECIMAL(9,2) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_produtos_1_idx` (`id_tipo` ASC),
  INDEX `fk_produtos_2_idx` (`id_fabricante` ASC),
  CONSTRAINT `fk_produtos_1`
    FOREIGN KEY (`id_tipo`)
    REFERENCES `farmacia`.`tipos_produto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_produtos_2`
    FOREIGN KEY (`id_fabricante`)
    REFERENCES `farmacia`.`fabricantes` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`produtos_compras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`produtos_compras` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`produtos_compras` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_produto` INT NOT NULL,
  `id_compra` INT NOT NULL,
  `quantidade` INT NOT NULL,
  INDEX `fk_produtos_compras_2_idx` (`id_compra` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_produtos_compras_1`
    FOREIGN KEY (`id_produto`)
    REFERENCES `farmacia`.`produtos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_produtos_compras_2`
    FOREIGN KEY (`id_compra`)
    REFERENCES `farmacia`.`compras` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `farmacia`.`receitas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `farmacia`.`receitas` ;

CREATE TABLE IF NOT EXISTS `farmacia`.`receitas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_produtos_compras` INT NOT NULL,
  `id_medico` INT NOT NULL,
  `receita` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_receitas_1_idx` (`id_produtos_compras` ASC),
  INDEX `fk_receitas_2_idx` (`id_medico` ASC),
  CONSTRAINT `fk_receitas_1`
    FOREIGN KEY (`id_produtos_compras`)
    REFERENCES `farmacia`.`produtos_compras` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_receitas_2`
    FOREIGN KEY (`id_medico`)
    REFERENCES `farmacia`.`medicos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
```

**Populando o banco de dados**

```sql
use farmacia;

# Inserindo dados

-- Tipos de produto
insert into tipos_produto (nome) values ('Remédios');
insert into tipos_produto (nome) values ('Cosméticos');
insert into tipos_produto (nome) values ('Diversos');

-- Fabricantes
insert into fabricantes (nome) values ('Roche');
insert into fabricantes (nome) values ('Vitalis');
insert into fabricantes (nome) values ('Palmolina');

-- Médicos
insert into medicos (nome, crm) values ('Alfredo Muniz', '123123SP');
insert into medicos (nome, crm) values ('Fernanda Silva', '122122MG');
insert into medicos (nome, crm) values ('Julieta Santana', '112112SC');

-- Clientes
insert into clientes (
	nome, endereco, telefone, 
    codigo_postal, localidade, numero_contribuinte
) 
values (
	'Felicity Jones', 'Rua da Paz, 34', '(11) 2345-8899',
    '34.4567-098', 'Santos', '234.789.433-98'
);
insert into clientes (
	nome, endereco, telefone, 
    codigo_postal, localidade, numero_contribuinte
) 
values (
	'Angelina Jolie', 'Ruda do Ipiranga 456', '(21) 7544-3234',
    '56.654-567', 'Rio de Janeiro', '345.678.234-12'
);
insert into clientes (
	nome, endereco, telefone, 
    codigo_postal, localidade, numero_contribuinte
) 
values (
	'Ricardo Chavez', 'Rua Certa, 678', '(21) 2678-3984',
    '12.4569-223', 'Planaltina', '786.123.445-31'
);

-- Produtos
insert into produtos (id_tipo, id_fabricante, nome, designacao, composicao, preco_venda) 
values (1, 1, 'Dipirona', 'Dores de cabeça', 'Dipirona', '12.44');
insert into produtos (id_tipo, id_fabricante, nome, designacao, composicao, preco_venda) 
values (2, 2, 'Sabonete', 'Limpeza', 'Sabonete', '3.56');
insert into produtos (id_tipo, id_fabricante, nome, designacao, composicao, preco_venda) 
values (3, 3, 'Lixeira', 'Armazenar lixo', 'Aço', '15.22');

-- Compras
insert into compras (id_cliente, id_medico, data) values (1, 1, '2019-05-18');
insert into compras (id_cliente, id_medico, data) values (2, 2, '2019-08-01');
insert into compras (id_cliente, id_medico, data) values (3, 3, '2019-06-26');

-- Produtos e compras
insert into produtos_compras (id_produto, id_compra, quantidade) values (1, 1, 2);
insert into produtos_compras (id_produto, id_compra, quantidade) values (2, 2, 3);
insert into produtos_compras (id_produto, id_compra, quantidade) values (3, 3, 1);

-- Receitas
insert into receitas (id_produtos_compras, id_medico, receita) values (1, 1, 'receita1.pdf');
insert into receitas (id_produtos_compras, id_medico, receita) values (2, 2, 'receita2.pdf');
insert into receitas (id_produtos_compras, id_medico, receita) values (3, 3, 'receita3.pdf');

```

**Consultas simples**

```sql
use farmacia;

-- Realizando consultas simples

-- Tipos de produto
select * from tipos_produto;
select id, nome from tipos_produto;
select nome, id from tipos_produto;
select id, nome from tipos_produto order by id desc;
select id, nome from tipos_produto order by nome desc;

-- Fabricantes
select * from fabricantes;

-- Medicos
select * from medicos;

-- Clientes
select * from clientes;

-- Compras
select * from compras;

-- Produtos e Compras
select * from produtos_compras;
select * from produtos_compras where quantidade > 2;

-- Receitas
select * from receitas;
```

**Consultas complexas**

```sql
use farmacia;

-- compras

-- Passo 1 - Trazer as compras
select * from compras;

-- Passo 2 - Colocar o nome dos clientes nas compras
select 
	com.id as 'ID da compra', 
    cli.nome as 'Nome',
    com.data as 'Data'
from 
	compras as com, 
    clientes as cli
where 
	com.id_cliente = cli.id;

-- Passo 3 - Produtos e Compras
select * from produtos_compras;

-- Passo 4 - Mostrando o valor total da compra
select 
    com.id as 'Compra',
    cli.nome as 'Cliente',
    prod.nome as 'Produto',
    prod.preco_venda as 'Preco Unitário',
    proc.quantidade as 'Quantidade Comprada',
    (prod.preco_venda * proc.quantidade) as 'Total Produto Compra',
    com.data as 'Data da Compra',
    sum(prod.preco_venda * proc.quantidade) as 'Total'
from
	produtos_compras as proc,
    produtos as prod,
    compras as com,
    clientes as cli
where
	com.id = proc.id_compra
    and prod.id = proc.id_compra
    and cli.id = com.id_cliente
group by com.id, cli.nome, prod.nome, prod.preco_venda, proc.quantidade, com.data;

-- Passo 4 com inner join
SELECT 
    com.id AS 'Compra',
    cli.nome AS 'Cliente',
    prod.nome AS 'Produto',
    prod.preco_venda AS 'Preco Unitário',
    proc.quantidade AS 'Quantidade Comprada',
    (prod.preco_venda * proc.quantidade) AS 'Total Produto Compra',
    com.data AS 'Data da Compra',
    SUM(prod.preco_venda * proc.quantidade) AS 'Total'
FROM
    produtos_compras AS proc
INNER JOIN compras AS com ON com.id = proc.id_compra
INNER JOIN produtos AS prod ON prod.id = proc.id_produto
INNER JOIN clientes AS cli ON cli.id = com.id_cliente
GROUP BY com.id, cli.nome, prod.nome, prod.preco_venda, proc.quantidade, com.data;

-- Passo 4 do vídeo
select 
    com.id as 'Venda',
    cli.nome as 'Cliente',
    sum(prod.preco_venda * proc.quantidade) as 'Total',
    com.data as 'Data da Compra'
from
	produtos_compras as proc,
    produtos as prod,
    compras as com,
    clientes as cli
where
	com.id = proc.id_compra
    and prod.id = proc.id_produto
    and cli.id = com.id_cliente
group by com.id;
```

**Atualizando e Excluindo Dados**

```sql
use farmacia;

-- Atualizando dados
select * from produtos;

update 
  produtos 
set 
  preco_venda = '4.16', 
  id_tipo = 1, 
  id_fabricante = 1 
where id = 2;

-- Excluindo dados
select * from produtos_compras;
select * from receitas;
delete from produtos_compras where id = 3;
```