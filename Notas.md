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

## Exercício Modelagem de Dados

Um grupo de analistas de sistemas recebeu a tarefa de ir até uma empresa que precisava criar um sistema para armazenar dados, e com isso, gerar relatórios mensais. Ao final das entrevistas, os analistas geraram um documento onde está descrito a essência do que a empresa faz e precisa.

Você recebeu esse documento e tem a missão de criar um Modelo de Entidade de Relacionamentos para que o sistema possa ser criado. Lembre-se, seu trabalho é a base para um sistema robusto.

### Documento

Uma empresa fabricante de picolés deseja armazenar informações acerca de seus negócios. 

Os picolés fabricados são divididos em: normal (com água) e ao leite. As informações comuns armazenadas dos picolés são: sabor, ingredientes, preço e tipo da embalagem.

Especificamente, picolés normais possuem um conjunto de aditivos nutritivos (vitaminas ou sais minerais), cada um com nome e fórmula química; e picolés ao leite contêm um conjunto de conservantes, cada um com nome e descrição.

Os dois tipos de picolés são vendidos em lotes exclusivos (ou normais, ou ao leite) para os revendedores, e cada venda gera uma nota fiscal que pode conter um ou vários lotes. As notas fiscais possuem data, valor, número de série e descrição.

Todo revendedor possui uma pessoa de contato para eventuais resoluções de problemas, além disso, armazena-se do revendedor o CNPJ e a razão social.

Deseja-se obter relatórios sobre as vendas mensais dos picolés de cada tipo e quais revendedores compraram mais picolés nos últimos meses.

### Resolvendo o exercício

O que precisamos fazer:

1. Encontrar as entidades;
2. Definir os atributos;
3. Definir os relacionamentos;

Vamos então quebrar o texto em partes e resolver parte por parte:

>Uma empresa fabricante de picolés deseja armazenar informações acerca de seus negócios. 

Isso é apenas o contexto. Não é necessário fazer nada aqui.

>Os picolés fabricados são divididos em: normal (com água) e ao leite. As informações comuns armazenadas dos picolés são: sabor, ingredientes, preço e tipo da embalagem.

Entidades e atributos:
* Picolés (id, id sabor, preço, id tipo da embalagem);
* Sabor (id, nome);
* Tipos de Picolé (id, nome);
* Tipo de embalagem (id, nome);
* Ingredientes (id, nome);
* Ingredientes do Picolé (id, id ingrediente, id picolé);

>Especificamente, picolés normais possuem um conjunto de aditivos nutritivos (vitaminas ou sais minerais), cada um com nome e fórmula química; e picolés ao leite contêm um conjunto de conservantes, cada um com nome e descrição.

Entidades:
* Aditivos nutritivos (id, nome, fórmula química);
* Conservantes (id, nome, descrição);
* Adititivos nutritivos do Picolé (id, id aditivo nutritivo, id picolé);
* Conservantes do Picolé (id, id conservante, id picolé);

>Os dois tipos de picolés são vendidos em lotes exclusivos (ou normais, ou ao leite) para os revendedores, e cada venda gera uma nota fiscal que pode conter um ou vários lotes. As notas fiscais possuem data, valor, número de série e descrição.

Entidades:
* Lotes (id, id tipo de picole, quantidade);
* Notas fiscais (id, data, valor, número de série, descrição, id revendedor);
* Lotes da Nota fiscal (id, id lote, id nota fiscal)

>Todo revendedor possui uma pessoa de contato para eventuais resoluções de problemas, além disso, armazena-se do revendedor o CNPJ e a razão social.

Entidades:
* Revendedores (id, contato, cnpj, razão social)

>Deseja-se obter relatórios sobre as vendas mensais dos picolés de cada tipo e quais revendedores compraram mais picolés nos últimos meses.

Isso também é para contexto. Não é necessário fazer nada aqui.

## A Linguagem SQL

SQL, do inglês *Structured Query Language*, ou Linguagem de Consulta Estruturada traduzindo para o português, é a linguagem de bancos de dados relacionais. A linguagem SQL foi inspirada na Álgebra Relacional.

A linguagem SQL se divide em cinco subgrupos:

* DQL - *Data Query Language* (Linguagem de Consulta de Dados);
* DML - *Data Manipulation Language* (Linguagem de Manipulação de Dados);
* DDL - *Data Definition Language* (Linguagem de Definição de Dados);
* DCL - *Data Control Language* (Linguagem de Controle de Dados);
* DTL - *Data Transaction Language* (Linguagem de Transação Dados).

Cada subgrupo SQL possui comandos próprios de execução, e ao executar estes comandos, sempre temos como resultado duas coisas:

1. O resultado da execução do comando;
2. Uma mensagem de execução que pode ser de sucesso ou de erro.

Apesar de não obrigatório, costumamos escrever os comandos SQL em letra maiúscula, o que ajuda a entender melhor nosso código, já que o que for referente aos comandos SQL estarão destacados em maiúsculo, e o que for referente aos nossos dados, tabelas e etc., estarão em minúsculo.

Todos os comandos SQL são finalizados com ";" (ponto e vírgula).

### DQL - Data Query Language

No subgrupo DQL temos apenas um comando SQL: SELECT. Este comando é utilizado para realizar consultas no banco de dados. 

Embora tenha apenas um comando, a DQL é a parte da SQL mais utilizada. O comando SELECT permite ao usuário especificar uma consulta (query) como uma descrição do resultado esperado. Este comando é composto de várias cláusulas e opções, possibilitando elaborar consultas das mais simples às mais complexas.

#### Exemplo de utilização do SELECT

Exemplo:

`SELECT * FROM tipos_produto;`

No exemplo acima, estamos selecionando todos os dados da tabela tipos_produto. O asterisco indica que queremos os dados de todos os campos da tabela.

Exemplo:

`SELECT codigo, descricao FROM tipo_produto;`

No exemplo acima, estamos especificando os campos dos quais queremos os dados.

#### Apelidos

Podemos aplicar "apelidos" no nome de tabelas e campos quando estamos utilizando o comando SELECT. Fazemos isso através da palavra reservada `AS`. Veja o seguinte exemplo:

`SELECT codigo AS cod, descricao AS desc FROM produtos;`

Assim, o nome das colunas aparecerão como especificado no apelido.

Também podemos dar um apelido pra tabela, e fazemos isso após o FROM.

`SELECT p.codigo AS cod, p.descricao AS desc FROM produtos AS p`

### DML - Data Manipulation Language

No subgrupo DML, temos três comandos SQL: INSERT, UPDATE e DELETE. Este subgrupo da linguagem SQL é utilizado para realizar inclusões, alterações e exclusões de dados presentes em registros do banco de dados.

* INSERT: Usado para inserir um registro em uma tabela existente;
* UPDATE: Usado para alterar valores de dados em um ou mais registros de uma tabela;
* DELETE: Usado para remover registros de uma tabela.

#### Exemplo de utilização do INSERT

Exemplo:

`INSERT INTO tipos_produto (descricao) VALUES ('Notebook');`

No exemplo acima, estamos inserindo o valor Notebook na tabela tipos_produto. A tabela possui um campo código, que é a chave primária e se auto-incrementa, então o código será inserido automaticamente.

Podemos adicionar um item com vários atributos de uma só vez:

`INSERT INTO produtos (descricao, preco, codigo_tipo_produto) VALUES ('Smartphone', 1200, 3);`

No exemplo acima, estamos inserindo os valores na tabela produtos. O campo código é a chave primária que se auto-incrementa, então o codigo será inserido automaticamente.

#### Exemplo de utilização do UPDATE

Exemplo:

`UPDATE tipos_produto SET descricao = 'Laptop' WHERE codigo = 3;`

No exemplo acima, estamos atualizando um registro. Note que estamos utilizando o filtro com a cláusula WHERE, especificando qual registro queremos atualizar.

Também podemos atualizar mais de um valor usando somente um UPDATE:

`UPDATE produtos SET descricao = 'Notebook', preco = 2.800 WHERE codigo = 20;`

É necessário tomar bastante cuidado com o comando UPDATE! Quando não é oferecida uma cláusula WHERE, que é o que filtra quais dados serão alterados, ele altera os dados da tabela inteira.

#### Exemplo de utilização do DELETE

Exemplo:

`DELETE FROM tipos_produto WHERE codigo = 3;`

No exemplo acima, estamos excluindo da tabela o registro que tenha o código igual a 3.

Assim como no comando UPDATE, é necessário tomar cuidado com o comando DELETE, pois quando não é oferecida uma cláusula WHERE, ele deleta todos osdados da tabela.

### DDL - Data Definition Language

No subgrupo DDL, temos três comandos SQL: CREATE, ALTER e DROP. Este subgrupo é utilizado para criar, alterar e excluir bancos de dados, tabelas e elementos associados, como índice e visão.

* CREATE: Usado para criar um banco de dados, tabela e outros objetos em um banco de dados;
* ALTER: Usado para alterar a estrutura de tabelas ou outro objeto em um banco de dados;
* DROP: Usado para apagar bancos de dados, tabelas e outros objetos;

#### Exemplo de utilização do CREATE

Exemplo:

`CREATE DATABASE financeiro;`

No exemplo acima ,estamos criando um banco de dados chamado financeiro.

`CREATE TABLE tipos_produto (codigo INT PRIMARY KEY, descricao VARCHAR(50));`

No exemplo acima, estamos criando uma tabela contendo os campos código, que é chave primária e do tipo inteiro, e descricao, que é do tipo varchar com até 50 caracteres.

#### Exemplo de utilização do ALTER

Exemplo:

`ALTER TABLE tipos_produto ADD peso DECIMAL(8,2);`

No exemplo acima, estamos alterando a estrutura da tabela e acrescentando um novo campo chamado peso, que é do tipo decimal com até oito dígitos antes da vírgula e dois dígitos após a vírgula.

#### Exemplo de utilização do DROP

Exemplo:

`DROP TABLE tipos_produto;`

No exemplo acima, estamos apagando a tabela. Este comando apaga toda a estrutura e os dados, desde que esta tabela não tenha relacionamentos.

Também é possível excluir bancos de dados com este mesmo comando:

`DROP DATABASE financeiro;`

### DCL - Data Control Language

No subgrupo DCL, temos dois comandos SQL: GRANT e REVOKE. Este subgrupo da linguagem SQL é utilizado para controlar os aspectos de autorização de dados e licenças de usuários para controlar quem tem acesso para manipular dados dentro do banco de dados.

* GRANT: Usado para autorizar um usuário a executar ou setar operações no banco de dados;
* REVOKE: Usado para remover ou restringir a capacidade de um usuário de executar operações;

#### Exemplo de utilização do GRANT

Exemplo:

`GRANT SELECT ON tipos_produto TO geek;`

No exemplo acima, estamos dando permissão de consulta na tabela tipos_produto para o usuário geek.

#### Exemplo de utilização do REVOKE

Exemplo:

`REVOKE CREATE TABLE FROM geek;`

No exemplo acima, estamos retirando a permissão de criação de tabelas no banco de dados do usuário geek.

### DTL - Data Transaction Language

No subgrupo DTL, temos três comandos: BEGIN, COMMIT e ROLLBACK.

* BEGIN (ou START TRANSACTION): Usado para marcar o começo de uma transação que pode ser completada ou não;
* COMMIT: Finaliza uma transação;
* ROLLBACK: Faz com que as mudanças nos dados existentes do último COMMIT sejam descartadas.

#### Exemplo de utilização do BEGIN e COMMIT

O exemplo a seguir é mais complexo devido ao próprio uso do comando BEGIN, mas já estudamos todos os comandos que serão usados aqui.

```sql
CREATE TABLE 'tipos_produtos' (codigo INT PRIMARY KEY, descricao VARCHAR(50));
BEGIN TRANSACTION; -- Começa a transação
   INSERT INTO tipos_produto VALUES ('Notebook');
   INSERT INTO tipos_produto VALUES ('Nobreak');
COMMIT; -- Termina a transação
```

#### Exemplo de utilização do ROLLBACK

```sql
CREATE TABLE 'tipos_produtos' (codigo INT PRIMARY KEY, descricao VARCHAR(50));
BEGIN TRANSACTION; -- Começa a transação
   INSERT INTO tipos_produto VALUES ('Notebook');
   INSERT INTO tipos_produto VALUES ('Nobreak');
ROLLBACK; -- Termina a transação
```

## A linguagem SQL (parte 2)

Aqui aprenderemos partes mais avançadas da linguagem SQL.

### Filtrando consultas com o WHERE

Quando se trata de consultas, utilizaremos a DQL.

Quando queremos ver todos os dados de uma tabela, utilizamos o seguinte código SQL:

```sql
SELECT * FROM tipos_produto;
```

Podemos utilizar o `WHERE` para filtrar consultas e ter resultados mais precisos:

```sql
SELECT * FROM tipos_produto WHERE codigo = 1;
```

No código acima, estamos selecionando todos os dados onde o código do tipo de produto seja igual a um.

### Consultas em múltiplas tabelas

Suponhamos que queiramos mostrar três colunas de uma tabela juntamente com uma coluna de outra tabela. Este seria o código:

```sql
SELECT 
   p.codigo AS Código, 
   p.descricao AS Descrição, 
   p.preco AS Preço, 
   tp.descricao AS Tipo 
FROM 
   produtos AS p, 
   tipos_produto AS tp 
WHERE 
   p.codigo_tipo_produto = tp.codigo;
```

Lembre-se que só é possível fazer uma consulta assim se as tabelas tiverem um relacionamento entre si.

### Junção de tabelas

Em um banco de dados podemos ter duas ou mais tabelas relacionadas. É bastante comum ter a necessidade de trazer dados de diferentes tabelas ao fazer consultas. Para criar uma seleção assim, devemos definir certos critérios, e eles são chamados de **junções**.

Uma junção de tabelas cria uma pseudo-tabela derivada de duas ou mais tabelas de acordo com as regras especificadas, que são parecidas com as regras da **Teoria dos Conjuntos**.

As diferentes junções são muitas vezes formas diferentes de se fazer a mesma coisa.

Para fazer as junções, precisaremos de um banco de dados e algumas tabelas. O seguinte código irá criar o banco de dados e as tabelas que precisaremos:

```sql
-- Criando o banco de dados
CREATE DATABASE juncao;

-- Indicando qual banco de dados vamos utilizar para criar as tabelas
USE juncao;

-- Criando a primeira tabela
CREATE TABLE profissoes(
   id INT NOT NULL AUTO_INCREMENT,
   cargo VARCHAR(60) NOT NULL,
   PRIMARY KEY (id) -- indicando a chave primária
);

-- Criando a segunda tabela
CREATE TABLE clientes(
   id INT NOT NULL AUTO_INCREMENT,
   nome VARCHAR(60) NOT NULL,
   data_nascimento DATE NOT NULL,
   telefone VARCHAR(10) NOT NULL,
   id_profissao INT NOT NULL,
   PRIMARY KEY (id),
   -- Indicando a chave estrangeira e a qual tabela ela pertence
   FOREIGN KEY (id_profissao) REFERENCES profissoes(id)
);
```

Agora iremos inserir alguns dados. O formato da data de nascimento é yyyy-mm-dd, em que 'y' refere-se ao ano, 'm' ao mês e 'd' ao dia:

```sql
INSERT INTO profissoes (cargo) VALUES ('Programador');
INSERT INTO profissoes (cargo) VALUES ('Analista de Sistemas');
INSERT INTO profissoes (cargo) VALUES ('Suporte');
INSERT INTO profissoes (cargo) VALUES ('Gerente');

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) 
VALUES  ('João Pereira', '1981-06-15', '1234-5678', 1);

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) 
VALUES ('Ricardo da Silva', '1973-10-10', '2234-5669', 2);

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) 
VALUES ('Felipe Oliveira', '1987-08-01', '4234-5640', 3);

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) 
VALUES ('Mario Pirez', '1991-02-05', '5234-5621', 1);
```

#### Junção de produto cartesiano

Uma junção de produto cartesiano é uma junção entre duas tabelas que origina uma terceira tabela constituída por todos os elementos da primeira combinadas com todos os elementos da segunda.

Podemos escrever o seguinte código para selecionar todos os dados da tabela "profissoes" e "clientes":

```sql
SELECT * FROM profissoes, clientes;
```

Mas o seguinte código é mais adequado, pois mostra as informações de uma maneira melhor:

```sql
SELECT 
   c.id AS ID,
   c.nome AS Nome,
   c.data_nascimento AS Data,
   c.telefone AS Telefone,
   p.cargo AS Cargo
FROM 
   profissoes AS p, 
   clientes AS c
WHERE c.id_profissao = p.id;
```

É possível fazer qualquer tipo de junção utilizando a junção por produto cartesiano, entretanto, em entrevistas de emprego ou exercícios de cursos talvez seja requerido que você utilize o `JOIN` para fazer as junções.

#### Junção interna (inner join)

Uma junção interna é caracterizada por uma consulta que retorna apenas os dados que atendem às condições de junção, isto é, quais linhas de uma tabela se relacionam com as linhas de outras tabelas. Para isso, utilizamos a cláusula `ON`, que é semelhante à cláusula `WHERE`. Sempre que utilizamos o `JOIN`, usamos o `ON` para detalhar a condição.

No código abaixo, teremos o mesmo resultado da consulta do exemplo anterior:

```sql
SELECT 
   c.id AS ID,
   c.nome AS Nome,
   c.data_nascimento AS Data,
   c.telefone AS Telefone,
   p.cargo AS Cargo
FROM 
   clientes AS c
INNER JOIN
   profissoes AS p
ON c.id_profissao = p.id;
```

#### Junção externa (outer join)

Uma junção externa é uma consulta que não requer que os registros de uma tabela possuam registros equivalentes em outra. Quando não há correspondência de um valor, ele é apresentado como NULL.

##### Junção externa a esquerda (left outer join)

O resultado desta consulta sempre contém todos os registros da tabela a esquerda (a primeira tabela mencionada na consulta), mesmo quando não exista registros correspondentes na tabela a direita. Se não houver valores correspondentes na tabela a direita, o valor apresentado será NULL.

```sql
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;
```

##### Junção externa a direita (right outer join)

Esta consulta é inversa à anterior, e retorna sempre todos os registros da tabela a direita (a segunda tabela mencionada na consulta).

```sql
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;
```

##### Junção externa completa (full outer join)

Esta consulta faz referência aos dois lados. Ela apresenta todos os dados das tabelas a esquerda e a direita. Ela apresentará valores nulos para registros sem correspondência. Esta junção não funciona no MySQL, mas pode ser simulada utilizando um `LEFT JOIN` e um `RIGHT JOIN`.

```sql
SELECT * FROM clientes
FULL OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;
```

Esta é versão do `FULL OUTER JOIN` para o MySQL:

```sql
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id
UNION -- Unindo as duas tabelas
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;
```

#### Junção cruzada (cross join)

Esta consulta é usada quando queremos juntar duas ou mais tabelas por cruzamento. Ou seja, queremos todos os dados de uma tabela para cada linha de outra tabela, ou vice-versa.

```sql
SELECT 
   c.id AS ID,
   c.nome AS Nome,
   c.data_nascimento AS Data,
   c.telefone AS Telefone,
   p.cargo AS Cargo
FROM 
   clientes AS c
CROSS JOIN
   profissoes AS p;
```

Assim temos uma linha com cada profissão para cada cliente.

#### Auto junção (self join)

Esta consulta é uma junção de uma tabela a si mesma. Vamos criar e popular uma tabela para servir como exemplo:

```sql
CREATE TABLE consumidor(
   id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   nome VARCHAR(50) NOT NULL,
   contato VARCHAR(50) NOT NULL,
   endereco VARCHAR(50) NOT NULL,
   cidade VARCHAR(100) NOT NULL,
   cep VARCHAR(20) NOT NULL,
   pais VARCHAR(50) NOT NULL
);

INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais) 
VALUES (
   'Alfredo Nunes', 
   'Maria Nunes', 
   'Rua da paz, 47', 
   'São Paulo', 
   '123.456-78', 
   'Brasil'
);
INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais) 
VALUES (
   'Ana Trujillo', 
   'Guilherme Souza', 
   'Rua Dourada, 452', 
   'Goiânia', 
   '123.456-79', 
   'Brasil'
);
INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais) 
VALUES (
   'Leandro Veloz', 
   'Pedro Siqueira', 
   'Rua vazia, 72', 
   'São Paulo', 
   '123.456-70', 
   'Brasil'
);
```

