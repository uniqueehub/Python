####math modules
##1.math.ceil()
import math
print(math.ceil(34.5)) ##35
print(math.ceil(-67.8)) ##-68
print(math.ceil(87.1)) ##88
print(math.ceil(81.0)) ##81
##2.math.copysign()
a=10
b=10
print(math.copysign(a,b))#10.0
print(math.copysign(5,-7))#-5.0
##3.math.fabs- return absolute value
print(math.fabs(13.2))#13.2
print(math.fabs(-14.6))#14.6
###4.math.factorial
print(math.factorial(5))#120
print(math.factorial(10))#3628800
###5.math floor
print(math.floor(-13.6))#-14
print(math.floor(13.6))#13
###6.math.gcd()
print(math.gcd(34,67))#1
print(math.gcd(60,48,44,52))#4
##7.math.frexp()
print(math.frexp(3))#(0.75, 2)
print(math.frexp(15.7))#(0.98125, 4)
print(math.frexp(-15))#(-0.9375, 4)
###8.math.fsum()
print(math.fsum(range(10)))#45.0
arr = [1, 4, 6]
print(math.fsum(arr))#11.0
arr = [2.5, 2.4, 3.09]
print(math.fsum(arr))#7.99
##9.isinf()-infinity or not
print(math.isinf(23646874979989e894898498))#true
##10.isnan()
print (math.isnan(math.pi))#false
print (math.isnan(math.e))#false
print (math.isnan(float('nan')))#true
##11.ldexp return x*(2**i))
print(math.ldexp(9, 3))#72.0
print(math.ldexp(-5, 2))#-20.0
print(math.exp(89))
print(math.pow(2,4))
print(math.sqrt(78))
print(math.tan(90))
print(math.cos(30))

