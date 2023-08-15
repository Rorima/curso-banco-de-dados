# Exercícios da Seção 3

**Defina Modelagem Conceitual:**

>Na modelagem conceitual, é feita a representação abstrata do negócio, onde são definidas as entidades, seus atributos e relacionamentos.

**Defina Modelagem Lógica:**

>Na modelagem lógica, o modelo conceitual é implementado em uma ferramenta gráfica e mais detalhes são adicionados. É aqui que são criadas as tabelas, definidos os tipos de dados para cada coluna como também as chaves primárias e estrangeiras. Neste nível, as regras de integridade e normalização são aplicadas.

**Defina Modelagem Física:**

>Na modelagem física, o modelo lógico é implementado em um banco de dados real. O particionamento, índicies e organização física dos dados são definidas neste nível.

**Explique a Cardinalidade Máxima e Mínima entre relações:**

>A cardinalidade é sempre o relacionamento entre coisas. A cardinalidade máxima é sempre um ou muitos. A cardinalidade mínima é sempre zero ou um. São cardinalidades comuns as seguitnes; *um-para-um*, *um-para-muitos* e *muitos-para-muitos*.
>
>Um exemplo de relacionamento um-para-um é o relacionamento entre um escritório e um executivo. Um executivo tem apenas um escritório, e um escritório suporta apenas um executivo.
>
>Um exemplo de relacionamento um-para-muitos é o de uma mãe e filhos. Uma mãe tem muitos filhos, mas os filhos tem uma só mãe.
>
>Um exemplo de relacionamento um muitos-para-muitos é o de amigos. Amigos podem ter amigos e vice-versa.

**O que é a Normalização de Dados?**

>É ajustar as tabelas de um banco de dados para que elas respeitem as Formas Normais. Assim o banco de dados não terá informações redundantes.

**Defina a Primeira Forma Normal**

> A Primeira Forma Normal nos diz que:
>
> * Não devemos depender da ordem dos dados de uma tabela;
> * Não podemos misturar tipos de dados diferentes em uma mesma coluna (campo);
> * Não devemos fazer uma tabela sem chave primária;
> * Não devemos ter grupos repetidos em uma coluna.

**Defina a Segunda Forma Normal:**

> A Segunda Forma Normal diz que cada atributo (ou coluna) não-chave deve  depender da chave primária inteira.

**Defina a Terceira Forma Normal:**

> A Terceira Forma Normal diz que um atributo não-chave não pode depender de outro atributo não-chave. Ela diz que todo atributo não-chave em uma tabela deve depender na chave inteira, e nada além da chave.

**O que é o MER - Modelo de Entidade e Relacionamento?**

> Um Modelo de Entidade e Relacionamento descreve coisas relacionadas entre si em um domínio específico de conhecimento. Ele é geralmente composto por tipos de entidades que classificam coisas e especificam relacionamentos que podem existir entre as entidades.

**O que é o DER - Diagrama de Entidade e Relacionamento?**

> Um diagrama de Entidade e Relacionamento mostra várias entidades do mesmo tipo e os relacionamentos entre essas entidades.

**Construa o Diagrama Entidade-Relacionamento para o sistema abaixo:**

Em uma clínica trabalham médicos de diversas especialidades. 

Cada médico é identificado pelo seu CRM, possui um nome e recebe um salário na clínica. 

Um médico pode ter formação em diversas especialidades (ortopedia, traumatologia, etc) mas só exerce uma delas na clínica. 

Para todo paciente internado na clínica são cadastrados alguns dados pessoais: nome, RG, CPF, endereço, telefone(s) para contato e data de nascimento. 

Um paciente tem sempre um determinado médico como responsável (com um horário de visita diário predeterminado), porém vários outros médicos podem participar do seu tratamento. 

Pacientes estão sempre internados em quartos individuais, que são identificados por um número e ficam em um andar da clínica. 


**Construa o Diagrama Entidade-Relacionamento para o sistema abaixo:**

Uma faculdade oferece vários cursos cujos currículos são compostos por diversas disciplinas. 

Cada disciplina pode ser oferecida para vários cursos distintos; uma disciplina pode ter outras disciplinas como pré-requisitos em série ou em paralelo. 

