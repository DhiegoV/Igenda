# Nome
Tag atividade.

# Descrição
Para classificar atividades, igenda oferece o suporte a tags. Tags aqui são
palavras ou pequenos grupos nominais. Existem tags pré-definidas, como
"projeto", "prova" e "seminário", mas o usuário é livre para criar suas
próprias. Isto possibilita que Igenda seja usado para atividades de propósito
geral, apesar do foco estudantil.

# Ator
Aluno.

# Pré-condições
Alguma atividade deve existir para a qual serão aplicadas tags.

# Fluxo principal
1. O usuário entra com o comando para aplicar tags passando como argumento o
   número relacionado à atividade desejada.
2. O sistema mostra ao usuário as tags existentes, cada uma com um número
   relacionado;
3. O usuário referencia, pelos números, as tags que quer aplicar à atividade
   previamente escolhida.

# Fluxo alternativo
Entre 1 e 2:
1. Caso a atividade referenciada não exista, o sistema avisa ao usuário;
2. O usuário é levado de volta ao prompt principal.

# Referências cruzadas
Para mais sobre listagem de atividades, vide listar_atividades.csv .

