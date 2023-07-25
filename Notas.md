# Anotações Rápidas

Estas são anotações rápidas que eu fiz enquanto estudava o curso de Bancos de Dados SQL e NoSQL do Básico ao Avançado. O objetivo destas anotações é que elas sejam uma referência para eu poder consultar no futuro, além de ser uma documentação do meu aprendizado e uma prova de que verdadeiramente estudei banco de dados.

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

Um modelo lógico também pode ser definido da seguinte maneira:

```
TipoDeProduto (CodtipoProd, DescrTipoProd)

Produto(CodProd, DescrProd, PrecoProd, CodTipoProd)
         CodTipoProd referencia TipoDeProduto
```

### Modelo Físico

Também é chamado de Modelo de Implementação, e descreve por meio de alguma linguagem (comumente SQL) como será feita a armazenagem do banco. Neste nível, se escolhe qual Sistema Gerenciador de Banco de Dados (SGBD) será utilizado, levando em consideração o modelo lógico adotado.

Exemplo de detalhamento de colunas (campos) de uma tabela na **preparação** para o modelo físico:

|Nome do Campo| Tipo de Dado | Tamanho do Campo |
|---|---|---|
|Código do Paciente| Numérico | 5 dígitos |
|Nome do Paciente| Alfanumérico | 50 caracteres |
|Endereço| Alfanumérico | 50 caracteres |
|Bairro| Alfanumérico | 40 caracteres |
|Cidade| Alfanumérico | 40 caracteres |
|Estado| Alfanumérico | 2 caracteres |
|CEP| Alfanumérico | 9 caracteres |
|Data de Nascimento| Data | 10 caracteres |

Uma outra forma é utilizando a própria lniguagem SQL para criação de tabelas com suas colunas, tipos de dados e relacionamentos.

## Outros conceitos essenciais

### Entidade

É um objeto ou evento do mundo real sobre o qual desejamos manter registros em um banco de dados. Como um aluno, carro, produto, vendedor, venda, etc. Entidade e Tabela em um banco de dados é a mesma coisa.

### Atributo

Propriedade ou característica que descreve uma entidade. São as colunas (campos) das tabelas que irão armazenar os dados.

### Atributo Chave

Também conhecido como **chave primária**, ***primary key*** ou ***pk***, é um campo que pode possuir valor único (sem repetição) em todo o conjunto de dados da entidade. Este atributo é usado para identificar unicamente um registro da tabela.

### Relacionamentos

Geralmente as entidades nunca estão sozinhas; normalmente estão associadas com outras entidades. Reconhecer e registrar os relacionamentos entre entidades fornece uma descrição muito mais rica do modelo. Um relacionamento pode acontecer entre uma, duas ou várias entidades.

### Chave Estrangeira

Também conhecida como ***foreign key*** ou ***fk***, é um atributo presente em uma entidade que indica um relacionamento e representa a chave primária de uma outra entidade.

### Grau de Relacionamento

Indica a quantidade de entidades ligadas a um relacionamento. Os principais graus de relacionamento são: Unário, Binário e Ternário, mas dependendo da complexidade do projeto, podemos ter relacionamentos com graus maiores que os citados.

* Relacionamento Unário: Chamado também de grau 1 - Uma entidade se relaciona com ela mesma. Um exemplo disso é um funcionário que gerencia outro funcionário, ou uma pessoa que se casa com outra pessoa. Não é um relacionamento comum.
* Relacionamento Binário: Chamado também de grau 2 - Uma entidade se relaciona com outra entidade. É o tipo mais comum de relacionamento. Um exemplo disso é um vendedor que vende um produto e um aluno que cursa uma disciplina.
* Relacionamento Ternário: Chamado também de grau 3 - Três entidades estão relacionadas por um mesmo relacionamento. Um exemplo disso é um cliente que fez um pedido que foi atendido por um vendedor e foi utilizado um tipo de pagamento para o atendimento citado.

### Cardinalidade Máxima

Define a quantidade máxima de ocorrências de uma entidade que poderá estar associada a outra, por exemplo: Um vendedor pode vender apenas um tipo de produto, e um produto pode ser vendido por vários vendedores.

#### Relacionamento Binário Um-para-Um (1:1)

Indica que uma ocorrência da entidade A pode se relacionar exclusivamente com uma ocorrência da entidade B e vice-versa. Exemplo: Um vendedor ocupa um único escritório e um escritório pode ser ocupado por um único vendedor. 