Na faculdade há diferentes tipos de pessoas identificadas por um único número funcional: os alunos, professores e funcionários – cada qual com seus atributos gerais e específicos (defina alguns). 

Os alunos como na Geek University, só podem estar inscritos em um único curso em um dado momento (status ativo), e só poderão se inscrever em outro curso caso todas as suas inscrições estejam finalizadas (status concluído) – são armazenadas informações de ano de início e de término. 

Em cada semestre, os alunos matriculam-se em turmas correspondentes às disciplinas do seu curso. 

Professores podem ministrar para várias turmas, e toda turma tem obrigatoriamente um professor. 

Os funcionários auxiliam os professores, sem exclusividade. 

Tanto os professores quanto os funcionários podem decidir se matricular em um curso da universidade, com as devidas restrições. 

A base de dados deve permitir a geração de listas de notas para cada turma, onde deve constar com que professor um aluno fez qual disciplina.

**Construa o Diagrama Entidade-Relacionamento para o sistema abaixo:**

Uma garagem para estacionamento de veículos pretende implementar um sistema que lhe permita administrar a informação relativa ao estacionamento dos seus clientes. 

A garagem é composta por um conjunto de vagas, cada uma podendo estar ocupada ou não. 

Há dois tipos de vagas: avulsa (se houver disponibilidade) ou mensal. 

Cada vaga tem um preço – a avulsa tem um custo por hora e a mensal, um custo fixo. 

Os preços serão diferenciados de acordo com o tipo de veículo: automóvel ou moto.

Cada vaga mensal possui um cliente associado. Para cada cliente é registrado seu nome e CPF, sendo que um dado cliente pode contratar várias vagas mensais. 

A cada vez que um cliente estacionar um veículo (fizer uma estacionagem), deverá se armazenar o CPF do cliente, código da vaga, a data/hora de entrada e de saída, a placa do veículo estacionado e o custo gerado (que pode ser 0 para clientes mensais).

**Construa o Diagrama Entidade-Relacionamento para o sistema abaixo:**

Uma pizzaria de tele-entrega apresenta um cardápio composto por diversos tipos de pizza, cujos dados são: número do item, nome da pizza, lista de ingredientes e preços das pizzas pequena, média e grande, como por exemplo: (12, francesa, (queijo, presunto, champignon, aspargo), 10.00, 15.00, 18.00). 

Na pizzaria trabalham funcionários que emitem pedidos de pizzas. Cada pedido possui um número e uma data de emissão, além do nome, telefone e endereço do cliente que solicitou o pedido. 

Um pedido, emitido por apenas um funcionário, é composto por vários itens: cada item possui um número e se refere a uma determinada pizza do cardápio, em um determinado tamanho (pequena, média ou grande) e em uma certa quantidade. 

Dos funcionários entregadores (ou seja, responsáveis pela entrega de um ou mais pedidos), deve-se saber o número do telefone celular para um eventual contato durante uma entrega. 

Uma entrega destina-se a um bairro, e para cada bairro existe um tempo máximo de espera para a entrega de um pedido. 

Defina outras entidades/atributos que julgar relevante.

**Construa o Diagrama Entidade-Relacionamento para o sistema abaixo:**

Uma empresa de reparo de automóveis pretende implementar um sistema para administrar a informação relativa aos reparos efetuados nos veículos de seus clientes. 

O sistema de informação deverá permitir manter um registro de todos os reparos efetuados. A empresa registra as seguintes informações de cada cliente: código de identificação, nome, endereço, telefone. 

A informação relativa aos veículos que um dado cliente teve ou tem e as datas em que fizeram o primeiro reparo, também são importantes. 

Em relação aos funcionários da oficina é necessário registrar a seguinte informação: código de identificação, nome, endereço, telefone e categoria profissional. 

O custo/hora da mão-de-obra depende da categoria do funcionário e é definido por meio de uma tabela que é atualizada regularmente. 

Em relação a cada reparo é necessário saber: qual veículo, qual cliente, a data em que o reparo foi efetuado e o custo total do reparo. 

A empresa pretende saber para cada reparo quais peças foram utilizadas e o seu preço, bem como o tempo de mão de obra gasto por cada funcionário e o respectivo custo. 

A informação relativa às peças em estoque deverá ser: código de identificação, designação, custo unitário e quantidade armazenada.
