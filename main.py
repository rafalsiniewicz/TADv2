from data import *
import matplotlib.pyplot as plt
from tkinter import *


def operation():

    T = []
    ofx = 0
    ofy = 0
    # miesiace = int(input())
    miesiace = int(txt.get())
    # regola =  int(input("podaj regole :2,3,4,5,6,7,10,12\n"))
    regola = int(txt2.get())
    # systems.setf(regola);
    systems = allSystems(1, 1, regola, 2)
    offset = systems.readData(txt3.get(),txt4.get())
    miesiace += offset
    j = 0
    #print(len(T))
    #print(miesiace - offset)
    for i in range(offset + 1, miesiace + 1):
        # print(j)

       # labeltext[j].set("#############" + str(i) + "###############\n")
        #print("#############" + str(i) + "###############\n")
        systems.computeToFill(i)
        systems.update(i)

        j += 1
    # systems.print_()
    temp = 0
    YvalSys = []
    TimesSys = []
    functSys = []
    text = ""
    leg = []
    color = ['b','g','r','y','c','k','m']
    for i in range(systems.n):
        YvalSys.append(systems.getSysYval(i))
        TimesSys.append(systems.getSysTimes(i))
        functSys.append(systems.getSysFunctions(i))
        plt.plot(TimesSys[i],YvalSys[i],'ro', c = color[(i)%len(color)])
        leg.append("system: "+str(i+1))
        text = text + "system: " + str(i+1) + " " + str(functSys[i]) + "\n"
    max = plt.ylim()[1]
    plt.text(0,max, text)
    plt.legend(leg)
    plt.grid(True)
    # labeltext1.set(functSys3)
    temp = 0

    #print(text)
    plt.show()


# systems.save(fileout);
# fileout.close();
# file.close();

window = Tk()

window.title("GUI")
window.geometry('600x400')

label = Label(window, text="Miesiące symulacji")
label.grid(column=10, row=0)
txt = Entry(window, width = 10)
txt.grid(column=10, row=1)
txt.focus()
txt.insert(0, "500")

label2 = Label(window, text="Reguła: 2,3,4,5,6,7,10,12")
label2.grid(column=10, row=2)
txt2 = Entry(window, width=10)
txt2.grid(column=10, row=3)
txt2.insert(0, "2")

label3 = Label(window, text="Plik txt z danymi")
label3.grid(column=30, row=2)
txt3 = Entry(window)
txt3.grid(column=30, row=3)
txt3.insert(0, "datainput2.txt")

label4 = Label(window, text="Plik txt z okresami")
label4.grid(column=30, row=0)
txt4 = Entry(window)
txt4.grid(column=30, row=1)
txt4.insert(0, "timeinput2.txt")

btn = Button(window, text="Enter", bg="white", fg="black", command=operation)
btn.grid(column=10, row=6)
#do helpa czy czegos takiego
'''t = "reguły wyboru funkcjolanlości ze zbioru zaległych:\n " \
    "2 - najdłuższy łączny czas zalegania (zsumowane czasy krotnosci) jeśli są takie sameto wybieramy ten który ma największą krotność\n" \
    "3 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy łączny czas zalegania\n" \
    "4 - najdłuższy czas zalegania (wybieramy najdłuższy z krotności) jeśli są takie sameto wybieramy ten który ma największą krotność\n" \
    "5 - największą krotność jeśli są takie sameto wybieramy ten który ma najdłuższy czas zalegania\n" \
    "6 - najkrótszy łączny czas zalegania jeśli są takie same to wybieramy ten który ma największą krotność\n" \
    "7 - najdłuższy łączny czas zalegania jeśli są takie same to wybieramy losowo\n" \
    "10 - największą krotność jeśli są takie sameto wybieramy losowo\n" \
    "12 - wybór losowy\n"
'''
window.mainloop()