Agora a auto junção:

```sql
SELECT 
   a.nome AS Consumidor1,
   b.nome AS Consumidor2,
   a.cidade
FROM consumidor AS a
INNER JOIN consumidor AS b
ON a.id <> b.id
AND a.cidade = b.cidade;
```

No exemplo acima, estamos realizando uma auto junção onde os ids sejam diferentes e a cidade seja igual.

#### Junção baseada em comparador (equi-join)

Uma junção equi-join é um tipo específico de junção baseada em comparador, que usa apenas comparações de igualdade na junção.

```sql
SELECT *
FROM clientes
JOIN profissoes
ON clientes.id_profissao = profissoes.id;
```

Nesse exemplo, estamos realizando um equi-join utilizando como compardor os campos de relacionamento.

#### Junção natural (natural join)

Uma junção natural é um caso especial de equi-join. O resultado desta junção é uma tabela que mostra os campos comuns entre tabelas. Os campos comuns são os campos que possuem os mesmos nomes nas duas tabelas.

```sql
SELECT *
FROM clientes
NATURAL JOIN profissoes;
```

No caso dessas duas tabelas utilizadas, o único campo comum é o id, então ele será usado. Cada linha do id de uma tabela corresponde a linha do id da outra tabela.

### Funções de Agregação

Ao desenvolver sistemas, é muito comum que uma aplicação necessite de informações resumidas, como por exemplo, obter a menor ou maior venda do dia, o maior salário de um funcionário, o mês que teve mais vendas e etc.

A linguagem SQL contém diversas funções nativas para esse fim, que podem ser usadas para agregar um conjunto de valores em um único resultado através de uma consulta. 

Uma função de agregação processa um conjunto de valores contidos em uma única coluna de uma tabela e retorna um único valor como resultado. Sua sintaxe é semelhante aquela utilizada em funções de programação, contudo, o parâmetro de entrada é sempre a coluna cujos valores desejamos processar. Podemos informar no comando SELECT uma ou mais funções de agregação, de acordo com a necessidade.

Exemplo: 

`nome-da-funcao(coluna)`

Considere o seguinte código e a explicação das funções logo abaixo:

```sql
CREATE TABLE categorias(
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(60) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE produtos(
  id INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(60) NOT NULL,
  preco_venda DECIMAL(9,2) NOT NULL,
  preco_custo DECIMAL(9,2) NOT NULL,
  id_categoria INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

INSERT INTO categorias (nome) VALUES ('Material Escolar');
INSERT INTO categorias (nome) VALUES ('Acessório Informática');
INSERT INTO categorias (nome) VALUES ('Material Escritório');
INSERT INTO categorias (nome) VALUES ('Game');

INSERT INTO produtos (
  descricao,
  preco_venda,
  preco_custo,
  id_categoria)
VALUES('Caderno','5.45', '2.30', 1);
INSERT INTO produtos (
  descricao,
  preco_venda,
  preco_custo,
  id_categoria)
VALUES('Caneta','1.20', '0.45', 1);
INSERT INTO produtos (
  descricao,
  preco_venda,
  preco_custo,
  id_categoria)
VALUES('Pendrive 32GB','120.54', '32.55', 2);
INSERT INTO produtos (
  descricao,
  preco_venda,
  preco_custo,
  id_categoria)
VALUES('Mouse','17.00', '4.30', 2);
```

#### Max

Esta função analisa um conjunto de valores e retorna o maior entre eles.

Exemplo:

```sql
SELECT MAX(preco_venda) FROM produtos;
```

Outro exemplo:

```sql
SELECT id_categoria, MAX(preco_venda) 
FROM produtos
GROUP BY id_categoria;
```

No exemplo acima, estamos buscando o maior preço de venda em todas as categorias de produtos que temos. Ao final estamos agrupando pelo id da categoria. Iremos estudar sobre agrupamento e ordenação mais a fente. Quando utilizamos uma função de agregação em uma consulta juntamente com outros campos, devemos sempre utilizar o agrupamento (`GROUP BY`) por algum elemento da consulta.

Outro exemplo:

```sql
SELECT id_categoria, MAX(preco_venda) 
FROM produtos
GROUP BY id_categoria
HAVING MAX(preco_venda) > 10;
```

No exemplo acima, estamos buscando o maior preço de venda em cada uma das categorias de produtos que temos em que o preço de venda seja maior que 10.00. Ao final, estamos agrupando pelo id da categoria. A cláusula `HAVING` funciona quase como um `WHERE`, mas é geralmente utilizada em conjunto com funções de agregação, enquanto que o `WHERE` é utilizado com o `SELECT`.

#### Min

Esta função analisa um conjunto de valores e retorna o menor entre eles.

Exemplo:

```sql
SELECT MIN(preco_venda) FROM produtos;
```

#### Sum

Esta função realiza a soma dos valores em uma única coluna e retorna esse resultado.

Exemplo:

```sql
SELECT SUM(preco_venda) FROM produtos WHERE id_categoria = 1;
```

No exemplo acima, somamos todos os preços de venda dos produtos em que a categoria seja igual a 1.

#### Avg

Esta função calcula a média aritmética dos valores em uma única coluna.

Exemplo:

```sql
SELECT AVG(preco_venda) FROM produtos;
```

No exemplo acima, estamos calculando a média aritmética dos preços de venda da tabela produtos.

#### Round

Esta função arredonda valores para especificar quantas casas decimais queremos apresentar.

Exemplo:

```sql
SELECT ROUND(AVG(preco_venda), 2) FROM produtos;
```

Estamos apresentando duas casas decimais após a vírgula.

#### Count

Esta função retorna o total de linhas selecionadas. Podemos passar por parâmetro o nome da coluna ou um asterisco. Por padrão, quando informado o nome de uma coluna, valores do tipo NULL serão ignorados, mas quando informado um asterisco, todas as linhas serão contabilizadas.

```sql
SELECT COUNT(preco_venda) AS Quantidade 
FROM produtos 
WHERE id_categoria = 1;
```

No exemplo acima, estamos contando quantos produtos da categoria 1 temos cadastrados.

### Agrupamento e Ordenação

Considere o seguinte código:

```sql
CREATE DATABASE agrupamento;

USE agrupamento;

CREATE TABLE  tipos(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(60) NOT NULL
);

CREATE TABLE fabricantes(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(60) NOT NULL
);

CREATE TABLE produtos(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(60) NOT NULL,
  id_fabricante INT NOT NULL,
  quantidade INT NOT NULL,
  id_tipo INT NOT NULL,
  FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id),
  FOREIGN KEY (id_tipo) REFERENCES tipos(id)
);
```

Agora popularemos as tabelas:

```sql
INSERT INTO tipos (nome) VALUES ('Console');
INSERT INTO tipos (nome) VALUES ('Notebook');
INSERT INTO tipos (nome) VALUES ('Celular');
INSERT INTO tipos (nome) VALUES ('Smartphone');
INSERT INTO tipos (nome) VALUES ('Sofá');
INSERT INTO tipos (nome) VALUES ('Armário');
INSERT INTO tipos (nome) VALUES ('Refrigerador');

INSERT INTO fabricantes (nome) VALUES ('Sony');
INSERT INTO fabricantes (nome) VALUES ('Dell');
INSERT INTO fabricantes (nome) VALUES ('Microsoft');
INSERT INTO fabricantes (nome) VALUES ('Samsung');
INSERT INTO fabricantes (nome) VALUES ('Apple');
INSERT INTO fabricantes (nome) VALUES ('Beline');
INSERT INTO fabricantes (nome) VALUES ('Magno');
INSERT INTO fabricantes (nome) VALUES ('CCE');
INSERT INTO fabricantes (nome) VALUES ('Nintendo');

INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Playstation 3', 1, 100, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Core 2 Duo 4GB Ram 500GB HD', 2, 200, 2);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Xbox 360 120GB', 3, 350, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('GT-I6220 Quad band', 4, 300, 3);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('iPhone 4 32GB', 5, 50, 4);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Playstation 2', 1, 100, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Sofá Estofado', 6, 200, 5);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Armário de Serviço', 7, 50, 6);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Refrigerador 420L', 8, 200, 7);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo)
VALUES ('Wii 120GB', 8, 250, 1);
```

#### GROUP BY

Utilizamos esta cláusula para agrupar elementos do mesmo tipo.

Exemplo:

```sql
SELECT 
   t.nome AS Tipo, 
   SUM(p.quantidade) AS 'Quantidade em Estoque'
FROM 
   tipos AS t, 
   produtos AS p
WHERE t.id = p.id_tipo
GROUP BY t.nome;
```

No exemplo acima, estamos solicitando a quantidade de produtos em estoque, agrupados pelo tipo. Utilizamos a função de agregação `SUM()` para efetuar a soma de cada tipo de produto.

Outro exemplo:

```sql
SELECT 
   f.nome AS Fabricante, 
   SUM(p.quantidade) AS 'Quantidade em Estoque'
FROM 
   fabricantes AS f, 
   produtos AS p
WHERE f.id = p.id_fabricante
GROUP BY f.nome;
```

No exemplo acima estamos ordenando a tabela pelo nome do fabricante.

Outro exemplo:

```sql
SELECT
   t.nome AS Tipo,
   f.nome AS Fabricante,
   SUM(p.quantidade) AS 'Quantidade em Estoque'
FROM 
   tipos AS t,
   fabricantes AS f,
   produtos AS p
WHERE
   t.id = p.id_tipo
   AND
   f.id = p.id_fabricante
GROUP BY t.nome, f.nome;
```

No exemplo acima, estamos solicitando a quantidade de produtos em estoque de acordo com os tipos e fabricantes.

Outro exemplo:

```sql
SELECT
   t.nome AS Tipo,
   f.nome AS Fabricante,
   SUM(p.quantidade) AS 'Quantidade em Estoque'
FROM 
   tipos AS t,
   fabricantes AS f,
   produtos AS p
WHERE
   t.id = p.id_tipo
   AND 
   f.id = p.id_fabricante
GROUP BY
   t.nome,
   f.nome
HAVING SUM(p.quantidade) > 200;
```
No exemplo acima, estamos solicitando a quantidade de produtos em estoquede acordo com os tipos e fabricantes em que a quantidade seja maior que 200 itens em estoque.

Outro exemplo:

```sql
SELECT
   t.nome AS Tipo
FROM 
   produtos AS p, 
   tipos AS t
WHERE
   t.id = p.id_tipo
GROUP BY
   t.nome;
```

No exemplo acima estamos mostrando todos os tipos de produtos sem repetir o nome deles. Se não utilizássemos o `GROUP BY`, teríamos vários valores repetidos.

#### ORDER BY

Utilizamos esta cláusula para ordenar os dados em ordem alfabética ou numérica. A ordenação pode ser `ASC` (ascendente) ou `DESC` (descendente). Por padrão, a ordenação é ascendente, ou seja, do menor para o maior.

Se quisermos realizar a ordenação padrão trazendo todos os campos, podemos utilizar o asterisco, mas se quisermos ordenar por um campo específico ou mesmo mudar a forma de ordenação, devemos informar os campos.

Exemplo:

```sql
SELECT
   id,
   nome,
   id_tipo,
   id_fabricante,
   quantidade
FROM
   produtos
ORDER BY
   id ASC;
```

No exemplo acima, a tabela é ordenada pelo id de forma ascendente. Um `SELECT` normal, sem o `ORDER BY`, produziria o mesmo resultado, pois por padrão a ordenação é feita pelo id de forma ascendente.

Outro exemplo:

```sql
SELECT
   id,
   nome,
   id_tipo,
   id_fabricante,
   quantidade
FROM
   produtos
ORDER BY
   id DESC;
```

No exemplo acima, ordenamos a tabela pelo campo id de maneira descendente.

Outro exemplo:

```sql
SELECT
   id,
   nome,
   id_tipo,
   id_fabricante,
   quantidade
FROM
   produtos
ORDER BY
   quantidade DESC;
```

Aqui ordenamos de forma descendente pela quantidade de produtos.

### Funções de data e hora

No comando `SELECT` há diversas funções que foram embutidas para facilitar o manuseio de alguns tipos de dados em determinadas condições. Essas funções são particularmente úteis a programadores de aplicativos, uma vez que conseguirão obter diretamente do banco de dados o tratamento a formatos ou resultados que dependeriam de algum algoritmo, sem ter que escrever código na linguagem fonte do aplicativo para tais recursos. Esses comandos podem ser utilizados em uma base de dados, mas não são dependentes de bases de dados. A seguir iremos conhecer as funções de data e hora.

#### CURDATE

Esta função retorna a data atual no formato yyyy-mm-dd. `CURDATE` significa *current date*, que em português significa "data atual".

Exemplo:

```sql
SELECT CURDATE() AS 'Data Atual';
```

#### CURTIME

Esta função funciona como a função anterior. A diferença é que ela mostra a hora atual ao invés de mostrar a data. Ela retorna a hora atual no formato hh:mm:ss.

Exemplo:

```sql
SELECT CURTIME() AS 'Tempo Atual';
```

Há uma função que faz a mesma coisa que essa, e o nome dela é `CURRENT_TIME()`

#### DATE_ADD

Esta função adiciona um intervalo à data. O intervalo pode ser uma data seguida de um horário. O intervalo pode ser em dias, dias e horas e minutos, dias e segundos, minutos e segundos e etc.

A sintaxe é: `DATE_ADD(data, intervalo)`

Exemplo:

```sql
SELECT DATE_ADD(CURDATE(), INTERVAL 3 DAY) AS 'Data de Vencimento';
```

No exemplo acima, estamos adicionando 3 dias na data atual.

#### DATE_SUB

Esta função funciona como a função anterior. A diferença é que ela subtrai da data ao invés de adicionar.

Exemplo:

```sql
SELECT DATE_SUB(CURDATE(), INTERVAL 10 MINUTE) AS 'Data de Vencimento';
```

#### DATEDIFF

Esta função retorna o valor da diferença entre duas datas, podendo ambos ser data ou data e horário. 

Esta é a sintaxe: `DATEDIFF(expressão1, expressão2)`

Exemplo:

```sql
SELECT DATEDIFF(CURDATE(), DATE_SUB(CURDATE(), INTERVAL 10 DAY)) AS 'Dias em Atraso';
```

No exemplo acima, estamos calculando o atraso em dias de uma data 10 dias no passado para a data atual.

#### DATE_FORMAT

Esta função retorna a data no formato especificado.

Esta é a sintaxe: `DATE_FORMAT(data, formato)`

Exemplo:

```sql
SELECT DATE_FORMAT(CURDATE(), '%d/%m/%Y') AS 'Data Formatada';
```

No exemplo acima estamos formatando a data para dd/mm/yyyy.

#### DAYNAME

Esta função retorna o dia da semana para uma data.

Exemplo:

```sql
SELECT DAYNAME(CURDATE()) AS 'Dia da Semana';
```

Para mostrar o dia da semana em português, basta colocar uma instrução antes do `SELECT`:

```sql
SET lc_time_names = 'pt_BR';
SELECT DAYNAME(CURDATE()) AS 'Dia da Semana';
```

#### DAYOFMONTH

Esta função mostra o dia do mês para uma data.

Exemplo:

```sql
SELECT DAYOFMONTH(CURDATE()) AS 'Dia do Mês';
```

#### DAYOFWEEK

Esta função mostra o dia da semana para uma data. Domingo é 1, segunda-feira é 2, etc.

Exemplo:

```sql
SELECT DAYOFWEEK(CURDATE()) AS 'Dia da Semana';
```

#### DAYOFYEAR

Esta função mostra o dia do ano para uma data. Um ano tem 365 dias.

Exemplo:

```sql
SELECT DAYOFYEAR(CURDATE()) AS 'Dia do Ano';
```

#### FROM_DAYS

Esta função mostra a data real referente a um número 'n' em dias.

Sintaxe: `FROM_DAYS(numero_de_dias)`

Exemplo:

```sql
SELECT FROM_DAYS(780500) AS 'Data Real';
```

No comando acima, estamos transformando a numeração informada em dias para uma data referente a esta numeração. Essa função funciona somente com o calendário gregoriano. O ano de partida é o ano 0, então estamos calculando 780.500 dias após o ano 0, que dá a data real de 08/12/2136.

#### NOW

Esta função retorna a data e hora atuais.

Exemplo:

```sql
SELECT NOW() AS 'Data/Hora Atual';
```

Neste próximo exemplo iremos usar a formatação brasileira:

```sql
SELECT DATE_FORMAT(NOW(), '%d/%m/%Y %h:%m:%s') AS 'Data/Hora Atual';
```

Existe outra função que faz o mesmo que a função `NOW()`, e ela é a `CURRENT_TIMESTAMP()`.

#### TIME

Esta função extrai somente a hora de um tempo.

Exemplo:

```sql
SELECT TIME(CURRENT_TIMESTAMP()) AS 'Hora';
```

#### SEC_TO_TIME

Esta função retorna um valor convertido em horas, minutos e segundos.

A sintaxe é: `SEC_TO_TIME(segundos)`

Exemplo:

```sql
SELECT SEC_TO_TIME(2000) AS 'Tempo Total';
```

No exemplo acima, estamos convertendo 2000 segundos para um tempo em horas, minutos e segundos.

#### TIME_TO_SEC

Esta função é o oposto da função anterior.

Exemplo:

```sql
SELECT TIME_TO_SEC(NOW()) AS 'Tempo Total';
```

#### HOUR, MINUTE, SECOND

Estas funções extraem a hora, o minuto e o segundo de um tempo, respectivamente.

Exemplo:

```sql
SELECT 
   HOUR(NOW()) AS Hora,
   MINUTE(NOW()) AS Minuto,
   SECOND(Now()) AS Segundo;
```

#### PERIOD_DIFF

Retorna o número de meses entre dois períodos, que devem estar no formato yymm ou yyyymm.

Sintaxe: `PERIOD_DIFF(periodo1, periodo2)`

Exemplo:

```sql
SELECT PERIOD_DIFF(202312, 202308) AS 'Meses Restantes';
```

No comando acima, estamos calculando a diferença em meses entre 12/2023 e 08/2023.

#### TIME_DIFF

Esta função funciona como a função anterior, mas ela calcula a diferença entre horas.

Exemplo:

```sql
SELECT TIME_DIFF('12:35:34', '12:30:46') AS 'Diferença';
```

#### QUARTER

Esta função mostra o trimestre do ano para uma data.

Exemplo:

```sql
SELECT QUARTER('2019-03-17') AS 'Trimestre do Ano';
```

#### WEEK

Esta função mostra a semana do ano para uma data.

Exemplo:

```sql
SELECT WEEK('2019-03-17') AS 'Semana do Ano';
```

#### WEEKDAY

Esta função mostra o dia da semana que inicia com segunda-feira para uma data.

Exemplo:

```sql
SELECT WEEKDAY('2019-03-17') AS 'Dia da Semana';
```

No comando acima, temos o número do dia da semana para a data informada.

#### YEAR

Esta função mostra o ano de uma data.

Exemplo:

```sql
SELECT YEAR('2019-03-17') AS 'Ano';
```

#### MONTH

Esta função mostra o mês de uma data.

Exemplo:

```sql
SELECT MONTH('2019-03-17') AS 'Mês';
```

#### DAY

Esta função mostra o dia de uma data.

Exemplo:

```sql
SELECT DAY('2019-03-17') AS 'Dia';
```

### Subconsultas

De forma geral, grande parte das consultas realizadas em bancos de dados podem ser resolvidas de forma simples, todavia existem casos em que é necessário aumentar a complexidade dessas consultas, até mesmo para facilitar o resultado final e melhorar a leitura delas. Por isso, precisamos das subconsultas ou *subqueries*.

Uma subconsulta é uma instrução `SELECT` dentro de outro `SELECT`, que retorna algumas colunas específicas que são usadas em algumas funções, como `INSERT`, `UPDATE` e `DELETE`, por exemplo.

Uma subconsulta é chamada de consulta interna, enquanto que a consulta que a contém é chamada de consulta externa.

Considere o seguinte código:

