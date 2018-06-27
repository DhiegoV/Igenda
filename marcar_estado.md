# Nome
Marcar estado.

# Descrição
O usuário pode marcar o estado de uma atividade. Isto é, se ela foi concluída
ou está em andamento. A toda atividade, quando criada, é atribuído o estado
"Não iniciada". Ao marcar conclusão de uma atividade, é dada a opção de
excluí-la também, caso o usuário opte por não excluir, ela será arquivada.

# Ator
Usuário.

# Pré-condições
Deve existir pelo menos uma atividade já registrada no sistema.

# Fluxo principal
1. O usuário entra com o comando para marcar estado, passando como argumento o
   número que referencia a atividade desejada;
2. O sistema mostra ao usuário uma lista de estados, cada um com o seu número;
3. O usuário referencia, com um número, o estado desejado;
4. O sistema muda o estado da atividade para o indicado pelo usuário.

# Fluxo alternativo
Entre 1 e 2:
1. Se a atividade indicada pelo usuário não existe, o sistema informa o usuário
   disso;
2. O usuário é levado de volta ao prompt principal.

Entre 3 e 4:
1. Se número informado não fizer referência a nenhum estado, o sistema informa
   o usuário de acordo;
2. O sistema volta à execução do passo 1 do fluxo principal.

