from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = cadastro_lineEdit.text()
    linha2 = cadastro_lineEdit_2.text()
    linha3 = cadastro_lineEdit_3.text()

    if cadastro.radioButton.isChecked() :      
        print("Categoria Alimentos foi selecionado")
    elif cadastro.radioButton_2.isChecked() :      
        print("Categoria Descricao foi selecionado")
    else cadastro.radioButton_3.isChecked() :      
        print("Categoria Preco foi selecionado")

    print("Codigo",linha1)
    print("Descricao",linha2)
    print("Preco",linha3)


app=QtWidgets.QApplication([])
cadastro=uic.loadUi("cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()