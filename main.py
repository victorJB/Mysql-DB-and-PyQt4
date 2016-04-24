import MySQLdb

from PyQt4 import QtGui

import sys


class Ventana(QtGui.QWidget):

    def __init__(self):
        super(Ventana, self).__init__()

        self.setWindowTitle("Biblioteca")

        self.resize(450, 350)

        ##Estableciendo conexion con la base de datos
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="library")
        self.cursor = self.conn.cursor()

        self.label1 = QtGui.QLabel("Username", self)
        self.label2 = QtGui.QLabel("Password", self)
        self.label3 = QtGui.QLabel("Bienvenido al Sistema de Biblioteca", self)
        self.label4 = QtGui.QLabel("Nuevo usuario ------>", self)
        self.label5 = QtGui.QLabel("Bienvenido al Sistema de Biblioteca", self)
        self.label6 = QtGui.QLabel("Bienvenido al Sistema de Biblioteca ", self)
        self.label7 = QtGui.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.label8 = QtGui.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)

        self.idUsuario = 0
        self.nombreDelUsuario = ""

        ## boton ventana princial Aceptar
        self.button1 = QtGui.QPushButton("Aceptar", self)

        ##boton ventana principal Registrar
        self.button2 = QtGui.QPushButton("Registrar", self)

        ##boton ventana agregar nuevo usuario Registrar
        self.button3 = QtGui.QPushButton("Registrar", self)

        ##boton ventana agregar nuevo usuario Cancelar
        self.button4 = QtGui.QPushButton("Cancelar", self)

        ##boton al loguearse como usuario correcto Aceptar
        self.button5 = QtGui.QPushButton("Aceptar", self)

        ##boton al entrar a la base de datos Ver Lista de Usuarios
        self.button6 = QtGui.QPushButton("Ver Lista de Usuarios", self)

        ##Boton al registrar un usuario correcto Aceptar
        self.button7 = QtGui.QPushButton("Aceptar", self)

        ##Botones Base de Datos
        self.button8 = QtGui.QPushButton("Renovar libro", self)
        self.button9 = QtGui.QPushButton("Cerrar Sesion", self)
        self.button10 = QtGui.QPushButton("Buscar libro", self)
        self.button11 = QtGui.QPushButton("Aceptar", self)
        self.button12 = QtGui.QPushButton("Aceptar", self)

        ##Botones Unicamente Modo Admin
        self.button13 = QtGui.QPushButton("Agregar nuevo libro", self)
        self.button14 = QtGui.QPushButton("Modificar libro", self)
        self.button15 = QtGui.QPushButton("Autorizar prestamo", self)
        self.button16 = QtGui.QPushButton("Devolver prestamo", self)

        self.lineEdit9 = QtGui.QLineEdit(self)
        self.lineEdit10 = QtGui.QLineEdit(self)
        self.lineEdit11 = QtGui.QLineEdit(self)
        self.lineEdit12 = QtGui.QLineEdit(self)
        self.label9 = QtGui.QLabel("Mis prestamos de libros", self)
        self.label10 = QtGui.QLabel("Libros disponibles en la Biblioteca", self)
        self.label11 = QtGui.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.label12 = QtGui.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.label13 = QtGui.QLabel("Usernamenndjhdjdjdjdjdjddhdhdh hdhd", self)
        self.textEdit2 = QtGui.QTextEdit("", self)
        self.textEdit2.setGeometry(20, 60, 650, 500)
        self.textEdit2.hide()

        self.button8.hide()
        self.button9.hide()
        self.button10.hide()
        self.button11.hide()
        self.button12.hide()
        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.lineEdit9.hide()
        self.lineEdit10.hide()
        self.lineEdit11.hide()
        self.lineEdit12.hide()
        self.label9.hide()
        self.label10.hide()
        self.label11.hide()
        self.label12.hide()
        self.label13.hide()

        self.lineEdit1 = QtGui.QLineEdit(self)

        ##Line Edit utilizada unicamente para password en ventana inicial
        self.lineEdit2 = QtGui.QLineEdit(self)

        self.lineEdit3 = QtGui.QLineEdit(self)
        self.lineEdit4 = QtGui.QLineEdit(self)
        self.lineEdit5 = QtGui.QLineEdit(self)
        self.lineEdit6 = QtGui.QLineEdit(self)
        self.lineEdit7 = QtGui.QLineEdit(self)

        ##Line Edit utilizada unicamente para password en ventana Registro de nuevo usuario
        self.lineEdit8 = QtGui.QLineEdit(self)

        self.textEdit1 = QtGui.QTextEdit("",self)
        self.textEdit1.setGeometry(20, 60, 650 , 500)
        self.textEdit1.hide()

        self.label1.move(90, 90)
        self.label2.move(90, 120)
        self.label3.move(135, 20)
        self.label4.move(160, 225)
        self.button1.move(300, 89)
        self.button2.move(300, 220)
        self.button6.move(680, 80)
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()
        self.label8.hide()
        self.lineEdit3.hide()
        self.lineEdit4.hide()
        self.lineEdit5.hide()
        self.lineEdit6.hide()
        self.lineEdit7.hide()
        self.lineEdit8.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.hide()
        self.button6.hide()
        self.button7.hide()
        self.lineEdit1.setGeometry(150, 90, 135, 20)
        self.lineEdit2.setGeometry(150, 120, 135, 20)
        self.lineEdit1.setText("")
        self.lineEdit2.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")
        self.lineEdit7.setText("")
        self.lineEdit8.setText("")
        self.pixmapa1 = QtGui.QPixmap("C:\\HelloW.jpg")


        ##Colocando ambas LineEdit con propiedades de password unicamente
        self.lineEdit2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit8.setEchoMode(QtGui.QLineEdit.Password)

        self.button1.clicked.connect(self.iniciarBase)
        self.button2.clicked.connect(self.insertarNuevoUsuario)
        self.button3.clicked.connect(self.registrandoNuevoUsuario)
        self.button4.clicked.connect(self.cargarVentanaInicial)
        self.button5.clicked.connect(self.interfazBaseDatos)
        self.button6.clicked.connect(self.listarUsuarios)
        self.button7.clicked.connect(self.cargarVentanaInicial)
        self.button9.clicked.connect(self.cargarVentanaInicial)

        #self.cursor.execute("SELECT * from usuario")
        #renglon = self.cursor.fetchall()
        #print(renglon)

    def insertarNuevoUsuario(self):

        self.label1.setText("Direccion")
        self.label2.setText("Municipio")
        self.label1.move(65, 120)
        self.label2.move(65, 160)
        self.label3.setText("Registro de Nuevo Usuario")
        self.label3.move(210, 30)
        self.label4.setText("Nombre de usuario")
        self.label4.move(65, 80)
        self.label5.setVisible(True)
        self.label5.setText("Estado")
        self.label5.move(65, 200)
        self.label6.setVisible(True)
        self.label6.setText("Email")
        self.label7.setVisible(True)
        self.label6.move(65, 240)
        self.label7.setText("Password")
        self.label7.move(65, 280)
        self.label8.hide()
        self.resize(550, 430)
        self.move(350, 150)
        self.lineEdit3.setVisible(True)
        self.lineEdit4.setVisible(True)
        self.lineEdit5.setVisible(True)
        self.lineEdit6.setVisible(True)
        self.lineEdit1.setGeometry(180, 80, 250, 20)
        self.lineEdit8.setGeometry(180, 280, 250, 20)
        self.lineEdit3.setGeometry(180, 120, 250, 20)
        self.lineEdit4.setGeometry(180, 160, 250, 20)
        self.lineEdit5.setGeometry(180, 200, 250, 20)
        self.lineEdit6.setGeometry(180, 240, 250, 20)
        self.button1.hide()
        self.button2.hide()
        self.button5.hide()
        self.lineEdit2.hide()
        self.button3.setVisible(True)
        self.button4.setVisible(True)
        self.button4.move(310, 340)
        self.button3.move(210, 340)
        self.lineEdit1.setText("")
        self.lineEdit8.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")
        if (self.label4.isEnabled() == True):
            self.label4.setVisible(True)
        if (self.lineEdit8.isEnabled() == True):
            self.lineEdit8.setVisible(True)

    def cargarVentanaInicial(self):

        self.resize(450, 350)
        self.label1.setText("Username")
        self.label2.setText("Password")
        self.label3.setText("Bienvenido al Sistema de Biblioteca")
        self.label4.setText("Nuevo usuario ------>")
        self.label5.setText("Bienvenido al Sistema de Biblioteca kdkdkdkd")
        self.label6.setText("Bienvenido al Sistema de Biblioteca jjdjdjd")
        self.label7.setText("Usernamenndjhdjdjdjdjdjddhdhdh hdhdhdhdhdhdjhd")
        self.button1.setText("Aceptar")
        self.button2.setText("Registrar")
        self.button3.setText("Registrar")
        self.button4.setText("Cancelar")
        self.label1.move(80, 100)
        self.label2.move(80, 130)
        self.label3.move(135, 20)
        self.label4.move(150, 215)
        self.button1.move(300, 99)
        self.lineEdit1.move(150, 100)
        self.lineEdit2.move(150, 130)
        self.button2.move(300, 210)
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()
        self.lineEdit3.hide()
        self.lineEdit4.hide()
        self.lineEdit5.hide()
        self.lineEdit6.hide()
        self.lineEdit8.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.hide()
        self.button7.hide()
        self.button1.setVisible(True)
        self.button2.setVisible(True)
        self.lineEdit1.setGeometry(140, 100, 145, 20)
        self.lineEdit2.setGeometry(140, 130, 145, 20)
        self.lineEdit1.setText("")
        self.lineEdit2.setText("")
        self.lineEdit3.setText("")
        self.lineEdit4.setText("")
        self.lineEdit5.setText("")
        self.lineEdit6.setText("")

        ##Ocultar Interfaz De DB
        self.button6.hide()
        self.button8.hide()
        self.button9.hide()
        self.button10.hide()
        self.button11.hide()
        self.button12.hide()
        self.button13.hide()
        self.button14.hide()
        self.button15.hide()
        self.button16.hide()
        self.label9.hide()
        self.label10.hide()
        self.label11.hide()
        self.label12.hide()
        self.label13.hide()
        self.textEdit1.hide()
        self.textEdit2.hide()
        self.lineEdit9.hide()
        self.nombreDelUsuario = ""


        if(self.lineEdit1.isEnabled() == True):
            self.lineEdit1.setVisible(True)
        if (self.lineEdit2.isEnabled() == True):
            self.lineEdit2.setVisible(True)
        if(self.label1.isEnabled() == True):
            self.label1.setVisible(True)
        if (self.label2.isEnabled() == True):
            self.label2.setVisible(True)
        if (self.label3.isEnabled() == True):
            self.label3.setVisible(True)
        if (self.label4.isEnabled() == True):
            self.label4.setVisible(True)



    def iniciarBase(self):

        nombre = "'"+str(self.lineEdit1.text()+"'")
        contra = "'"+str(self.lineEdit2.text()+"'")
        self.cursor.execute("SELECT * from usuario where username =%s" %(nombre))
        datos = self.cursor.fetchone()

        if(datos != None):

            if(str(self.lineEdit1.text()) == 'Victor Omar Jimenez Barajas' and str(self.lineEdit2.text()) == 'universidad'):
                self.idUsuario = int(datos[0])
                self.nombreDelUsuario += "Administrador"
                self.resize(250, 100)
                self.move(500, 250)
                self.label2.hide()
                self.label3.hide()
                self.label1.hide()
                self.label5.hide()
                self.label6.hide()
                self.label7.hide()
                self.button1.hide()
                self.button3.hide()
                self.button2.hide()
                self.button4.hide()
                self.lineEdit1.hide()
                self.lineEdit2.hide()
                self.lineEdit3.hide()
                self.lineEdit4.hide()
                self.lineEdit5.hide()
                self.lineEdit6.hide()
                self.lineEdit8.hide()
                self.label4.move(90, 15)
                self.label4.setText("Login Correcto")
                self.button5.setVisible(True)
                self.button5.move(86, 50)


            elif(datos[1] == str(self.lineEdit1.text()) and datos[6] == str(self.lineEdit2.text())):
                self.idUsuario = int(datos[0])
                self.nombreDelUsuario += str(datos[1])
                self.resize(250, 100)
                self.move(500, 250)
                self.label2.hide()
                self.label3.hide()
                self.label1.hide()
                self.label5.hide()
                self.label6.hide()
                self.label7.hide()
                self.button1.hide()
                self.button3.hide()
                self.button2.hide()
                self.button4.hide()
                self.lineEdit1.hide()
                self.lineEdit2.hide()
                self.lineEdit3.hide()
                self.lineEdit4.hide()
                self.lineEdit5.hide()
                self.lineEdit6.hide()
                self.lineEdit8.hide()
                self.label4.move(90, 15)
                self.label4.setText("Login Correcto")
                self.button5.setVisible(True)
                self.button5.move(86, 50)

            else:
                if (self.label8.isEnabled() == True):
                    self.label8.setVisible(True)
                self.label8.setGeometry(125, 60, 200, 200)
                self.label8.setPixmap(self.pixmapa1)

        else:
            if (self.label8.isEnabled() == True):
                self.label8.setVisible(True)
            self.label8.setGeometry(125,60,200,200)
            self.label8.setPixmap(self.pixmapa1)


    def interfazBaseDatos(self):
        if(self.nombreDelUsuario == 'Administrador'):
            self.resize(850, 650)
            self.move(200, 10)
            self.label4.hide()
            self.button5.hide()
            self.button6.setVisible(True)
            self.textEdit1.setVisible(True)
            self.textEdit1.setGeometry(40, 90, 560, 200)
            self.textEdit2.setVisible(True)
            self.textEdit2.setGeometry(40, 350, 560, 200)
            self.label9.setVisible(True)
            self.label9.setText("Usuarios Registrados")
            self.label10.setVisible(True)
            self.label10.setText("Libros registrados en la Biblioteca")
            self.label9.setGeometry(45, 60, 200, 20)
            self.label10.setGeometry(45, 320, 200, 20)
            self.button9.setVisible(True)
            self.button9.setGeometry(400, 20, 80, 20)


            if (self.label3.isEnabled() == True):
                self.label3.setVisible(True)
            mensaje1 = "Bienvenido " + self.nombreDelUsuario
            self.label3.setText(mensaje1)
            self.label3.setGeometry(250, 20, 200, 20)

        else:
            self.resize(850, 650)
            self.move(200, 10)
            self.label4.hide()

            self.button5.hide()
            self.button6.hide()
            self.button8.setVisible(True)
            self.button9.setVisible(True)
            self.button10.setVisible(True)
            self.button8.setGeometry(630, 100,80,25)
            self.button9.setGeometry(400, 20, 80, 20)
            self.button10.setGeometry(630, 360, 80, 25)
            self.lineEdit9.setGeometry(630, 400, 160, 20)
            self.lineEdit9.setVisible(True)
            self.textEdit1.setVisible(True)
            self.textEdit1.setGeometry(40, 90, 560, 200)
            self.textEdit2.setVisible(True)
            self.textEdit2.setGeometry(40, 350, 560, 200)


            if (self.label3.isEnabled() == True):
                self.label3.setVisible(True)

            mensaje1 = "Bienvenido " + self.nombreDelUsuario
            self.label3.setText(mensaje1)
            self.label3.setGeometry(250, 20, 200, 20)
            self.label9.setVisible(True)
            self.label10.setVisible(True)
            self.label9.setGeometry(45, 60, 200, 20)
            self.label10.setGeometry(45, 320, 200, 20)


    def registrandoNuevoUsuario(self):

        if(self.lineEdit1.text() != "" and self.lineEdit8.text() != "" and self.lineEdit3.text() != "" and self.lineEdit4.text() != "" and self.lineEdit5.text() != "" and self.lineEdit6.text() != "" ):
            nombreUsuario = str(self.lineEdit1.text())
            contrasenaUsuario = str(self.lineEdit8.text())
            direccionUsuario = str(self.lineEdit3.text())
            estadoUsuario = str(self.lineEdit5.text())
            correoUsuario= str(self.lineEdit6.text())
            municipioUsuario = str(self.lineEdit4.text())
            self.cursor.execute("""INSERT INTO usuario (username, direccion, municipio, estado, email, contrasena) VALUES('%s','%s','%s','%s','%s','%s')""" % (nombreUsuario,direccionUsuario, municipioUsuario, estadoUsuario, correoUsuario,contrasenaUsuario))
            self.conn.commit()
            self.registroCorrecto()
            #self.cargarVentanaInicial()

    def listarUsuarios(self):

        self.textEdit1.clear()
        self.cursor.close()
        self.conn.close()
        self.conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="library")
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * from usuario")
        renglon = self.cursor.fetchall()
        i = 0
        j =0
        data = ""

        while(i<len(renglon)):
            j = 0
            while(j<7):
                self.textEdit1.insertPlainText(str(renglon[i][j]))
                self.textEdit1.insertPlainText(" || ")
                j = j+1
            i = i+1
            self.textEdit1.insertPlainText("\n")

    def registroCorrecto(self):

        self.label1.hide()
        self.label2.hide()
        self.label4.hide()
        self.label5.hide()
        self.label6.hide()
        self.label7.hide()
        self.lineEdit1.hide()
        self.lineEdit2.hide()
        self.lineEdit3.hide()
        self.lineEdit4.hide()
        self.lineEdit5.hide()
        self.lineEdit6.hide()
        self.lineEdit7.hide()
        self.lineEdit8.hide()
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()
        self.button5.hide()
        self.button6.hide()
        self.button7.setVisible(True)
        self.resize(250, 100)
        self.move(500, 250)
        self.label3.move(90, 15)
        self.label3.setText("Registro Correcto")
        self.button7.setVisible(True)
        self.button7.move(86, 50)


app = QtGui.QApplication(sys.argv)

ventana = Ventana()
ventana.show()
sys.exit(app.exec_())
ventana.cursor.close()
ventana.conn.close()