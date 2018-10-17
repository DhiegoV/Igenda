
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

