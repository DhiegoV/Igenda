
class Fachada:

	def __init__(self):
		self.atividades = []

	def apagar_atividade(self, atividade):
		self.atividades.remove(atividade)

	def criar_atividade(self, atividade):
		self.atividades.append(atividade)

	def obter_atividades(self):
		return self.atividades

