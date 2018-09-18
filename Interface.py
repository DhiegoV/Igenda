
from Atividade import Atividade
from Fachada import Fachada

class Interface:

    def __init__(self):
        self.fachada = Fachada()
        self.ajuda = \
            "l listar atividades\n" \
            "c criar atividade\n"   \
            "x sair"

    def iniciar(self):

        print("Insira h para ajuda")

        while True:
            self.prompt()

    def prompt(self):

        entrada = input('> ')

        if entrada == 'h':
            print(self.ajuda)
        elif entrada == 'x':
            exit()
        elif entrada == 'c':
            self.criar_atividade()
        elif entrada == 'l':
            self.listar_atividades()

    def criar_atividade(self):
        
        nome = input('nome: ')
        deadline = input('deadline: ')
        disciplina = input('disciplina: ')

        atividade = Atividade(nome, deadline, disciplina)
        
        self.fachada.criar_atividade(atividade)

    def listar_atividades(self):

        atividades = self.fachada.obter_atividades()

        for atividade in atividades:
            print(atividade)

