# print numbers from 1 to 10
i= 1
while i <= 10:
     print (i)
     
     i+=1    

# 2. Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1


# 2. Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1


# 3. Print numbers from 1 to 20
i = 1
while i <= 20:
    print(i)
    i += 1


# 4. Print even numbers from 1 to 30
i = 1
while i <= 30:
    if i % 2 == 0:
        print(i)
    i += 1


# 5. Print odd numbers from 1 to 30
i = 1
while i <= 30:
    if i % 2 != 0:
        print(i)
    i += 1


# 6. Print numbers from 5 to 15
i = 5
while i <= 15:
    print(i)
    i += 1


# 7. Print numbers from 20 to 10 in reverse
i = 20
while i >= 10:
    print(i)
    i -= 1


# 8. Print multiples of 3 from 3 to 30
i = 3
while i <= 30:
    print(i)
    i += 3


# 9. Print multiples of 5 from 5 to 50
i = 5
while i <= 50:
    print(i)
    i += 5


# 10. Print numbers from 0 to 10
i = 0
while i <= 10:
    print(i)
    i += 1

# 11. Print numbers from -5 to 5
i = -5
while i <= 5:
    print(i)
    i += 1


# 12. Print numbers from 50 to 60
i = 50
while i <= 60:
    print(i)
    i += 1


# 13. Print every second number from 2 to 20
i = 2
while i <= 20:
    print(i)
    i += 2


# 14. Print every third number from 3 to 30
i = 3
while i <= 30:
    print(i)
    i += 3


# 15. Print numbers from 100 to 90
i = 100
while i >= 90:
    print(i)
    i -= 1


# 16. Print numbers from 1 to 50
i = 1
while i <= 50:
    print(i)
    i += 1


# 17. Print numbers from 25 to 1
i = 25
while i >= 1:
    print(i)
    i -= 1


# 18. Print the first 15 natural numbers
i = 1
while i <= 15:
    print(i)
    i += 1


# 19. Print the first 10 even numbers
i = 2
while i <= 20:
    print(i)
    i += 2


# 20. Print the first 10 odd numbers
i = 1
while i <= 19:
    print(i)
    i += 2



# 21. Sum from 1 to 10
i = 1
s = 0
while i <= 10:
    s = s + i
    i += 1
print(s)


# 22. Sum from 1 to 100
i = 1
s = 0
while i <= 100:
    s = s + i
    i += 1
print(s)


# 23. Sum of even numbers from 1 to 50
i = 2
s = 0
while i <= 50:
    s = s + i
    i += 2
print(s)


# 24. Sum of odd numbers from 1 to 50
i = 1
s = 0
while i <= 50:
    s = s + i
    i += 2
print(s)


# 25. Sum from 10 to 20
i = 10
s = 0
while i <= 20:
    s = s + i
    i += 1
print(s)


# 26. Table of 2
i = 1
while i <= 10:
    print(2, "x", i, "=", 2*i)
    i += 1


# 27. Table of 7
i = 1
while i <= 10:
    print(7, "x", i, "=", 7*i)
    i += 1


# 28. Table of a number
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1


# 29. Product from 1 to 5
i = 1
n = 1
while i <= 5:
    n = n * i
    i += 1
print(n)


# 30. Sum of multiples of 4
i = 4
s = 0
while i <= 40:
    s = s + i
    i += 4
print(s)

# 31. Sum from 1 to a given number
n = int(input("Enter number: "))
i = 1
s = 0

while i <= n:
    s = s + i
    i += 1

print(s)


# 32. Square of numbers from 1 to 10
i = 1
while i <= 10:
    print(i * i)
    i += 1


# 33. Cube of numbers from 1 to 10
i = 1
while i <= 10:
    print(i * i * i)
    i += 1


# 34. Sum of squares from 1 to 5
i = 1
s = 0

while i <= 5:
    s = s + i * i
    i += 1

print(s)


# 35. Count numbers from 1 to 100
i = 1
s = 0

while i <= 100:
    s += 1
    i += 1

print(s)


# 36. Difference from 20 to 10
i = 20
s = 0

while i >= 10:
    s = s + i
    i -= 1

print(s)


# 37. Average of numbers from 1 to 10
i = 1
s = 0

while i <= 10:
    s = s + i
    i += 1

print(s / 10)


# 38. Sum of numbers divisible by 3
i = 3
s = 0

while i <= 30:
    s = s + i
    i += 3

print(s)


# 39. Multiplication table in reverse
n = int(input("Enter number: "))
i = 10

