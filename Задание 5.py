import random
import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(characters) for i in range(length))

message = input("Введите сообщение: ")
n = int(input("Введите количество подстановочных символов: "))

encoded_message = ''.join(char + generate_random_string(n) for char in message)
print("Закодированное сообщение:")
print(encoded_message)
