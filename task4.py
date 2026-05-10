translations = {
    "cat": "кіт",
    "dog": "собака",
    "house": "дім",
    "car": "машина",
    "book": "книга",
    "water": "вода",
    "sun": "сонце",
    "moon": "місяць",
    "tree": "дерево",
    "apple": "яблуко",
    "friend": "друг",
    "love": "любов",
    "city": "місто",
    "sky": "небо",
    "phone": "телефон",
    "road": "дорога",
    "fire": "вогонь",
    "wind": "вітер",
    "snow": "сніг",
    "rain": "дощ",
}


def select_task():
    task = input("виберіть завдання: 1-2 ")
    match task:
        case "1":
            word = input("введіть слово англійською: ").lower()
            task1(word)
        case "2":
            task2()
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
            select_task()


def task1(word):
    if word in translations:
        print(word, "=", translations[word])
    else:
        print("слово не знайдено")


def task2():
    my_games = input("введіть ваші ігри через кому: ").lower().split(",")
    my_games = set(game.strip() for game in my_games)

    count = int(input("введіть кількість друзів: "))

    common = my_games
    for i in range(1, count + 1):
        games = input(f"введіть ігри друга {i} через кому: ").lower().split(",")
        games = set(game.strip() for game in games)
        common = common & games

    if common:
        print("ігри в які можуть зіграти всі:", ", ".join(common))
    else:
        print("немає спільних ігор")


while True:
    select_task()