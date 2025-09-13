base = int(input())
while base != -1:
    number = input()
    while number != '-1':
        digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        result = 0
        for i in range(len(number)):
            digit_value = digits.index(number[-(i + 1)]) 
            result = result + digit_value * (base ** i) 
        print(result)
        number = input()
    base = int(input())

