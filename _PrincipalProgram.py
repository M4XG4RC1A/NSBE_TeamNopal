from tkinter import *
import win32com.client as wincl
from time import time, sleep
speak = wincl.Dispatch("SAPI.SpVoice")

def changeSlideShoe(ValSlide):
	ShoesVal.set(ValSlide);
	Control.set(0)
	pass
def changeSlidePants(ValSlide):
	PantsVal.set(ValSlide);
	Control.set(0)
	pass
def changeSlideShirt(ValSlide):
	ShirtVal.set(ValSlide);
	Control.set(0)
	pass
def changeSlideHead(ValSlide):
	HeadVal.set(ValSlide);
	Control.set(0)
	pass
def EmotionsLoop():
	audifonos = Head.get()
	camisa = Shirt.get()
	pantalon = Pants.get()
	zapatos = Shoes.get()
	if Control.get() == 0 and Control2.get() >= 3000:
		if audifonos == 1 and camisa == 1 and pantalon == 1 and  zapatos == 1:
		    Emotions.config(image = Ropa[0]);Emotions2.config(image = Ropa[0])
		    print("Ready to go");speak.Speak("Ready to go")
		elif audifonos == 1 and camisa == 1 and pantalon == 1 and  zapatos == 0:
		    Emotions.config(image = Ropa[1]);Emotions2.config(image = Ropa[1])
		    print("uh should i put my shoes on or i'm gonna get sick");speak.Speak("uh should i put my shoes on or i'm gonna get sick")
		elif audifonos == 1 and camisa == 1 and pantalon == 0 and  zapatos == 1:
		    Emotions.config(image = Ropa[2]);Emotions2.config(image = Ropa[2])
		    print("ufff it's cold");speak.Speak("ufff it's cold")
		elif audifonos == 1 and camisa == 0 and pantalon == 1 and  zapatos == 1:
		    Emotions.config(image = Ropa[2]);Emotions2.config(image = Ropa[2])
		    print("ufff it's cold");speak.Speak("ufff it's cold")
		elif audifonos == 1 and camisa == 1 and pantalon == 0 and  zapatos == 0:
		    Emotions.config(image = Ropa[3]);Emotions2.config(image = Ropa[3])
		    print("I really should put my pants up ");speak.Speak("I really should put my pants up ")
		elif audifonos == 1 and camisa == 0 and pantalon == 1 and  zapatos == 0:
		    Emotions.config(image = Ropa[5]);Emotions2.config(image = Ropa[5])
		    print("Getting ready");speak.Speak("Getting ready")
		elif audifonos == 1 and camisa == 0 and pantalon == 0 and  zapatos == 1:
		    Emotions.config(image = Ropa[1]);Emotions2.config(image = Ropa[1])
		    print("This doesnt seem right");speak.Speak("This doesnt seem right")
		elif audifonos == 1 and camisa == 0 and pantalon == 0 and  zapatos == 0:
		    Emotions.config(image = Ropa[4]);Emotions2.config(image = Ropa[4])
		    print("Im ready to hear music");speak.Speak("Im ready to hear music")
		elif audifonos == 0 and camisa == 1 and pantalon == 0 and  zapatos == 0:
		    Emotions.config(image = Ropa[5]);Emotions2.config(image = Ropa[5])
		    print("Getting ready");speak.Speak("Getting ready")
		elif audifonos == 0 and camisa == 1 and pantalon == 1 and  zapatos == 0:
		    Emotions.config(image = Ropa[5]);Emotions2.config(image = Ropa[5])
		    print("Some shoes and i'll be ready to go ");speak.Speak("Some shoes and i'll be ready to go ")
		elif audifonos == 0 and camisa == 1 and pantalon == 1 and  zapatos == 1:
		    Emotions.config(image = Ropa[6]);Emotions2.config(image = Ropa[6])
		    print("Now im ready for school ");speak.Speak("Now im ready for school ")
		elif audifonos == 0 and camisa == 1 and pantalon == 0 and  zapatos == 1:
		    Emotions.config(image = Ropa[9]);Emotions2.config(image = Ropa[9])
		    print("Im pretty sure I should put my pants first");speak.Speak("Im pretty sure I should put my pants first")
		elif audifonos == 0 and camisa == 0 and pantalon == 1 and  zapatos == 0:
		    Emotions.config(image = Ropa[3]);Emotions2.config(image = Ropa[3])
		    print("Now I can put my shoes on");speak.Speak("Now I can put my shoes on")
		elif audifonos == 0 and camisa == 0 and pantalon == 1 and  zapatos == 1:
		    Emotions.config(image = Ropa[5]);Emotions2.config(image = Ropa[5])
		    print("Now i just gotta work on the upper part of my body ");speak.Speak("Now i just gotta work on the upper part of my body ")
		elif audifonos == 0 and camisa == 0 and pantalon == 0 and  zapatos == 1:
		    Emotions.config(image = Ropa[7]);Emotions2.config(image = Ropa[7])
		    print("Oops i forgot something ");speak.Speak("Oops i forgot something ")
		else:
			print("Default")
			Emotions.config(image = Ropa[8]);Emotions2.config(image = Ropa[8])
		Control.set(1)
	elif Control2.get() <= 3000:
		C = Control2.get()
		Control2.set(C+200)
	raiz.after(200,EmotionsLoop)
	pass
