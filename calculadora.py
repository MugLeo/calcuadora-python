from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)

#raiz.wm_attributes('-alpha', 0.7)

miFrame.pack()

miFrame.config(bg="#D0D6CF")

operacion=0
resultado=0
paranm1=0
paranm2=0
borrarPantalla=0
realizar_operacion=0

#------- Pantalla -----------------#
numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla,font=('',25))
pantalla.grid(row=0,column=1,columnspan=5)
#propiedad del metodo grid para agrandar input text 
#ipady=20
pantalla.config(fg="#50FF29",background="black",justify="right")

#------------pulsando teclado-----------------------#
def numeroPulsado(num):
	"""funcion encargada mostrar los numeros pulsados en la pantalla"""
	global borrarPantalla
	global realizar_operacion

	#No ha pulsado numeros o ya introdujo una operacion a realizar
	if numeroPantalla.get()=="" or borrarPantalla!=0:

		numeroPantalla.set(num)
		
		borrarPantalla=0

		realizar_operacion=1

	else:
		#contatena valores para la operacion
		numeroPantalla.set(numeroPantalla.get() + num)

		realizar_operacion=1

#------------suma-----------------------#
def suma(num):
	"""Realiza la operacion suma
	
	Argumentos:
 	num -- valor en pantalla
 
 	Test:
	>>> resultado=1
	>>> operacion=1
	>>> realizar_operacion=1
	>>> paranm1=0
	>>> paranm2=0
	>>> borrarPantalla=1
	>>> suma(2)
	4

	"""
	global operacion
	global resultado
	global realizar_operacion
	global borrarPantalla
	global paranm1
	global paranm2


	#si viene de otra operacion y no ha realizado operaciones
	if operacion!=0 and operacion!=1 and realizar_operacion!=0:
		#si ya ha realizado operaciones
		if resultado!=0:
			paranm1=resultado
		paranm2=num
		resultado=el_resultado()
		operacion=1
		return resultado
		#si ya seleciono esta operacion y no ha realizado operaciones
	if operacion!=0 and realizar_operacion!=0:
		#operacion cuando acumula resultado por primera vez
		if resultado!=0:
			paranm1=resultado
		operacion=1			
		paranm2=num
		resultado=el_resultado()
		return resultado
	else:
		operacion=1
		paranm1 = num
		realizar_operacion=0


#------------resta-----------------------#
def resta(num):
	"""Realiza la operacion resta"""
	global operacion
	global resultado
	global borrarPantalla
	global realizar_operacion
	global paranm1
	global paranm2

	if num!="":

		borrarPantalla=1

		if operacion!=0 and operacion!=2 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			paranm2=num
			resultado=el_resultado()
			operacion=2
			return
		if operacion!=0 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			operacion=2
			paranm2=num
			resultado=el_resultado()
			return
		else:
			operacion=2
			paranm1 = num
			realizar_operacion=0

#------------multiplica-----------------------#
def multiplica(num):
	"""Realiza la operacion de multiplicar"""	

	global operacion
	global resultado
	global borrarPantalla
	global realizar_operacion
	global paranm1
	global paranm2

	if num!="":

		borrarPantalla=1

		if operacion!=0 and operacion!=3 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			paranm2=num
			resultado=el_resultado()
			operacion=3
			return
		if operacion!=0 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			operacion=3
			paranm2=num
			resultado=el_resultado()
			return
		else:
			operacion=3
			paranm1 = num
			realizar_operacion=0

#------------divide-----------------------#
def divide(num):
	"""Realiza la operacion de dividir"""
	
	global operacion
	global resultado
	global borrarPantalla
	global realizar_operacion
	global paranm1
	global paranm2

	if num!="":

		borrarPantalla=1

		if operacion!=0 and operacion!=4 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			paranm2=num
			resultado=el_resultado()
			operacion=4
			return
		if operacion!=0 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			operacion=4
			paranm2=num
			resultado=el_resultado()
			return
		else:
			operacion=4
			paranm1 = num
			realizar_operacion=0

