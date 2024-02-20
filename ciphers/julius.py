from string import ascii_letters


def encrypt(text, key):
    letters = ascii_letters
    result = ""

    for char in text:
        if char in letters:
            new_key = (letters.index(char) + key) % len(letters)
            result += letters[new_key]
        else:
            result += char

    return result


def decrypt(text, key):
    key *= -1
    return encrypt(text, key)


def brute_force(text):
    letters = ascii_letters
    key = 1
    result = ""
    bf_data = {}

    while key <= len(letters):
        result = decrypt(text, key)
        bf_data[key] = result
        result = ""
        key += 1
    return bf_data
