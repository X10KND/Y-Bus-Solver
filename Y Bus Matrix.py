import math
import cmath
import pandas as pd

DECIMAL = 2
f = open("input.txt", "r")

m = int(f.readline()) #Number of buses
ybus = [[0 for x in range(m)] for x in range(m)]

n = int(f.readline()) #Rows of data
data = [[0 for x in range(6)] for x in range(n)]

#Input Data Table
for i in range(n):

    datapoint = f.readline().split(" ")

    data[i][0] = int(datapoint[0]) #From bus
    data[i][1] = int(datapoint[1]) #To bus

    data[i][2] = float(datapoint[2]) #R, pu
    data[i][3] = float(datapoint[3]) #X, pu

    data[i][4] = complex(0, float(datapoint[4])) #B, pu

    if  data[i][4].imag < 0.0:
        data[i][4] = 1 / data[i][4]

    if  data[i][3] > 0.0:
        data[i][5] = 1 / complex(data[i][2], data[i][3])
    if  data[i][3] < 0.0:
        data[i][5] = complex(data[i][2], data[i][3])

#Calculate non-diagonal
for i in range(n):
    ybus[data[i][0] - 1][data[i][1] - 1] = -1 * complex(data[i][5].real, data[i][5].imag)
    ybus[data[i][1] - 1][data[i][0] - 1] = -1 * complex(data[i][5].real, data[i][5].imag)

#Calculate diagonal
for bus in range(1, m + 1):
    for i in range(n):
        if bus == data[i][0] or bus == data[i][1]:
            ybus[bus - 1][bus - 1] += data[i][5] + data[i][4]
    ybus[bus - 1][bus - 1] = complex(ybus[bus - 1][bus - 1].real, ybus[bus - 1][bus - 1].imag)

YBUS = []
for row in ybus:
    arr = []
    for x in row:
        if type(x) == complex:
            arr.append(complex(round(x.real, DECIMAL), round(x.imag, DECIMAL)))
        else:
            arr.append(round(x, DECIMAL))

    YBUS.append(arr)

df = pd.DataFrame(YBUS)
print(df.to_string(index=False, header=False))