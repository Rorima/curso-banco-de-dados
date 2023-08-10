# Normalização

Utilizei [este vídeo](https://www.youtube.com/watch?v=GFQaEYEc8_8&ab_channel=Decomplexify) para aprender sobre Normalização de Bancos de Dados.

O que é Normalização de Banco de Dados? Por que devemos fazer? Como devemos fazer? O que pode acontecer se eu não fizer a normalização do meu banco de dados?

Um banco de dados não consegue se proteger contra dados ruins, mas é possível que um bom design de banco de dados consiga se proteger contra alguns tipos de dados ruins. Nesses casos, os dados estão mostrando algo que não pode ser logicamente verdade. Um cliente com duas datas de nascimento é logicamente impossível.

Quando há dados contraditórios no banco de dados, não singifica necessariamente que os dados são ruins, mas sim que o design do banco de dados é ruim, e que ele não foi normalizado.

Quando uma tabela de um banco de dados é normalizada, isso signfica que ela foi estruturada em uma maneira que ela não expressa informações redundantes.

Tabelas normalizadas são mais fáceis de serem entendidas, mais fáceis de serem melhoradas e extendidas, além de que estão protegidas de anomalias de inserção, de atualização e de deleção.

Para normalizar bancos de dados, utilizamos as Formas de Normalização, que vão de uma até a cinco. Imagine essas formas como uma verificação de segurança. Para que uma tabela esteja dentro de uma Forma Normal, ela deve obedecer todas as Formas Normais antecessoras.

## Primeira Forma Normal

> A Primeira Forma Normal nos diz que:
>
> * Não devemos depender da ordem dos dados de uma tabela;
> * Não podemos misturar tipos de dados diferentes em uma mesma coluna (campo);
> * Não devemos fazer uma tabela sem chave primária;
> * Não devemos ter grupos repetidos em uma coluna.

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

> A Segunda Forma Normal diz que cada atributo (ou coluna) não-chave deve  depender da chave primária inteira.

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

> A Terceira Forma Normal diz que um atributo não-chave não pode depender de outro atributo não-chave. Ela diz que todo atributo não-chave em uma tabela deve depender na chave inteira, e nada além da chave.

Para demonstrar a Terceira Forma Normal, imaginemos que queiramos adicionar uma nova coluna à tabela anterior, que mostra o nível de habilidade do jogador. Nesse jogo para o qual utilizamos como exemplo, há nove níveis de habilidade. O nível de habilidade se relaciona com a classificação. O iniciante tem um nível de habilidade de 1 a 3, o intermediário de 4 a 6, e o avançado de 7 a 9.

| id_jogador | classificacao_jogador | nivel_habilidade_jogador |
| ---------- | --------------------- | ------------------------ |
| jdog21     | intermediario         | 4                        |
| gilal19    | iniciante             | 3                        |
| trev73     | avançado              | 8                        |
| tina42     | inicianate            | 1                        |

Agora que temos o nível de habilidade dos jogadores na tabela, um problema pode acontecer. Vamos supor que o jogador gilal19 suba um nível de habilidade e fique com 4 ao invés de 3. Seu nível é atualizado, mas não a classificação, por causa de algum erro. Agora temos uma inconsistência.

Na tabela nós podemos ver que tanto nível de habilidade do jogador quanto a classificação do jogador são dependentes do jogador, mas o erro é que a classificação do jogador é primeiramente dependente do nível de habilidade. Veja as dependências a seguir:

{id_jogador} → {nivel_habilidade_jogador}

{id_jogador} → {nivel_habilidade_jogador} → {classificacao_jogador}

A seta indica que o elemento a direita depende do da esquerda.

A Terceira Forma Normal diz que um atributo não-chave não pode depender de outro atributo não-chave. Ela diz que todo atributo não-chave em uma tabela deve depender na chave inteira, e nada além da chave.

Para resolver o problema, basta remover a coluna de classificação do jogador e criar uma nova tabela contendo a classificação e o nível de habilidade.

| id_jogador | classificacao_jogador |
| ---------- | --------------------- |
| jdog21     | intermediario         |
| gilal19    | iniciante             |
| trev73     | avançado              |
| tina42     | inicianate            |

| nivel_habilidade_jogador | classificacao_jogador |
| ------------------------ | --------------------- |
| 1                        | iniciante             |
| 2                        | iniciante             |
| 3                        | iniciante             |
| 4                        | intermediario         |
| 5                        | intermediario         |
| 6                        | intermediario         |
| 7                        | avancado              |
| 8                        | avancado              |
| 9                        | avancado              |

Em quase todos os casos, normalizar um banco de dados até a Terceira Forma Normal é o suficiente.

## Quarta Forma Normal

>A Quarta Forma Normal diz que dependências multivaloradas em uma tabela devem ser dependências multivaloradas na chave.

Suponhamos que um dono de um site que vende casas precisa organizar todos os dados das casas disponíveis em um banco de dados. Ele vende dois modelos diferentes de casas, com dois tamanhos e duas cores diferentes para cada modelo. Uma maneira de mostrar isso em tabelas é colocar todas as combinações em uma só tabela. Veja:

| modelo  | cor     | tamanho |
| ------- | ------- | ------- |
| Antigo  | Amarelo | Pequeno |
| Antigo  | Amarelo | Grande  |
| Antigo  | Azul    | Pequeno |
| Antigo  | Azul    | Grande  |
| Moderno | Branco  | Pequeno |
| Moderno | Branco  | Grande  |
| Moderno | Bege    | Pequeno |
| Moderno | Bege    | Grande  |

A tabela acima obedece a Terceira Forma Normal. A chave primária são as três colunas, e tudo depende da chave primária. Ainda assim, essa tabela está vulnerável a problemas. Suponhamos que o dono do site queira adicionar a cor verde ao modelo moderno. Assim, duas linhas a mais seriam adicionadas à tabela, uma pra mostrar a cor verde e o tamanho grande, e outra, a cor verde e o tamanho pequeno. Se esquecermos de adicionar uma linha para a casa moderna verde e grande e só colocarmos para a casa moderna verde e pequena, então teremos uma inconsistência de dados, pois apesar de termos uma cor disponível para o modelo grande, ela não seria mostrada. As cores disponíveis deveriam ser completamente independentes dos tamanhos disponíveis.

O relacionamento modelo e cor é um relacionamento de um para muitos, pois um modelo pode ter muitas cores. Um modelo também pode ter vários tamanhos. Este relacionamento é mostrado por uma seta com duas cabeças.

{modelo} ->> {cor}

{modelo} ->> {tamanho}

A Quarta Forma Normal diz que dependências multivaloradas em uma tabela devem ser dependências multivaloradas na chave. A tabela acima não está de acordo com a Quarta Forma Normal, pois cor e tamanho dependem do modelo, e modelo não é a chave, já que a chave são as três colunas. Assim, precisamos criar nvoas tabelas em que a chave é o modelo.

| modelo  | tamanho |
| ------- | ------- |
| Antigo  | Pequeno |
| Antigo  | Grande  |
| Moderno | Pequeno |
| Moderno | Grande  |

| modelo  | cor     |
| ------- | ------- |
| Antigo  | Amarelo |
| Antigo  | Azul    |
| Moderno | Branco  |
| Moderno | Bege    |

Assim, se quisermos adicionar a cor verde para o modelo moderno, basta colocá-la sem problemas.

| modelo  | cor     |
| ------- | ------- |
| Antigo  | Amarelo |
| Antigo  | Azul    |
| Moderno | Branco  |
| Moderno | Bege    |
| Moderno | Verde   |

## Quinta Forma Normal

>A Quinta Forma Normal nos diz que a tabela não pode ser um resultado lógico da junção de outras tabelas.

Suponhamos que haja três marcas de sorvete e cada uma delas oferece sabores de sorvete. Estas são as marcas e os sabores:

Gelinho: baunilha, chocolate, morango, chocolate com menta;

Albino: baunilha, uva;

Rainha: baunilha, morango, chocolate com menta.

Temos um amigo, Pedro, e perguntamos quais sabores e marcas ele gosta. Ele diz que gosta dos sabores baunilha e chocolate, e que gosta das marcas Gelinho e Albino.

Temos uma amiga, Sandra, e perguntamos quais sabores e marcas ela gosta. Ela diz que gosta dos sabores uva, chocolate com menta e morango, e das marcas Albino e Rainha.

Tendo tudo isso em mente, criamos uma tabela para mostrar o gosto de nossos amigos:

| pessoa | marca   | sabor               |
| ------ | ------- | ------------------- |
| Pedro  | Gelinho | Baunilha            |
| Pedro  | Gelinho | Chocolate           |
| Pedro  | Albino  | Baunilha            |
| Sandra | Albino  | Uva                 |
| Sandra | Rainha  | Chocolate com menta |
| Sandra | Rainha  | Morango             |

Depois de um tempo, Sandra diz que agora gosta também da marca Gelinho. Assim, precisamos atualizar a tabela. Podemos adicionar uma linha dizendo que ela gosta do sorvete de Morango do Gelinho, mas podemos esquecer de adicionar a linha que diz que ela gosta do de chocolate com menta do Gelinho.

Neste exemplo, erramos logo no início. Deveríamos criar uma tabela diferente para cada coisa: Uma para os sabores de cada marca, outra para as marcas preferidas das pessoas, e outra para os sabores preferidos das pessoas. Assim, se quisermos saber qual produto alguém gosta, basta fazer uma consulta na base de dados e fazer a junção das tabelas. A Quinta Forma Normal nos diz que a tabela não pode ser um resultado lógico da junção de outras tabelas.

Elas ficariam assim:

**Tabela marca_favorita_da_pessoa**

| pessoa | marca_favorita |
| ------ | -------------- |
| Pedro  | Gelinho        |
| Pedro  | Albino         |
| Sandra | Albino         |
| Sandra | Rainha         |

**Tabela sabor_favorito_da_pessoa**

| pessoa | sabor_favorito      |
| ------ | ------------------- |
| Pedro  | Baunilha            |
| Pedro  | Chocolate           |
| Sandra | Uva                 |
| Sandra | Chocolate com menta |
| Sandra | Morango             |

**Tabela sabores_disponiveis_marca**

| marca   | sabor               |
| ------- | ------------------- |
| Gelinho | Baunilha            |
| Gelinho | Morango             |
| Gelinho | Chocolate com menta |
| Albino  | Baunilha            |
| Albino  | Uva                 |
| Rainha  | Baunilha            |
| Rainha  | Morango             |
| Rainha  | Chocolate com menta |