```sql
CREATE DATABASE subconsulta;

USE subconsulta;

CREATE TABLE escritorios(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   pais VARCHAR(30) NOT NULL
);

CREATE TABLE funcionarios(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   nome VARCHAR(20) NOT NULL,
   sobrenome VARCHAR(20) NOT NULL,
   id_escritorio INT NOT NULL,
   FOREIGN KEY (id_escritorio) REFERENCES escritorios(id)
);

CREATE TABLE pagamentos(
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   id_funcionario INT NOT NULL,
   salario DECIMAL(9,2) NOT NULL,
   data DATE NOT NULL,
   FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
);

INSERT INTO escritorios (pais) VALUES ('Brasil');
INSERT INTO escritorios (pais) VALUES ('Estados Unidos');
INSERT INTO escritorios (pais) VALUES ('Alemanha');
INSERT INTO escritorios (pais) VALUES ('França');

INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Pedro', 'Souza', 1);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Sandra', 'Rubin', 2);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Mikail', 'Schumer', 3);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Olivier', 'Gloçan', 4);

INSERT INTO pagamentos (id_funcionario, salario, data)
VALUES(1, '5347.55', '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data)
VALUES(2, '9458.46', '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data)
VALUES(3, '4669.97', '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data)
VALUES(4, '2770.32', '2019-03-17');
```

#### Realizando uma subconsulta

Quando uma consulta é executada, sua subconsulta é executada primeiro, e retorna um conjunto de resultados. Em seguida, esse conjunto de resultados é usado como uma entrada da consulta externa.

```sql
SELECT nome, sobrenome
FROM funcionarios
WHERE id_escritorio IN (
   SELECT id 
   FROM escritorios 
   WHERE pais = 'Brasil'
);
```

No exemplo acima, estamos selecionando os campos "nome" e "sobrenome" da tabela de funcionário em que o id do escritório esteja dentro do resultado da subconsulta.

Também é possível obter o mesmo resultado utilizando uma consulta comum. Veja o código abaixo:

```sql
SELECT nome, sobrenome
FROM funcionarios, escritorios AS e
WHERE id_escritorio = e.id AND e.pais= 'Brasil';
```

Outro exemplo:

```sql
SELECT 
   f.nome, 
   f.sobrenome, 
   e.pais, 
   p.salario
FROM 
   pagamentos AS p, 
   funcionarios AS f, 
   escritorios AS e
WHERE 
   f.id_escritorio = e.id
   AND f.id = p.id_funcionario
   AND salario = (
      SELECT MAX(salario) FROM pagamentos
   );
```

No exemplo acima, estamos efetuando uma junção de tabela por produto cartesiano, utilizando uma função agregada e uma subconsulta para ver quem tem o maior salário na empresa.

Outro exemplo:

``` sql
SELECT nome
FROM funcionarios AS f, pagamentos AS p
WHERE f.id = p.id_funcionario AND p.salario > '5000';

SELECT nome
FROM funcionarios
WHERE funcionarios.id IN (
  SELECT id_funcionario
  FROM pagamentos
  WHERE salario > '5000'
);
```

No exemplo acima estamos consultando quem ganha mais de 5 mil.

Outro exemplo:

```sql
SELECT 
   f.nome,
   f.sobrenome,
   e.pais,
   p.salario
FROM 
   pagamentos AS p,
   funcionarios AS f,
   escritorios AS e
WHERE
   f.id_escritorio = e.id
   AND f.id = p.id_funcionario
   AND salario < (
      SELECT AVG(salario) FROM pagamentos
   );
```

O exemplo acima se parece bastante com o exemplo anterior. A diferença é que estamos vendo quem ganha menos que a média.

## Introdução ao MySQL

O servidor de banco de dados MySQL (SGBD) foi lançado pela empresa MySQL AB em 23 de maio de 1995. Nesse tempo, a Internet estava dando seus primeiros passos ao público em geral, e esse banco de dados, junto com a linguagem PHP, praticamente nasceram juntos e dominaram a Internet por muito tempo.

A empresa MySQL AB lançou o banco de dados MySQL como um *software* *open-source* desde seu início. Isso significa que o código fonte, desenvolvido em C e C++, estava disponível para qualquer pessoa ler, modificar e ajudar a melhorar o sistema.

Em janeiro de 2008, a empresa Sun Microsystems comprou a MySQL AB por U$ 1 bilhão. Em abril de 2009, a empresa Oracle comprou a Sun Microsystems por U$ 7.4 bilhões. Por conta dessas compras, a comunidade do MySQL aproveitou que seu código era open-source e criou um *fork* (ou bifurcação) do projeto chamando-o de MariaDB, que pretende manter o máximo de compatibilidade possível com o MySQL, mas adicionando suas próprias melhorias. Sendo assim, hoje podemos utilizar tanto o MySQL, oferecido hoje pela Oracle, ou o MariaDB, que tem o suporte da comunidade.

O servidor MySQL é utilizado por empresas do mundo inteiro, incluindo: Google, Facebook, Twitter, Flickr e YouTube.

### Console do MySQL

Quando instalado, o MySQL Server não apresenta nenhuma interface gráfica para o usuário, sendo assim, é necessário que o usuário utilize o console.

Para iniciar o console MySQL, abra o terminal e digite:

`mysql -u root -p`

Logo após digitar isso, você vai precisar usar a senha do usuário root que você cadastrou durante a instalação. O singificado desse comando é:

* `mysql`: acesse o MySQL;
* `-u`: Indica o usuário;
* `root`: Esse é o nome de usuário;
* `-p`: Indica a senha (password).

Logo após dar ENTER, você poderá digitar sua senha. Você não pode digitar a senha logo na frente do `-p` porque daria pra ver qual é a senha. Quando você dá ENTER, o console te deixa digitar a senha trocando os seus caracteres por asteriscos, assim não dá pra ver qual é a senha.

#### Criando usuários

Não é recomendado utilizar o servidor de banco de dados com o usuário administrador. O ideal é criar um ou mais usuários com poderes reduzidos para cada novo projeto que criamos.

Para criar um usuário digite o seguinte comando:

```sql
CREATE USER 'nome'@'localhost' IDENTIFIED BY 'senha';
```

Substitua `'nome'` e `'senha'` pelo nome de usuário e senha desejados.

O `'@localhost'` significa que o usuário está sendo criado na máquina local.

Depois disso, dê privilégios de ação ao novo usuário:

```sql
GRANT ALL PRIVILEGES ON base_de_dados.* TO 'nome'@'localhost' WITH GRANT OPTION;
```

Troque `base_de_dados` pelo nome da base na qual você deseja dar privilégios ao usuário. Você pode usar o asterisco nesse mesmo lugar para se referir a todas as bases de dados.

Por fim, use o `FLUSH PRIVILEGES` para que as mudanças sejam efetivadas. Esse comando é usado para recarregar os privilégios da tabela de privilégios do MySQL.

```sql
FLUSH PRIVILEGES;
```

Agora para logar com o usuário que você acabou de criar você pode utilizar o mesmo comando que utiliza para logar com o administrador. Primeiramente é necessário que você saia do console escrevendo o comando `EXIT;`, e então entre com o novo usuário:

`mysql -u nome -p`

`nome` é deve ser substituído pelo nome que você escolheu para o seu usuário.

E então digite sua senha.

#### Comandos úteis

Você pode verificar os bancos de dados existentes pelo seguinte comando:

```sql
SHOW DATABASES;
```

Inicialmente, aparecerá quatro bancos de dados, que são os bancos de dados que são instalados por padrão quando você instala o servidor MySQL. Eles são necessários para o servidor de dados.

**Escolhendo um banco de dados**

Podemos usar um banco de dados utilizando o seguinte comando 

```sql
USE nome_banco;
```

`nome_banco` deve ser substituído pelo nome do banco de dados.

**Mostrando as tabelas**

Podemos ver todas as tabelas de um banco de dados usando o seguinte comando 

```sql
SHOW TABLES;
```

### Códigos SQL

Primeiramente precisamos criar o banco de dados, as tabelas e então populá-las. Aqui está o código para fazer isso:

```sql
CREATE DATABASE secao04;

USE secao04;

CREATE TABLE  tipos_produto(
	codigo INT NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(30) NOT NULL,
    PRIMARY KEY (codigo)
);

CREATE TABLE produtos(
	codigo INT NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(30) NOT NULL,
    preco DECIMAL(9, 2) NOT NULL,
    codigo_tipo INT NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codigo_tipo) REFERENCES tipos_produto (codigo)
);

INSERT INTO tipos_produto (descricao) VALUES ('Computadores');
INSERT INTO tipos_produto (descricao) VALUES ('Impressoras');

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', '1200', '1');
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Laptop', '1800', '1');
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impressora Jato de Tinta', '300', '2');
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impressora Laser', '500', '2');
```

**Prática DQL**

```sql
-- Selecionando tudo
SELECT * FROM tipos_produto;

SELECT * FROM produtos;

-- Selecionando com alias
SELECT
	p.codigo AS cod,
    p.descricao AS descri,
    p.preco AS pre,
    p.codigo_tipo AS ctp
FROM produtos AS p;
```

**Prática DML**

```sql
-- Adicionando novos produtos
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Notebook', '1200', '1');
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Macbook Pro', '7200', '1');
-- Adicionando um novo tipo
INSERT INTO tipos_produto (descricao) VALUES ('Apple');
-- Adicionando um novo produto com o novo tipo
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Macbook Air', '5200', '3');
-- Fazendo a alteração de dados
UPDATE produtos SET codigo_tipo = 3 WHERE codigo = 6;
UPDATE produtos SET descricao = 'Impressora a Laser', preco = '700' WHERE codigo = 4;
UPDATE produtos SET codigo_tipo = 2 WHERE codigo >= 6;
DELETE FROM tipos_produto WHERE codigo = 3;
```

**Prática DDL**

Primeiro criaremos um novo banco de dados e uma nova tabela:

```sql
CREATE DATABASE treino;
USE treino;
CREATE TABLE pessoas(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);
```

O comando `CREATE` já faz parte da DDL.

Agora adicionaremos um campo a tabela:

```sql
ALTER TABLE pessoas ADD ano_nascimento INT NOT NULL;
```

Excluindo uma tabela:

```
DROP TABLE pessoas;
```

**Prática DCL**

No console MySQL:

```sql
GRANT ALL PRIVILEGES ON secao04.* TO 'user'@'localhost' WITH GRANT OPTION;
```

**Prática DTL**

```sql
START TRANSACTION;
	INSERT INTO tipos_produto (descricao) VALUES ('Acessórios');
    INSERT INTO tipos_produto (descricao) VALUES ('Equipamentos');
COMMIT;
```

## PostgreSQL

O servidor de bancos de dados PostgreSQL (SGBD) teve seu projeto iniciado na década de 1980 na Universidade de Berkeley, com o nome de Ingres, e posteriormente teve seu nome alterado para Post Ingres. Por fim, foi lançado em sua verção inical como PostgreSQL em 1996.

O PostgreSQL é um banco de dados open-source, e foi pioneiro em muitos dos conceitos que só se tornaram disponíveis em alguns sitemas de bancos de dados comerciais mais tarde. Ele é usado por milhares de empresas, incluindo: Uber, Spotify, Instagram, Netflix, Reddit, Twitch, etc.

### Código SQL da seção 3

**Criando tabelas**

```sql
CREATE TABLE tipos_produtos(
	id SERIAL PRIMARY KEY,
	descricao CHARACTER VARYING(50) NOT NULL
);

CREATE TABLE produtos(
	id SERIAL PRIMARY KEY,
	descricao CHARACTER VARYING(50) NOT NULL,
	preco MONEY NOT NULL,
	id_tipo INT REFERENCES tipos_produtos(id) NOT NULL
);

CREATE TABLE cadastro_paciente(
	id SERIAL PRIMARY KEY,
	nome CHARACTER VARYING(50) NOT NULL,
	endereco CHARACTER VARYING(50) NOT NULL,
	bairro CHARACTER VARYING(40) NOT NULL,
	cidade CHARACTER VARYING(40) NOT NULL,
	estado CHAR(2) NOT NULL,
	cep CHARACTER VARYING(7) NOT NULL,
	data_nascimento DATE NOT NULL
);

CREATE TABLE professores (
	id SERIAL PRIMARY KEY,
	telefone INT NOT NULL, -- indicado pelo professor
	nome CHARACTER VARYING(50) NOT NULL
);

CREATE TABLE turmas (
	id SERIAL PRIMARY KEY,
	capacidade INT NOT NULL,
	id_professor INT REFERENCES professores(id)
);
```

No PostgreSQL, o tipo `SERIAL` significa que o tipo é int e que se auto-incrementa. O `CHARACTER VARYING` é o mesmo `VARCHAR` do MySQL. O PostgreSQL também tem o `VARCHAR`, mas o `CHARACTER VARYING` é mais usado.

**Inserindo Dados**

```sql
INSERT INTO tipos_produtos (descricao) VALUES ('Computador');
INSERT INTO tipos_produtos (descricao) VALUES ('Impressoras');
INSERT INTO tipos_produtos (descricao) VALUES ('Diversos');

INSERT INTO produtos (descricao, preco, id_tipo) 
VALUES ('Notebook DELL 1544', 2345.67, 1);
INSERT INTO produtos (descricao, preco, id_tipo) 
VALUES ('Impr. Jato de Tinta', 456.00, 2);
INSERT INTO produtos (descricao, preco, id_tipo) 
VALUES ('Mouse Sem Fio', 45.00, 3);

INSERT INTO cadastro_paciente (
	nome, endereco, bairro, cidade, 
	estado, cep, data_nascimento
)
VALUES (
	'Angelina Jolie', 'Rua da paz, 44', 'Nova Lima',
	'Santos', 'SP', '123123', '1978-04-24'
);
```

### Código SQL da seção 4

**DDL**:

```sql
-- Criando uma tabela para armazenar informaçoes sobre usuários
CREATE TABLE users (
    user_id serial PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL,
    email VARCHAR (100) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- Criando uma tabela para armazenar posts
CREATE TABLE posts (
    post_id serial PRIMARY KEY,
    title VARCHAR (255) NOT NULL,
    content TEXT,
    user_id INT REFERENCES users(user_id),
    created_at TIMESTAMP NOT NULL
);

/* Adicionando uma constraint de chave estrangeira
* Essa constraint faz com que o id do usuário na tabela
* postsreferencie um usuário válido na tabela de usuários.
*/
ALTER TABLE posts
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id)
REFERENCES users(user_id);
```

**DQL**

```sql
-- Selecionando todos os usuários da tabela "usuarios"
SELECT * FROM users;

-- Selecionando colunas específicas da tabela "usuarios"
SELECT user_id, username FROM users;

-- Selecionando todos os posts da tabela "posts"
SELECT * FROM posts;

-- Selecionando posts com um id de usuário específico
SELECT * FROM posts WHERE user_id = 1;

-- Fazendo join com as tabelas para conseguir os detalhes das duas
SELECT u.username, p.title
FROM users u
INNER JOIN posts p ON u.user_id = p.user_id;

-- Calculando o número total de posts para cada usuário e ordenando os resultados
SELECT u.username, COUNT(p.post_id) AS post_count
FROM users u
LEFT JOIN posts p ON u.user_id = p.user_id
GROUP BY u.username
ORDER BY post_count DESC;

-- Encontrando os usuários que nunca criaram um post
SELECT u.username
FROM users u
LEFT JOIN posts p ON u.user_id = p.user_id
WHERE p.post_id IS NULL;
```

**DML**

```sql
-- Inserindo um novo usuário na tabela de usuários
INSERT INTO users (username, email, created_at)
VALUES
    ('john_doe', 'john.doe@example.com', NOW()),
    ('jane_smith', 'jane.smith@example.com', NOW());

-- Inserindo novos posts na tabela de posts
INSERT INTO posts (title, content, user_id, created_at)
VALUES
    ('Post 1', 'This is the content of post 1', 1, NOW()),
    ('Post 2', 'This is the content of post 2', 2, NOW());

-- Atualizando o endereço de email de um usuário
UPDATE users
SET email = 'new_email@example.com'
WHERE username = 'john_doe';

-- Atualizando o conteúdo de um post
UPDATE posts
SET content = 'Updated content for Post 1'
WHERE post_id = 1;

-- Deletando um usuário e seus posts
DELETE FROM users
WHERE username = 'jane_smith';

-- Deletando um post específico
DELETE FROM posts
WHERE post_id = 2;
```

**DCL**

```sql
-- Criando um novo usuário
CREATE USER myuser WITH PASSWORD 'mypassword';

-- Dando os privilégios SELECT e INSERT na tabela "usuarios"
GRANT SELECT, INSERT ON users TO myuser;

-- Dando os privilégios SELECT, INSERT, UPDATE, e DELETE na tabela "posts"
GRANT SELECT, INSERT, UPDATE, DELETE ON posts TO myuser;

-- Revogando os privilégios de INSERT na tabela "usuários"
REVOKE INSERT ON users FROM myuser;

-- Revogando todos os privilégios da tabela "posts"
REVOKE ALL PRIVILEGES ON posts FROM myuser;

-- Dando o privilégio de uso na arquivo de sequência "user_id_seq"
GRANT USAGE ON SEQUENCE user_id_seq TO myuser;

-- Dando privilégios de superusuário
ALTER USER myuser WITH SUPERUSER;

-- Revogando privilégios de superusuário
ALTER USER myuser WITH NOSUPERUSER;

-- Removendo o usuário
DROP USER myuser;
```

**TCL**

```sql
-- Começando uma nova transação
BEGIN;

-- Inserindo um novo usuário
INSERT INTO users (username, email, created_at)
VALUES ('alice', 'alice@example.com', NOW());

-- Inserindo um novo post
INSERT INTO posts (title, content, user_id, created_at)
VALUES ('Post by Alice', "This is Alice's post", 3, NOW());

-- Commitando a transação para salvar as mudanças
COMMIT;

-- Começando uma nova transação
BEGIN;

-- Atualizando o email de usuário
UPDATE users
SET email = 'new_email@example.com'
WHERE username = 'alice';

-- Fazendo um rollback para desfazer as mudanças
ROLLBACK;

-- Começando uma nova transação
BEGIN;

-- Deletando um post específico
DELETE FROM posts
WHERE title = 'Post by Alice';

-- Commitando a transação
COMMIT;
```

**Código usado na aula**

```sql
CREATE TABLE tipos_produto (
	codigo SERIAL NOT NULL,
	descricao VARCHAR(30) NOT NULL,
	PRIMARY KEY (codigo)
);

CREATE TABLE produtos (
	codigo SERIAL PRIMARY KEY,
	descricao VARCHAR(30) NOT NULL,
	preco MONEY NOT NULL,
	codigo_tipo INT NOT NULL,
	FOREIGN KEY (codigo_tipo) REFERENCES tipos_produto(codigo)
);

INSERT INTO tipos_produtos (descricao) VALUES ('Computador');
INSERT INTO tipos_produtos (descricao) VALUES ('Impressoras');
INSERT INTO tipos_produtos (descricao) VALUES ('Diversos');

INSERT INTO produtos (descricao, preco, codigo_tipo) 
VALUES ('Notebook DELL 1544', 2345.67, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) 
VALUES ('Impr. Jato de Tinta', 456.00, 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) 
VALUES ('Mouse Sem Fio', 45.00, 3);
```

```sql
SELECT 
	p.codigo AS cod,
	p.descricao AS descr,
	p.preco AS pre,
	p.codigo_tipo AS ctp
FROM produtos AS p;
```

```sql
UPDATE tipos_produto SET descricao = 'Nobreak' WHERE codigo = 3;
```

```sql
DELETE FROM produtos WHERE codigo = 1;
```

```sql
ALTER TABLE tipos_produto ADD peso DECIMAL(8, 2);
```

```sql
DROP TABLE produtos;
```

```sql
CREATE USER estagiario WITH PASSWORD 'estagiario';
```

```sql
GRANT ALL ON empresas TO estagiario;
GRANT USAGE, SELECT ON SEQUENCE empresas_id_seq TO estagiario;
```

O PostgreSQL não dá um GRANT completo. Por isso é necessária a segunda linha de código no exemplo acima. Se você for apagar esse usuário, você vai  ter que remover essa permissão adicional também, senão não dá pra apagar o usuário.

```sql
REVOKE ALL ON empresas FROM estagiario;
```

```sql
GRANT SELECT ON empresas TO estagiario;
```

```sql
REVOKE USAGE, SELECT ON SEQUENCE empresas_id_seq FROM estagiario;
```

```sql
DROP USER estagiario;
```

