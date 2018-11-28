# Nome

Editar atividade.

# Descrição

Este caso de uso trata da edição dos atributos da atividade.

# Ator

Aluno.

# Pré-condições

A atividade a ser editada deve existir no sistema.

# Fluxo principal

1. O usuário entra com o comando para editar atividades;
2. O sistema mostra a lista de atividades enumerada;
3. O sistema pergunta ao usuário qual o número da atividade a ser editada;
4. O usuário responde com o número da atividade que quer editar;
5. O sistema mostra uma lista numerada dos atributos, ao lado de cada um está o seu valor atual, entre parênteses;
6. O sistema pergunta ao usuário qual o número da atributo a ser editado;
7. O usuário responde com o número do atributo que quer editar;
8. O sistema pergunta o novo valor para o atributo;
9. O usuário responde com o novo valor;
10. O usuário retorna ao prompt principal.

# Fluxos alternativos

## Entre 1 e 2:

1. Caso o sistema não tenha nenhuma atividade para editar;
2. O sistema informa ao usuário que não existe atividade para editar;
3. O usuário retorna ao prompt principal.

## Entre 4 e 5 e entre 7 e 8:

1. Caso o número digitado não corresponda a alguma coisa na lista ou for omitido;
2. O sistema informa ao usuário que o número digitado não corresponde a nada;
3. O usuário retorna ao prompt principal.

# Pós-condições:

A atividade deve ter sido editada como esperado.

