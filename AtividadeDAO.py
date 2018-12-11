
import sqlite3

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

	def obter_atividades(self):
		atividades = self.consultar_banco('select * from atividade')
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
