users= {}

current_user = None

def reg():
    global users

    login = input("Введите логин:").strip().lower()
    password = input("Введите пароль:")

    if login in users:
        print("данный логин уже занят,придумайте другой,sob sob😢")
        return


    if not login:
         print("Логин не может иметь пустых символов")
         return

    if len(password) < 6:
        print("пароль должен содержать  не менее 6 символов")
        return

    users[login] = password
    print("Аккаунт создан,HI!✌️")


def log():
    global current_user

    login = input("Введите логин:").strip().lower()
    password = input("Введите пароль:")

    if login in users and users[login] == password:
        current_user = login
        print("Успешный вход")
    else:
        print("Логин либо пароль указан не верно,попробуйте еще раз")


def show_profile():
    if current_user is None:
        print("Выполните вход в аккаунт")
    else:
        print(f"Логин: {current_user}")


def logout():
    global current_user

    current_user = None
    print("Вы вышли с аккаунта,bye bye")


def main():
    while True:
        print("\n===Главное меню===")
        print("1.Новый пользователь")
        print("2.Войти в аккаунт")
        print("3.Мой профиль")
        print("4.Выйти из аккаунта")
        print("0.Завершить сеанс")

        choice = input("Укажите пункт:")

        if choice == "1":
            print('Создание нового профиля')
            reg()


        elif choice == "2":
            print('Войти в аккаунт')
            log()

        elif choice == "3":
            print('Ваши данные')
            show_profile()

        elif choice == "4":
            print('Выйти с аккаунта')
            logout()

        elif choice == "0":
            print("Bye bye")
            break

        else:
            print("Указан не верный пункт,свертесь со списком,sob sob")



if __name__ == "__main__":
    main()
