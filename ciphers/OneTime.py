import random


class OneTime:
    def encrypt(self, text):
        plain = [ord(i) for i in text]
        key = []
        result = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            result.append(c)
            key.append(k)

        return result, key

    def decrypt(self, result, key):
        plain = []

        for i in range(len(key)):
            p = int((result[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))

        result = ''.join(i for i in plain)

        return result
