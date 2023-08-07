def main():

    filename = input("Введіть назву файлу: ")

    try:

        with open(filename, 'w') as file:
            while True:

                user_input = input("Введіть текст (порожній рядок для завершення): ")


                if not user_input:
                    break


                file.write(user_input + '\n')

        print("Дані успішно записані у файл.")

    except Exception as e:
        print("Під час роботи програми сталася помилка:", e)


if __name__ == "__main__":
    main()