def TakeAGift(regalo):
	if regalo == "calcetin":
	    print("*emoticon asco*")
	    Emotions.config(image = Regalos[0]);Emotions2.config(image = Regalos[0])
	elif  regalo == "galleta":
	    print("*emoticon hambriado*")
	    Emotions.config(image = Regalos[1]);Emotions2.config(image = Regalos[1])
	elif  regalo == "carbon":
	    print("*emoticon enojado*")
	    Emotions.config(image = Regalos[2]);Emotions2.config(image = Regalos[2])
	elif  regalo == "araña":
	    print("*emoticon asustado*")
	    Emotions.config(image = Regalos[3]);Emotions2.config(image = Regalos[3])
	elif  regalo == "carrito":
	    print("*emoticon sorpendido con estrellas en los ojos*")
	    Emotions.config(image = Regalos[4]);Emotions2.config(image = Regalos[4])
	elif  regalo == "balon":
	    print("*emoticon Feliz*")
	    Emotions.config(image = Regalos[5]);Emotions2.config(image = Regalos[5])
	else:
	    print("Escriba un regalo de los de arriba justo como se indica")
	    Emotions.config(image = Regalos[0]);Emotions2.config(image = Regalos[0])
	Control.set(0)
	Control2.set(0)
	pass
root=Tk()
root.title("Team Nopal")
root.iconbitmap('Logo.ico')

#Images
#Back
Back = PhotoImage(file="Background.png")
NoImg = PhotoImage(file="None.png")

#Ropa
R1 = PhotoImage(file="R1.png")
R2 = PhotoImage(file="R2.png")
R3 = PhotoImage(file="R3.png")
R4 = PhotoImage(file="R4.png")
R5 = PhotoImage(file="R5.png")
R6 = PhotoImage(file="R6.png")
R7 = PhotoImage(file="R7.png")
R8 = PhotoImage(file="R8.png")
R9 = PhotoImage(file="R9.png")
R10 = PhotoImage(file="R10.png")
Ropa = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10]
#Regalos
Reg1 = PhotoImage(file="Reg1.png")
Reg2 = PhotoImage(file="Reg2.png")
Reg3 = PhotoImage(file="Reg3.png")
Reg4 = PhotoImage(file="Reg4.png")
Reg5 = PhotoImage(file="Reg5.png")
Reg6 = PhotoImage(file="Reg6.png")
Regalos = [Reg1,Reg2,Reg3,Reg4,Reg5,Reg6]
#ObjetosRegalos
Obj1 = PhotoImage(file="Obj1.png")
Obj2 = PhotoImage(file="Obj2.png")
Obj3 = PhotoImage(file="Obj3.png")
Obj4 = PhotoImage(file="Obj4.png")
Obj5 = PhotoImage(file="Obj5.png")
Obj6 = PhotoImage(file="Obj6.png")
#Clothes
Clothe1 = PhotoImage(file="Zapatos.png")
Clothe2 = PhotoImage(file="Pantalon.png")
Clothe3 = PhotoImage(file="Camisa.png")
Clothe4 = PhotoImage(file="Audifonos.png")