```sql
BEGIN TRANSACTION;

INSERT INTO tipos_produtos (descricao) VALUES ('Equipamentos');
INSERT INTO tipos_produtos (descricao) VALUES ('Nobreak');

COMMIT;
```

### Código SQL da seção 5

**Criação e consulta**

```sql
CREATE TABLE tipos_produto(
	codigo SERIAL PRIMARY KEY,
	descricao VARCHAR(50) NOT NULL
);

CREATE TABLE produtos(
	codigo SERIAL PRIMARY KEY,
	descricao VARCHAR(50) NOT NULL,
	preco MONEY NOT NULL,
	codigo_tipo INT REFERENCES tipos_produto(codigo)
);

INSERT INTO tipos_produto (descricao) VALUES ('Computador');
INSERT INTO tipos_produto (descricao) VALUES ('Impressora');

INSERT INTO produtos (descricao, preco, codigo_tipo)
VALUES ('Desktop', 1200, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo)
VALUES ('Laptop', 1800, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo)
VALUES ('Impr. Laser', 500, 2);
INSERT INTO produtos (descricao, preco, codigo_tipo)
VALUES ('Impr. Jato de Tinta', 300, 2);

SELECT * FROM tipos_produto WHERE codigo = 1;

SELECT * FROM produtos WHERE descricao = 'Laptop';

SELECT * FROM produtos WHERE preco <= '500';

SELECT
	p.codigo AS "Código",
	p.descricao AS "Descrição",
	p.preco AS "Preço",
	tp.descricao AS "Tipo Produto"
FROM 
	produtos AS p, 
	tipos_produto AS tp
WHERE 
	p.codigo_tipo = tp.codigo;
```

**Junções**

```sql
CREATE DATABASE juncao;

CREATE TABLE profissoes(
	id SERIAL PRIMARY KEY,
	cargo VARCHAR(60) NOT NULL
);

CREATE TABLE clientes(
	id SERIAL PRIMARY KEY, 
	nome VARCHAR(60) NOT NULL,
	data_nascimento DATE NOT NULL,
	telefone VARCHAR(10) NOT NULL,
	id_profissao INT  REFERENCES profissoes(id) NOT NULL
);

CREATE TABLE consumidor(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    contato VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    pais VARCHAR(50) NOT NULL
);

INSERT INTO profissoes (cargo) VALUES ('Programador');
INSERT INTO profissoes (cargo) VALUES ('Analista de Sistemas');
INSERT INTO profissoes (cargo) VALUES ('Suporte');
INSERT INTO profissoes (cargo) VALUES ('Gerente');

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao)
VALUES ('João Pereira', '1981-06-15', '1234-5688', 1);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao)
VALUES ('Ricardo da Silva', '1973-10-10', '2234-5669', 2);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao)
VALUES ('Felipe Oliveira', '1987-08-01', '4234-5640', 3);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao)
VALUES ('Mário Pirez', '1991-02-05', '5234-5621', 1);

INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais)
VALUES ('Alfredo Nunes', 'Maria Nunes', 'Rua da paz, 47', 'São Paulo', '123.456-87', 'Brasil');
INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais)
VALUES ('Ana Trujillo', 'Guilherme Souza', 'Rua Dourada, 452', 'Goiânia', '232.984-23', 'Brasil');
INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais)
VALUES ('Leandro Veloz', 'Pedro Siqueira', 'Rua Vazia, 72', 'São Paulo', '936.738-23', 'Brasil');

-- Junção de produto cartesiano
SELECT 
	c.id, 
	c.nome, 
	c.data_nascimento, 
	c.telefone, 
	p.cargo 
FROM 
	clientes AS c, 
	profissoes AS p
WHERE c.id_profissao = p.id;

-- Inner Join
SELECT 
	c.id, c.nome, 
	c.data_nascimento, 
	c.telefone, 
	p.cargo
FROM clientes AS c 
INNER JOIN profissoes AS p
ON  c.id_profissao = p.id;

-- Left Outer Join
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Right Outer Join
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Full Outer Join -- Funciona no PostgreSQL mas nao funciona no MySQL
SELECT * FROM clientes
FULL OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Full Outer Join (Versão MySQL)
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id
UNION
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Cross Join
SELECT 
	c.id, c.nome, 
	c.data_nascimento,
	c.telefone, 
	p.cargo
FROM clientes AS c
CROSS JOIN profissoes AS p;

-- Self Join
SELECT 
	a.nome AS Consumidor1, 
	b.nome AS Consumidor2, 
	a.cidade
FROM consumidor AS a
INNER JOIN consumidor AS b
ON a.id <> b.id
AND a.cidade = b.cidade
ORDER BY a.cidade;
```

**Funções de agregação**

```sql
CREATE DATABASE agregacao;

CREATE TABLE categorias(
	id SERIAL PRIMARY KEY,
 	nome VARCHAR(60) NOT NULL
);

CREATE TABLE produtos(
	id SERIAL PRIMARY KEY, 
	descricao VARCHAR(60) NOT NULL,
	preco_venda DECIMAL(8,2) NOT NULL,
	preco_custo MONEY NOT NULL,
	id_categoria INT REFERENCES categorias(id) NOT NULL
);

INSERT INTO categorias (nome) VALUES ('Material Escolar');
INSERT INTO categorias (nome) VALUES ('Acessório Informática');
INSERT INTO categorias (nome) VALUES ('Material Escritório');
INSERT INTO categorias (nome) VALUES ('Game');

INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Caderno', 5.45, 2.30, 1);
INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Caneta', 1.20, 0.45, 1);
INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Pendrive 32GB', 120.54, 32.55, 2);
INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Mouse', 17.00, 4.30, 2);

-- max
SELECT MAX(preco_venda) FROM produtos;

-- min
SELECT MIN(preco_venda) FROM produtos;

SELECT AVG(preco_custo) FROM produtos; -- não funciona porque é tipo Money

SELECT AVG(preco_venda) FROM produtos; -- precisão grande

SELECT TO_CHAR(AVG(preco_venda),'99999999D99') AS Media FROM produtos; -- Formatado para string. O D indica as casas decimais. Cada nove representa um dígito

SELECT ROUND(AVG(preco_venda)::numeric,2) FROM produtos; -- Formatado para numerico

SELECT ROUND(AVG(preco_custo::numeric), 2) FROM produtos; -- Calculando a média de valor Money. Estamos fazendo um casting

SELECT ROUND(AVG(preco_venda), 4) FROM produtos;

SELECT COUNT(preco_venda) AS Quantidade FROM produtos WHERE id_categoria = 1;

-- group by
SELECT id_categoria, MAX(preco_venda) FROM produtos GROUP BY id_categoria;

-- having
SELECT id_categoria, MAX(preco_venda) FROM produtos GROUP BY id_categoria HAVING MAX(preco_venda) > 10;
```

**Agrupamento**

```sql
CREATE DATABASE agrupamento;

CREATE TABLE tipos(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(60) NOT NULL
);

CREATE TABLE fabricantes(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(60) NOT NULL
);

CREATE TABLE produtos(
	id SERIAL PRIMARY KEY, 
	nome VARCHAR(60) NOT NULL,
	id_fabricante INT REFERENCES fabricantes(id) NOT NULL,
	quantidade INT NOT NULL,
	id_tipo INT REFERENCES tipos(id) NOT NULL
);

INSERT INTO tipos (nome) VALUES ('Console');
INSERT INTO tipos (nome) VALUES ('Notebook');
INSERT INTO tipos (nome) VALUES ('Celular');
INSERT INTO tipos (nome) VALUES ('Smartphone');
INSERT INTO tipos (nome) VALUES ('Sofá');
INSERT INTO tipos (nome) VALUES ('Armário');
INSERT INTO tipos (nome) VALUES ('Refrigerador');

INSERT INTO fabricantes (nome) VALUES ('Sony');
INSERT INTO fabricantes (nome) VALUES ('Dell');
INSERT INTO fabricantes (nome) VALUES ('Microsoft');
INSERT INTO fabricantes (nome) VALUES ('Samsung');
INSERT INTO fabricantes (nome) VALUES ('Apple');
INSERT INTO fabricantes (nome) VALUES ('Beline');
INSERT INTO fabricantes (nome) VALUES ('Magno');
INSERT INTO fabricantes (nome) VALUES ('CCE');
INSERT INTO fabricantes (nome) VALUES ('Nintendo');

INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Playstation 3', 1, 100, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Core 2 Duo 4GB RAM 500GB HD', 2, 200, 2);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Xbox 360 120GB', 3, 350, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('GT-I6220 Quad band', 4, 300, 3);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('iPhone 4 32GB', 5, 50, 4);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Playstation 2', 1, 100, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Sofá Estofado', 6, 200, 5);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Armário de Serviço', 7, 50, 6);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Refrigerador 420L', 8, 200, 7);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Wii 120GB', 8, 250, 1);

-- Group By
SELECT 
	t.nome AS Tipo, 
	f.nome AS Fabricante, 
	SUM(p.quantidade) AS Quantidade_em_Estoque 
FROM 
	tipos AS t, 
	fabricantes AS f, 
	produtos AS p 
WHERE 
	t.id = p.id_tipo 
	AND f.id = p.id_fabricante 
GROUP BY 
	t.nome, 
	f.nome;

-- Having
SELECT 
	t.nome AS Tipo, 
	f.nome AS Fabricante, 
	SUM(p.quantidade) AS Quantidade_em_Estoque 
FROM 
	tipos AS t, 
	fabricantes AS f, produtos AS p 
WHERE 
	t.id = p.id_tipo 
	AND f.id = p.id_fabricante 
GROUP BY 
	t.nome, 
	f.nome
HAVING 
	SUM(p.quantidade) > 200;

-- Order By ASC
SELECT 
	id, 
	nome, 
	id_fabricante, 
	quantidade, 
	id_tipo 
FROM produtos 
ORDER BY id DESC LIMIT 3;

SELECT id, nome, id_tipo, id_fabricante, quantidade  FROM produtos ORDER BY id ASC;

-- Order by DESC
SELECT id, nome, id_tipo, id_fabricante, quantidade FROM produtos ORDER BY quantidade DESC LIMIT 5;
```

**Data e Hora**

```sql
-- Data Atual
SELECT CURRENT_DATE AS Data_Atual;

-- Hora Atual
SELECT CURRENT_TIME AS Hora_Atual;

-- Calcular data futura
SELECT CURRENT_DATE + INTERVAL '3 DAY' AS Data_Vencimento;

SELECT CURRENT_DATE + INTERVAL '1 MONTH' AS Data_Vencimento;

SELECT CURRENT_DATE + INTERVAL '2 YEAR' AS Data_Vencimento;

-- Calcular data passada 
SELECT CURRENT_DATE - INTERVAL '3 DAY' AS Data_Matricula;

SELECT CURRENT_DATE - INTERVAL '1 MONTH' AS Data_Matricula;

SELECT CURRENT_DATE - INTERVAL '2 YEAR' AS Data_Matricula;

-- Diferenca entre datas

-- Em anos
SELECT DATE_PART('year', '2019-01-01'::date) - DATE_PART('year', '2011-10-02'::date) AS Em_anos;

-- Em meses
SELECT (DATE_PART('year', '2019-01-01'::date) - DATE_PART('year', '2011-10-02'::date)) * 12 +
(DATE_PART('month', '2019-01-01'::date) - DATE_PART('month', '2011-10-02'::date)) AS Em_meses;

-- Em semanas
SELECT TRUNC(DATE_PART('day', '2019-01-01'::timestamp - '2011-12-22'::timestamp)/7) AS Em_Semanas;

-- Em dias
SELECT DATE_PART('day', '2019-01-01'::timestamp - '2011-10-02'::timestamp) AS Em_dias;

-- Em Horas
SELECT DATE_PART('day', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp) * 24 + 
DATE_PART('hour', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp) AS Em_horas;

-- Em Minutos
SELECT (DATE_PART('day', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp) * 24 + 
DATE_PART('hour', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp)) * 60 +
DATE_PART('minute', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp) AS Em_minutos;

-- Em Segundos
SELECT ((DATE_PART('day', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp) * 24 + 
DATE_PART('hour', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp)) * 60 +
DATE_PART('minute', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp)) * 60 +
DATE_PART('second', '2019-01-01 11:55'::timestamp - '2019-01-01 09:55'::timestamp) AS Em_segundos;

-- Formatando data no PostgreSQL
SELECT TO_CHAR(CURRENT_DATE, 'dd/mm/YYYY') AS Data_Atual;

SELECT TO_CHAR(NOW(), 'dd/mm/YYYY HH24:MM:SS') AS Data_Hora_Atual;

DAYNAME PostgreSQL

-- Com inicial maiúscula
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'Day') AS Dia_da_Semana;

-- Com short maiúscula
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'Dy') AS Dia_da_Semana;

-- Com inicial minúscula
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'day') AS Dia_da_Semana;

-- Com short minúscula
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'dy') AS Dia_da_Semana;

-- Tudo maiúscula
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'DAY') AS Dia_da_Semana;

-- Mes tudo maiúsculo
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'MONTH') AS Mes;

-- Mes tudo minúsculo
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'month') AS Mes;

-- Mes iniciais minúsculo
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'mon') AS Mes;

-- Mes iniciais maiúsculo
SELECT TO_CHAR(CURRENT_TIMESTAMP, 'Mon') AS Mes;

SHOW lc_time;

SET lc_time='pt_BR.UTF8';

SELECT TO_CHAR(CURRENT_TIMESTAMP, 'TMDay') AS Dia_da_Semana;

SELECT TO_CHAR(CURRENT_TIMESTAMP, 'TMMonth') AS Mes;

-- Extraindo partes de uma data
SELECT EXTRACT(MONTH FROM CURRENT_TIMESTAMP) AS Numero_do_Mes;

SELECT EXTRACT(DAY FROM CURRENT_TIMESTAMP) AS Dia_do_Mes;

SELECT EXTRACT(YEAR FROM CURRENT_TIMESTAMP) AS Ano;

SELECT EXTRACT(WEEK FROM CURRENT_TIMESTAMP) AS Numero_da_Semana;

SELECT NOW() AS Data_hora;

SELECT EXTRACT(HOUR FROM CURRENT_TIMESTAMP) AS hora;

SELECT EXTRACT(Minute FROM CURRENT_TIMESTAMP) AS Minuto;

SELECT EXTRACT(Second FROM CURRENT_TIMESTAMP) AS Segundo;

SELECT EXTRACT(millisecond FROM CURRENT_TIMESTAMP) AS MiliSegundo;

-- Convertendo de segundos para hora
SELECT TO_CHAR((71741.733159 || 'seconds')::interval, 'HH24:MM:SS') AS Tempo_Total;

SELECT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP::time) AS Em_Segundos;
```

**Subconsultas**

```sql
CREATE DATABASE subconsulta;

CREATE TABLE escritorios(
   id SERIAL PRIMARY KEY,
   pais VARCHAR(30) NOT NULL
);

CREATE TABLE funcionarios(
   id SERIAL PRIMARY KEY, 
   nome VARCHAR(20) NOT NULL,
   sobrenome VARCHAR(20) NOT NULL,
   id_escritorio INT REFERENCES escritorios(id) NOT NULL
);

CREATE TABLE pagamentos(
   id SERIAL PRIMARY KEY,
   id_funcionario INT REFERENCES funcionarios(id) NOT NULL,
   salario DECIMAL(8,2) NOT NULL,
   data DATE NOT NULL
);

INSERT INTO escritorios (pais) VALUES ('Brasil');
INSERT INTO escritorios (pais) VALUES ('Estados Unidos');
INSERT INTO escritorios (pais) VALUES ('Alemanha');
INSERT INTO escritorios (pais) VALUES ('França');

INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Pedro', 'Souza', 1);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Sandra', 'Rubin', 2);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Mikail', 'Schumer', 3);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) 
VALUES ('Olivier', 'Gloçan', 4);

INSERT INTO pagamentos (id_funcionario, salario, data) 
VALUES (1, '5347.55', '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data) 
VALUES (2, '9458.46', '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data) 
VALUES (3, '4669.67', '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data) 
VALUES (4, '2770.32', '2019-03-17');

-- Exemplo 1
SELECT 
   nome, 
   sobrenome 
FROM funcionarios 
WHERE id_escritorio IN (
   SELECT id 
   FROM escritorios 
   WHERE pais = 'Brasil'
);

-- Sem subconsulta
SELECT 
   nome, 
   sobrenome 
FROM 
   funcionarios, 
   escritorios AS e 
WHERE 
   id_escritorio = e.id 
   AND e.pais = 'Brasil'; 

-- Exemplo 2
SELECT 
   f.nome, 
   f.sobrenome, 
   e.pais, 
   p.salario 
FROM 
   pagamentos AS p, 
   funcionarios AS f, 
   escritorios AS e
WHERE 
   f.id_escritorio = e.id 
   AND f.id = p.id_funcionario
   AND salario = (SELECT MAX(salario) FROM pagamentos);


-- Exemplo 3
SELECT 
   f.nome, 
   f.sobrenome, 
   e.pais, 
   p.salario 
FROM 
   pagamentos AS p, 
   funcionarios AS f, 
   escritorios AS e
WHERE 
   f.id_escritorio = e.id 
   AND f.id = p.id_funcionario
   AND salario < (SELECT AVG(salario) FROM pagamentos);
```

### Projeto na prática

Os analistas de sistemas estão desenvolvendo um sistema para uma empresa e foram fazer diversas entrevistas com os funcionários de diversas áreas. Ao final dessa análise de requisitos, foi gerado um documento descritivo com o que será necessário para o sistema. Sua tarefa é analisar esse documento, extrair as entidades, campos, relacionamentos e gerar o Modelo de Entidade e Relacionamento.

**Projeto Completo Parte 1 - Modelagem**

Uma pequena locadora de vídeos possui ao redor de 2000 DVDs, cujo empréstimo deve ser controlado. Cada DVD possui um número de identificação e contém um único filme. Cada filme recebe um identificador próprio, e sabe-se o título e categoria (comédia, drama, aventura, ...).

Para cada filme cadastrado há pelo menos um DVD. Além disso, filmes mais longos necessitam de dois DVDs. Os clientes podem desejar encontrar os filmes estrelados pelo seu ator predileto. Por isso, é necessário manter a informação dos atores que estrelam em cada filme, mas nem todo filme possui estrelas.

Muitos clientes, quando vêem a listagem de atores do filme escolhido, ficam interessados em saber, para um determinado ator, o seu nome real e de quais outros filmes do mesmo gênero aquele ator participou. 

A locadora possui muitos clientes cadastrados, dos quais sabe-se nome, sobrenome, telefone e endereço de contato. Além disso, cada cliente recebe um número de associado.

Finalmente o sistema deve permitir a consulta a empréstimos de DVDs, com informações de qual cliente alugou o quê, datas de empréstimo e devolução, valor pago ou a pagar, atrasos, etc.

**Resolução**

Para resolver o problema utilizaremos o site https://dbdiagram.io/home. Nele podemos criar Diagramas de Entidade e Relacionamento e podemos exportá-lo para vários formatos, inclusive o formato SQL compatível com o PostgreSQL.

Este é o código do dbdiagram:

```sql
// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

table generos {
  id int [primary key]
  genero varchar [not null]
}

Table filmes {
  id int [primary key]
  titulo varchar [not null]
  id_genero int [ref: > generos.id, not null]
  valor decimal(8,2) [not null]
}

table dvds {
  id int [primary key]
  id_filme int [ref: > filmes.id, not null]
  quantidade int [not null]
}

table atores {
  id int [primary key]
  nome varchar [not null]
}

table atores_filme {
  id int [primary key]
  id_filme int [ref: > filmes.id, not null]
  id_ator int [ref: > atores.id, not null]
  personagem varchar [not null]
}

table clientes {
  id int [primary key]
  nome varchar [not null]
  sobrenome varchar [not null]
  telefone varchar [not null]
  endereco varchar [not null]
}

table emprestimos {
  id int [primary key]
  id_cliente int [ref: > clientes.id, not null]
  id_dvd int [ref: > dvds.id, not null]
  data datetime [not null]
}

table filmes_emprestimo {
  id int [primary key]
  id_emprestimo int [ref: > emprestimos.id, not null]
  id_filme int [ref: > filmes.id, not null]
}

table devolucoes {
  id int [primary key]
  id_emprestimo int [ref: > emprestimos.id, not null]
  data datetime [not null]
}

table filmes_devolucao {
  id int [primary key]
  id_devolucao int [ref: > devolucoes.id, not null]
  id_filmes_emprestimo int [ref: > filmes_emprestimo.id, not null]
}
```

