from notes_manager import add_note, view_notes, delete_note

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Просмотреть все заметки")
        print("3. Удалить заметку")
        print("4. Выйти")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

main()  # Просто вызываем функцию main
