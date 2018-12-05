
class Atividade:

	def __init__(self, nome, deadline, disciplina, concluida=False):
		self.nome = nome
		self.deadline = deadline
		self.disciplina = disciplina
		self.concluida = concluida

	def __str__(self):
		if self.concluida:
			concluida_str = 'concluída'
		else:
			concluida_str = 'não concluída'

		return self.nome + \
			   ' [de ' + self.disciplina + ']' + \
			   ' [para ' + self.deadline + ']' + \
			   ' (' + concluida_str + ')'

