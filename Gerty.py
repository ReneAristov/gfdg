import tkinter as tk  # Импортируем библиотеку tkinter для создания графического интерфейса

class Calculator:  # Определение класса Calculator, который реализует калькулятор
    def __init__(self, root):  # Инициализация калькулятора
        self.root = root  # Ссылка на корневое окно
        self.root.title("Калькулятор")  # Заголовок окна
        self.first_number = None  # Переменная для первого числа (для операций)
        self.operation = None  # Переменная для выбранной операции
        self.create_buttons()  # Создание кнопок с числами
        self.create_operation_buttons()  # Создание кнопок с операциями
        
        # Создание поля ввода для отображения чисел и результатов
        self.entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=2, relief="solid")  
        self.entry.grid(row=0, column=0, columnspan=4)  # Устанавливаем позицию поля ввода
        
        # Кнопка очистки
        self.button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 16), command=self.clear)
        self.button_clear.grid(row=5, column=0)  # Размещение кнопки на сетке
        
        # Кнопка равно
        self.button_equal = tk.Button(root, text="=", width=5, height=2, font=("Arial", 16), command=self.equal)
        self.button_equal.grid(row=5, column=1)  # Размещение кнопки равно

    def create_buttons(self):  # Метод для создания кнопок с цифрами
        numbers = [  # Список с числами и их позициями
            ['1', 1, 1], ['2', 1, 2], ['3', 1, 3],
            ['4', 2, 1], ['5', 2, 2], ['6', 2, 3],
            ['7', 3, 1], ['8', 3, 2], ['9', 3, 3],
            ['0', 4, 2],  # Кнопка 0
        ]

        for text, row, col in numbers:  # Проходим по списку чисел
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 16),
                               command=lambda num=text: self.button_click(num))  # Создание кнопки с числом
            button.grid(row=row, column=col)  # Установка позиции кнопки на сетке

    def create_operation_buttons(self):  # Метод для создания кнопок с операциями
        operations = [  # Список операций и их позиций
            ['+', 1, 4], ['-', 2, 4], ['*', 3, 4], ['/', 4, 4], 
        ]

        for op, row, col in operations:  # Проходим по списку операций
            button = tk.Button(self.root, text=op, width=5, height=2, font=("Arial", 16),
                               command=lambda op=op: self.set_operation(op))  # Создание кнопки с операцией
            button.grid(row=row, column=col)  # Установка позиции кнопки на сетке

    def button_click(self, number):  # Метод обработки нажатия кнопки с числом
        self.entry.insert(tk.END, number)  # Добавляем число в поле ввода

    def set_operation(self, operation):  # Метод для установки операции
        if self.entry.get():  # Проверяем, не пустое ли поле ввода
            self.first_number = float(self.entry.get())  # Сохраняем первое число
            self.operation = operation  # Сохраняем выбранную операцию
            self.entry.insert(tk.END, operation)  # Добавляем операцию в поле ввода

    def clear(self):  # Метод очистки поля ввода
        self.entry.delete(0, tk.END)  # Удаляем все содержимое из поля ввода

    def equal(self):  # Метод для выполнения вычислений при нажатии на "="
        try:
            second_number = float(self.entry.get().split(self.operation)[-1])  # Получаем второе число
            if self.operation == '+':  # Если операция сложения
                result = self.first_number + second_number
            elif self.operation == '-':  # Если операция вычитания
                result = self.first_number - second_number
            elif self.operation == '*':  # Если операция умножения
                result = self.first_number * second_number
            elif self.operation == '/':  # Если операция деления
                if second_number == 0:  # Если второе число равно нулю
                    result = "Ошибка! Деление на 0"  # Ошибка деления на 0
                else:
                    result = self.first_number / second_number  # Выполняем деление

            self.entry.delete(0, tk.END)  # Очищаем поле ввода
            self.entry.insert(tk.END, result)  # Выводим результат

        except Exception:  # Если произошла ошибка при вычислениях
            self.entry.delete(0, tk.END)  # Очищаем поле ввода
            self.entry.insert(tk.END, "Ошибка")  # Выводим сообщение об ошибке

# Основной блок для запуска приложения
root = tk.Tk()  # Создаем корневое окно
calc = Calculator(root)  # Создаем объект калькулятора
root.mainloop()  # Запуск главного цикла обработки событий
