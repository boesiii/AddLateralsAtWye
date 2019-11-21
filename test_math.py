import math

start_x = 1291764.86
start_y = 474261.69
final_x = 1291772.78
final_y = 474267.79

c = '01:00'
a = 142.42
print (a)
a = a - 90
print (a)
length = 10

#calculate new position using length
endx = length * math.cos(a)
endy = length * math.sin(a)
new_x = start_x + endx
new_y = start_y + endy
print ('final_x',' ' , final_x)
print (new_x)
print ('final_y',' ' , final_y)
print (new_y)

