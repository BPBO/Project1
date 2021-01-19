'''--------------------------------------------------------------------
    Tittle: Interfaz grafica de la calculadora
    Developed by: Alex Montano Rojas
    Date: January of 2021
-----------------------------------------------------------------------
'''

import tkinter  # Libreria que maneja el entorno grafico en python
from tkinter import *
from tkinter import messagebox

from Arbol_de_Expresiones.ArbolDeExpre import ArbolExp


class main(Frame):
	
	"""Definicion de la clase frame para la 
	creacion del entorno visual"""

	def __init__(self,master=None):
		super().__init__(master, width=400, height=300, bg="#404040")
		self.master.resizable(0,0)
		self.master = master
		self.master.title("Calculator")
		self.pack()
		self.crearWidgets()

	def crearWidgets(self):

		"""Crea los elementos dentro del Frame"""
		
		#self.lbl1 = Label(self, text="f:", font=(25),
		#				 bg="#404040", fg="white")
		self.lbl2 = Label(self, text="R:", font=(25), bg="#404040",
						fg="white")
		self.entrada = StringVar()
		self.txt1 = Entry(self, textvariable=self.entrada, font=(35),
						bg="#404040", fg="white")
		self.txt1.config(bd=5)
		#self.txt1.config(highlightbackground="#000000")
		self.salida = StringVar()

		self.btn1 = Button(self, text="=",font=(25),
						command=self.calcular, bg="#9999FF")
		self.btn2 = Button(self, text="C",font=(20), command=self.limpiar,
						bg="#FF6666")

		self.btn01 = Button(self, text="1",font=(25), command=self.boton01)
		self.btn01.config(bg="#A0A0A0")
		self.btn02 = Button(self, text="2",font=(25), command=self.boton02)
		self.btn02.config(bg="#A0A0A0")
		self.btn03 = Button(self, text="3",font=(25), command=self.boton03)
		self.btn03.config(bg="#A0A0A0")
		self.btn04 = Button(self, text="4",font=(25), command=self.boton04)
		self.btn04.config(bg="#A0A0A0")
		self.btn05 = Button(self, text="5",font=(25), command=self.boton05)
		self.btn05.config(bg="#A0A0A0")
		self.btn06 = Button(self, text="6",font=(25), command=self.boton06)
		self.btn06.config(bg="#A0A0A0")
		self.btn07 = Button(self, text="7",font=(25), command=self.boton07)
		self.btn07.config(bg="#A0A0A0")
		self.btn08 = Button(self, text="8",font=(25), command=self.boton08)
		self.btn08.config(bg="#A0A0A0")
		self.btn09 = Button(self, text="9",font=(25), command=self.boton09)
		self.btn09.config(bg="#A0A0A0")

		self.btn00 = Button(self, text="0",font=(25), command=self.boton00)
		self.btn00.config(bg="#A0A0A0")
		self.btnS = Button(self, text="+",font=(25), command=self.botonS)
		self.btnS.config(bg="#FF9933")
		self.btnR = Button(self, text="-",font=(25), command=self.botonR)
		self.btnR.config(bg="#FF9933")
		self.btnM = Button(self, text="*",font=(25), command=self.botonM)
		self.btnM.config(bg="#FF9933")
		self.btnD = Button(self, text="/",font=(25), command=self.botonD)
		self.btnD.config(bg="#FF9933")

		self.btnPA = Button(self, text="(",font=(20), command=self.botonPA)
		self.btnPA.config(bg="#FF9933")
		self.btnPC = Button(self, text=")",font=(20), command=self.botonPC)
		self.btnPC.config(bg="#FF9933")

		#COORDENADAS
		self.txt1.place(x=5, y=5, height=70, width=390)
		#self.txt2.place(x=25, y=65, width=100)

		self.btn1.place(x=280, y=245, height=50, width=115)
		self.btn2.place(x=360, y=80, height=50, width=35)
		self.btnM.place(x=280, y=190, height=50, width=115)
		self.btnD.place(x=280, y=135, height=50, width=115)

		self.btn01.place(x=5, y=80, height=50, width=86)
		self.btn02.place(x=96, y=80, height=50, width=86)
		self.btn03.place(x=187, y=80, height=50, width=86)
		self.btn04.place(x=5, y=135, height=50, width=86)
		self.btn05.place(x=96, y=135, height=50, width=86)
		self.btn06.place(x=187, y=135, height=50, width=86)
		self.btn07.place(x=5, y=190, height=50, width=86)
		self.btn08.place(x=96, y=190, height=50, width=86)
		self.btn09.place(x=187, y=190, height=50, width=86)

		self.btn00.place(x=96, y=245, height=50, width=86)
		self.btnS.place(x=5, y=245, height=50, width=86)
		self.btnR.place(x=187, y=245, height=50, width=86)

		self.btnPA.place(x=280, y=80, height=50, width=35)
		self.btnPC.place(x=320, y=80, height=50, width=35)
		

	def calcular(self):
		"""Calcula el resultado de la expresion"""
		A = ArbolExp()
		cadena = self.entrada.get()
		A.generar(cadena)
		if A.raiz is not None:
			resp = A.calcular(A.raiz)
			self.salida.set(str(resp))
		else:
			self.salida.set("Error, expresion no valida!")
			#messagebox.showinfo("Error","expresion no valida!")
		self.entrada.set(self.salida.get())
		self.txt1.config(state=DISABLED)

	def limpiar(self):
		"""Vacia los cuadros de textos"""
		self.txt1.config(state=NORMAL)
		self.entrada.set("")
		self.salida.set("")

	def boton00(self):
		self.entrada.set(self.entrada.get() + "0")
	
	def boton01(self):
		self.entrada.set(self.entrada.get() + "1")
	
	def boton02(self):
		self.entrada.set(self.entrada.get() + "2")
	
	def boton03(self):
		self.entrada.set(self.entrada.get() + "3")
	
	def boton04(self):
		self.entrada.set(self.entrada.get() + "4")
	
	def boton05(self):
		self.entrada.set(self.entrada.get() + "5")
	
	def boton06(self):
		self.entrada.set(self.entrada.get() + "6")
	
	def boton07(self):
		self.entrada.set(self.entrada.get() + "7")
	
	def boton08(self):
		self.entrada.set(self.entrada.get() + "8")

	def boton09(self):
		self.entrada.set(self.entrada.get() + "9")
	
	def botonS(self):
		self.entrada.set(self.entrada.get() + "+")
	
	def botonR(self):
		self.entrada.set(self.entrada.get() + "-")
	
	def botonM(self):
		self.entrada.set(self.entrada.get() + "*")
	
	def botonD(self):
		self.entrada.set(self.entrada.get() + "/")

	def botonPA(self):
		self.entrada.set(self.entrada.get() + "(")

	def botonPC(self):
		self.entrada.set(self.entrada.get() + ")")
	
        


Lienzo = Tk() 	# instancia del objeto frame para la visualizacion de 
				#la ventana en python
ventana = main(Lienzo) # Creacion de la ventana segun parametizacion
Lienzo.mainloop()