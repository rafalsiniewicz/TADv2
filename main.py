from data import *
import matplotlib.pyplot as plt

print("podaj liczbe miesiecy symulacji\n")
miesiace = int(input())

regola =  int(input("podaj regole :2,3,4,5,6,7,10,12\n"))
#systems.setf(regola);
systems = allSystems(1, 1, regola, 2)
offset = systems.readData("datainput2.txt")
miesiace += offset
for i in range(offset + 1, miesiace + 1):
    print("#############" + str(i) + "###############\n")
    systems.computeToFill(i)
    systems.update(i)
    #systems.print_()

YvalSys1 = systems.getSysYval(0)
TimesSys1 = systems.getSysTimes(0)
functSys1 = systems.getSysFunctions(0)

YvalSys2 = systems.getSysYval(1)
TimesSys2 = systems.getSysTimes(1)
functSys2 = systems.getSysFunctions(1)

YvalSys3 = systems.getSysYval(2)
TimesSys3 = systems.getSysTimes(2)
functSys3 = systems.getSysFunctions(2)

print(functSys3)
print(functSys1)
print(functSys2)
plt.figure(1)
plt.plot(TimesSys1,YvalSys1)
plt.plot(TimesSys2,YvalSys2)
plt.plot(TimesSys3,YvalSys3)
plt.show()

plt.figure(1)
plt.plot(TimesSys1,functSys1)
plt.plot(TimesSys2,functSys2)
plt.plot(TimesSys3,functSys3)
plt.show()
#systems.save(fileout);
#fileout.close();
#file.close();
