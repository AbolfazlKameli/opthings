def encode(plain):
    return [ord(elm) - 78 for elm in plain]


def decode(encode):
    return "".join(chr(elm + 78) for elm in encode)


