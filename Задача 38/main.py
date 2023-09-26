# Задача 38: Дополнить телефонный справочник возможностью изменения и 
# удаления данных. Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

class Phonebook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = {}

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name, phone_number = line.strip().split(',')
                    self.contacts[name] = phone_number
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for name, phone_number in self.contacts.items():
                file.write(f"{name},{phone_number}\n")

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        self.save_contacts()

    def get_contact(self, name):
        return self.contacts.get(name)

    def update_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            self.save_contacts()

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()

    def list_contacts(self):
        for name, phone_number in self.contacts.items():
            print(f"{name}: {phone_number}")

def main():
    phonebook = Phonebook("contacts.txt")
    phonebook.load_contacts()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить контакт")
        print("2. Получить контакт")
        print("3. Обновить контакт")
        print("4. Удалить контакт")
        print("5. Список контактов")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            phonebook.add_contact(name, phone_number)
        elif choice == "2":
            name = input("Введите имя контакта: ")
            contact = phonebook.get_contact(name)
            if contact:
                print(f"Номер телефона: {contact}")
            else:
                print("Контакт не найден.")
        elif choice == "3":
            name = input("Введите имя контакта для обновления: ")
            new_phone_number = input("Введите новый номер телефона: ")
            phonebook.update_contact(name, new_phone_number)
        elif choice == "4":
            name = input("Введите имя контакта для удаления: ")
            phonebook.delete_contact(name)
        elif choice == "5":
            phonebook.list_contacts()
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите корректное действие.")

if __name__ == "__main__":
    main()