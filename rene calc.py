import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.first_number = None  
        self.operation = None 
        self.create_buttons()
        self.create_operation_buttons()
       
        self.entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)
        self.button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 16), command=self.clear)
        self.button_clear.grid(row=5, column=0)
        self.button_equal = tk.Button(root, text="=", width=5, height=2, font=("Arial", 16), command=self.equal)
        self.button_equal.grid(row=5, column=1)
        

    def create_buttons(self):
        """Создание кнопок чисел."""
        numbers = [
            ['1', 1, 1], ['2', 1, 2], ['3', 1, 3],
            ['4', 2, 1], ['5', 2, 2], ['6', 2, 3],
            ['7', 3, 1], ['8', 3, 2], ['9', 3, 3],
            ['0', 4, 2], 
        ]

        for text, row, col in numbers:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 16),
                               command=lambda num=text: self.button_click(num))
            button.grid(row=row, column=col)

    def create_operation_buttons(self):
        operations = [
            ['+', 1, 4], ['-', 2, 4], ['*', 3, 4], ['/', 4, 4], 
        ]

        for op, row, col in operations:
            button = tk.Button(self.root, text=op, width=5, height=2, font=("Arial", 16),
                               command=lambda op=op: self.set_operation(op))
            button.grid(row=row, column=col)

    def button_click(self, number):
        self.entry.insert(tk.END, number)

    def set_operation(self, operation):
        if self.entry.get():  
            self.first_number = float(self.entry.get())  
            self.operation = operation  
            self.entry.insert(tk.END, operation)

    def clear(self):
        self.entry.delete(0, tk.END)

    def equal(self):
        try:
            second_number = float(self.entry.get().split(self.operation)[-1])  
            if self.operation == '+':
                result = self.first_number + second_number
            elif self.operation == '-':
                result = self.first_number - second_number
            elif self.operation == '*':
                result = self.first_number * second_number
            elif self.operation == '/':
                if second_number == 0:
                    result = "Ошибка! Деление на 0"
                else:
                    result = self.first_number / second_number

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Ошибка")


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
