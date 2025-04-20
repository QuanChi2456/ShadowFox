# Let us store the value of Principal Amount in 'P',  Time in 'T', Rate of Interest in 'R' and the Simple Interest in SI
P = int(input("Enter the Principal Amount : "))
T = int(input("Enter the Time : "))
R = int(input("Enter the Rate of Interest: "))
si = ((P*T*R)/100)
print("Simple Interest =",si)