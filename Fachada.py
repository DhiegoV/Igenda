
class Fachada:

    def __init__(self):
        self.atividades = []

    def criar_atividade(self, atividade):
        self.atividades.append(atividade)

    def obter_atividades(self):
        return self.atividades

