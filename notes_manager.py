from file_handler import read_notes, write_notes, delete_note_by_title


def add_note():
    """Добавить заметку."""
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    note = f"Заголовок: {title}\nТекст: {text}"
    
    notes = read_notes()
    notes.append(note)
    write_notes(notes)
    print("Заметка добавлена!")


def view_notes():
    """Просмотреть все заметки."""
    notes = read_notes()
    if not notes:
        print("Заметки отсутствуют.")
    else:
        for note in notes:
            print(note)
            print("\n---\n")


def delete_note():
    """Удалить заметку по заголовку."""
    title = input("Введите заголовок заметки, которую хотите удалить: ")
    delete_note_by_title(title)
    print(f"Заметка с заголовком '{title}' удалена!")
