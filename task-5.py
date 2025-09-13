def to_base(n, base):
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

def from_base(s, base):
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i, ch in enumerate(reversed(s)):
        result += digits.index(ch) * (base ** i)
    return result

def main():
    mode = input().strip()        # encrypt OR decrypt
    base = int(input().strip())   
    message = input().strip()     # message or base-b numbers

    if mode == "encrypt":
        
        encrypted = []
        for ch in message:
            ascii_val = ord(ch)
            encrypted.append(to_base(ascii_val, base))
        print(" ".join(encrypted))

    elif mode == "decrypt":
       
        parts = message.split()
        decrypted = ""
        for num in parts:
            decimal_val = from_base(num, base)
            decrypted += chr(decimal_val)
        print(decrypted)

if __name__ == "__main__":
    main()
