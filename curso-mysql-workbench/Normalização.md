# Normalização

Utilizei [este vídeo](https://www.youtube.com/watch?v=GFQaEYEc8_8&ab_channel=Decomplexify) para aprender sobre Normalização de Bancos de Dados.

O que é Normalização de Banco de Dados? Por que devemos fazer? Como devemos fazer? O que pode acontecer se eu não fizer a normalização do meu banco de dados?

Um banco de dados não consegue se proteger contra dados ruins, mas é possível que um bom design de banco de dados consiga se proteger contra alguns tipos de dados ruins. Nesses casos, os dados estão mostrando algo que não pode ser logicamente verdade. Um cliente com duas datas de nascimento é logicamente impossível.

Quando há dados contraditórios no banco de dados não singifica necessariamente que os dados são ruins, mas sim que o design do banco de dados é ruim, e que ele não foi normalizado.

Quando uma tabela de um banco de dados é normalizada, isso signfica que ela foi estruturada em uma maneira que ela não expressa informações redundantes.

Tabelas normalizadas são mais fáceis de serem entendidas, mais fáceis de serem melhoradas e extendidas, além de que estão protegidas de anomalias de inserção, de atualização e de deleção.

Para normalizar bancos de dados, utilizamos as Formas de Normalização, que vão de uma até a cinco. Imagine essas formas como uma verificação de segurança.

## Primeira Forma Normal

Existem algumas maneiras que podemos violar a Primeira Forma Normal. Aqui estão algumas:

### Depender da ordem dos dados apresentados

Não devemos depender da ordem dos dados de uma tabela, pois isso viola a 1FN (ou Primeira Forma Normal). Por exemplo, se tivermos um banco de dados onde haja uma tabela com o nome de todos os integrantes do Quarteto Fantástico e fizermos uma consulta para sabermos quem eles são; a base de dados dará os nomes em uma ordem aleatória. 

| personagem        |
| ----------------- |
| Coisa             |
| Senhor Fantástico |
| Mulher Invisível  |
| Tocha Humana      |

Suponha que queiramos que a tabela seja reorganizada para mostrar do jogador mais alto para o mais baixo; isso seria uma violação da 1FN, pois a tabela não tem a altura dos jogadores, somente o nome. Assim, não podemos depender da ordem em que os dados são mostrados quando fazemos uma consulta em uma tabela.

A solução é simples: seja explícito. Se o objetivo é saber a altura, então deve-se criar uma nova coluna para mostrar a altura do jogador.

| personagem        | altura_cm |
| ----------------- | --------- |
| Senhor Fantástico | 185       |
| Coisa             | 183       |
| Tocha Humana      | 178       |
| Mulher Invisível  | 122       |

### Misturar tipos de dados

Em um banco de dados relacional, não é permitido ser impreciso quanto ao tipo de dado de uma coluna. Não podemos misturar números inteiros e strings. Sendo assim, misturar tipos de dados é uma violação da 1FN, e na verdade o banco de dados nem deixará uma pessoa fazer isso.

### Fazer uma tabela sem uma chave primária

Uma chave primária é uma coluna, ou uma combinação de colunas, que é usada para a identificação de uma linha em uma tabela. Por exemplo, na nossa tabela com o nome e a altura dos personagens do Quarteto Fantástico, o nome do personagem é uma boa escolha para chave primária, para que assim a gente consiga acessar a altura de cada um deles com facilidade, utilizando o nome como identificador da linha. Isso também previne que um personagem tenha duas alturas.

Toda tabela que criarmos deve ter uma chave primária. Se ela não tiver, ela não obedece a 1FN.

### Repetir grupos

Guardar um grupo repetido de itens de dados em uma só linha viola a 1FN.

Vamos supor que tenhamos uma tabela com o nome de alunos e o que cada um tem em sua mochila. Se torna impraticável fazer uma consulta para saber quais alunos têm régua ou quantos livros um aluno leva na mochila se todos esses dados estão dispostos em uma só linha. Isso acontece na seguinte tabela:

| nome_aluno | itens_mochila                 |
| ---------- | ----------------------------- |
| João       | 1 caderno, 2 livro, 1 pochete |
| Maria      | 1 caderno, 4 livro, 2 régua   |
| Patrícia   | 2 caderno, 1 pochete          |

Essa tabela viola a 1FN pois tem um grupo repetido de itens em suas linhas. Para que possamos fazer consultas com mais facilidade, é necessário adicionar uma coluna chamada "quantidade" na tabela e colocar como chave primária a combinação de nome e item, pois a combinação de nome e item é única.

Veja:

| nome_aluno | item    | quantidade |
| ---------- | ------- | ---------- |
| João       | caderno | 1          |
| João       | livro   | 2          |
| João       | pochete | 1          |
| Maria      | caderno | 1          |
| Maria      | livro   | 4          |
| Maria      | régua   | 2          |
| Patrícia   | caderno | 2          |
| Patrícia   | pochete | 1          |

Pode-se pensar que essa tabela viola a 1FN tendo chaves primárias repetidas, mas na verdade a chave primária é uma combinação da primeira e segunda colunas, e sendo assim, a chave primária é sempre única. Há, por exemplo, somente uma combinação de "João caderno" em toda a tabela.

Utilizamos nomes como chave primária para todos os exemplos dados até agora, mas o ideal é escolher algo que não se repita. Geralmente escolhe-se um número identificador, e este número é a chave primária.

## Segunda Forma Normal

Veja a seguinte tabela:

| id_jogador | tipo_item       | quantidade_item |
| ---------- | --------------- | --------------- |
| jdog21     | amuletos        | 2               |
| jdog21     | aneis           | 4               |
| gilal19    | moedas de cobre | 18              |
| trev73     | escudos         | 3               |
| trev73     | flechas         | 5               |
| trev73     | moedas de cobre | 30              |
| trev73     | aneis           | 7               |

Suponha que queiramos adicionar mais uma coluna a essa tabela, e essa nova coluna vai mostrar a classificação do jogador, que pode ser básico, intermediário ou avançado. A tabela fica assim:

| id_jogador | tipo_item       | quantidade_item | classificacao_jogador |
| ---------- | --------------- | --------------- | --------------------- |
| jdog21     | amuletos        | 2               | intermediario         |
| jdog21     | aneis           | 4               | intermediario         |
| gilal19    | moedas de cobre | 18              | iniciante             |
| trev73     | escudos         | 3               | avançado              |
| trev73     | flechas         | 5               | avançado              |
| trev73     | moedas de cobre | 30              | avançado              |
| trev73     | aneis           | 7               | avançado              |

Isso não é um bom design! Por quê? Vamos supor que o jogador gilal19 perca todas as suas moedas de cobre, e assim ficasse sem qualquer item em seu inventário. Se isso acontecesse, ela seria apagada da base de dados. Se tentarmos encontrar a classificação do jogador gilal19, não encontraremos mais, pois ela foi apagada. Esse problema é conhecido como uma **anomalia de deleção**.

Agora vamos supor que jdog21 melhora sua classificação, mas há um erro no banco de dados e somente uma linha é atualizada. Assim, ele ficaria com a classificação intermediária e avançada ao mesmo tempo. Com uma tabela assim, a nossa base de dados se faz aberta a esse tipo de inconsistência lógica. Esse problema é conhecido como uma **anomalia de atualização**.

Suponhamos que uma nova jogadora entrou no jogo, não tem nada em seu inventário, e que ela é iniciante. Queremos registrar que ela é iniciante, mas como ela não tem nada em seu inventário, não conseguimos colocar o nome dela na tabela. O nome desse problema é **anomalia de inserção**.

### O que é a Segunda Forma Normal?

A Segunda Forma Normal trata de como as colunas que não são chave primária se relacionam com a chave primária. Na tabela acima, as colunas não-chave são quantidade_item e classificação_jogador. Como vimos antes, a chave primária é a combinação do id_jogador e tipo_item. A Segunda Forma Normal diz que cada atributo (ou coluna) não-chave deve  depender da chave primária inteira.

Tendo essa definição em mente, podemos nos perguntar: A coluna item_quantidade depende da chave primária inteira? A resposta é sim, pois a combinação id_jogador e tipo_item é essencial para que se saiba a quantidade do item que um jogador possui em seu inventário. A classificação do jogador depende da chave primária inteira? A resposta é não, pois o tipo_item não tem nada a ver com a classificação do jogador. A classificação depende somente do jogador, pois é uma propriedade do jogador somente. Para cada jogador, há somente uma classificação.

O design da tabela ficou ruim quando decidimos adicionar uma coluna de classificação para os jogadores em uma tabela que não era adequada pra recebê-la. Para resolver isso, basta criar outra tabela onde o atributo classificacao_jogador dependa inteiramente na chave, que nesse caso será somente id_jogador.

| id_jogador | classificacao_jogador |
| ---------- | --------------------- |
| jdog21     | intermediario         |
| gilal19    | iniciante             |
| trev73     | avançado              |
| tina42     | inicianate            |

Assim, as duas tabelas estão na Segunda Forma Normal

## Terceira Forma Normal

16m