#Principal Frame
raiz = Frame(root,width=1536,height=864,bg="white")
Label(raiz, image=Back).place(relwidth=1,relheight=1)
raiz.pack()

#Numerical Variables
ShoesVal = IntVar();
ShoesVal.set(0);
PantsVal = IntVar();
PantsVal.set(0);
ShirtVal = IntVar();
ShirtVal.set(0);
HeadVal = IntVar();
HeadVal.set(0);
#Control
Control = IntVar();
Control.set(0);
Control2 = IntVar();
Control2.set(3000);

#Scales
Shoes = Scale(raiz, label="Shoes", from_=0, to=1,width=30,length=100,orient=HORIZONTAL, command=changeSlideShoe);
Shoes.set(0);
Shoes.place(x=614,y=102);
Pants = Scale(raiz, label="Pants", from_=0, to=1,width=30,length=100,orient=HORIZONTAL, command=changeSlidePants);
Pants.set(0);
Pants.place(x=864,y=102);
Shirt = Scale(raiz, label="Shirt", from_=0, to=1,width=30,length=100,orient=HORIZONTAL, command=changeSlideShirt);
Shirt.set(0);
Shirt.place(x=1114,y=102);
Head = Scale(raiz, label="Head", from_=0, to=1,width=30,length=100,orient=HORIZONTAL, command=changeSlideHead);
Head.set(0);
Head.place(x=1364,y=102);

#Images
ShoeLab = Label(raiz, image=Clothe1, width=100, height=100)
ShoeLab.place(x=501,y=90)
PantsLab = Label(raiz, image=Clothe2, width=100, height=100)
PantsLab.place(x=751,y=90)
ShirtLab = Label(raiz, image=Clothe3, width=100, height=100)
ShirtLab.place(x=1001,y=90)
HeadLab = Label(raiz, image=Clothe4, width=100, height=100)
HeadLab.place(x=1251,y=90)

#Gifts
Cookie = Button(raiz, image=Obj1,width=100, height=100, bg="white", command=lambda:TakeAGift("galleta"))
Cookie.place(x=501,y=326)
Spider = Button(raiz, image=Obj2,width=100, height=100, bg="white", command=lambda:TakeAGift("araña"))
Spider.place(x=701,y=326)
Car = Button(raiz, image=Obj3,width=100, height=100, bg="white", command=lambda:TakeAGift("carrito"))
Car.place(x=901,y=326)
Coal = Button(raiz, image=Obj4,width=100, height=100, bg="white", command=lambda:TakeAGift("carbon"))
Coal.place(x=601,y=475)
Socks = Button(raiz, image=Obj5,width=100, height=100, bg="white", command=lambda:TakeAGift("calcetin"))
Socks.place(x=801,y=475)
Ball = Button(raiz, image=Obj6,width=100, height=100, bg="white", command=lambda:TakeAGift("balon"))
Ball.place(x=701,y=624)

#Face
Emotions = Label(raiz, image=NoImg, width=89, height=65)
Emotions.place(x=170,y=100)
Emotions2 = Label(raiz, image=NoImg, width=89, height=65)
Emotions2.place(x=1257,y=480)

#Loop
EmotionsLoop()

#End
raiz.mainloop()