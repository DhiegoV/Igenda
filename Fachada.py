
class Fachada:

	def __init__(self):
		self.atividades = []

	def apagar_atividade(self, atividade):
		"""Dada uma atividade, apague-a do sistema.

		`atividade` eh uma instancia de Atividade.
		"""
		self.atividades.remove(atividade)

	def marcar_estado_atividade(self, atividade):
		"""Dada uma atividade, marque-a como concluida.

		`atividade` eh uma instancia de Atividade.
		"""
		for atividade_guardada in self.atividades:
			if atividade_guardada == atividade:
				atividade_guardada.concluida = True

	def criar_atividade(self, atividade):
		"""Dada uma atividade, adicione-a ao sistema.

		`atividade` eh uma instancia de Atividade.
		"""
		self.atividades.append(atividade)

	def obter_atividades(self):
		"""Retorne uma lista com as atividades do sistema."""
		return self.atividades

