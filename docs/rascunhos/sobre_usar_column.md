
Fazer uma interface amigável mesmo tratando-se de linha de comando é
complicado. Uma das formas de fazer isso é mostrando tabelas com colunas
alinhadas, é aí que `column` entra. Não o utilizaremos, mas fica registrado que
cogitamos usá-lo.

Ele é uma ferramenta do Linux, mas não parte do POSIX, que _encoluna_ listas e
formata tabelas. Ambas estas funções podemos usar: a primeira serviria para que
numerosos itens não ocupassem tanto espaço vertical, pois isso:

	amarelo
	azul
	vermelho

vira isso:

	amarelo		azul		vermelho

A segunda serviria para ajudar na visualização das atividades, pois o que seria
isso:

	1 comprar pão (não concluída)
	2 comprar ovos (não concluída)
	3 fazer dever de casa (não concluída)
	4 prova (não concluída)

pode virar isso:
	
	número  atividade            estado
	1       comprar pão          (não concluída)
	2       comprar ovos         (não concluída)
	3       fazer dever de casa  (não concluída)
	4       prova                (não concluída)

### Problemas

Usar uma ferramenta externa gera dependência. Como eu quero que este seja um
programa multi-plataforma, não usaremos o `column`. Ao invés dele, temos ao
nosso dispor o mais complicado, mas parte do Python, método [format()][] do
tipo `str`. Usando ele, conseguimos o feito de tornar o programa executável em
qualquer ambiente que tenha o interpretador Python instalado, ao invés de,
usando o `column`, precisar também que este esteja instalado.

[format()]: https://docs.python.org/3.6/library/stdtypes.html#str.format

