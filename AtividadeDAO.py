
import sqlite3

class UsuarioDAO:

	def __init__(self):
		self.conexao = sqlite3.connect("atividades.sqlite")

	# ALTERAÇÕES

	def salvar_atividades(self, atividades):
		self.alterar_banco(
			'insert into atividade(nome, deadline, disciplina, concluida) VALUES ' +
			'(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(
				usuario.get_nome(),
				usuario.get_email(),
				usuario.get_idade(),
				usuario.get_senha(),
				usuario.get_apelido()
			)
		)

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