Essa ferramenta, por mais que exporte um código PostgreSQL, o código não é 100% compatível, e vai ser necessário fazer algumas mudanças para que o código funcione. Aqui vai o código SQL já mudado:

```sql
--CREATE DATABASE locadora;

CREATE TABLE "generos" (
  "id" SERIAL PRIMARY KEY,
  "genero" varchar(50) NOT NULL
);

CREATE TABLE "filmes" (
  "id" SERIAL PRIMARY KEY,
  "titulo" varchar(100) NOT NULL,
  "id_genero" int NOT NULL,
  "valor" decimal(8,2) NOT NULL
);

CREATE TABLE "dvds" (
  "id" SERIAL PRIMARY KEY,
  "id_filme" int NOT NULL,
  "quantidade" int NOT NULL
);

CREATE TABLE "atores" (
  "id" SERIAL PRIMARY KEY,
  "nome" varchar(100) NOT NULL
);

CREATE TABLE "atores_filme" (
  "id" SERIAL PRIMARY KEY,
  "id_filme" int NOT NULL,
  "id_ator" int NOT NULL,
  "personagem" varchar(100) NOT NULL
);

CREATE TABLE "clientes" (
  "id" SERIAL PRIMARY KEY,
  "nome" varchar (50) NOT NULL,
  "sobrenome" varchar (50) NOT NULL,
  "telefone" varchar (20) NOT NULL,
  "endereco" varchar (100) NOT NULL
);

CREATE TABLE "emprestimos" (
  "id" SERIAL PRIMARY KEY,
  "id_cliente" int NOT NULL,
  "id_dvd" int NOT NULL,
  "data" date NOT NULL
);

CREATE TABLE "filmes_emprestimo" (
  "id" SERIAL PRIMARY KEY,
  "id_emprestimo" int NOT NULL,
  "id_dvd" int NOT NULL
);

CREATE TABLE "devolucoes" (
  "id" SERIAL PRIMARY KEY,
  "id_emprestimo" int NOT NULL,
  "data" date NOT NULL
);

CREATE TABLE "filmes_devolucao" (
  "id" SERIAL PRIMARY KEY,
  "id_devolucao" int NOT NULL,
  "id_filmes_emprestimo" int NOT NULL
);

ALTER TABLE "filmes" ADD FOREIGN KEY ("id_genero") REFERENCES "generos" ("id");

ALTER TABLE "dvds" ADD FOREIGN KEY ("id_filme") REFERENCES "filmes" ("id");

ALTER TABLE "atores_filme" ADD FOREIGN KEY ("id_filme") REFERENCES "filmes" ("id");

ALTER TABLE "atores_filme" ADD FOREIGN KEY ("id_ator") REFERENCES "atores" ("id");

ALTER TABLE "emprestimos" ADD FOREIGN KEY ("id_cliente") REFERENCES "clientes" ("id");

ALTER TABLE "emprestimos" ADD FOREIGN KEY ("id_dvd") REFERENCES "dvds" ("id");

ALTER TABLE "filmes_emprestimo" ADD FOREIGN KEY ("id_emprestimo") REFERENCES "emprestimos" ("id");

ALTER TABLE "filmes_emprestimo" ADD FOREIGN KEY ("id_dvd") REFERENCES "dvds" ("id");

ALTER TABLE "devolucoes" ADD FOREIGN KEY ("id_emprestimo") REFERENCES "emprestimos" ("id");

ALTER TABLE "filmes_devolucao" ADD FOREIGN KEY ("id_devolucao") REFERENCES "devolucoes" ("id");

ALTER TABLE "filmes_devolucao" ADD FOREIGN KEY ("id_filmes_emprestimo") REFERENCES "filmes_emprestimo" ("id");
```

Criaremos outro banco de dados, mas desta vez utilizaremos o código escrito pelo MySQL WorkBench. Faremos as mudanças necessárias. Este é o código já editado:

```sql
-- -----------------------------------------------------
-- Table `locadora`.`atores`
-- -----------------------------------------------------
CREATE TABLE atores (
   id SERIAL PRIMARY KEY,
   nome VARCHAR(100) NOT NULL
);

-- -----------------------------------------------------
-- Table `locadora`.`generos`
-- -----------------------------------------------------
CREATE TABLE generos (
   id SERIAL PRIMARY KEY,
   genero VARCHAR(45) NOT NULL
);

-- -----------------------------------------------------
-- Table `locadora`.`clientes`
-- -----------------------------------------------------
CREATE TABLE clientes (
   id SERIAL PRIMARY KEY,
   nome VARCHAR(45) NOT NULL,
   sobrenome VARCHAR(45) NOT NULL,
   telefone VARCHAR(45) NOT NULL,
   endereco VARCHAR(45) NOT NULL
);

-- -----------------------------------------------------
-- Table `locadora`.`filmes`
-- -----------------------------------------------------
CREATE TABLE filmes (
   id SERIAL PRIMARY KEY,
   id_genero INT NOT NULL,
   titulo VARCHAR(100) NOT NULL,
   valor DECIMAL(8,2) NOT NULL,
   FOREIGN KEY (id_genero)
   REFERENCES generos (id)
);

-- -----------------------------------------------------
-- Table `locadora`.`atores_filme`
-- -----------------------------------------------------
CREATE TABLE atores_filme (
   id SERIAL PRIMARY KEY,
   id_filme INT NOT NULL,
   id_ator INT NOT NULL,
   personagem VARCHAR(100) NOT NULL,
   FOREIGN KEY (id_filme)
   REFERENCES filmes (id), 
   FOREIGN KEY (id_ator)
   REFERENCES atores (id)
);

-- -----------------------------------------------------
-- Table `locadora`.`dvds`
-- -----------------------------------------------------
CREATE TABLE dvds (
   id SERIAL PRIMARY KEY,
   id_filme INT NOT NULL,
   quantidade INT NOT NULL,
   FOREIGN KEY (id_filme)
   REFERENCES filmes (id)
);

-- -----------------------------------------------------
-- Table `locadora`.`emprestimos`
-- -----------------------------------------------------
CREATE TABLE emprestimos (
   id SERIAL PRIMARY KEY,
   id_cliente INT NOT NULL,
   data DATE NOT NULL,
   FOREIGN KEY (id_cliente)
   REFERENCES clientes (id)
);

-- -----------------------------------------------------
-- Table `locadora`.`filmes_emprestimo`
-- -----------------------------------------------------
CREATE TABLE filmes_emprestimo (
   id SERIAL PRIMARY KEY,
   id_dvd INT NOT NULL,
   id_emprestimo INT NOT NULL,
   FOREIGN KEY (id_dvd)
   REFERENCES dvds (id),
   FOREIGN KEY (id_emprestimo)
   REFERENCES emprestimos (id)
);

-- -----------------------------------------------------
-- Table `locadora`.`devolucoes`
-- -----------------------------------------------------
CREATE TABLE devolucoes (
   id SERIAL PRIMARY KEY,
   id_emprestimo INT NOT NULL,
   data DATE NOT NULL,
   FOREIGN KEY (id_emprestimo) 
   REFERENCES emprestimos (id)
);

-- -----------------------------------------------------
-- Table `locadora`.`filmes_devolucao`
-- -----------------------------------------------------
CREATE TABLE locadorafilmes_devolucao (
   id SERIAL PRIMARY KEY,
   id_devolucao INT NOT NULL,
   id_filme_emprestimo INT NOT NULL,
   FOREIGN KEY (id_devolucao)
   REFERENCES devolucoes (id),
   FOREIGN KEY (id_filme_emprestimo)
   REFERENCES filmes_emprestimo (id)
);
```

**Inserindo dados**

```sql
-- Atores
INSERT INTO atores (nome) VALUES ('Brad Pitt');
INSERT INTO atores (nome) VALUES ('Angelina Jolie');
INSERT INTO atores (nome) VALUES ('Felicity Jones');

-- Generos
INSERT INTO generos (genero) VALUES ('Comédia');
INSERT INTO generos (genero) VALUES ('Terror');
INSERT INTO generos (genero) VALUES ('Suspense');

-- Filmes
INSERT INTO filmes (titulo, id_genero, valor) 
VALUES ('Tomb Raider', 3, 8.99);
INSERT INTO filmes (titulo, id_genero, valor) 
VALUES ('Star Wars', 2, 12.99);
INSERT INTO filmes (titulo, id_genero, valor) 
VALUES ('Loucademia de Polícia', 1, 5.99);

-- Dvds
INSERT INTO dvds (id_filme, quantidade) VALUES (1, 1);
INSERT INTO dvds (id_filme, quantidade) VALUES (2, 1);
INSERT INTO dvds (id_filme, quantidade) VALUES (3, 1);

-- Clientes
INSERT INTO clientes (nome, sobrenome, telefone, endereco)
VALUES ('José', 'Pereira', '00-12345678', 'Rua do ouro - SP');
INSERT INTO clientes (nome, sobrenome, telefone, endereco)
VALUES ('Maria', 'Silva', '00-11234567', 'Rua da prata - MG');
INSERT INTO clientes (nome, sobrenome, telefone, endereco)
VALUES ('Rita', 'Souza', '00-12234567', 'Rua da paz - RJ');

-- Emprestimos
INSERT INTO emprestimos (id_cliente, data, id_dvd) VALUES (1, '2019-03-01', 1);
INSERT INTO emprestimos (id_cliente, data, id_dvd) VALUES (2, '2019-03-15', 2);
INSERT INTO emprestimos (id_cliente, data, id_dvd) VALUES (3, '2019-06-05', 3);

-- Filmes Emprestimo
INSERT INTO filmes_emprestimo (id_emprestimo, id_dvd) VALUES (1, 1);
INSERT INTO filmes_emprestimo (id_emprestimo, id_dvd) VALUES (2, 2);
INSERT INTO filmes_emprestimo (id_emprestimo, id_dvd) VALUES (3, 3);

-- Devolucoes
INSERT INTO devolucoes (id_emprestimo, data) VALUES (1, '2019-07-08');
INSERT INTO devolucoes (id_emprestimo, data) VALUES (2, '2019-07-09');
INSERT INTO devolucoes (id_emprestimo, data) VALUES (3, '2019-07-10');

-- Filmes Devolucao
INSERT INTO filmes_devolucao (id_devolucao, id_filmes_emprestimo) VALUES (1, 1);
INSERT INTO filmes_devolucao (id_devolucao, id_filmes_emprestimo) VALUES (2, 2);
INSERT INTO filmes_devolucao (id_devolucao, id_filmes_emprestimo) VALUES (3, 3);

-- Atores filme
INSERT INTO atores_filme (id_filme, id_ator, personagem)
VALUES (1, 2, 'Lara Croft');
INSERT INTO atores_filme (id_filme, id_ator, personagem)
VALUES (2, 1, 'Bartimeu');
INSERT INTO atores_filme (id_filme, id_ator, personagem)
VALUES (3, 3, 'Dona Maria');
```

**Selecionando dados**

```sql
-- Select simples

-- Atores
SELECT * FROM atores;

-- Clientes
SELECT * FROM clientes;

-- Filmes
SELECT * FROM filmes;

-- Generos
SELECT * FROM generos;

-- Filtros
SELECT * FROM generos WHERE id = 2;
SELECT * FROM generos WHERE genero = 'Terror';

-- Filmes e generos
SELECT filmes.titulo, filmes.valor, generos.genero
FROM filmes, generos
WHERE filmes.id_genero = generos.id;

-- Atores filme
SELECT 
	ato.nome AS "Nome",
	f.titulo AS "Filme",
	atof.personagem AS "Personagem"
FROM atores AS ato
INNER JOIN atores_filme AS atof
ON ato.id = atof.id_ator
INNER JOIN filmes AS f
ON f.id = atof.id_filme;

-- Funções agregadas
SELECT SUM(valor) AS "Soma" FROM filmes;
SELECT MAX(valor) AS "Preço Máximo" FROM filmes;

-- Subconsulta
SELECT * FROM filmes WHERE valor IN (SELECT MAX(valor) FROM filmes);
```

Código do professor

```sql
-- Consultas complexas
-- Encontrar todos os filmes que determinado ator atua
SELECT f.titulo, g.genero, af.personagem
	FROM atores_filme AS af, filmes AS f, generos AS g, atores AS a
	WHERE f.id = af.id_filme AND g.id = f.id_genero AND a.id = af.id_ator
	AND a.nome = 'Felicity Jones';
	
-- Encontrar todos os filmes que determinado ator atuou por genero
SELECT f.titulo, af.personagem
	FROM atores_filme AS af, filmes AS f, generos AS g, atores AS a
	WHERE f.id = af.id_filme AND g.id = f.id_genero AND a.id = af.id_ator
	AND g.genero = 'Comedia' AND a.nome = 'Bred Pitt';
	
-- Verificar qual cliente alugou o que
SELECT e.id, c.nome, c.sobrenome, e.data, f.titulo, g.genero
	FROM emprestimos AS e, clientes AS c, filmes AS f, generos AS g, dvds AS d, filmes_emprestimo AS fe
	WHERE fe.id_emprestimo = e.id AND e.id_cliente = c.id AND f.id = d.id_filme AND fe.id_dvd = d.id
	AND f.id_genero = g.id;
	
-- Verificar o que os clientes devolveram
SELECT de.id, c.nome, c.sobrenome, de.data, f.titulo
	FROM devolucoes AS de, 
		clientes AS c, 
		filmes AS f, 
		filmes_devolucao AS fd, 
		dvds AS d, 
		emprestimos AS e, 
		filmes_emprestimo AS fe
	WHERE fd.id_filme_imprestimo = fe.id
	AND fd.id_devolucao = de.id
	AND f.id = d.id_filme
	AND fe.id_dvd = d.id
	AND c.id = e.id_cliente
	AND fe.id_emprestimo = e.id;
	

-- Verificar quanto cada cliente pagou
SELECT e.id, c.nome, c.sobrenome, SUM(f.valor)
	FROM filmes_devolucao AS fd,
		clientes AS c,
		dvds AS d,
		filmes AS f,
		devolucoes AS de,
		emprestimos AS e,
		filmes_emprestimo AS fe
	WHERE fd.id_filme_imprestimo = fe.id
	AND fd.id_devolucao = de.id
	AND f.id = d.id_filme
	AND fe.id_dvd = d.id
	AND c.id = e.id_cliente
	AND fe.id_emprestimo = e.id
	GROUP BY e.id, c.nome, c.sobrenome;
```

Meu código:

```sql
-- Consultas complexas
-- Encontrando todos os filmes que determinado ator atua
SELECT
	f.titulo AS "Filme",
	g.genero AS "Genero",
	af.personagem AS "Personagem"
FROM filmes AS f
INNER JOIN generos AS g
ON f.id_genero = g.id
INNER JOIN atores_filme AS af
ON af.id_filme = f.id
INNER JOIN atores AS ato
ON f.id = af.id_filme AND af.id_ator = ato.id
WHERE ato.nome = 'Angelina Jolie';

-- Encontrar todos os filmes que determinado ator atuou por genero
SELECT
	f.titulo AS "Filme",
	g.genero AS "Genero",
	af.personagem AS "Personagem"
FROM filmes AS f
INNER JOIN generos AS g
ON f.id_genero = g.id
INNER JOIN atores_filme AS af
ON af.id_filme = f.id
INNER JOIN atores AS ato
ON f.id = af.id_filme AND af.id_ator = ato.id
WHERE ato.nome = 'Angelina Jolie' AND g.genero = 'Suspense';

-- Verificar qual cliente alugou o quê
SELECT
	cli.nome,
	cli.sobrenome,
	fil.titulo,
	emp.data
FROM clientes AS cli
INNER JOIN emprestimos AS emp
ON emp.id_cliente = cli.id
INNER JOIN filmes AS fil
ON emp.id_dvd = fil.id;

-- Verificar o que os clientes devolveram
SELECT
	cli.nome,
	cli.sobrenome,
	fil.titulo,
	dev.data AS "Devolução"
FROM clientes AS cli
INNER JOIN emprestimos AS emp
ON emp.id_cliente = cli.id
INNER JOIN filmes AS fil
ON emp.id_dvd = fil.id
INNER JOIN devolucoes AS dev
ON dev.id_emprestimo = emp.id;

-- Verificar quanto cada cliente pagou
SELECT
	cli.nome AS "Nome",
	cli.sobrenome AS "Sobrenome",
	fil.titulo AS "Título do Filme",
	fil.valor AS "Valor pago"
FROM emprestimos AS emp
INNER JOIN clientes AS cli
ON emp.id_cliente = cli.id
INNER JOIN dvds AS dvd
ON emp.id_dvd = dvd.id
INNER JOIN filmes AS fil
ON dvd.id_filme = fil.id;
```

**Atualizando dados**

```sql
UPDATE atores SET nome = 'Bread Pit Silva' WHERE id = 1;

UPDATE emprestimos SET data = '2019-08-03' WHERE id = 3;
```

**Excluindo dados**

```sql
-- Deletando um gênero
DELETE FROM filmes_devolucao WHERE id = 1;
DELETE FROM filmes_emprestimo WHERE id = 1;
DELETE FROM devolucoes WHERE id = 1;
DELETE FROM emprestimos WHERE id = 1;
DELETE FROM dvds WHERE id = 1;
DELETE FROM atores_filme WHERE id = 1;
DELETE FROM filmes WHERE id = 1;
DELETE FROM generos WHERE id = 3;
```

Porque todos os campos das tabelas são NOT NULL, é necessário excluir todos os resquícios de todas as tabelas.

## SQLite

O SQLite é uma biblioteca open-source escrita em C, que implementa um banco de dados SQL embutido. Ele não é uma biblioteca cliente usada para conectar com um grande servidor de banco de dados, mas sim o próprio servidor. Com esta biblioteca podemos ler e escrever diretamente no arquivo de banco de dados no disco. A versão 1.0 foi lançada em agosto de 2000 por D. Richard Hipp, e segue uma sintaxe SQL baseada no PostgreSQL.

O SQLite é o SGBD mais utilizado no mundo. Encontramos esta biblioteca em:

* Todo smartphone Android;
* Todo smartphone iOS;
* Todo navegador web (Firefox, Chrome, Safari, Opera, etc.);
* Toda Smart TV;
* Todo roteador Wi-Fi;

Milhares de empresas utilizam o SQLite em seus produtos, incluindo: 

- Adobe;
- Airbus;
- Apple;
- Bosch;
- Dropbox;
- Facebook;
- General Electric;
- Google;
- McAfee;
- Microsoft;
- Mozilla;
- Skype.

O SQLite não implementa certos comandos do SQL:

* RIGHT e FULL OUTER JOIN;
* ALTER TABLE não é implementado por completo. Somente: RENAME TABLE, ADD COLUMN, RENAME COLUMN;
* Gatilhos FOR EACH ROW são suportados mas não os gatilhos FOR EACH STATEMENT;
* As VIEWs são somente de leitura. Você não vai conseguir executar DELETE, INSERT ou UPDATE em uma view. Você pode criar um gatilho em uma tentativa de aplicar DELETE, INSERT ou UPDATE em uma view e fazer o que você quiser no corpo do gatilho;
* GRANT e REVOKE.

### Código da seção 3

O SQL do SQLite se parece bastante com o SQL do PostgreSQL. Somente algumas coisas mudam. 

**Criando tabelas**

```sql
CREATE TABLE tipos_produtos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL 
);

CREATE TABLE produtos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL,
	preco REAL NOT NULL,
	id_tipo_produto INTEGER NOT NULL,
	FOREIGN KEY (id_tipo_produto) REFERENCES tipos_produtos(id) 
);

CREATE TABLE pacientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	endereco TEXT NOT NULL,
	bairro TEXT NOT NULL,
	cidade TEXT NOT NULL,
	estado TEXT NOT NULL,
	cep TEXT NOT NULL,
	data_nascimento TEXT NOT NULL
);

CREATE TABLE professor (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	telefone INTEGER NOT NULL,
	nome TEXT NOT NULL
);

CREATE TABLE turma(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capacidade INTEGER NOT NULL,
	id_professor INTEGER NOT NULL,
	FOREIGN KEY (id_professor) REFERENCES professor(id)
);
```

**Inserindo dados**

