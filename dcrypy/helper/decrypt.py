def binary_exponentiation(a, b, m):
    res = 1
    while b>0:
        if b&1:
            res *= a%m
        a *= a%m
        b>>=1
    return res
        

class Decryption:
    def __init__(self, ciphertext: str) -> None:
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.rev_alphabets = self.alphabets[::-1]
        self.ciphertext = ''.join(ciphertext.split()).lower()
        self.plaintext = ''
        self.key = ''

    def affine(self, a: int, b: int) -> str:
        a_c = 1
        while 1:
            if (a*a_c)%26 == 1:
                break
            a_c+=1
        d = {}
        for i in range(len(self.alphabets)):
            d[self.alphabets[i]] = i
        for i in self.ciphertext:
            self.plaintext += chr(97 + a_c*(d[i] - b)%26)
        return self.plaintext

    def atbash(self) -> str:
        for char in self.ciphertext:
            self.plaintext += self.rev_alphabets[self.alphabets.index(char)]
        return self.plaintext

    def beaufort(self, key: str) -> str:
        self.key = ''.join(key.split()).lower()
        n1, n2 = len(self.ciphertext), len(key)
        temp = (n1//n2)*key + key[:n1%n2]
        temp = temp.lower()
        for i in range(n1):
            t1, t2 = self.ciphertext[i], temp[i]
            self.plaintext += self.alphabets[ord(t2) - ord(t1)]
        return self.plaintext

    def caesar_with_shift(self, shift: int) -> str:
        shift%=26
        for char in self.ciphertext:
            if ord(char)>96 and ord(char)<123:
                self.plaintext += chr((ord(char) + 26 - shift - 97)%26 + 97)
            else:
                self.plaintext += char
        return self.plaintext

    def caesar_without_shift(self) -> str:
        answer = []
        for shift in range(1, 27):
            temp = ''
            for char in self.ciphertext:
                if ord(char)>96 and ord(char)<123:
                    temp += chr((ord(char) + 26 - shift - 97)%26 + 97)
                else:
                    temp += char
            answer.append(temp)
        return answer

    def keyword(self, key: str) -> str:
        self.key = ''.join(key.split()).lower()
        d = {}
        keyword = ''
        enc = ''
        for i in self.key:
            if i not in keyword:
                keyword+=i
        for i in self.alphabets:
            if i not in keyword:
                enc+=i
        n = len(keyword)
        for i in range(n):
            d[keyword[i]] = self.alphabets[i]
        for i in range(n, 26):
            d[enc[i-n]] = self.alphabets[i]
        for i in self.ciphertext:
            self.plaintext += d[i]
        return self.plaintext

    def substitution(self, key: int) -> str:
        d = {}
        for i in range(len(self.alphabets)):
            d[self.alphabets[i]] = self.alphabets[(i-key)%26]
        for i in self.ciphertext:
            if i in d:
                self.plaintext+=d[i]
            else:
                self.plaintext+=i
        return self.plaintext

    def vigenere(self, key: str) -> str:
        self.key = ''.join(key.split()).lower()
        n1, n2 = len(self.ciphertext), len(key)
        temp = (n1//n2)*key + key[:n1%n2]
        temp = temp.lower()
        for i in range(len(temp)):
            self.plaintext += self.alphabets[(ord(self.ciphertext[i]) - ord(temp[i]) + 26)%26]
        return self.plaintext

    def rsa(self, c, d, p, q) -> int:
        n = p*q
        m = binary_exponentiation(c, d, n)
        return m