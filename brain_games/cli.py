import prompt


# Приветствует пользователя и запрашивает имя.
def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("Можно узнать ваше имя?")
    print(f"Hello, {name}!")
    return name