Quando mostrado em um diagrama, a numeração é colocada em cada uma das pontas (bem próximo às entidades) para indicar a cardinalidade do relacionamento entre as entidades.

Em inglês, esse relacionamento é chamado de One-to-One.

#### Relacionamento Binário Um-para-Muitos (1:n)

Indica que uma ocorrência de entidade A pode se relacionar com várias ocorrências da entidade B, porém o inverso não é permitido. Exemplo: Um vendedor atende muitos clientes, porém cada cliente é atendido por apenas um vendedor específico.

Em inglês, esse relacionamento é chamado de One-to-Many.

#### Relacionamento Binário Muitos-para-Muitos (n:m)

Indica que uma ocorrência da entidade A pode se relacionar com várias ocorrências da entidade B e vice-versa. Exemplo: Um vendedor atende muitos clientes, e um cliente pode ser atendido por diversos vendedores.

Em inglês, esse relacionamento é chamado de Many-to-Many.

Na prática, o relacionamento n:m é dividido em duas relaçãos 1:n e uma nova entidade é criada para representar o relacionamento.

### Cardinalidade Mínima

Define a quantidade mínima de ocorrências de uma entidade que precisa estar associada a outra entidade (em caráter obrigatório). São consideradas como cardinalidades mínimas: 0 e 1. São representadas por: 0..1, 1..1, 0..n, 1..n, 0..\*, 1..\*, etc. O asterisco também significa muitos, como o n.

Exemplo: Um vendedor ocupa um único escritório, porém é obrigatório que ele tenha um escritório. Lê-se: no mínimo Um, no máximo Um (1..1);

Um escritório pode ser ocupado por um único vendedor, porém pode ser que a sala esteja vazia, ainda sem vendedor. Lê-se: no mínimo Zero, no máximo Um (0..1).

### Formas de Representação

Podemos encontrar uma variedade grande de representações gráficas para o Modelo Entidade Relacionamento. Os mais comuns são o **Clássico** e o **Pé de Galinha**. 

#### Clássico:

<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/erd-symbols/Entity.PNG" style="zoom:70%;" /><img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/erd-symbols/RelationshipShape.PNG" style="zoom:70%;" /><img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/erd-symbols/Attribute.PNG" style="zoom:70%;" />

Aqui a cardinalidade é representada por números (1..1, 1..n, etc.).

#### Pé de Galinha:

<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/erd-symbols/ERD-Notation.PNG" style="zoom:70%;" />

### Ferramenta indicada para modelagem

MySQL Workbench é uma ferramenta excelente para fazer diagramas. Construímos o diagrama, e podemos utilizá-lo com qualquer banco de dados relacional.

## Normalização de Dados

Chamamos de normalização de dados o processo formal e passo a passo que examina o documento descritivo gerado pelos analistas de sistemas durante a análise de requisitos em busca de definir as entidades, atributos, relacionamentos, chaves primárias e chaves estrangeiras do banco de dados a ser modelado. Este processo é realizado utilizando regras bem estabelecidas como Formas **Normais definidas** por Edgar Frank Codd em seu artigo.

Um dos objetivos principais da normalização é evitar, ou pelo menos amenizar anomalias e inconsistências que podem ocorrer durante a inclusão, exclusão, alteração e consulta de registros em um banco de dados.

Um banco de dados normalizado dentro dos padrões reduz o trabalho de manutenção e ajuda a evitar o desperdício do espaço de armazenamento, dentre outros benefícios.

O processo de normalização aplica uma série de regras sobre as tabelas de um banco de dados para verificar se ele foi corretamente projetado. Embora existam cinco formas normais (ou regras de normalização), na prática, usamos apenas um conjunto de três **Formas Normais**, ou seja, um banco de dados é considerado normalizado se nele for aplicadas essas três regras de Formas Normais.

Uma tabela que aceita campos vazios é uma tabela problemática. Todos os campos devem ser importantes para estar na tabela e campos importantes não podem ficar vazios.

O processo de normalização é sequencial. Isso significa que você só pode aplicar as regras da segunda forma normal se as tabelas já se encontrarem na primeira forma normal.

### Primeira Forma Normal (1FN)

Veja a seguinte tabela:

**Tabela Cliente**

