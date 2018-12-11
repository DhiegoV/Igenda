
import sqlite3
from Atividade import Atividade

class AtividadeDAO:

	def __init__(self):
		self.conexao = sqlite3.connect("atividades.sqlite")

	# ALTERAÇÕES

	def inicializar_banco(self):

		self.alterar_banco(
			'''
			create table atividade(
				nome varchar(50),
				deadline varchar(50),
				disciplina varchar(100),
				concluida varchar(5)
			)
			'''
		)

	def salvar_atividades(self, atividades):

		try:
			for atividade in atividades:
				self.alterar_banco(
					'insert into atividade(nome, deadline, disciplina, concluida) VALUES ' +
					'(\'{}\', \'{}\', \'{}\', \'{}\')'.format(
						atividade.nome,
						atividade.deadline,
						atividade.disciplina,
						str(atividade.concluida)
					)
				)
		except sqlite3.OperationalError:
			self.inicializar_banco()
			self.salvar_atividades(atividades)

	# CONSULTAS

	def carregar_atividades(self):
		tuplas_atividades = self.consultar_banco('select * from atividade')

		atividades = []
		for tupla in tuplas_atividades:
			atividade = Atividade(
				tupla[0], # nome
				tupla[1], # deadline
				tupla[2], # disciplina
				bool(tupla[3]) # concluida
			)

			atividades.append(atividade)

		return atividades

	# MÉTODOS DE UTILIDADE

	def alterar_banco(self, comando_sql):
		cursor = self.conexao.cursor()
		cursor.execute(comando_sql)
		cursor.close()
		self.conexao.commit()

	def consultar_banco(self, comando_sql):
		cursor = self.conexao.cursor()
		cursor.execute(comando_sql)
		tupla = cursor.fetchall()
		cursor.close()
		return tupla
