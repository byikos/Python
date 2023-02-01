import random
import string


def generate_password(length=int(input(f'De cuantos caracteres quieres el password:'))):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

print(generate_password())