| Código_cliente | Nome  | Telefone             | Endereco                       |
| -------------- | ----- | -------------------- | ------------------------------ |
| C001           | José  | 9999-9990            | Rua um, 1, São Paulo 12345-678 |
| C002           | Maria | 9999-9991, 9999-9992 | Rua um, 2, São Paulo 12345-678 |
| C003           | João  | 9999-9993            | Rua um, 3, São Paulo 12345-678 |

Uma entidade estará na primeira forma normal (1FN) se todos os campos forem atômicos (simples) e não multivalorados (com múltiplos valores). Isso significa que um campo da tabela deve ter somente um valor, por exemplo: Suponhamos que temos uma coluna chamada `Endereço`. Nesta coluna existem vários endereços juntamente com o CEP. Tal coluna vai contra a 1FN, pois comporta CEP e endereço, ao invés de comportar somente um desses dados. Para resolver esse problema, deve-se criar outra coluna para comportar o CEP. Ainda é possível ir além e dividir o endereço em mais colunas, como Rua e Bairro.

Veja a tabela modificada:

**Tabela Cliente**

| Código_cliente | Nome  | Telefone             | Rua       | Cidade    | CEP       |
| -------------- | ----- | -------------------- | --------- | --------- | --------- |
| C001           | José  | 9999-9990            | Rua um, 1 | São Paulo | 12345-678 |
| C002           | Maria | 9999-9991, 9999-9992 | Rua um, 2 | São Paulo | 12345-678 |
| C003           | João  | 9999-9993            | Rua um, 3 | São Paulo | 12345-678 |

E se um cliente tiver dois telefones, e outros três, e outros um somente? Deve-se criar uma coluna para cada telefone? Se fizéssemos isso, teríamos algumas entradas vazias, já que alguns clientes possuem somente um telefone. Neste caso, a solução é criar uma nova tabela. Cria-se uma tabela chamada `Telefones_cliente` e adiciona-se o código do cliente, que é a Primary Key da tabela `Cliente`. Assim, pode-se adicionar quantos telefones forem necessários.

**Tabela Telefones Cliente**

| Codigo_cliente | Telefone  |
| -------------- | --------- |
| C001           | 9999-9990 |
| C002           | 9999-9991 |
| C002           | 9999-9992 |
| C003           | 9999-9993 |

Assim a 1FN foi aplicada à tabela.

---

A primeira forma normal tenta resolver um dos maiores problemas de bancos de dados, que é a repetição (redundância de dados) e a desorganização deles. Imagine um campo `telefone` que permita a entrada de mais de um valor (dois números de telefone) por exemplo. Como faríamos a busca em um dos valores apenas? Sendo assim, é necessário aplicar a 1FN para resolver esse problema.

Nem toda tabela precisa obrigatoriamente ser normalizada com a 1FN. A normalização é um processo corretivo que deve ser aplicado em casos específicos onde o problema for identificado. Tudo irá depender de como a análise dos dados foi feita. Um analista experiente aplica a normalização de dados por padrão, pois ele olha para uma tabela e já "sente" que tem algo errado ali, e aplica a a correção.

### Segunda Forma Normal (2FN)

Uma entidade estará na 2FN se ela já se encontrar na 1FN e todos os atributos não-chave forem totalmente dependentes da chave primária.

Exemplo: **Tabela Pedidos**

| N_pedido | Codigo_produto | Produto              | Quant | Valor_unit | Subtotal |
| -------- | -------------- | -------------------- | ----- | ---------- | -------- |
| 1005     | 1-934          | Impressora Laser     | 5     | 1.500,00   | 7.500,00 |
| 1006     | 1-935          | Impressora Desjet    | 3     | 350,00     | 1.050,00 |
| 1007     | 1-936          | Impressora Matricial | 1     | 190,00     | 190,00   |
| 1008     | 1-937          | Impressora Mobile    | 6     | 980,00     | 5.880,00 |

Há um problema nessa tabela. O nome do produto não é dependente da chave primária, e sim do código do produto. O nome do produto está diretamente ligado ao código do produto. Sendo assim, a coluna `Produto` deveria estar em uma tabela separada, utilizando o `Codigo_produto` como **PK**.

Exemplo da tabela **Produtos**:

| Codigo_produto | Produto              |
| -------------- | -------------------- |
| 1-934          | Impressora Laser     |
| 1-935          | Impressora Desjet    |
| 1-936          | Impressora Matricial |
| 1-937          | Impressora Mobile    |

E esta seria a tabela **Pedidos**:

