def getPower(n, m):
    # m = hangi kuvvetten us alinacagi. n = hangi sayiya kadar uslerin toplanacagi. 
    sum = 0
    for i in range(1, n+1):
        sum += i**m
        #print(sum)
    print("")
    return sum


def leastSquares(degree):   
    n = 10 #kacinci sayiya kadar gidilecegi.
    matrix = []
    for i in range(degree+1):
        line = []
        for j in range(i, i + degree+1):
            value = getPower(n, j)
            line.append(value)
        matrix.append(line)
    print("Matrix: ",matrix)
    return (matrix)

def getData():
    import csv
    data = []
    with open('Covid19.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print("Baslik: ", row[0])
                line_count += 1
            else:
                print(line_count, ": ", row[0])
                line_count += 1
                data.append(int(row[0]))
    print("Okuma tamamlandi.")
    return (data)

def getYSums(degree, data):
    yVector = []
    for j in range(0, degree + 1):
        sum = 0
        for i in range(1,11):
            sum += (data[i-1] * ((i) ** (j)))
            print("sUm: ",sum, data[i-1], "*", ((i)**j))
        yVector.append(sum)
        print("sum: ", sum)
    return(yVector)

def getPolynom():
    lst = []


def button1Onclick():


    import numpy as np
    import matplotlib.pyplot as plt

    degree = int(regDegree.get())
    matrix = leastSquares(degree) #X kisimlari
    allData = getData()
    data = getYSums(degree , allData)   #Y kismi



    s = np.linalg.solve(matrix, data)
    lst = list(s)
    lst.reverse()
    print(lst)


    X = np.linspace(1, 10, 10)
    F = np.poly1d(lst)
    #F= -1.112*X**2 + 106.4*X +235.7

    Y = []
    for i in range(1,11):
        Y.append(F(i))
    print(Y)
    plt.plot(X, Y)
    plt.show()



import tkinter

print("Hadi")
print("Basladi.")
pencere = tkinter.Tk()
pencere.geometry("200x200")

regText = tkinter.Label(text = "Regresyon Derecesi:")
regText.place(x=10,y=20)
regDegree = tkinter.Entry(width=10)
regDegree.place(x=120, y =20)
day1 = tkinter.Label(text = "İlk Gün:")
day1.place(x=10,y=40)
firstDay = tkinter.Entry(width=10)
firstDay.place(x=120, y =40)

day2 = tkinter.Label(text = "Son Gün:")
day2.place(x=10,y=60)
lastDay = tkinter.Entry(width=10)
lastDay.place(x=120, y =60)

button1 = tkinter.Button(text= "Başlat", command=button1Onclick)
button1.place(x=120,y =80)
pencere.mainloop()



#data[0], data[1], data[2]
#F = (1.21)*X**2+ (-4.98)*X + 5.19  #5
#F = (-3.84)*X**2+ (288.20)*X - 1699
#F = (8.941)*X**2+ (-86.26)*X + 164
#F = 6.784*X**2 -46.88*X+ 63.65 #10
#F = 0.032*X**3 +7.902*X**2 -77.32*X + 146.5 #n=20 degree = 3
#F= -3.842*X**2 + 288.2*X -1699