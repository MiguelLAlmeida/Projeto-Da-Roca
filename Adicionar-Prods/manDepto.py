import sys
from PySide6.QtCore import QtMsgType
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QDialog, QTableWidgetItem
from FrmDepto_ui import Ui_DRprods
from FrmConexao_ui import Ui_dlgConectar
import pyodbc as bd
from datetime import datetime

global conexao, meuCursor

class FormPrincipal(QMainWindow, Ui_DRprods):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # associa o evento Click de cada botão a um método
        # da classe FormPrincipal que implementa o algoritmo
        # que se espera que esse botão dispare para execução
        self.action_Sair.triggered.connect(self.sairDoPrograma)
        self.action_Salvar.triggered.connect(self.salvarRegistro)

        self.osDados = []
        self.quantosDados = 0
        self.registroAtual = -1  # índice do registro visitado (na tela)
        self.buscarDados()

        self.show()
        self.situacao = "navegando"

    def buscarDados(self):
        try:
            sComando = "SELECT nome, imagem, "+\
                " valor, descricao, categoria  "+\
                " FROM daroca.produtos "+\
                " ORDER BY id"
            resultado = meuCursor.execute(sComando)
            self.osDados = resultado.fetchall()    # vetor de registros
            self.quantosDados = len(self.osDados)  # quantos registros
            if self.quantosDados > 0:   # dados foram trazidos
                self.registroAtual = 0  # posiciona no primeiro índice
        except:
            print("Erro ao buscar os dados para navegação.")

    def salvarRegistro(self):
        self.situacao = "incluindo"
        if self.situacao == "incluindo":
            sComando = "Insert into daroca.produtos "+\
                " (nome, imagem, valor, "+\
                " descricao, categoria) "+\
                " values( ?, ?, ?, ?, ? ) "

            try:        # tente executar o comando abaixo:
                meuCursor.execute(sComando,
                                           self.nomeProd.text(), 
                                           self.imgProd.text(),
                                           int(self.valorProd.value()),
                                           self.descProd.text(),
                                           int(self.categProd.value()),
                                )
                meuCursor.commit()  # enviar as mudanças para o BD
                self.statusBar.showMessage("Inserido") 
   
            except Exception as erro:     # em caso de erro
                if hasattr(erro, 'message'):
                    mensagem = erro.message
                else:
                    mensagem = erro.args[1]
                self.statusBar.showMessage(mensagem)
        self.situacao = "navegando"

    def sairDoPrograma(self):
        self.close()

class DialogoConexao(QDialog, Ui_dlgConectar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

aplicacao = QApplication(sys.argv)
dlgCon = DialogoConexao()   # cria instância da janela de conexão ao BD
if dlgCon.exec() == QDialog.Accepted:
    try:
        conexao = bd.connect(driver="SQL Server",
                            server=f"{dlgCon.edServidor.text()}",
                            database=f"{dlgCon.edBancoDeDados.text()}",
                            uid=f"{dlgCon.edUsuario.text()}",
                            pwd=f"{dlgCon.edSenha.text()}") 
        print("Conexão bem sucedida!")
        meuCursor = conexao.cursor()  # cursor: objeto de acesso ao BD
        janela = FormPrincipal()
        aplicacao.exec()
    except:
        print("Não foi possível conectar ao banco de dados")




