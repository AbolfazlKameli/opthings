def encode(plain):
    return [ord(elm) - 78 for elm in plain]


def decode(plain):
    return "".join(chr(elm + 78) for elm in plain)