#------------potencia-----------------------#
def btn_potencia(num):
	"""Realiza la operacion de calcular la potencia"""
	
	global operacion
	global resultado
	global borrarPantalla
	global realizar_operacion
	global paranm1
	global paranm2

	if num!="":

		borrarPantalla=1

		if operacion!=0 and operacion!=5 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			paranm2=num
			resultado=el_resultado()
			operacion=5
			return
		if operacion!=0 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			operacion=5
			paranm2=num
			resultado=el_resultado()
			return
		else:
			operacion=5
			paranm1 = num
			realizar_operacion=0

#------------divEntera-----------------------#
def btn_divEntera(num):
	"""Devuelve el el cociente de una divicion, solo los numero enteros"""
	
	global operacion
	global resultado
	global borrarPantalla
	global realizar_operacion
	global paranm1
	global paranm2
	if num!="":

		borrarPantalla=1

		if operacion!=0 and operacion!=6 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			paranm2=num
			resultado=el_resultado()
			operacion=6
			return
		if operacion!=0 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			operacion=6
			paranm2=num
			resultado=el_resultado()
			return
		else:
			operacion=6
			paranm1 = num
			realizar_operacion=0

#------------modulo-----------------------#
def btn_divModulo(num):
	"""Devuelve el resto de una divicion"""
	
	global operacion
	global resultado
	global borrarPantalla
	global realizar_operacion
	global paranm1
	global paranm2

	if num!="":

		borrarPantalla=1

		if operacion!=0 and operacion!=7 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			paranm2=num
			resultado=el_resultado()
			operacion=7
			return
		if operacion!=0 and realizar_operacion!=0:
			if resultado!=0:
				paranm1=resultado
			operacion=7
			paranm2=num
			resultado=el_resultado()
			return
		else:
			operacion=7
			paranm1 = num
			realizar_operacion=0

#------------resultado-----------------------#
def el_resultado():
	"""Calcula el resultado"""

	global operacion
	global realizar_operacion
	global paranm1
	global paranm2

	if operacion == 1:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)+int(paranm2)
			else:
				resultado=int(paranm1)+int(paranm2)
		except ValueError:
			resultado=float(paranm1)+float(paranm2)

	if operacion == 2:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)-int(paranm2)
			else:
				resultado=int(paranm1)-int(paranm2)
		except ValueError:
			resultado=float(paranm1)-float(paranm2)

	if operacion == 3:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)*int(paranm2)
			else:
				resultado=int(paranm1)*int(paranm2)
		except ValueError:
			resultado=float(paranm1)*float(paranm2)

	if operacion == 4:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)/int(paranm2)
			else:
				resultado=int(paranm1)/int(paranm2)
		except ZeroDivisionError:
			resultado="No puede dividir por 0"
			numeroPantalla.set("No puede dividir por 0")
			return
		except ValueError:
			resultado=float(paranm1)/float(paranm2)

	if operacion == 5:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)**int(paranm2)
			else:
				resultado=int(paranm1)**int(paranm2)
		except ValueError:
			resultado=float(paranm1)**float(paranm2)

	if operacion == 6:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)//int(paranm2)
			else:
				resultado=int(paranm1)//int(paranm2)
		except ValueError:
			resultado=float(paranm1)//float(paranm2)

	if operacion == 7:
		try:
			if type(paranm1)==float and type(paranm2)!=float:
				resultado=float(paranm1)%int(paranm2)
			else:
				resultado=int(paranm1)%int(paranm2)
		except ValueError:
			resultado=float(paranm1)%float(paranm2)

	#split a la cadena para validar si el primer valor despues del punto es 0 parseo a integer
	decimales=str(resultado).split(".")
	flag=False
	decimales.pop(0)

	for i in decimales:
		if int(i)!=0 and flag==False:
			flag=True

	if flag==False:
		resultado=int(float(resultado))

	numeroPantalla.set(resultado)
	paranm1=0
	paranm2=0
	realizar_operacion=0
	return resultado

