import sys
import my_functions

sys.stdout.reconfigure(encoding="utf-8")


def main():
    while True:
        print("\n========== МЕНЮ ==========")
        print("1 - Обчислити значення X")
        print("2 - Побудувати піраміду")
        print("0 - Вихід")
        print("==========================")

        choice = input("Введіть номер пункту: ")

        if choice == "1":
            try:
                a = float(input("Введіть число a: "))
                b = float(input("Введіть число b: "))

                if a == b:
                    print("Помилка! Числа a та b не повинні бути однаковими.")
                else:
                    x = my_functions.calculate_x(a, b)
                    print("Отримане значення X:", round(x, 2))

            except ValueError:
                print("Помилка! Введіть саме число.")

        elif choice == "2":
            try:
                n = int(input("Введіть N від 1 до 10: "))

                if n < 1 or n > 10:
                    print("Помилка! N повинно бути від 1 до 10.")
                else:
                    my_functions.pyramid(n)

            except ValueError:
                print("Помилка! Потрібно ввести ціле число.")

        elif choice == "0":
            print("Роботу програми завершено.")
            break

        else:
            print("Такого пункту меню немає. Спробуйте ще раз.")


main()