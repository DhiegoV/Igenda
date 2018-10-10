
class Fachada:

	def __init__(self):
		self.atividades = []

	def apagar_atividade(self, atividade):
		"""Dada uma atividade, apague-a do sistema.

		`atividade` eh uma instancia de Atividade.
		"""
		self.atividades.remove(atividade)

	def criar_atividade(self, atividade):
		"""Dada uma atividade, adicione-a ao sistema.

		`atividade` eh uma instancia de Atividade.
		"""
		self.atividades.append(atividade)

	def obter_atividades(self):
		"""Retorne uma lista com as atividades do sistema."""
		return self.atividades

