a = int(input())
b = int(input())
c = int(input())
if a==b==c and a+b+c == 180 :
    print('Equilateral')
elif (a==b or b==c or a==c) and a+b+c == 180 : 
    print('Isosceles')
elif (a!=b!=c) and a+b+c == 180 :
    print('Scalene')
elif a+b+c != 180:
    print('Error')