while i >= 1:
    print(n, "x", i, "=", n * i)
    i -= 1


# 40. Factorial of a number
n = int(input("Enter number: "))
i = 1
s = 1

while i <= n:
    s = s * i
    i += 1

print(s)

# 41. Numbers divisible by 4
i = 1
while i <= 50:
    if i % 4 == 0:
        print(i)
    i += 1


# 42. Divisible by both 3 and 5
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1


# 43. Count even numbers
i = 1
s = 0
while i <= 100:
    if i % 2 == 0:
        s += 1
    i += 1
print(s)


# 44. Count odd numbers
i = 1
s = 0
while i <= 100:
    if i % 2 != 0:
        s += 1
    i += 1
print(s)


# 45. Check positive number
n = int(input("Enter number: "))
while n > 0:
    print("Positive")
    break
if n <= 0:
    print("Not positive")


# 46. Print 1 to 15
i = 1
while i <= 15:
    print(i)
    i += 1


# 47. Skip multiples of 4
i = 1
while i <= 30:
    if i % 4 != 0:
        print(i)
    i += 1


# 48. Numbers not divisible by 2
i = 1
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1


# 49. Count numbers divisible by 7
i = 1
s = 0
while i <= 100:
    if i % 7 == 0:
        s += 1
    i += 1
print(s)


# 50. Numbers between two limits
a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))
while a <= b:
    print(a)
    a += 1


# 51. Even or odd
n = int(input("Enter number: "))
while n % 2 == 0:
    print("Even")
    break
if n % 2 != 0:
    print("Odd")


# 52. Numbers ending in 5
i = 1
while i <= 100:
    if i % 10 == 5:
        print(i)
    i += 1


# 53. Largest of five numbers
i = 1
n = int(input("Enter number: "))
big = n
while i < 5:
    n = int(input("Enter number: "))
    if n > big:
        big = n
    i += 1
print(big)


# 54. Smallest of five numbers
i = 1
n = int(input("Enter number: "))
small = n
while i < 5:
    n = int(input("Enter number: "))
    if n < small:
        small = n
    i += 1
print(small)


# 55. Count numbers divisible by 6
i = 1
s = 0
while i <= 100:
    if i % 6 == 0:
        s += 1
    i += 1
print(s)


# 56. First 10 multiples
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1


# 57. Check divisibility by 5
n = int(input("Enter number: "))
while n % 5 == 0:
    print("Divisible by 5")
    break
if n % 5 != 0:
    print("Not divisible by 5")


# 58. Numbers whose squares are even
i = 1
while i <= 50:
    if (i * i) % 2 == 0:
        print(i)
    i += 1


# 59. Divisible by 8 but not by 4
i = 1
while i <= 100:
    if i % 8 == 0 and i % 4 != 0:
        print(i)
    i += 1
# No output: every multiple of 8 is divisible by 4.


# 60. Sum of numbers divisible by 9
i = 9
s = 0
while i <= 100:
    s += i
    i += 9
print(s)

# 61. Input until 0
n = int(input("Enter number: "))
while n != 0:
    n = int(input("Enter number: "))


# 62. Password check
p = input("Enter password: ")
while p != "python123":
    p = input("Enter password: ")
print("Correct password")


# 63. Sum of 5 numbers
i = 1
s = 0
while i <= 5:
    n = int(input("Enter number: "))
    s = s + n
    i += 1
print(s)


# 64. Count positive numbers
i = 1
s = 0
while i <= 10:
    n = int(input("Enter number: "))
    if n > 0:
        s += 1
    i += 1
print(s)


# 65. Count negative numbers
i = 1
s = 0
while i <= 10:
    n = int(input("Enter number: "))
    if n < 0:
        s += 1
    i += 1
print(s)


# 66. Input until negative number
n = int(input("Enter number: "))
while n >= 0:
    n = int(input("Enter number: "))


# 67. Count digits
n = int(input("Enter number: "))
s = 0
while n > 0:
    n = n // 10
    s += 1
print(s)


# 68. Sum of digits
n = int(input("Enter number: "))
s = 0
while n > 0:
    s = s + n % 10
    n = n // 10
print(s)


# 69. Reverse a number
n = int(input("Enter number: "))
s = 0
while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10
print(s)


# 70. Last digit
n = int(input("Enter number: "))
print(n % 10)


# 71. Remove last digit repeatedly
n = int(input("Enter number: "))
while n > 0:
    n = n // 10
    print(n)


# 72. Palindrome check
n = int(input("Enter number: "))
a = n
s = 0
while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10

if a == s:
    print("Palindrome")
