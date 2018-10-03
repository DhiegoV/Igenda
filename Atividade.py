
class Atividade:

	def __init__(self, nome, deadline, disciplina):
		self.nome = nome
		self.deadline = deadline
		self.disciplina = disciplina

	def __str__(self):
		return self.nome + ' | ' + self.disciplina