#------------resultado-----------------------#
def btn_result(paranm_pantalla):
	"""Boton igual"""
	global operacion
	global paranm1
	global paranm2
	global resultado

	realizar_operacion=0

	if resultado!=0:
		paranm1=resultado
		paranm2=paranm_pantalla
	else:
		paranm2=paranm_pantalla
	try:
		resultado=el_resultado()
		operacion=0
	except UnboundLocalError:
		return
	

#------------clear-----------------------#
def btn_clear():
	"""Limpia la pantalla"""
	global paranm1
	global paranm2
	global operacion
	global resultado

	operacion=0
	paranm1=0
	paranm2=0
	resultado=0
	numeroPantalla.set("")


#-------------fila 1--------------------#
boton7=Button(miFrame,text="7", command=lambda:numeroPulsado("7"),font=('',30),activebackground="orange")
boton7.grid(row=1,column=1)
boton8=Button(miFrame,text="8", command=lambda:numeroPulsado("8"),font=('',30))
boton8.grid(row=1,column=2)
boton9=Button(miFrame,text="9", command=lambda:numeroPulsado("9"),font=('',30))
boton9.grid(row=1,column=3)
botonDiv=Button(miFrame,text="/",command=lambda:divide(numeroPantalla.get()),font=('',30))
botonDiv.grid(row=1,column=4)
botonClear=Button(miFrame,text="clear",command=lambda:btn_clear(),font=('',30))
botonClear.grid(row=1,column=5)

#-------------fila 2--------------------#
boton4=Button(miFrame,text="4", command=lambda:numeroPulsado("4"),font=('',30))
boton4.grid(row=2,column=1)
boton5=Button(miFrame,text="5",command=lambda:numeroPulsado("5"),font=('',30))
boton5.grid(row=2,column=2)
boton6=Button(miFrame,text="6", command=lambda:numeroPulsado("6"),font=('',30))
boton6.grid(row=2,column=3)
botonMult=Button(miFrame,text="*", command=lambda:multiplica(numeroPantalla.get()),font=('',30))
botonMult.grid(row=2,column=4)
botonPotencia=Button(miFrame,text="Potencia",command=lambda:btn_potencia(numeroPantalla.get()),font=('',30))
botonPotencia.grid(row=2,column=5)

#-------------fila 3--------------------#
boton1=Button(miFrame,text="1", command=lambda:numeroPulsado("1"),font=('',30))
boton1.grid(row=3,column=1)
boton2=Button(miFrame,text="2", command=lambda:numeroPulsado("2"),font=('',30))
boton2.grid(row=3,column=2)
boton3=Button(miFrame,text="3", command=lambda:numeroPulsado("3"),font=('',30))
boton3.grid(row=3,column=3)
botonResta=Button(miFrame,text="-", command=lambda:resta(numeroPantalla.get()),font=('',30))
botonResta.grid(row=3,column=4)
botonEntera=Button(miFrame,text="Div entera",command=lambda:btn_divEntera(numeroPantalla.get()),font=('',30))
botonEntera.grid(row=3,column=5)
#-------------fila 4--------------------#
boton0=Button(miFrame,text="0", command=lambda:numeroPulsado("0"),font=('',30))
boton0.grid(row=4,column=1)
botonComa=Button(miFrame,text=".", command=lambda:numeroPulsado("."),font=('',30))
botonComa.grid(row=4,column=2)
botonIgual=Button(miFrame,text="=",command=lambda:btn_result(numeroPantalla.get()),font=('',30))
botonIgual.grid(row=4,column=3)
botonSuma=Button(miFrame,text="+",command=lambda:suma(numeroPantalla.get()),font=('',30))
botonSuma.grid(row=4,column=4)
botonModulo=Button(miFrame,text="Div modulo",command=lambda:btn_divModulo(numeroPantalla.get()),font=('',30))
botonModulo.grid(row=4,column=5)

raiz.mainloop()

import doctest
doctest.testmod()

#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()