else:
    print("Not palindrome")


# 73. Armstrong number
n = int(input("Enter number: "))
a = n
s = 0
l = len(str(n))

while n > 0:
    r = n % 10
    s = s + r ** l
    n = n // 10

if a == s:
    print("Armstrong")
else:
    print("Not Armstrong")


# 74. Product of digits
n = int(input("Enter number: "))
s = 1
while n > 0:
    r = n % 10
    s = s * r
    n = n // 10
print(s)


# 75. Count even digits
n = int(input("Enter number: "))
s = 0
while n > 0:
    r = n % 10
    if r % 2 == 0:
        s += 1
    n = n // 10
print(s)


# 76. Count odd digits
n = int(input("Enter number: "))
s = 0
while n > 0:
    r = n % 10
    if r % 2 != 0:
        s += 1
    n = n // 10
print(s)


# 77. Largest digit
n = int(input("Enter number: "))
big = 0
while n > 0:
    r = n % 10
    if r > big:
        big = r
    n = n // 10
print(big)


# 78. Smallest digit
n = int(input("Enter number: "))
small = 9
while n > 0:
    r = n % 10
    if r < small:
        small = r
    n = n // 10
print(small)


# 79. Check whether number contains 7
n = int(input("Enter number: "))
found = 0
while n > 0:
    r = n % 10
    if r == 7:
        found = 1
    n = n // 10

if found == 1:
    print("Contains 7")
else:
    print("Does not contain 7")


# 80. Print digits from right to left
n = int(input("Enter number: "))
while n > 0:
    print(n % 10) #(aaaaaa????????)
    n = n // 10

# 81. Check prime number
n = int(input("Enter number: "))
i = 2
while i < n:
    if n % i == 0:
        print("Not prime")
        break
    i += 1
else:
    if n > 1:
        print("Prime")
    else:
        print("Not prime")


# 82. Prime numbers from 1 to 100
n = 2
while n <= 100:
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1
    if i == n:
        print(n)
    n += 1


# 83. Factors of a number
n = int(input("Enter number: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1


# 84. Count factors
n = int(input("Enter number: "))
i = 1
s = 0
while i <= n:
    if n % i == 0:
        s += 1
    i += 1
print(s)


# 85. Perfect number
n = int(input("Enter number: "))
i = 1
s = 0
while i < n:
    if n % i == 0:
        s += i
    i += 1

if s == n and n > 0:
    print("Perfect number")
else:
    print("Not perfect")


# 86. Fibonacci series for 10 terms
a = 0
b = 1
i = 1
while i <= 10:
    print(a)
    c = a + b
    a = b
    b = c
    i += 1


# 87. Palindrome number

n = int(input("Enter number: "))
a = n
s = 0

while n > 0:
    r = n % 10
    s = s * 10 + r
    n = n // 10

if a == s:
    print("Palindrome")
else:
    print("Not palindrome")


# 88. LCM of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
i = a
while i % b != 0:
    i += a
print(i)


# 89. Check co-prime numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
i = 1
s = 0
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        s += 1
    i += 1

if s == 1:
    print("Co-prime")
else:
    print("Not co-prime")


# 90. Perfect squares from 1 to 100
i = 1
while i * i <= 100:
    print(i * i)
    i += 1


# 91. Squares for 10 terms
i = 1
while i <= 10:
    print(i * i)
    i += 1


# 92. Powers of 2 for 10 terms
i = 1
n = 2
while i <= 10:
    print(n)
    n = n * 2
    i += 1


# 93. Star triangle
i = 1
while i <= 5:
    print("*" * i)
    i += 1


# 94. Number triangle
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1


# 95. Reverse star triangle
i = 5
while i >= 1:
    print("*" * i)
    i -= 1


# 96. Countdown
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Go!")


# 97. Number guessing game
n = 7
a = int(input("Guess the number: "))
while a != n:
    a = int(input("Try again: "))
print("Correct!")


# 98. Three password attempts
p = "python123"
i = 1
while i <= 3:
    a = input("Enter password: ")
    if a == p:
        print("Correct")
        break
    i += 1
if i > 3:
    print("Attempts over")


# 99. Sum until user enters 0
s = 0
n = int(input("Enter number: "))
while n != 0:
    s += n
    n = int(input("Enter number: "))
print(s)


# 100. Simple calculator
while True:
    a = int(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /) or q to quit: ")

    if op == "q":
        break

    b = int(input("Enter second number: "))

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/" and b != 0:
        print(a / b)
    else:
        print("Invalid operator or division by zero")