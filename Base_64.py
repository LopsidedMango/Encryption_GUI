import pybase64

def encrypt(input_):
    secret = input_
    secret = secret.encode("ascii")
    secret = pybase64.b64encode(secret)
    secret = secret.decode("ascii")
    return secret
def decrypt(input_):
    secret = input_
    secret = secret.encode("ascii")
    secret = pybase64.b64decode(secret)
    secret = secret.decode("ascii")
    return secret
