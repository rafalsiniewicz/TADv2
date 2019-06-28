from data import *
import matplotlib.pyplot as plt
from tkinter import *

def operation():
	labeltext=[]
	for i in range(0,int(txt.get())):
		labeltext.append(StringVar())
	T=[]
	print("podaj liczbe miesiecy symulacji\n")
	#miesiace = int(input())
	miesiace=int(txt.get())
	#regola =  int(input("podaj regole :2,3,4,5,6,7,10,12\n"))
	regola =int(txt2.get())
	#systems.setf(regola);
	systems = allSystems(1, 1, regola, 2)
	offset = systems.readData("datainput2.txt")
	miesiace += offset
	j=0
	print(len(T))
	print(miesiace-offset)
	for i in range(offset + 1, miesiace + 1):
		#print(j)
		
		labeltext[j].set("#############" + str(i) + "###############\n")
		print("#############" + str(i) + "###############\n")
		systems.computeToFill(i)
		systems.update(i)

		j+=1
		#systems.print_()
	temp=0
	for i in range(0,int(txt.get())):
		T.append(Label(window, height=2, width=30,textvariable=labeltext[i]))
		T[i].grid(column=10, row=10+i)
		temp=i

	YvalSys1 = systems.getSysYval(0)
	TimesSys1 = systems.getSysTimes(0)
	functSys1 = systems.getSysFunctions(0)

	YvalSys2 = systems.getSysYval(1)
	TimesSys2 = systems.getSysTimes(1)
	functSys2 = systems.getSysFunctions(1)

	YvalSys3 = systems.getSysYval(2)
	TimesSys3 = systems.getSysTimes(2)
	functSys3 = systems.getSysFunctions(2)

	#labeltext1.set(functSys3)
	temp+=1
	T.append(Label(window, height=2, width=30,text=functSys3))
	T[temp].grid(column=10, row=10+temp)
	T.append(Label(window, height=2, width=30,text=functSys1))
	T[temp+1].grid(column=10, row=10+temp+1)
	T.append(Label(window, height=2, width=30,text=functSys2))
	T[temp+2].grid(column=10, row=10+temp+2)
	print(functSys3)
	print(functSys1)
	print(functSys2)
	plt.figure(1)
	plt.plot(TimesSys1,YvalSys1)
	plt.plot(TimesSys2,YvalSys2)
	plt.plot(TimesSys3,YvalSys3)
	plt.show()

	#systems.save(fileout);
	#fileout.close();
	#file.close();

window = Tk()
 
window.title("GUI")
window.geometry('600x400')

label = Label( window, text = "Podaj liczbe miesiecy symulacji" )
label.grid(column=10, row=0)
txt = Entry(window,width=10)
txt.grid(column=10, row=1)
txt.focus()
txt.insert(0,"0")

label2 = Label( window, text = "Podaj regole :2,3,4,5,6,7,10,12" )
label2.grid(column=10, row=2)
txt2 = Entry(window,width=10)
txt2.grid(column=10, row=3)
txt2.insert(0,"0")

btn = Button(window, text="Enter", bg="white", fg="black",command=operation)
btn.grid(column=10, row=6)


window.mainloop()

