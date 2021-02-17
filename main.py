import math
E_CONST = 2.718
y = input()
z = input()
apperation1 = math.fabs(int(z)) - int(y) - 39
apperation2 = int(z)**4-int(y)-10
apperation3 = int(57)*int(z)**7-int(y)**8
apperation4 = math.sqrt(E_CONST**int(z)+int(y)-37)
apperation5 = apperation1/apperation2
functionmath = apperation5 - apperation3 - apperation4
print(functionmath)
