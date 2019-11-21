import math

start_x = 1307796.60
start_y = 420858.24      
final_x = 1307801.75
final_y = 420866.81

a = 121
print (a)
a = a - 90
print (a)
length = 10

#calculate new position using length
endx = length * math.cos(math.radians(a))
endy = length * math.sin(math.radians(a))
print (endx)
print (endy)
new_x = start_x + endx
new_y = start_y + endy
print ('final_x',' ' , final_x)
print (new_x)
print ('final_y',' ' , final_y)
print (new_y)

