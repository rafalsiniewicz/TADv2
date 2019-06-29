from data import *
import matplotlib.pyplot as plt
from tkinter import *

def operation():
	labeltext=[]
	for i in range(0,int(txt.get())):
		labeltext.append(StringVar())
	T=[]
	print("t=",T)
	#print("podaj liczbe miesiecy symulacji\n")
	#miesiace = int(input())
	miesiace=int(txt.get())
	#regula =  int(input("podaj regule :2,3,4,5,6,7,10,12\n"))
	regula =int(listbox.get(listbox.curselection()))
	#print(listbox.get(listbox.curselection()))
	#systems.setf(regula);
	systems = allSystems(1, 1, regula, 2)
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
	
	functSys3=''.join(str(functSys3))
	funct3=StringVar()
	funct3.set(functSys3)
	functSys2=''.join(str(functSys2))
	funct2=StringVar()
	funct2.set(functSys2)
	functSys1=''.join(str(functSys1))
	funct1=StringVar()
	funct1.set(functSys1)
	T.append(Label(window, height=2, width=30,textvariable=funct3))
	T[temp].grid(column=10, row=10+temp)
	T.append(Label(window, height=2, width=30,textvariable=funct3))
	T[temp+1].grid(column=10, row=10+temp+1)
	T.append(Label(window, height=2, width=30,textvariable=funct2))
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
label.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=0, row=1)
txt.focus()
txt.insert(0,"0")

label2 = Label( window, text = "Wybierz regule :2,3,4,5,6,7,10,12" )
label2.grid(column=0, row=2)
scrollbar = Scrollbar(window)
scrollbar.grid(column=10, row=3)

listbox = Listbox(window, yscrollcommand=scrollbar.set, height=8,width=5)
for i in range(2,8):
	listbox.insert(END, str(i))
'''listbox.insert(END, "2 - najdłuższy łączny czas zalegania (zsumowane czasy krotnosci) jeśli są takie sameto wybieramy ten który ma największą krotność")
listbox.insert(END, "3 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy łączny czas zalegania")
listbox.insert(END, "4 - najdłuższy czas zalegania (wybieramy najdłuższy z krotności) jeśli są takie sameto wybieramy ten który ma największą krotność")
listbox.insert(END, "5 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy czas zalegania" )
listbox.insert(END, "6 - najkrótszy łączny czas zalegania jeśli są takie same to wybieramy ten który ma największą krotność")
listbox.insert(END, "7 - najdłuższy łączny czas zalegania jeśli są takie same to wybieramy losowo")
listbox.insert(END, "10 - największą krotność jeśli są takie sameto wybieramy losowo")
listbox.insert(END, "12 - wybór losowy")'''
listbox.insert(END, str(10))
listbox.insert(END, str(12))
label = Label(window, text = "-najdłuższy łączny czas zalegania (zsumowane czasy krotnosci) jeśli są takie sameto wybieramy ten który ma największą krotność")
label.place(x=100,y=60)
label = Label(window, text = "-największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy łączny czas zalegania" )
label.place(x=100,y=75)
label = Label(window, text = "-najdłuższy czas zalegania (wybieramy najdłuższy z krotności) jeśli są takie sameto wybieramy ten który ma największą krotność" )
label.place(x=100,y=92)
label = Label(window, text = "-największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy czas zalegania" )
label.place(x=100,y=107)
label = Label(window, text = "-najkrótszy łączny czas zalegania jeśli są takie same to wybieramy ten który ma największą krotność" )
label.place(x=100,y=124)
label = Label(window, text = "-najdłuższy łączny czas zalegania jeśli są takie same to wybieramy losowo" )
label.place(x=100,y=139)
label = Label(window, text = "-największą krotność jeśli są takie sameto wybieramy losowo" )
label.place(x=100,y=157)
label = Label(window, text = "-wybór losowy" )
label.place(x=100,y=173)
listbox.grid(column=0, row=3)

scrollbar.config(command=listbox.yview)
'''txt2 = Entry(window,width=10)
txt2.grid(column=10, row=3)
txt2.insert(0,"0")'''

btn = Button(window, text="Enter", bg="white", fg="black",command=operation)
btn.grid(column=0, row=6)


window.mainloop()