| N_pedido | Codigo_produto | Quant | Valor_unit | Subtotal |
| -------- | -------------- | ----- | ---------- | -------- |
| 1005     | 1-934          | 5     | 1.500,00   | 7.500,00 |
| 1006     | 1-935          | 3     | 350,00     | 1.050,00 |
| 1007     | 1-936          | 1     | 190,00     | 190,00   |
| 1008     | 1-937          | 6     | 980,00     | 5.880,00 |

E assim a coluna `Codigo_produto` será uma chave estrangeira na tabela **Pedidos**, pois ela é uma chave primária de outra tabela (**Produtos**).

Conforme vimos, tanto com a 1FN quanto com a 2FN, quando aplicamos a normalização de dados, é comum gerar novas tabelas a fim de satisfazer as formas normais que estão sendo aplicadas. É importante deixar claro que a normalização de dados, apesar de ser simples, causa grande dificuldade nos iniciantes da área.

### Terceira Forma Normal (3FN)

Cada uma das formas normais tende a ir refinando a modelagem e deixando a estrutura de dados mais íntegra e exclusiva, evitando repetições desnecessárias e possíveis sobrecargas no gerenciador de banco de dados. Uma tabela estará na 3FN se ela estiver na 2FN e se nenhuma coluna não-chave depender de outra coluna não-chave. Ou seja, na 3FN temos que eliminar os campos que podem ser obtidos pela equação de outros campos da mesma tabela.

Exemplo da tabela **Pedidos**:

| N_pedido | Codigo_produto | Quant | Valor_unit | Subtotal |
| -------- | -------------- | ----- | ---------- | -------- |
| 1005     | 1-934          | 5     | 1.500,00   | 7.500,00 |
| 1006     | 1-935          | 3     | 350,00     | 1.050,00 |
| 1007     | 1-936          | 1     | 190,00     | 190,00   |
| 1008     | 1-937          | 6     | 980,00     | 5.880,00 |

Veja que se multiplicarmos a quantidade do produto pelo seu preço unitário, teremos o subtotal. Portanto, o campo `Subtotal` é desnecessário e deve ser removido.

Aqui está a tabela **Pedidos** editada:

| N_pedido | Codigo_produto | Quant | Valor_unit |
| -------- | -------------- | ----- | ---------- |
| 1005     | 1-934          | 5     | 1.500,00   |
| 1006     | 1-935          | 3     | 350,00     |
| 1007     | 1-936          | 1     | 190,00     |
| 1008     | 1-937          | 6     | 980,00     |

### Outras Formas Normais

Um modelo de dados é considerado normalizado se as três Formas Normais forem aplicadas a ele. Dependendo da complexidade do projeto, apesar de raro, é possível que seja necessário aplicar a 4FN ou a 5FN. Vamos aprender sobre elas, mas não se prenda a elas.

#### Quarta Forma Normal (4FN)

Uma entidade estará na 4FN se na tabela não conter múltiplas entradas multivaloradas (valores repetidos em diferentes colunas). A presença de uma ou mais linhas em uma tabela implica na presença de uma ou mais outras linhas na mesma tabela.

#### Quinta Forma Normal (5FN)

Uma entidade estará na 5FN quando um atributo está em outra tabela sem a necessidade de estar na tabela pesquisada, e pode ser removido sem a perda de nenhuma informação.

## MER - Modelo Entidade Relacionamento

Há um padrão que deve ser utilizado para nomear tabelas:

* O nome sempre deve ser escrito com letras minúsculas;
* Pode-se escrever o nome da tabela tanto no singular quanto no plural;
* Se o nome da tabela for composto, deve-se separar os nomes com um underline;
* Não se pode usar acentuação, espaço e caracteres especiais;

Ao criar uma tabela, é indicado que a primeira coluna seja um identificador. Geralmente o nome é `id`. Além disso, ele é um valor do tipo inteiro, e também é uma **PK**.

Todos os campos da tabela devem ser marcados com `NN`, que significa *NOT NULL*. Isso significa que não serão aceitos campos nulos.

Também é aconselhável marcar a opção `AI`, que significa *AUTO INCREMENT*, ou "incremento automático".

Lembre-se de nunca colocar como Chave Primária um dado colocado por um usuário. Então se você tiver uma tabela de pessoas, não utilize o CPF como chave primária, pois a pessoa pode entrar o dado errado ou de maneira errada.

