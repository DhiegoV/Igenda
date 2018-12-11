from Atividade import Atividade
from Fachada import Fachada

class Interface:

	def __init__(self):
		self.fachada = Fachada()
		self.ajuda = \
			"a apagar atividade\n"           \
			"c criar atividade\n"            \
			"e editar atividade\n"           \
			"h mostrar essa ajuda\n"         \
			"l listar atividades\n"          \
			"m marcar estado de atividade\n" \
			"x sair"

	def iniciar(self):
		"""Inicie o sistema."""

		self.fachada.carregar_atividades()

		print("Insira h para ajuda")

		while True:
			self.prompt()

	def finalizar(self):
		"""Finalize o sistema."""

		self.fachada.salvar_atividades()
		exit()

	def prompt(self):
		"""Solicite entrada do usuario."""

		entrada = input('> ')

		if entrada == 'h':
			print(self.ajuda)
		elif entrada == 'x':
			self.finalizar()
		elif entrada == 'a':
			self.apagar_atividade()
		elif entrada == 'c':
			self.criar_atividade()
		elif entrada == 'e':
			self.editar_atividade()
		elif entrada == 'l':
			self.listar_atividades()
		elif entrada == 'm':
			self.marcar_estado_atividade()

	def apagar_atividade(self):
		"""Permita o usuario escolher uma atividade para apagar."""

		self.listar_atividades()

		numero_atividade = int(input('número da atividade: '))

		atividades = self.fachada.obter_atividades()
		atividade_selecionada = atividades[numero_atividade-1]

		self.fachada.apagar_atividade(atividade_selecionada)

	def editar_atividade(self):
		self.listar_atividades()

		# TODO colocar excecao aqui, pra caso nao seja digitado numero
		numero_atividade = int(input("número da atividade a editar: "))

		lista_atividades = self.fachada.obter_atividades()
		# TODO colocar excecao aqui, pra caso numero informado nao corresponda a alguma coisa
		atividade = lista_atividades[numero_atividade-1]

		print(
			"1 nome", "(" + atividade.nome + ")\n"
			"2 deadline", "(" + atividade.deadline + ")\n"
			"3 disciplina", "(" + atividade.disciplina + ")"
		)

		# TODO colocar excecao aqui, pra caso nao seja digitado numero
		numero_atributo = int(input("número do atributo a editar: "))

		if numero_atributo == 1:
			novo_nome = input("novo nome: ")
			atividade.nome = novo_nome
		elif numero_atributo == 2:
			nova_deadline = input("nova deadline: ")
			atividade.deadline = nova_deadline
		elif numero_atributo == 3:
			nova_disciplina = input("nova disciplina: ")
			atividade.disciplina = nova_disciplina
		else:
			print("número não corresponde a nenhum atributo")

		# atualizando lista de atividades com a atividade modificada
		lista_atividades[numero_atividade-1] = atividade

		self.fachada.atualizar_atividades(lista_atividades)

	def criar_atividade(self):
		"""Crie uma atividade solicitando ao usuario os dados necessarios."""

		nome = input('nome: ')
		deadline = input('deadline: ')
		disciplina = input('disciplina: ')

		atividade = Atividade(nome, deadline, disciplina)

		self.fachada.criar_atividade(atividade)

	def marcar_estado_atividade(self):
		"""Permita ao usuario marcar o estado de uma atividade."""

		self.listar_atividades()

		numero_atividade = int(input('marcar conclusão em atividade de número: '))

		atividades = self.fachada.obter_atividades()
		atividade_selecionada = atividades[numero_atividade - 1]

		self.fachada.marcar_estado_atividade(atividade_selecionada)

	def listar_atividades(self):
		"""Mostre ao usuario uma lista numerada de atividades."""

		atividades = self.fachada.obter_atividades()

		contador = 1
		for atividade in atividades:
			print(str(contador) + ' ' + str(atividade))
			contador += 1

