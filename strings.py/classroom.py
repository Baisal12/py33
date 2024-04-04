'>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<'
# 1. cd
'>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<'
# 2.
#x = 10
#y = 20
#z = 30
#x, y, z = y, z, x
#print(x)
#print(y)
#print(z)
'>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<'
# 3.
#r = 2400
#m = 15
#k = 84
#print(r*m*k)
'>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<'
# 4.
#num = int(input('введите отрицательное число'))
#print(abs(num))
'>>>>>>>>>>>>>>><<<<<<<<<<<<<<<'
# 5.
#y = int(input('введите число'))
#a = y**5
#b = a%5
#print(b)
'>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<'
# 6.
#a = 12.24
#print(a**2)
#print(a**3)
#print(sqrt(a))
'>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<'
# 7.
#a=3
#b=4
#c=((3**2) + (4**2))
#print(c)
'>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<'
# 8.
#num1 = int(input())
#num2 = int(input())
#num3 = int(input())
#print(num1*num2%num3)






a = [set(), set(), set()] 
inp1 = input() 
inp2 = int(input()) 
if inp2 == 1: 
    a[inp2 - 1].update([inp1]) 
    a[inp2].update(['default value']) 
    a[inp2 + 1].update(['default value']) 
elif inp2 == 2: 
    a[inp2 - 1].update([inp1]) 
    a[inp2 - 2].update(['default value']) 
    a[inp2].update(['default value']) 
elif inp2 == 3: 
    a[inp2 - 1].update([inp1]) 
    a[inp2 - 3].update(['default value']) 
    a[inp2 - 2].update(['defaultvalue']) 
else: 
    a[0].update(['default value']) 
    a[1].update(['default value']) 
    a[2].update(['default value']) 
print(a)













a = [set(), set(), set()] 
inp1 = input() 
inp2 = int(input()) 

if inp2 == 1: 
    a[inp2 - 1].update([inp1]) 
    a[inp2].update(['default value']) 
    a[inp2 + 1].update(['default value']) 
elif inp2 == 2: 
    a[inp2 - 1].update([inp1]) 
    a[inp2 - 2].update(['default value']) 
    a[inp2].update(['default value']) 
elif inp2 == 3: 
    a[inp2 - 1].update([inp1]) 
    a[inp2 - 3].update(['default value']) 
    a[inp2 - 2].update(['default value']) 
else:
    print(a)