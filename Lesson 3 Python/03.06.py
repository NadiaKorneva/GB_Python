user_words = input("Введите слова:").split()

def int_func(input_word: str):
    return "".join([
        input_word[0].upper(), input_word[1:]
    ])

user_words = [int_func(x) for x in user_words]

print(" ".join(user_words))