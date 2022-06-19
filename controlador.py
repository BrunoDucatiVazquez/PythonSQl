from PyQt5 import uic, QtWidgets
from numpy import datetime_data
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "",
    database = "cadastro-produtos",
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ""

    if formulario.radioButton.isChecked():
        print("Categoria Informatica foi selecionado")
        categoria = "Informatica"
    elif formulario.radioButton_2.isChecked():
        print("Categoria Alimentos foi selecionado")
        categoria = "Alimentos"
    elif formulario.radioButton_3.isChecked():
        print("Categoria Eletronicos foi selecionado")
        categoria = "Eletronicos"
    print("Codigo:", linha1)
    print("Descrição:", linha2)
    print("Preço:", linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "select * from produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos[0][0])

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            segunda_tela.tableWidget.setItem(i,j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
formulario.show()
app.exec()