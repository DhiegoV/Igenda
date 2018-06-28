# Nome
Editar atividade.

# Descrição
Este caso de uso trata da edição do par título e descrição pelo usuário.

# Ator
Aluno.

# Pré-condições
A atividade a ser editada deve existir no sistema.

# Fluxo principal
1. O usuário entra com o comando para editar atividades, passando como
   argumento o número relacionado à atividade desejada;
2. O sistema pergunta ao usuário o título desejado à atividade;
3. O usuário entra com o título da atividade;
4. O sistema leva o usuário a um editor de texto, onde digita a descrição da
   atividade e salva;
5. O sistema informa onde a atividade foi salva;
6. O usuário retorna ao prompt principal.

# Fluxo alternativo
Entre 1 e 2:
1. Caso o número informado não referencie nenhuma atividade, o sistema informa
   o usuário a respeito;
2. O usuário retorna ao prompt principal.

