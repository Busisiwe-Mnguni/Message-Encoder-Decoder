base = int(input())
while base != -1:
    number = int(input())
    while number != -1:
        digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        result = ''
        if number == 0:
            result = '0'
        else:
            while number > 0:
                digit = number % base
                result = digits[digit] + result
                number = number //base
        print(result)
        number = int(input())
    base = int(input())
