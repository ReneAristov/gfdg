import os

def read_notes():
    """Чтение заметок из файла."""
    if os.path.exists("notes.txt"):  # Проверяем, существует ли файл
        with open("notes.txt", "r", encoding="utf-8") as file:
            return file.read().split("\n---\n")  # Разделяем заметки по разделителю
    return []  # Если файла нет или он пуст, возвращаем пустой список


def write_notes(notes):
    """Запись заметок в файл."""
    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("\n---\n".join(notes))  # Записываем заметки обратно в файл


def delete_note_by_title(title):
    """Удаление заметки по заголовку."""
    notes = read_notes()
    
    # Простой способ удаления заметки по заголовку
    new_notes = []
    for note in notes:
        if not note.startswith(f"Заголовок: {title}"):
            new_notes.append(note)
    
    if len(new_notes) == len(notes):
        print(f"Заметка с заголовком '{title}' не найдена.")  # Если заметка не была найдена
    else:
        write_notes(new_notes)  # Если была удалена, записываем обновленные заметки
        print(f"Заметка с заголовком '{title}' успешно удалена.")


