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