```sql
-- INSERTS

-- Tipos Produto
INSERT INTO tipos_produtos (descricao) VALUES ('Computadores');
INSERT INTO tipos_produtos (descricao) VALUES ('Impressoras');
INSERT INTO tipos_produtos (descricao) VALUES ('Diversos');

-- Produtos
INSERT INTO produtos (descricao, preco, id_tipo_produto) VALUES ('Notebook DELL 1544', 2345.67, 1);
INSERT INTO produtos (descricao, preco, id_tipo_produto) VALUES ('Impr. Jato de Tinta', 456.00, 2);
INSERT INTO produtos (descricao, preco, id_tipo_produto) VALUES ('Mouse sem fio', 45, 3);

-- Pacientes
INSERT INTO pacientes (nome, endereco, bairro, cidade, estado, cep, data_nascimento) 
	VALUES ('Angelina Jolie', 'Rua da paz, 44', 'Nova Lima', 'Santos', 'SP', '121213213', '1978-04-24');

-- professor
INSERT INTO professor (telefone, nome) VALUES (12345, 'Fernando Perez');

-- TURMA 
INSERT INTO turma (capacidade, id_professor) VALUES (50, 1);

-- Selects
SELECT * FROM tipos_produtos;

SELECT * FROM produtos;

SELECT * FROM pacientes;

SELECT * FROM professor;

SELECT * FROM turma;
```

### Código da seção 4

```sql
-- CREATE DATABASE secao04;

CREATE TABLE tipos_produto(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL
);

CREATE TABLE produtos(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
	descricao TEXT NOT NULL,
	preco REAL NOT NULL,
	codigo_tipo INTEGER REFERENCES tipos_produto(codigo) NOT NULL
);


INSERT INTO tipos_produto (descricao) VALUES ('Computador');
INSERT INTO tipos_produto (descricao) VALUES ('Impressora');

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', '1200', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Laptop', '1800', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Jato Tinta', '300', 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Laser', '500', 2);

-- Select
SELECT * FROM tipos_produto;

SELECT codigo, descricao FROM tipos_produto;

SELECT * FROM produtos;

SELECT codigo, descricao, codigo_tipo FROM produtos;

-- Erro Select
SELECT cod, desc, pre, ctp FROM produtos;

-- Alias 
SELECT p.codigo AS cod, p.descricao AS descr, p.preco AS pre, p.codigo_tipo AS ctp FROM produtos AS p;
```

**DML**

```sql
INSERT INTO tipos_produto (descricao) VALUES ('Notebook');

INSERT INTO produtos(descricao, preco, codigo_tipo)
VALUES ('Notebook', 1200, 3);

UPDATE tipos_produto SET descricao = 'Nobreak' WHERE codigo = 3;

UPDATE produtos  SET descricao = 'PC', preco = "2800" WHERE codigo = 5;

UPDATE produtos SET codigo_tipo = 1 WHERE codigo_tipo = 3;

DELETE FROM tipos_produto WHERE codigo = 3;

DELETE FROM produtos;
```

**DDL**

```sql
-- Create
-- CREATE DATABASE secao04;

-- Create
CREATE TABLE tipos_produto(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL
);

-- Create
CREATE TABLE produtos(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
	descricao TEXT NOT NULL,
	preco REAL NOT NULL,
	codigo_tipo INTEGER NOT NULL,
	FOREIGN KEY(codigo_tipo) REFERENCES tipos_produto(codigo)
);

-- Alter
ALTER TABLE tipos_produto ADD peso REAL;

-- Verificando se o novo campo foi realmente adicionado
SELECT * FROM tipos_produtos;

-- Drop 
DROP TABLE tipos_produtos;

-- Não existe o comando abaixo no SQLite. Basta deletar o arquivo do banco de dados;
-- DROP DATABASE secao04;
```

**DCL**

Não existem comandos `GRANT` e `REVOKE` no SQLite.

**DTL**

```sql
-- CREATE DATABASE secao04;

CREATE TABLE tipos_produto(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL
);

CREATE TABLE produtos(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT, 
	descricao TEXT NOT NULL,
	preco REAL NOT NULL,
	codigo_tipo INTEGER NOT NULL,
	FOREIGN KEY(codigo_tipo) REFERENCES tipos_produto(codigo)
);

INSERT INTO tipos_produto (descricao) VALUES ('Computador');
INSERT INTO tipos_produto (descricao) VALUES ('Impressora');

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', '1200', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Laptop', '1800', 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Jato Tinta', '300', 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Laser', '500', 2);


-- c) Vamos consultar os dados da tabela tipos_produto;
SELECT * FROM tipos_produto;

-- d) Já temos a tabela tipos_produto, então podemos iniciar a transação;

-- Begin Transaction 
BEGIN TRANSACTION;

	INSERT INTO tipos_produto (descricao) VALUES ('Notebook');
	INSERT INTO tipos_produto (descricao) VALUES ('Nobreak');

-- Commit
COMMIT;

-- Vamos checar se os dados foram realmente salvos:
SELECT * FROM tipos_produto;

-- Roll Back

-- a) Vamos iniciar uma nova transação
BEGIN TRANSACTION;

-- b) Inserir uns dados (poderia ser insert, update, delete, etc)
INSERT INTO tipos_produto (descricao) VALUES ('Tablet');
INSERT INTO tipos_produto (descricao) VALUES ('Baterias');

-- Vamos checar se os dados foram salvos mesmo sem o commit:
SELECT * FROM tipos_produto;

-- Veja que aparentemente tudo está funcionando normalmente. Mas se tivéssemos efetuado o commit não teríamos como fazer o rollback;

-- c) Efetuando o roll back
ROLLBACK;

-- Vamos checar se os dados foram desfeitos pelo rollback:
SELECT * FROM tipos_produto;

-- Sim!

-- OBS: Como o campo id da tabela é auto incremento, os dois inserts que fizemos descartaram os valores dos campos removidos. Isso significa que os ids utilizamos não serão reutilizados.

-- Só para efeito de comparação, vamos iniciar uma nova transação, inserir dados e commitar e então tentar o rollback

-- a) Vamos iniciar uma nova transação
BEGIN TRANSACTION;

-- b) Inserir uns dados (poderia ser insert, update, delete, etc)
INSERT INTO tipos_produto (descricao) VALUES ('Tablet');
INSERT INTO tipos_produto (descricao) VALUES ('Baterias');

-- c) Commitar
COMMIT;

-- d) Consultar os dados
SELECT * FROM tipos_produto;

-- e) Tentar o rollback (Não é possível efetuar o rollback após commitar)
ROLLBACK;

-- f) Consultar os dados
SELECT * FROM tipos_produto;

-- Note que a transação não foi desfeita.
```

### Código da seção 5

**Consultas**

```sql
CREATE DATABASE secao05;

CREATE TABLE tipos_produto(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT,
	descricao TEXT NOT NULL
);

CREATE TABLE produtos(
	codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
	descricao TEXT NOT NULL,
	preco REAL NOT NULL,
	codigo_tipo INTEGER NOT NULL,
	FOREIGN KEY (codigo_tipo) REFERENCES tipos_produto(codigo)
);

INSERT INTO tipos_produto (descricao) VALUES ('Computador');
INSERT INTO tipos_produto (descricao) VALUES ('Impressora');

INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Desktop', 1200, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Laptop', 1800, 1);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Jato Tinta', 300, 2);
INSERT INTO produtos (descricao, preco, codigo_tipo) VALUES ('Impr. Laser', 500, 2);

-- Select
-- SELECT * FROM tipos_produto WHERE codigo = 1;

-- SELECT codigo, descricao FROM tipos_produto WHERE descricao = 'Computador';

-- SELECT * FROM produtos WHERE preco <= 300;

-- SELECT codigo, descricao, codigo_tipo FROM produtos WHERE descricao = 'Laptop';

-- Alias 
SELECT p.codigo AS cod, p.descricao AS desc, p.preco AS pre, p.codigo AS ctp FROM produtos AS p WHERE p.codigo = 3;
```

**Consultas em múltiplas tabelas**

```sql
SELECT * FROM tipos_produto;
SELECT * FROM produtos;

-- Conulsta em multiplas tabelas
SELECT p.codigo AS 'Codigo', p.descricao AS 'Descricao', p.preco AS 'Preco', tp.descricao AS 'Tipo Produto' 
	FROM produtos AS p, tipos_produto AS tp
    WHERE p.codigo_tipo = tp.codigo;

-- Usando INNER JOIN
SELECT
    p.codigo AS 'Código',
    p.descricao AS 'Descrição',
    p.preco AS 'Preço',
    tp.descricao AS 'Tipo de Produto'
FROM produtos AS p
INNER JOIN tipos_produto AS tp
ON p.codigo_tipo = tp.codigo;
```

**Junções**

```sql

CREATE TABLE profissoes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	cargo TEXT NOT NULL
);

CREATE TABLE clientes(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	nome TEXT NOT NULL,
	data_nascimento TEXT NOT NULL,
	telefone TEXT NOT NULL,
	id_profissao INTEGER NOT NULL,
	FOREIGN KEY (id_profissao) REFERENCES profissoes(id)
);

CREATE TABLE consumidor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    contato TEXT NOT NULL,
    endereco TEXT NOT NULL,
    cidade TEXT NOT NULL,
    cep TEXT NOT NULL,
    pais TEXT NOT NULL
);

INSERT INTO profissoes (cargo) VALUES ('Programador');
INSERT INTO profissoes (cargo) VALUES ('Analista de Sistemas');
INSERT INTO profissoes (cargo) VALUES ('Suporte');
INSERT INTO profissoes (cargo) VALUES ('Gerente');

INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('João Pereira', '1981-06-15', '1234-5688', 1);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('Ricardo da Silva', '1973-10-10', '2234-5669', 2);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('Felipe Oliveira', '1987-08-01', '4234-5640', 3);
INSERT INTO clientes (nome, data_nascimento, telefone, id_profissao) VALUES ('Mário Pirez', '1991-02-05', '5234-5621', 1);

INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais) VALUES ('Alfredo Nunes', 'Maria Nunes', 'Rua da paz, 47', 'São Paulo', '123.456-87', 'Brasil');
INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais) VALUES ('Ana Trujillo', 'Guilherme Souza', 'Rua Dourada, 452', 'Goiânia', '232.984-23', 'Brasil');
INSERT INTO consumidor (nome, contato, endereco, cidade, cep, pais) VALUES ('Leandro Veloz', 'Pedro Siqueira', 'Rua Vazia, 72', 'São Paulo', '936.738-23', 'Brasil');


-- Junção de produto cartesiano
SELECT c.id, c.nome, c.data_nascimento, c.telefone, p.cargo 
	FROM clientes AS c, profissoes AS p
    WHERE c.id_profissao = p.id;


-- Inner Join
SELECT c.id, c.nome, c.data_nascimento, c.telefone, p.cargo
FROM clientes AS c INNER JOIN profissoes AS p
ON  c.id_profissao = p.id;

-- Left Outer Join
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Right Outer Join - Não Funciona no SQLite
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Full Outer Join Não Funciona no SQLite
SELECT * FROM clientes
FULL OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Full Outer Join Versão MySQL - Não Funciona no SQLite
SELECT * FROM clientes
LEFT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id
UNION
SELECT * FROM clientes
RIGHT OUTER JOIN profissoes
ON clientes.id_profissao = profissoes.id;

-- Cross Join
SELECT c.id, c.nome, c.data_nascimento, c.telefone, p.cargo
FROM clientes AS c
CROSS JOIN profissoes AS p;

-- Self Join
SELECT a.nome AS Consumidor1, b.nome AS Consumidor2, a.cidade
FROM consumidor AS a
INNER JOIN consumidor AS b
ON a.id <> b.id
AND a.cidade = b.cidade
ORDER BY a.cidade;
```

**Funções de agregação**

```sql
CREATE TABLE categorias(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE produtos(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	descricao TEXT NOT NULL,
	preco_venda REAL NOT NULL,
	preco_custo REAL NOT NULL,
	id_categoria INTEGER NOT NULL,
	FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);

INSERT INTO categorias (nome) VALUES ('Material Escolar');
INSERT INTO categorias (nome) VALUES ('Acessório Informática');
INSERT INTO categorias (nome) VALUES ('Material Escritório');
INSERT INTO categorias (nome) VALUES ('Game');

INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Caderno', 5.45, 2.3, 1);
INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Caneta', 1.20, 0.45, 1);
INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Pendrive 32GB', 120.54, 32.55, 2);
INSERT INTO produtos (descricao, preco_venda, preco_custo, id_categoria) VALUES ('Mouse', 17.00, 4.30, 2);

-- max
-- SELECT MAX(preco_venda) FROM produtos;

-- min
-- SELECT MIN(preco_venda) FROM produtos;

-- avg
-- SELECT AVG(preco_venda) FROM produtos;

-- round
-- SELECT ROUND(AVG(preco_venda), 3) FROM produtos;

-- count
-- SELECT COUNT(preco_venda) AS Quantidade FROM produtos WHERE id_categoria = 1;

-- group by
-- SELECT c.id, c.nome, MAX(p.preco_venda) FROM produtos AS p, categorias AS c WHERE c.id = p.id_categoria GROUP BY c.id;

-- having
SELECT id_categoria, MAX(preco_venda) FROM produtos GROUP BY id_categoria HAVING MAX(preco_venda) > 10;
```

**Funções de agrupamento e ordenação**

```sql
-- CREATE DATABASE agrupamento;


CREATE TABLE tipos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE fabricantes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL
);

CREATE TABLE produtos(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	nome TEXT NOT NULL,
	id_fabricante INTEGER REFERENCES fabricantes(id) NOT NULL,
	quantidade INTEGER NOT NULL,
	id_tipo INTEGER NOT NULL,
	FOREIGN KEY(id_tipo) REFERENCES tipos(id)
);

INSERT INTO tipos (nome) VALUES ('Console');
INSERT INTO tipos (nome) VALUES ('Notebook');
INSERT INTO tipos (nome) VALUES ('Celular');
INSERT INTO tipos (nome) VALUES ('Smartphone');
INSERT INTO tipos (nome) VALUES ('Sofá');
INSERT INTO tipos (nome) VALUES ('Armário');
INSERT INTO tipos (nome) VALUES ('Refrigerador');

INSERT INTO fabricantes (nome) VALUES ('Sony');
INSERT INTO fabricantes (nome) VALUES ('Dell');
INSERT INTO fabricantes (nome) VALUES ('Microsoft');
INSERT INTO fabricantes (nome) VALUES ('Samsung');
INSERT INTO fabricantes (nome) VALUES ('Apple');
INSERT INTO fabricantes (nome) VALUES ('Beline');
INSERT INTO fabricantes (nome) VALUES ('Magno');
INSERT INTO fabricantes (nome) VALUES ('CCE');
INSERT INTO fabricantes (nome) VALUES ('Nintendo');

INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Playstation 3', 1, 100, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Core 2 Duo 4GB RAM 500GB HD', 2, 200, 2);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Xbox 360 120GB', 3, 350, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('GT-I6220 Quad band', 4, 300, 3);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('iPhone 4 32GB', 5, 50, 4);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Playstation 2', 1, 100, 1);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Sofá Estofado', 6, 200, 5);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Armário de Serviço', 7, 50, 6);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Refrigerador 420L', 8, 200, 7);
INSERT INTO produtos (nome, id_fabricante, quantidade, id_tipo) VALUES ('Wii 120GB', 8, 250, 1);


-- Group By
SELECT t.nome AS Tipo, f.nome AS Fabricante, SUM(p.quantidade) AS 'Quantidade em Estoque' 
	FROM tipos AS t, fabricantes AS f, produtos AS p 
    	WHERE t.id = p.id_tipo AND f.id = p.id_fabricante 
    	GROUP BY t.nome, f.nome;


-- Having
SELECT t.nome AS Tipo, f.nome AS Fabricante, SUM(p.quantidade) AS 'Quantidade em Estoque' 
	FROM tipos AS t, fabricantes AS f, produtos AS p 
    	WHERE t.id = p.id_tipo AND f.id = p.id_fabricante 
    	GROUP BY t.nome, f.nome
    	HAVING SUM(p.quantidade) > 200;

-- Order By ASC
SELECT * FROM produtos;

SELECT id, nome, id_tipo, id_fabricante, quantidade  FROM produtos ORDER BY id ASC;

-- Order by DESC
SELECT id, nome, id_tipo, id_fabricante, quantidade FROM produtos ORDER BY quantidade DESC;
```

**Funções de data e hora**

```sql
-- SELECT date();

-- SELECT time();

-- SELECT datetime();

-- SELECT strftime('%d/%m/%Y') AS 'Data';

--SELECT strftime('%H:%M:%S') AS 'Hora';

-- SELECT strftime('%d/%m/%Y %H:%M:%S') AS 'Data Hora';

-- SELECT datetime('now', 'localtime');

-- SELECT time('now', 'localtime');

SELECT datetime(CURRENT_TIMESTAMP, 'localtime');
```

**Subconsultas**

```sql
-- CREATE DATABASE subconsulta;


CREATE TABLE escritorios(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	pais TEXT NOT NULL
);

CREATE TABLE funcionarios(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	nome TEXT NOT NULL,
	sobrenome TEXT NOT NULL,
	id_escritorio INTEGER NOT NULL,
	FOREIGN KEY(id_escritorio) REFERENCES escritorios(id)
);

CREATE TABLE pagamentos(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	salario REAL NOT NULL,
	data TEXT NOT NULL,
	id_funcionario INTEGER NOT NULL,
	FOREIGN KEY(id_funcionario) REFERENCES funcionarios(id)
);

INSERT INTO escritorios (pais) VALUES ('Brasil');
INSERT INTO escritorios (pais) VALUES ('Estados Unidos');
INSERT INTO escritorios (pais) VALUES ('Alemanha');
INSERT INTO escritorios (pais) VALUES ('França');

INSERT INTO funcionarios (nome, sobrenome, id_escritorio) VALUES ('Pedro', 'Souza', 1);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) VALUES ('Sandra', 'Rubin', 2);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) VALUES ('Mikail', 'Schumer', 3);
INSERT INTO funcionarios (nome, sobrenome, id_escritorio) VALUES ('Olivier', 'Gloçan', 4);

INSERT INTO pagamentos (id_funcionario, salario, data) VALUES (1, 5347.55, '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data) VALUES (2, 9458.46, '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data) VALUES (3, 4669.67, '2019-03-17');
INSERT INTO pagamentos (id_funcionario, salario, data) VALUES (4, 2770.32, '2019-03-17');


-- Exemplo 1
SELECT nome, sobrenome FROM funcionarios WHERE id_escritorio IN (SELECT id FROM escritorios WHERE pais = 'Brasil');

-- Sem subconsulta
SELECT nome, sobrenome FROM funcionarios, escritorios AS e WHERE id_escritorio = e.id AND e.pais = 'Brasil'; 

-- Exemplo 2
SELECT f.nome, f.sobrenome, e.pais, p.salario 
	FROM pagamentos AS p, funcionarios AS f, escritorios AS e
	WHERE f.id_escritorio = e.id 
		AND f.id = p.id_funcionario
		AND salario = (SELECT MAX(salario) FROM pagamentos);

-- Exemplo 3
SELECT f.nome, f.sobrenome, e.pais, p.salario 
	FROM pagamentos AS p, funcionarios AS f, escritorios AS e
	WHERE f.id_escritorio = e.id 
		AND f.id = p.id_funcionario
		AND salario < (SELECT AVG(salario) FROM pagamentos);
```

## MongoDB

**Observação**

O curso ensina o MongoDB na versão 4.0. No tempo em que estou estudando, a versão é a 7.0, e me parece que algumas coisas mudaram bastante. Sendo assim, decidi estudar um outro curso, no Youtube mesmo, para aprender como o MongoDB funciona.

