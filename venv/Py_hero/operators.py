# NOTES Operators
# Operators: + - / * ** %
# Comparison: > < >= <= == !=
# Logical Operators = and or

# Operators are=
# Arithmetic operators
# Assignment operators
# Assignment_2 operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

print("Arithmetic operators")
"""
+    Addition          =x + y
-    Subtraction       =x - y
*    Multiplication    =x * y
/    Division          =x / y
%    Modulus           =x % y
**   Exponentiation   =x ** y
//   Floor division   =x // y
"""

print("Add ",10+5)

print("Sub ",10-2)

print("Multiply ",14*2)

print("Divide ",15/3)

print("Modulo", 45%6)

print("power ",5**2)

print(5>2)
print(5<2)
print("equal to ",10==5)
print("equal to ",10==10)

print("Not equal to ",5!=6)

print("and operator if both true ",1==1 and 5==5)
print("Or operator ", 6==6 or 6==7)

print(f" {y} Python Assignment Operators {y}")
"""
Operator  Example     Same As
=        x = 5        x = 5
+=       x += 3       x = x + 3
-=       x -= 3       x = x - 3
*=       x *= 3       x = x * 3
/=       x /= 3       x = x / 3
%=       x %= 3       x = x % 3
//=      x //= 3      x = x // 3
**=      x **= 3      x = x ** 3
&=       x &= 3       x = x & 3
|=       x |= 3       x = x | 3
^=       x ^= 3       x = x ^ 3
>>=      x >>= 3      x = x >> 3
<<=      x <<= 3      x = x << 3
"""
y="******"
print(f" {y} Comparison Operators {y}")
'''
Operator       Name                        Example    
==            Equal                        x == y    
!=            Not equal                    x != y    
>             Greater than                 x > y    
<             Less than                    x < y    
>=            Greater than or equal to     x >= y    
<=            Less than or equal to        x <= y
'''

print(f"{y} Logical Operators {y}")

" Logical operators are used to combine conditional statements:"

''' 
Operator 
and     Returns True if both statements are true
or      Returns True if one of the statements is true
not     Reverse the result, returns False if the result is true
'''


print(f"{y}\nIdentity operators are used to compare the objects, not if they are equal,\n but if they are actually the same object, with the same memory location:")
'''
Operator    Description                                                Example    
is        Returns True if both variables are the same object            x is y    
is not    Returns True if both variables are not the same object        x is not y
'''