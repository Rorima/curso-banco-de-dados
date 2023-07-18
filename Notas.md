# Anotações Rápidas

Estas são anotações rápidas que eu fiz enquanto estudava o curso de Bancos de Dados SQL e NoSQL do Básico ao Avançado. O objetivo destas anotações é que ela seja uma referência para mim mesmo.

## Dado e informação

Dado: Elemento bruto, geralmente proveniente de uma entrada do usuário ou de outros sistemas.

Informação: Elemento processado constituído de dados.

Conhecimento: Informação entendida e utilizada para tomada de decisão.

## Bancos de dados relacionais e não relacionais

Bancos de dados relacionais são conhecidos como bancos SQL, já os não relacionais são conhecidos como NoSQL.

SQL: Structured Query Language - Linguagem de Consulta Estruturada;
NoSQL: Not Only SQL - Não somente SQL.

Bancos de dados relacionais utilizam por padrão SQL, enquanto que bancos de dados não relacionais podem ou não utilizar SQL, como também algo mais.

Bancos de dados relacionais utilizam tabelas como seu principal formato para organizar os dados. São chamados de relacionais pois pode haver um relacionamento entre as tabelas.

Os bancos de dados não relacionais são livres do modelo relacional, e promovem alta disponibilidade e maior escalabilidade. Algumas implementações oferecem o particionamento e a replicação de dados; sistemas baseados em chave/valor; sistemas orientados a documentos e sistemas baseados em grafos.

## Principais bancos de dados relacionais

* Oracle;
* PostgreSQL;
* Microsoft SQL Server;
* Teradata;
* MySQL;
* MariaDB;
* IBM DB2;
* SYBASE;
* H2;
* Access;
* SQLITE;
* HIVE;
* HyperSQL;
* Apache Derby;

## Principais bancos de dados não relacionais

* H-BASE;
* CouchDB;
* Redis;
* Cassandra;
* Neo4j;
* RavenDB;
* Membase;
* MongoDB;
* Riak;
* Elasticsearch;
* Oracle Coherence;
* Apache Solr;

## Arquitetura Cliente-Servidor

O cliente é o navegador que se conecta a um servidor (que oferece um serviço) para enviar e receber dados. O Dropbox é um exemplo de um servidor, e o cliente é o aplicativo no seu computador. Um banco de dados é um servidor de banco de dados, e podemos utilizar os serviços de um servidor a partir de um cliente, que geralmente é um software.

## Modelagem Conceitual, Lógica e Física

Os modelos de banco de dados são usados para descrever, mais detalhadamente, a estrutura de um banco de dados. Eles servem então como parte importante da documentação dos sistemas que auxiliam não somente os desenvolvedores que estão trabalhando no projeto, mas tmabém servem como documentação, que pode ser entregue ao cliente que contratou o serviço de desenvolvimento. Um modelo de dados não informa quais dados estão armazenados em um banco de dados, mas sim apenas quais e que tipos de dados contém. Estes modelos são baseados em três níveis: **Conceitual**, **Lógico** e **Físico**.

### Modelo Conceitual

Este é o modelo de mais alto nível, ou seja, que está mais próximo dos usuários. O nível conceitual é desenvolvido com alto nível de abstração, a partir dos requisitos do sistema, extraídos na fase de levantamento de requisitos pelos analistas de sistemas. Esse modelo pode ser elaborado de forma textual ou por meio de dois diagramas: Diagrama de Entidade e Relacionamento e/ou Diagrama de Classes (Diagramas UML - Unified Modeling Language (Linguagem de Modelagem Unificada)).

Exemplo do modelo conceitual textual:

1. Clientes: 
   * Dados necessários: nome completo, tipo de pessoa (física ou jurídica), endereço, bairro, cidade, estado, telefone, e-mail, nome de contato;

2. Pedido:
   * Dados necessários: código do produto, quantidade, código do cliente, código do vendedor.

Exemplo de um DER - Diagrama de Entidade e Relacionamento / Modelo de Entidade e Relacionamento:

![Imagem de um Diagrama de Entidade e Relacionamento](https://i0.wp.com/jhenriquetdg.wordpress.com/files/2009/07/der1.jpg)

Exemplo de um Diagrama de Classes:

![Imagem de um Diagrama de Classes](http://1.bp.blogspot.com/-GHYukGtJLj0/U3vZbuH6g2I/AAAAAAAAAGA/RyKnGYSedsY/s1600/diagrama+de+classe.jpg)

Quando se usa um Diagrama de Classes, indica-se que o sistema será implementado utilizando Orientação a Objeto, e nem todo sistema utiliza OOP. A recomendação é sempre fazer o modelo utilizando o Diagrama de Entidade e Relacionamento, pois a partir dele é possível trabalhar com qualquer paradigma de programação.

### Modelo Lógico

Esse modelo descreve como os dados serão armazenados no banco de dados e também seus relacionamentos. Nesse modelo ainda pode ser definida a tecnologia que será utilizada para armazenagem dos dados: Bancos de Dados Relacionais ou Bancos de Dados não Relacionais.

![Imagem Modelo Lógico](https://www.researchgate.net/profile/Joan-Casas-Roma/publication/325335453/figure/fig30/AS:629753367232549@1527156311932/The-database-logical-schema.png)

