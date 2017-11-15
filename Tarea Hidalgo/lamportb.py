#Lamport's bakery problem NF
from threading import Condition,Lock,Thread
import time, random
class Panaderia(): #reccurso
	def __init__(self):
		self.ocupado=False
		self.count=0

	#setters
	def set_vendiendo(self):
		self.ocupado= True
	def set_libre(self):
		self.ocupado = False
	def set_count(self):
		self.count+=1
	
	#@gets
	def get_ocupado(self):
		return self.ocupado
	def get_count(self):
		return self.count	



class Cliente(Thread):#proceso

	def __init__(self, numId):
		Thread.__init__(self)
		self.cv=Condition() #se crean "los thread" condicionales
		self.numId =numId
	def pagar(self): # esto es la Zona Critica	
		panaderia.set_count() #el contador aumenta
		panaderia.set_vendiendo() # el panadero esta ocupado, nadie puede pagar hasta q termine con el cliente actual
		print("Es el turno del thread ", self.numId," (In ZC) ")
		print("El cliente ",self.numId ," pago: ", random.randrange(500,50000,1))
		panaderia.set_libre() #el panadero termino de vender, otro cliente puede comprar
		self.cv.release() #El thread salio
		print("Salio el thread " , self.numId ," de la panaderia  (Out ZC)")

	def run(self):#entrar a la panaderia y sacar turno
		self.cv.acquire() # el cliente entro a la panaderia
		time.sleep(random.randrange(1,6,1)) #tiempo en que se demora en elegir las cosas q va a comprar
		t.append((int(self.numId))) #se agrega a una cola
		ticket=t.index(self.numId) # se obtiene el numero del ticket
		print("El cliente ",self.numId, " obtuvo el ticket ", ticket)
		while ticket!=panaderia.get_count(): #espera a que sea su turno
			pass	
		if (panaderia.get_ocupado()==False):#revisa si el panadero esta libre
			Cliente.pagar(self) #entra a pagar
		else:
			while(panaderia.get_ocupado()==True):#espera hasta q el panadero este libre
				pass
			Cliente.pagar(self) #entra a pagar

##int main()
t=[]
print("Ingrese el numero de threads")
n=int(input())
panaderia=Panaderia()
	
for i in range(0,n):
	thread=Cliente(i+1)
	print("El cliente "+str(i+1)+" entro a la panaderia")
	thread.start()
print(panaderia.get_count())

