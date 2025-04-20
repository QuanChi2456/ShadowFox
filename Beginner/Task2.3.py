dist = 490
time_min = 7

#converting minute into seconds
time_sec = time_min*60

speed = dist/time_sec

#Using int() removes the decimal point 
print("Speed =",int(speed),"m/s")