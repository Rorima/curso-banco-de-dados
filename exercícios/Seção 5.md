**Qual a necessidade de se utilizar a cláusula WHERE em uma consulta?**

O `WHERE` filtra a consulta, permitindo que sejam mostrados os dados que obedecem a uma certa restrição.

**Por que às vezes precisamos fazer consultas em múltiplas tabelas?**

Por causa das regras de normalização, é comum separar os dados em diversas tabelas diferentes e relacioná-las. Sendo assim, faz-se necessário fazer consultas em múltiplas tabelas para se obter os dados desejados.

**O que é a junção de tabelas?**

A junção de tabelas é o ato de juntar tabelas para se obter os dados desejados. Ela cria uma pseudo-tabela derivada de duas ou mais tabelas de acordo com as regras especificadas, que são parecidas com as regras da **Teoria dos Conjuntos**.

**O que são funções de agregação? Cite 3 que você ache mais importantes.**

As funções de agregação são funções que agregam um conjunto de valores em um único resultado através de uma consulta. As mais importantes são: 

* `SUM()`: soma todos os valores de uma coluna;
* `MAX()` mostra o maior valor da coluna;
* `MIN()` mostra o menor valor da coluna.

**Por que às vezes precisamos agrupar resultados?**

Quando utilizamos uma função de agregação em uma consulta juntamente com outros campos, devemos sempre utilizar o agrupamento (GROUP BY) por algum elemento da consulta.

**Qual é a forma padrão de ordenação de resultados em uma consulta?**

A forma padrão de ordenação em uma consulta é a ordenação ascendente feita pelo id da tabela.

**Cite 3 funções de dada e hora.**

* `NOW()`: Mostra a data e hora atuais;
* `CURDATE()`: Mostra a data atual;
* `DATE_FORMAT()`: Retorna a data em um formato especificado.

**O que são subconsultas?**

Uma subconsulta é uma instrução `SELECT` dentro de outro `SELECT`, que retorna algumas colunas específicas que são usadas em algumas funções, como `INSERT`, `UPDATE` e `DELETE`, por exemplo.