[Este](https://www.youtube.com/playlist?list=PL4cUxeGkcC9h77dJ-QJlwGlZlTd4ecZOA) foi o curso que usei.

---

O MongoDB é um poderoso banco de dados não relacional (NoSQL) que armazena **documentos** dentro de **coleções**. O importante é entender que no final das contas, o MongoDB é um banco de dados que podemos utilizar para armazenar dados. A grande diferença é que por ele não ser um banco de dados relacional, não precisa haver qualquer tipo de relação entre os documentos armazenados.

O projeto MongoDB foi escrito na linguagem C++, é open-source e teve sua prmieira versão lançada em 11 de fevereiro de 2009. A criadora foi a empresa 10gen, que atualmente chama-se MongoDB Inc.

O MongoDB é um dos bancos de dados NoSQL mais utilizados atualmente por ser extremamente eficiente para se trabalhar com grandes quantidades de dados. Dentre as empresas que o utilizam, destacam-se: Adobe, Amadeus, Amazon, Bosch e AstraZenica.

### Coleções e documentos

Nos bancos de dados relacionais temos tabelas, já no MongoDB temos algo chamado de "coleções". Dentro delas temos o que chamamos de "documentos". Esses documentos se parecem bastante com objetos do JavaScript ou arquivos JSON com chaves e valores.

Exemplo de documento:

```json
{
   "title":"Name of the Wind",
   "rating":9,
   "pages":400
}
```

Podemos ter documentos dentro de documentos:

```json
{
   "title":"Name of the Wind",
   "rating":9,
   "pages":400,
   "author":{
      "first_name":"John",
      "last_name":"Doe"
   }
}
```

Um documento dentro de outro seria uma alternativa ao uso de duas tabelas diferentes em SQL. Também é possível ter duas coleções diferentes se você preferir.

Dependendo da sua experiência com programação, fazer consultas no MongoDB também pode ser mais fácil do que em SQL.

Em uma coleção podemos ter vários documentos. Podemos ter várias coleções diferentes. Por exemplo, podemos ter uma coleção contendo usuários, posts de um blog e comentários. Cada uma dessas coleções pode ter vários documentos com dados respectivos a cada coleção.

Um documento da coleção "posts de blog":

```json
{
   "title":"My first blog post",
   "author":"Yoshi",
   "tags":["video games","reviews"],
   "upvotes":20,
   "body":"Lorem ipsum...",
   "_id":Object("ai5eg8H9Pk12")
}
```

Cada objeto tem que ter um id para identificá-lo e o próprio MongoDB dá um id para um documento quando você o cria. No caso acima, o id é `"_id":Object("ai5eg8H9Pk12")`.

Um documento pode ter como valor um outro documento ou um array de documentos. Nesse caso, chamamos esse tipo de documento de "documento aninhado".

Veja um exemplo:

```json
{
   "title":"My first blog post",
   "author":{
      "name":"Yoshi",
      "email":"yoshi@email.com",
      "role":"Game Reviewer"
   },
   "tags":["video games","reviews"],
   "upvotes":20,
   "body":"Lorem ipsum...",
   "_id":Object("ai5eg8H9Pk12")
}
```

### MongoDB Compass

Usando a ferramenta MongoDB Compass criaremos um banco de dados chamado "bookstore" e criaremos uma coleção chamada "books". Também criaremos um documento dentro desta coleção:

```json
/** 
* Paste one or more documents here
*/
{
   // o id é criado automaticamente e pode ser deletado se desejado
   // o próprio programa adiciona ele de novo no final
  "_id": {
    "$oid": "65035656e97c7a590ff14b85" 
  },
  "title": "Name of the Wind",
  "author": "Patric Rothfuss",
  "pages": 500,
  "genres": ["fantasy", "magical"],
  "rating": 9
}
```

Se você for adicionar mais de um documento de uma vez, coloque-os dentro de colchetes:

```json
[
  {
    "title": "The Final Empire",
    "author": "Brandon Sanderson",
    "pages": 450,
    "genres": ["fantasy", "dystopian"],
    "rating": 8
  },
  {
    "title": "The Way of Kings",
    "author": "Brandon Sanderson",
    "pages": 350,
    "genres": ["fantasy", "dystopian"],
    "rating": 9
  },
  {
    "title": "The Call of the Weird",
    "author": "Louis Theroux",
    "pages": 350,
    "genres": ["non-fiction", "strange", "comedy"],
    "rating":7
  }
]
```

### MongoDB Shell

Para entrar na shell a partir de um terminal, digite `mongosh`. O próprio Compass já tem uma shell embutida e você pode usá-la.

Alguns comandos:

* `use nome_banco`: entra em um banco de dados existente, e se ele não existir, cria um novo banco de dados (se uma coleção for adicionada);
* `db`: retorna em qual banco de dados você está conectado;
* `help`: mostra uma lista de comandos que você pode executar;
* `show dbs`: retorna os nomes dos bancos de dados existentes;
* `show collections`: retorna as coleções do banco atual;
* `cls`: limpa a tela;
* `var`: cria uma variável. Uso: `var nome = "yoshi"`;
* `exit`: exits the shell;

#### Adicionando novos documentos

Para adicionar documentos a uma coleção, precisamos primeiramente nos referir a coleção. Como queremos nos referir a coleção "books", escreveremos `db.books`. Usaremos um método chamado `insertOne`, que é usado para inserir um documento de cada vez na nossa coleção. Dentro do método passamos um argumento, que é o objeto que representa o livro que queremos adicionar: 

```json
db.books.insertOne(
   {
      "title": "The Color of Magic",
      "author": "Terry Pratchett",
      "pages": 300,
      "genres": ["fantasy", "magic"],
      "rating": 7
   }
)
```

No terminal, você pode tanto adicionar o código inteiro em uma só linha quanto também pode escrever linha por linha, separadas por ENTER.

Você pode também inserir um documento em uma coleção que ainda não existe. Olhe o seguinte código:

```json
db.authors.insertOne({
   "name": "Brandon Sanderson",
   "age": 60
})
```

Ele vai criar uma nova coleção inserir o documento.

Podemos também inserir vários documentos ao mesmo tempo usando o método `insertMany`. Coloque os documentos entre colchetes:

```json
db.books.insertMany([
   {
      "title": "The Light Fantastic",
      "author": "Terry Pratchett",
      "pages": 250,
      "genres": ["fantasy"],
      "rating": 6
   },
   {
      "title": "Dune",
      "author": "Frank Herbert",
      "pages": 500,
      "genres": ["sci-fi", "dystopian"],
      "rating": 10
   }
])
```

#### Buscando documentos

O MongoDB nos dá um método para buscar por documentos em uma coleção. O nome do método é `find()`, e ele retorna os primeiros 20 itens da coleção.

```json
db.books.find() // Retorna os primeiros 20 livros
```

Se você quiser mostrar mais 20 novos itens, você pode digitar `it`, que significa "iterar", e dar ENTER.

##### Usando filtros

Você também pode usar filtros como na interface gráfica. Basta colocar as características que você deseja dentro do método `find()`.

```json
db.books.find({author: "Terry Pratchett"})
// Mais específico
db.books.find({author: "Terry Pratchett"}, rating: 7)
```

**Especificando campos visíveis**

É possível dizer quais campos queremos que a consulta retorne. Fazemos isso através de um segundo argumento, e colocamos o valor 1 (true) para as chaves das quais queremos os valores:

```json
db.books.find({author: "Brandon Sanderson"}, {title: 1, author: 1})
```

Também é possível usar o segundo argumento sem especificar o primeiro. Assim você consegue uma lista de todos os livros, mas mostrando somente os campos que você deseja. Para isso, deixe o primeiro argumento como um documento vazio.

```json
db.books.find({}, {title: 1, author: 1})
```

**`findOne()`**

Com este método você pode encontrar um item pelo seu id:

```json
db.books.findOne({_id: ObjectId("6503629e44dd3993fdb80608")})
```

Também podemos encontrar outras propriedades, como o título ou o autor. Se houver outro livro com o mesmo autor, ele vai retornar o primeiro que encontrar:

```json
db.books.findOne({author: 'Terry Pratchett'})
```

##### Organizando e limitando dados

Para organizar e limitar dados devemos utilizar mais métodos, um atrás do outro, prática que é chamada de "method chaining" ou "corrente de métodos".

O método `count()` conta quantos elementos foram retornados na consulta:

```json
db.books.find().count()
db.books.find({author: "Brandon Sanderson"}).count()
```

O método `limit()` limita quantos resultados são retornados:

```json
db.books.find().limit(3)
```

O método `sort()` organiza os resultados. Coloque como argumento a chave pela qual você quer que os resultados sejam organizados. O valor pode ser 1 ou -1, para ordem crescente e decrescente respectivamente.

```json
db.books.find().sort({title: 1})
db.books.find().sort({rating: -1})
db.books.find().sort({rating: -1}).limit(3)
```

#### Documentos aninhados

Vimos que um documento é composto por chave e valor. Podemos também colocar como valor de uma chave um outro documento, ou ainda um *array* de documentos, e isso é chamado de "documento aninhado".

```json
{
   "title": "The Way of Kings",
   "genres": ["fantasy", "sci-fi"],
   "rating": 9,
   "author": "Brandon Sanderson",
   "_id": ObjectId("ai5eg7H9Pk12"),
   "stock": {
      "count": 21,
      "price": 7.99
   },
   "reviews": [
      {"name": "Great Read!", "body": "Lorem ipsum..."},
      {"name": "So so, I guess", "body": "Lorem ipsum..."},
      {"name": "My fav every book", "body": "Lorem ipsum..."}
   ]
}
```

Poderíamos criar também uma nova coleção para manter as *reviews*. Se esse fosse o caso, tériamos que fazer duas consultas para termos os livros e as *reviews*. No caso acima, onde as *reviews* já estão junto dos livros, podemos acessar tudo em uma só consulta. Poderíamos também fazer de maneira híbrida, deixando somente as últimas *reviews* nos livros e criar uma nova coleção com todas as *reviews*, assim quando o usuário clicar para ver todas as *reviews*, a consulta seria feita da coleção de *reviews*.

##### Inserindo documentos aninhados

Apagaremos todos os livros e colocaremos de novo com a estrutura nova. É mais fácil do que editar um a um. Falaremos sobre deleção nas próximas seções, mas para deletar todos os documentos de uma coleção digite o seguinte código:

```json
db.books.deleteMany({})
```

Inserindo um documento aninhado:

```json
db.books.insertOne({
   title: "The Way of Kings",
   author: "Brandon Sanderson",
   rating: 9,
   pages: 400,
   genres: ["fantasy"],
   reviews: [
      {name: "Yoshi", body: "Great book!"},
      {name: "Mario", body: "So so."}
   ]
})
```

Inserindo vários documentos aninhados:

```json
db.books.insertMany([
   {
      title: "The Light Fantastic",
      author: "Terry Pratchett",
      pages: 250,
      rating: 7,
      genres: ["fantasy", "magic"],
      reviews: [
         {name: "Luigi", body: "It was pretty good!"},
         {name: "Bowser", body: "Loved it!"},
      ]
   },
   {
      title: "The Name of the Wind",
      author: "Patrick Rothfuss",
      pages: 500,
      rating: 10,
      genres: ["fantasy"],
      reviews: [
         {name: "Peach", body: "One of my favs!"},
      ]
   },
   {
      title: "The Color of Magic",
      author: "Terry Pratchett",
      pages: 350,
      rating: 8,
      genres: ["fantasy", "magic"],
      reviews: [
         {name: "Luigi", body: "It was OK!"},
         {name: "Bowser", body: "Really good book!"},
      ]
   },
   {
      title: "1984",
      author: "George Orwell",
      pages: 300,
      rating: 6,
      genres: ["sci-fi", "dystopian"],
      reviews: [
         {name: "Peach", body: "Not my cup of tea."},
         {name: "Mario", body: "Meh..."},
      ]
   }
])
```

#### Consultas complexas e operadores

Operadores em MongoDB são identificados pelo cifrão `$`. Para usá-los, use o método `find()`, digite a chave, e como valor coloque um par de chaves (`{}`). Na estrutura chave- valor, a chave vai ser o operador, e o valor vai ser o valor para preencher o seu requisito.

Maior que - `$gt`:

```json
db.books.find({rating: {$gt: 7}})
```

Menor que - `$lt`:

```json
db.books.find({rating: {$lt: 7}})
```

Maior que ou igual a - `$gte`:

```json
db.books.find({rating: {$gte: 7}})
```

Menor que ou igual a - `$lte`:

```json
db.books.find({rating: {$lte: 7}})
```

Mais um exemplo:

```json
db.books.find({rating: {$gte: 6}, author: "Patrick Rothfuss"})
```

Operador `$or`:

O operador `$or` requer uma lista de objetos, que serão os filtros aplicados.

```json
db.books.find({$or: [{rating: 8}, {rating: 9}]})
db.books.find({$or: [{rating: 8}, {author: "Terry Pratchett"}]})
```

Vários operadores:

```json
db.books.find({$or: [{pages: {$lt: 300}}, {pages: {$gt: 400}}]})
```

#### Operadores `$in` e  `$nin`

O operador `$in` mostra resultados que estão dentro do array que você disponibiliza. No exemplo abaixo, será retornado todos os livros que têm uma avaliação de 7, 8 e 9.

```json
db.books.find({rating: {$in: [7, 8, 9]}})
```

O mesmo pode ser feito utilizando o operador `$or`, mas a maneira acima é mais fácil:

```json
db.books.find({$or: [{rating: 7}, {rating: 8}, {rating: 9}]})
```

O operador `$nin` mostra todos os resultados que não estão dentro do array que você disponibilizou. No exemplo abaixo, será retornado todos os livros que têm uma avaliação diferente de 8, 9 e 10.

```json
db.books.find({rating: {$nin: [8, 9, 10]}})
```

#### Consultando arrays

A consulta de arrays é um pouco diferente das consultas normais. Vamos buscar todos os livros que tenham como gênero "fantasia":

```json
db.books.find({genres: "fantasy"})
```

Porque estamos consultando dentro de um array, o MongoDB vai ver se o valor existe no array e vai retornar os itens que tenham "fantasy" em seus arrays de gênero.

É possível ser específico também, buscando um array com uma combinação específica de itens. Utilize a estrutura de array. Dessa maneira, apenas os livros que tem aquele array específico serão mostrados nos resultados.

```json
db.books.find({genres: ["fantasy"]})
```

Com o operador `$all` é possível verificar se há uma combinação de itens em um array. Eu quero saber quais livros têm o gênero "dystopian" e "sci-fi", independente se tiver outros gêneros. Esta é a consulta para fazer isso:

```json
db.books.find({genres: {$all: ["dystopian", "sci-fi"]}})
```

Para consultar documentos aninhados, devemos utilizar o ponto. Utilizamos o nome da chave, o ponto e o nome da chave do documento interno. Precisamos colocar tudo isso dentro de aspas para não dar erro. Olhe o seguinte código: 

```json
// Buscando todos os livros que receberam uma review de Luigi
db.books.find({"reviews.name": "Luigi"})
```

#### Deletando documentos

A deleção de documentos funciona de maneira parecida com a inserção. Há o `deleteOne()` e o `deleteMany()`

```json
db.books.deleteOne({_id: ObjectId("6509d4e92c14f38ba0f477c5")})
```

Deletando muitos documentos:

```json
// deletando todos os livros de Terry Pratchett
db.books.deleteMany({author: "Terry Pratchett"})
```

#### Atualizando documentos

Assim como para inserir e deletar, temos dois métodos para atualizar dados: `updateOne()` e `updateMany()`, respectivamente. Podemos utilizar o id para atualizar um documento. Utilizamos o operador `$set` para aplicar os novos valores.

```json
// mudando um só valor
db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c4")}, {$set: {rating: 9}})

// mudando mais de um valor de uma vez
db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c4")}, {$set: {rating: 8, pages: 360}})
```

Atualizando muitos livros:

```json
db.books.updateMany({author: "Terry Pratchett"}, {$set: {author: "Terry Pratchet"}})
```

**O operador `$inc`**

Este operador é muito útil se você não sabe o valor guardado em um documento e você quer aumentá-lo. Ele incrementa pelo valor que você desejar.

```json
// Incrementando as páginas em 2
db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c5")}, {$inc: {pages: 2}})

// Decrementando as páginas em 2
db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c5")}, {$inc: {pages: -2}})
```

**Métodos `$push` and `$pull`**

Estes métodos são usados para inserir e remover itens de uma array, respectivamente.

```json
db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c5")}, {$push: {genres: "fantasy"}})

db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c5")}, {$pull: {genres: "fantasy"}})
```

**Inserindo múltiplos itens em um array**

O operador `$each` pode colocar vários valores em um array.

```json
db.books.updateOne({_id: ObjectId("6509d4e92c14f38ba0f477c5")}, {$push: {genres: {$each: ["Drama", "Fiction"]}}})
```

### Código do curso

#### Inserindo dados

```json
db.inscricoes.insertMany([
	{
		"aluno": "Paula Fernandes",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		}
	},
	{
		"aluno": "Fernanda da Silva",
		"data": new Date(),
		"curso": {
			"nome": "Ciência da Computação"
		},
		"notas": [9.0, 7.0, 8],
		"skills": [
			{
				"nome": "Python",
				"nivel": "avançado"
			},
			{
				"nome": "Banco de Dados",
				"nivel": "avançado"
			}
		]
	},
	{
		"aluno": "Fabiano Perez",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		},
		"skills": [
			{
				"nome": "Python",
				"nivel": "básico"
			}
		]
	}
])

// Fazendo uma consulta para verificar os dados:
db.inscricoes.find().pretty()
```

O método `pretty()` faz com que os dados sejam mostrados de maneira mais legível.

#### Consultando dados

```json
// Mostrando a coleção
db.inscricoes.find().pretty()

// Buscando todas as pessoas que tenham como habilidade a linguagem Python
db.inscricoes.find(
	{
		"skills.nome": "Python"
	}
)

// Pessoas que tenham como habilidade Python e o nível seja avançado
db.inscricoes.find(
	{
		"skills.nome": "Python",
		"skills.nivel": "avançado"
	}
)

// Procurando as pessoas que estejam fazendo o curso de Programação Web
db.inscricoes.find(
	{
		"curso.nome": "Programação para Internet"
	}
)

// Procurando pessoas que fazem Ciência da Computação e Programação Web
db.inscricoes.find(
	{
		$or: [
			{"curso.nome": "Ciência da Computação"},
			{"curso.nome": "Programação para Internet"}
		]
	}
)

// Buscando um aluno específico
db.inscricoes.find(
	{
		"nome": "Fabiano Perez"
	}
)

// Usando o operador $or
db.inscricoes.find(
	{
		$or: [
			{"curso.nome": "Ciência da Computação"},
			{"curso.nome": "Programação para Internet"}
		],
		"aluno": "Fabiano Perez"
	}
)

// Alunos que tenham o nível de Python avançado ou intermediário
db.inscricoes.find(
	{
		"skills.nome": "Python",
		"skills.nivel": {
			$in: ["avançado", "intermediário"]
		}
	}
)
```

#### Atualizando dados

Adicionando os dados primeiro:

```json
db.inscricoes.insertMany([
	{
		"aluno": "Paula Fernandes",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		}
	},
	{
		"aluno": "Fernanda da Silva",
		"data": new Date(),
		"curso": {
			"nome": "Ciência da Computação"
		},
		"notas": [9.0, 7.0, 8],
		"skills": [
			{
				"nome": "Python",
				"nivel": "avançado"
			},
			{
				"nome": "Banco de Dados",
				"nivel": "avançado"
			}
		]
	},
	{
		"aluno": "Fabiano Perez",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		},
		"skills": [
			{
				"nome": "Python",
				"nivel": "básico"
			}
		]
	},
	{
		"aluno": "Guilherme Dantas",
		"data": new Date(),
		"curso": {
			"nome": "Programação para internet"
		},
		"notas": [7, 8.5, 10]
	},
	{
		"aluno": "Angelna Souza",
		"data": new Date(),
		"curso": {
			"nome": "Programação para internet"
		},
		"notas": [7.4, 9.5, 9.4]
	},
	{
		"aluno": "William Douglas",
		"data": new Date(),
		"curso": {
			"nome": "Programação para internet"
		},
		"notas": [6.4, 3.5, 6.4]
	}
	
])
```

Atualizando dados:

```json
// Atualizando um nome
db.inscricoes.updateOne(
  {"aluno": "Angelna Souza"},
  {$set: {"aluno": "Angelina Souza"}}
)

db.inscricoes.find({"nome": "Angelina Souza"})

// Atualizando o nome de vários cursos
db.inscricoes.updateMany(
  {"aluno": {$in: ["Guilherme Dantas", "Angelina Souza", "William Douglas"]}},
  {$set: {"curso.nome": "Programação para Internet"}}
)

db.inscricoes.find(
  {
    "aluno": {$in: ["Guilherme Dantas", "Angelina Souza", "William Douglas"]}
  }
).pretty()

// Removendo um aluno
db.inscricoes.deleteOne({"nome": "Angelina Souza"})

db.inscricoes.find({"curso.nome": "Programação para Internet"}, {"aluno": 1})

// Utilizando o $push
db.inscricoes.updateOne(
	{"aluno": "William Douglas"},
	{$push: {"notas": 6.7}
})

db.inscricoes.find({"aluno": "William Douglas"})

// Utilizando o $each
db.inscricoes.updateOne(
	{"aluno": "William Douglas"},
	{$push: {notas: {$each: [9.2, 5]}}}
)

db.inscricoes.find({"aluno": "William Douglas"}).pretty()
```

#### Ordenação e limitação

Adicionando alunos:

```json
db.inscricoes.insertMany([
	{
		"aluno": "Paula Fernandes",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		}
	},
	{
		"aluno": "Fernanda da Silva",
		"data": new Date(),
		"curso": {
			"nome": "Ciência da Computação"
		},
		"notas": [9.0, 7.0, 8],
		"skills": [
			{
				"nome": "Python",
				"nivel": "avançado"
			},
			{
				"nome": "Banco de Dados",
				"nivel": "avançado"
			}
		]
	},
	{
		"aluno": "Fabiano Perez",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		},
		"skills": [
			{
				"nome": "Python",
				"nivel": "básico"
			}
		]
	},
	{
		"aluno": "Guilherme Dantas",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		},
		"notas": [7, 8.5, 10]
	},
	{
		"aluno": "Angelina Souza",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		},
		"notas": [7.4, 9.5, 9.4]
	},
	{
		"aluno": "William Douglas",
		"data": new Date(),
		"curso": {
			"nome": "Programação para Internet"
		},
		"notas": [6.4, 3.5, 6.4]
	},
	{
		"aluno": "Jair Rodrigues",
		"data_nascimento": new Date(1981, 06, 19),
		"curso": {
			"nome": "História"
		},
		"notas": [6, 7, 8, 5.5]
	},
	{
		"aluno": "Bruna Marquezi",
		"data_nascimento": new Date(1995, 02, 06),
		"curso": {
			 "nome": "História"
		},
		"notas": [10, 9.7, 6.5, 8.7]
	}
])
```

Filtrando as consultas:

```json
// Encontrando dados com valores maiores do que o especificado
db.inscricoes.find({"notas": {$gt: 8.0}}).pretty()

// Igual o maior
db.inscricoes.find({"notas": {$gte: 8.0}}).pretty()

// Encontrando apenas um valor
db.inscricoes.findOne({"notas": {$gt: 7.7}})

// Ordenando em ordem crescente
db.inscricoes.find().sort({"aluno": 1}).pretty()

// Ordenando em ordem decrescente
db.inscricoes.find().sort({"aluno": -1}).pretty()

// Limitando os resultados
db.inscricoes.find().sort({"aluno": 1}).limit(3).pretty()
```

#### Buscas mais complexas

```json
// Inserindo um novo campo em um documento existente
db.inscricoes.updateOne(
	{"aluno" : "Bruna Markezi"},
	{
		$set: {
			"localizacao": {
				"endereco": "Avenida Zulmira Borba, 1978"
			}
		}
	}
)

// Para utilizar campos com coordenadas geográficas no MongoDB
// precisamos ter um campo chamado 'coordinates' e especificar
// o 'type'
db.inscricoes.update(
	{"aluno" : "Bruna Markezi"},
	{
		$set: {
			"localizacao": {
				"endereco": "Avenida Zulmira Borba, 1978",
				"coordinates": [-20.388008, -54.577545],
				"type": "Point"
			}
		}
	}
)
```

Buscando por dados de localização:

```json
// Informe qual é o campo que deve ser usado como índice de busca
db.inscricoes.createIndex(
	{
		"localizacao": "2dsphere"
	}
)

// Deve-se realizar uma consulta utilizando agregação
db.inscricoes.aggregate(
	[
		{
			$geoNear: {
				"near": {
					"coordinates": [-20.388008, -54.577546],
					"type": "Point"
				},
				"distanceField": "distancia.calculada",
				"spherical": true,
				"num": 4
			}
		}
	]
)

// OBS: Na consulta acima, estamos trazendo 4 resultados, sendo que o primeiro é o próprio elemento da busca.

// Caso queiramos ignorar o primeiro resultado, então devemos informar isso na consulta.
db.inscricoes.aggregate(
	[
		{
			$geoNear: {
				"near": {
					"coordinates": [-20.388008, -54.577546],
					"type": "Point"
				},
				"distanceField": "distancia.calculada",
				"spherical": true,
				"num": 4
			}
		},
		{
			$skip: 1
		}
	]
).pretty()
```

## Redis

O Redis (Remote Dictionary Server) é um banco de dados NoSQL open-source que trabalha com o conceito de chave-valor. Ele foi escrito em C por Salvatore Sanfilippo e teve sua versão inicial em 10 de maio de 2009.

Este banco de dados trabalha com armazenamento de dados em memória, ou seja, não é em disco, e desta forma, ele é considerado extremamente rápido.

Suas principais utilizações incluem: cache, gerenciamento de sessões e message broker.

Atualmente o Redis é o banco de dados do tipo chave-valor mais utilizado no mundo.

### Benefícios do uso do Redis

**Desempenho muito rápido**

Todos os dados do Redis residem na memória principal do seu servidor, em contraste com a maioria dos sistemas de gerenciamento de banco de dados que armazenam dados em disco ou SSDs. Ao eliminar a necessidade de acessar discos, bancos de dados na memória, como o Redis, evitam atrasos de tempo de busca e podem acessar dados com algoritmos mais simples que usam menos instruções de CPU. Operações comuns exigem menos do que 10 milissegundos para serem executadas.

**Estruturas de dados na memória**

O Redis permite que os usuários armazenem chaves que fazem o mapeamento para vários tipos de dados. O tipo de dado fundamental é uma *string*, que pode ser em formato de texto ou binário, e ter no máximo 512MB. O Redis também é compatível com listas de *strings* na ordem em que foram adicionadas, conjuntos de *strings* não ordenadas, conjuntos classificados ordenados de acordo com uma pontuação, *hashes* que armazenam uma lista de campos e valores e HyperLogs para contar os itens exclusivos de um conjunto de dados. Praticamente qualquer tipo de dado pode ser armazenado na memória usando o Redis.

**Versatilidade e facilidade de uso**

O Redis é disponibilizado com várias ferramentas que tornam o desenvolvimento e as operações mais rápidas e fáceis: o PUB/SUB (publisher-subscriber) para publicar mensagens nos canais que são entregues para os assinantes, o que é ótimo para sistemas de mensagens e chat; as chaves com TTL, que podem podem ter um tempo de vida útil determinado, após a qual elas se autoexcluem, o que ajuda a evitar sobrecarregar o banco de dados com itens desnecessários; os contadores atômicos, que garantem que condições de corrida não criem resultados incompatíveis; além da Lua, uma linguagem de *script* potente, porém leve.

**Replicação e persistência**

O Redis emprega uma arquitetura no estilo mestre/subordinado e é compatível com a replicação assíncrona em que os dados podem ser replicados para vários servidores subordinados. Isso pode disponibilizar desempenho de leitura melhorado (á medida que as solicitações podem ser divididas entre os servidores) e recuperação quando o servidor primário passar por uma interrupção.

Para disponibilizar durabilidade, o Redis oferece compatibilidade com **snapshots point-in-time** (copiando o conjunto de dados do Redis no disco) e criando um **Append Only File** (AOF) para armazenar cada alteração de dados no disco conforme elas vão sendo gravadas. Os dois métodos permitem a restauração rápida dos dados do Redis no caso de uma interrupção.

**Compatibilidade com a sua linguagem de desenvolvimento preferencial**

Mais de cem clientes de código aberto estão disponíveis para os desenvolvedores do Redis. As ilnguagens compatíveis incluem Java, Python, PHP, C, C++, C#, JavaScript, Note.js, Ruby, R, Go e outras.

### Casos de uso do Redis

**Armazenamento em cache**

O Redis inserido na "frente" de outro banco de dados cria um cache na memória com excelente desempenho para diminuir a latência de acesso, aumentar o *throughput* e facilitar a descarga de um banco de dados relacional ou NoSQL.

**Gerenciamento de sessões**

O Redis é altamente indicado para tarefas de gerenciamento de sessões. Basta usar o Redis como um armazenamento de chave-valor com o tempo de vida (TTL) correto nas chaves de sessão para gerenciar suas informações de sessão. Ogerenciamento de sessões é comumente exigido para aplicações on-line, como jogos, sites de comércio eletrônico e plataformas de mídia social.

**Classificações em tempo real**

Ao usar a estrutura de dados **Sorted Set** do Redis, os elementos são mantidos em uma lista classificada de acordo com suas pontuações. Isso facilita a criação de classificações dinâmicas para mostrar quem está vencendo o jogo, publicando as mensagens mais curtidas, ou qualquer outra coisa que demonstre quem está na liderança.

**Limite de taxa**

O Redis pode calcular e, quando necessário, acelerar a taxa dos eventos. Ao usar um contador do Redis associado a uma chave de API do cliente, você poderá contar o número de solicitações de acesso dentro de um determinado período e tomar as ações necessárias, caso um limite seja excedido. Os limitadores de taxa são usados comumente para limitar o número de publicaçõe sem um fórum, limitar a utilização de recursos e conter o impacto de remetentes de *spam*.

**Filas**

A estrutura de dados **List** facilita implementar uma fila leve e persistente. As listas oferecem operações atômicas, além de recursos de bloqueio, tornando-as adequadas para várias aplicações que exigem um agente de mensagens confiável ou uma lista circular.

**Chat e sistema de mensagens**

O Redis é compatível com PUB/SUB padrão com correspondência de padrões. Isso permite que o Redis seja compatível com salas de *chat* de alto desempenho, *streams* de comentários em tempo real e intercomunicações do servidor. Você também pode usar o PUB/SUB para ativar ações om base em eventos publicados.

### Quem usa o Redis?

* Twitter;
* GitHub;
* Weibo;
* Pinterest;
* Snapchat;
* Craigslist;
* Digg;
* StackOverflow;
* Flickr.

### Prática 1

**Inserindo dados**

Podemos configurar chaves e valores utilizando a palavra `set`.

`set "usuarios_online" 42`

Se foi adicionado com sucesso, você receberá um "OK" de volta. Você pode usar aspas duplas para declarar as chaves. Não se usa dois pontos para separar a chave do valor, apenas um espaço em branco.

**Recuperando dados**

Podemos pegar os dados de volta utilizando o `get`.

`get "usuarios_online"`

**Inserindo *strings***

Podemos inserir *strings* rodeando elas por aspas simples:

`set long_string 'This is a very long string of characters.'`

**Atualizando dados**

Para atualizar dados, basta utilizar o `set` de novo na mesma chave:

```
set nome 'João Silva'
set nome 'José Oliveira'
```

**Deletando dados**

Para deletar uma chave use a palavra `del` e o nome da chave:

`del long_string`

### Prática 2

**Declarando e mostrando alguns dados**

```
set usuarios_online 42
set nome 'John Doe'
set data_nascimento '15/06/1981'
get usuarios_online
get nome
get data_nascimento
```

**Vendo todas as chaves criadas**

Para ver todas as chaves existentes em memória digite:

`keys *`

O asterisco significa que queremos todas as chaves.

**Declarando chaves utilizando padrões**

Podemos declarar chaves utilizando dois pontos, e assim podemos criar padrões nas chaves:

```
set nota:14-04-2019:matematica 8.5
set nota:20-06-2019:historia 9.5
set nota:22-06-2019:fisica 6.3
set nota:02-05-2019:programacao 10
```

Aqui fizemos chaves que contêm o nome principal, que é `nota`, a data e a disciplina. Os valores são as notas.

**Pesquisando por chaves padronizadas**

Podemos pesquisar por essas chaves de maneira mais específica também:

`keys nota*`

Aqui pesquisamos todas as notas, não importando a data e nem a disciplina.

Podemos pesquisar tambem por nomes específicos dentro da chave:

`keys notas:*:matematica`

Aqui buscamos somente as notas de matemática, não importando a data.

`keys nota:*-06-*:*`

Aqui buscamos por todas as notas do mês seis, não imoprtando o dia, o ano ou a disciplina.

**Pesquisando por um número específico de caracteres**

Também podemos utilizar o ponto de interrogação para buscar por uma quantidade específica de caracteres:

`keys nota:*:??????`

Aqui estamos pesquisando as notas de qualquer data, em que o nome da disciplina seja composto por seis caracteres.

**Pesquisando por mais de um elemento na chave de uma só vez**

Se quisermos por exemplo, ter todas as notas do mês quatro e do mês seis, precisaríamos usar colchetes. Eles permitem que os valores que forem colocados dentro deles sejam buscados:

`keys nota:*-0[46]-*:*`

Aqui estamos buscando por notas de um dia qualquer, do mês quatro ou seis, de um ano qualquer, de uma disciplina qualquer. O zero é um número em comum com o mês quatro e o mês seis, por isso ele foi colocado fora do parêntesis

**Inserindo várias chaves e valores**

Utilizando o comando `mset`é possível inserir várias chaves e valores de uma vez:

`mset nota:03-07-2019:portugues 6 nota:05-07-2019:ingles 8.9 nota:10-07-2019:geografia 7.3`

**Código completo**

Código 1:

```
echo '#######################################'
echo 'Inserindo dados'
set usuarios_online 42
set nome 'John Doe'
set data_nascimento '15/06/1981'
echo ' '
echo ' '
echo '#######################################'
echo 'Recuperando dados'
get usuarios_online
get nome
get data_nascimento
echo ' '
echo ' '
echo '#######################################'
echo 'Recuperando todas as chaves'
keys *
echo ' '
echo ' '
echo '#######################################'
echo 'Inserindo chaves com padrões'
set nota:14-04-2019:matematica 8.5
set nota:20-06-2019:historia 9.5
set nota:22-06-2019:fisica 6.3
set nota:10-03-2019:ingles 6.4
set nota:10-03-2019:geografia 7.5
set nota:02-05-2019:programacao 10
echo ' '
echo ' '
echo '#######################################'
echo 'Recuperando chaves com padrões'
keys notas:*:matematica
keys nota:*-06-*:*
keys nota:*:matematica
keys nota:*:??????
echo ' '
echo ' '
echo '#######################################'
echo 'Recuperando vários valores de uma vez'
keys nota:*-0[46]-*:*
```

Código 2:

```
echo '#######################################'
echo 'Inderindo dados:'
set estrutura 'promocao:produto:dia-mes-ano:valor valor'
set promocao:ps4:20-05-2019:valor 1199.56
set promocao:xbox306:20-05-2019:valor 1399.56
set promocao:nintendo:20-05-2019:valor 2199.56
set promocao:ps4:22-05-2019:valor 1150.56

echo ''
echo ''

echo '#######################################'
echo 'Recuperando dados:'

echo ''

echo 'Recuperando todas as chaves:'
keys promocao:*

echo ''

echo 'Recuperando as chaves do ps4:'
keys promocao:ps4*

echo ''

echo 'Recuperando as chaves pela data:'
keys promocao:*:20*

echo ''
echo ''

echo '#######################################'
echo 'Inserindo vários valores:'
mset nota:03-07-2019:portugues 6 nota:05-07-2019:ingles 8.9 nota:10-07-2019:geografia 7.3
```

### Prática 3

**Inserindo dados utilizando *hashes***

O Redis também nos permite utilizar *hashes*, que nos dá a liberdade de alocar vários valores em uma só chave.

Não é possível utilizar o asterisco para consultar chaves *hashes*.

Precisamos utilizar o `hset`

```
hset prova:21-06-2019:felicity historia 9.5
hset prova:21-06-2019:felicity geografia 7.4
hset prova:21-06-2019:felicity fisica 8.7
hset prova:21-06-2019:felicity ingles 9
hset prova:21-06-2019:felicity matematica 8.3
```

**Consultando dados feitos por *hashes***

```
hget prova:21-06-2019:felicity historia
hget prova:21-06-2019:felicity ingles
```

**Retornando todas as chaves disponíveis para uma chave *hash***

`hkeys prova:21-06-2019:felicity`

**Removendo um campo**

`hdel prova:21-06-2019:felicity ingles`

**Adicionando vários valores para uma chave *hash***

hmset prova:21-06-2019:angelina historia 6.4 fisica 9.2 ingles 10 matematica 8.3

**Mostrando todos as chaves e valores**
`hgetall prova:21-06-2019:angelina`

### Listas

**Criandando uma lista e inserindo dados nela**

Para criar uma lista, basta adicionar dados a ela. Você pode adicionar dados em uma lista utilizando o comando `lpush`, que significa "left push", ou "adicionar à esquerda" em português. Este comando adiciona um item à esquerda (no começo) da lista.

```
lpush ultimos_lancamentos 'O Hobbit'
lpush ultimos_lancamentos 'Rocketman'
lpush ultimos_lancamentos 'X-Men: Fenix Negra'
lpush ultimos_lancamentos 'Homem-Aranha: Longe de Casa'
lpush ultimos_lancamentos 'O Rei Leão'
```

**Mostrando os itens de uma lista**

Utiliza-se o comando `lindex` mais o nome da lista e o índice do item para mostrar os itens individuais de uma lista. `lindex` significa "list index" ou "índice da lista" em português.

```
lindex ultimos_lancamentos 0
lindex ultimos_lancamentos 1
lindex ultimos_lancamentos 2
lindex ultimos_lancamentos 3
lindex ultimos_lancamentos 4
```

**Descobrindo quatnos itens há em uma lista**

O comando `llen` retorna a quantidade de itens presentes em uma lista. `llen` significa "list length", ou "tamanho da lista" em português.

`llen ultimos_lancamentos`

**Adicionando um elemento ao final da lista**

Utilize o comando `rpush` para adicionar itens à direita (no final) de uma lista. `rpush` significa "right push", ou "adicionar à direita" em português.

`rpush ultimos_lancamentos 'O Senhor dos Anéis: A Sociedade do Anel'`

**Mostrando vários itens de uma vez**

O comando `lrange` mostra itens de um índice até outro. `lrange` significa "list range", ou "extensão da lista" em português. Logo após colocar o nome da lista, separe por espaços o índice inicial e o final.

`lrange ultimos_lancamentos 0 2`

Aqui estamos mostrando os itens presentes do índice 0 até o 2.

**Excluindo itens de uma lista**

Para excluir itens, usa-se o comando `ltrim`, que significa "list trim", ou "aparar lista" em português. A sintaxe dele é igual a do `lrange`. Ele deixa na lista somente os itens que estão entre os índices apresentados, e deleta todo o resto.

`ltrim ultimos_lancamentos 3 5`

Aqui, os itens 0, 1 e 2 foram deletados.

### Filas

Uma fila funciona mais ou menos como uma lista. A diferença é que um item só pode entrar no final e só pode ser retirado do início.

**Criando uma fila**

Com o seguinte código, estamos criando uma fila de números de telefone:

```
rpush fila:confirma:celular '(00) 00000-0000'
rpush fila:confirma:celular '(00) 00000-0001'
rpush fila:confirma:celular '(00) 00000-0002'
rpush fila:confirma:celular '(00) 00000-0003'
```

**Mostrando dados**

Mostraremos alguns dados da fila:

```
echo 'Mostrando quantos itens tem na fila:'
llen fila:confirma:celular
echo ''

echo 'Mostrando todos os itens da fila:'
lrange fila:confirma:celular 0 -1
echo ''

echo 'Mostrando o primeiro item da fila:'
lindex fila:confirma:celular 0
echo ''
```

Aqui o -1 representa o último item da fila.

**Removendo itens**

Utilizamos o comando `lpop` para remover o primeiro item de uma fila. `lpop` significa "left pop", ou "remover à esquerda" em português. Aqui não devemos utilizar o `ltrim`, por exemplo, pois se a fila está sendo atualizada a todo momento, pode ser que quando você escolher o último índice, a fila já tenha atualizado e adicionado mais um item, assim você perde itens novos, que acabaram de ser colocados na parte de trás da fila. O `lpop` é mais adequado para remover itens do início da fila sem comprometer os itens anteriores.

`lpop fila:confirma:celular`

Esse comando retorna o item que foi retirado.

### Prática 4

