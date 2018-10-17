
Temos que obter do usuário uma data para a entrega da atividade, mas no
momento estamos só recebendo uma string dele.

### Como obter essa data?

Um dos problemas mais evidentes é exatamente o jeito que o usuário entrará com
essa data.

Uma sugestão do professor foi mostrar um calendário e deixar o usuário escolher
um dia. Todavia, uma coisa que ele deve ter se esquecido é que estamos tratando
de um programa de terminal, no qual não dá pra _clicar_ em alguma coisa, mas
apenas digitar. Tudo bem, então deixemos o usuário navegar com setas pelo
calendário. Isso parece uma boa ideia, mas adiciona muita complexidade: teremos
que saber a posição atual do cursor, detectar as teclas pressionadas, atualizar
isso no calendário e o pior: isso tudo só para a simples tarefa de selecionar o
dia de entrega da atividade.

Dada a minha cara de "caramba, isso vai ser complicado" que fiz quando o prof.
falou da ideia acima, ele sugeriu algo melhor: Pedir do usuário o dia, mês e
ano separadamente, imagino que da seguinte forma (os números são entradas do
usuário):

	[...]
	deadline,
	dia: 14
	mês: 5
	ano: 2018

Eu gostei, simplifica o programa e a gente pode usar as facilidades do tipo
`date` de Python. No entanto, ainda assim eu acho que pode melhorar: Da mesma
forma que eu penso (mas ainda falta escrever aqui) para a seleção de
disciplinas e futuras tags, seria mais útil e conveniente algumas opções mais
significativas, isto é, relativas ao dia corrente, do que apenas números
absolutos, como por exemplo "amanhã", "depois de amanhã" ou até mesmo submenus
como "na próxima..." que levariam para uma lista de dias de semana como a
seguinte:

	s segunda
	t terça
	q quarta
	i quinta
	x sexta
	b sábado
	d domingo

Outro submenu poderia ser "nesta..." que aí levaria para uma lista como esta
acima, mas faria referência à semana corrente. Outro ponto positivo destes dias
relativos é que escolhido um, a gente pode dispensar pedir o mês ou ano, pois
já sabemos deles.

Um exemplo de utilização:

	> c
	nome: prova
	deadline,

	a amanhã
	d depois de amanhã
	n nesta...
	p na próxima...
	ou insira um número
	dia: p

	s segunda
	t terça
	q quarta
	i quinta
	x sexta
	b sábado
	d domingo
	dia: q

	Marcada para próxima quarta, dia 14 de Janeiro de 2019

	disciplina: aps

Outro:

	> c
	nome: trabalho
	deadline,
	a amanhã
	d depois de amanhã
	n nesta...
	p na próxima...
	ou insira um número
	dia: 12

	mês,
	a atual
	p próximo
	ou insira um número
	mês: p

	Marcada para dia 12 de Fevereiro de 2019

	disciplina: quimica

