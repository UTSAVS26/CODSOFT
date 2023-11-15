import tkinter as tk

calculation = ""

# Adding the Numbers and Symbol to the String Calculation
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Evaluating the string Calculation
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.delete(1.0, "Error")

# Clearing the Input and Output Field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
# Title
root.title("Calculator")
# Dimension of the Calculator
root.geometry("322x390")

# Input and Output Frame
text_result = tk.Text(root, height = 2, width = 18, font = ("Comic Sans", 24))
text_result.grid(columnspan = 5)

# Number's Button
## 1
btn_1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_1.grid(row = 4, column = 1)

## 2
btn_2 = tk.Button(root, text = "2", command = lambda: add_to_calculation(2), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_2.grid(row = 4, column = 2)

## 3
btn_3 = tk.Button(root, text = "3", command = lambda: add_to_calculation(3), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_3.grid(row = 4, column = 3)

## 4
btn_4 = tk.Button(root, text = "4", command = lambda: add_to_calculation(4), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_4.grid(row = 3, column = 1)

## 5
btn_5 = tk.Button(root, text = "5", command = lambda: add_to_calculation(5), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_5.grid(row = 3, column = 2)

## 6
btn_6 = tk.Button(root, text = "6", command = lambda: add_to_calculation(6), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_6.grid(row = 3, column = 3)

## 7
btn_7 = tk.Button(root, text = "7", command = lambda: add_to_calculation(7), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_7.grid(row = 2, column = 1)

## 8
btn_8 = tk.Button(root, text = "8", command = lambda: add_to_calculation(8), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_8.grid(row = 2, column = 2)

## 9
btn_9 = tk.Button(root, text = "9", command = lambda: add_to_calculation(9), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_9.grid(row = 2, column = 3)

## 0
btn_0 = tk.Button(root, text = "0", command = lambda: add_to_calculation(0), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_0.grid(row = 5, column = 2)

# Operators
## Add(+)
btn_add = tk.Button(root, text = "+", command = lambda: add_to_calculation("+"), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_add.grid(row = 5, column = 4)

## Subtract(-)
btn_sub = tk.Button(root, text = "-", command = lambda: add_to_calculation("-"), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_sub.grid(row = 4, column = 4)

## Multiply(*)
btn_mul = tk.Button(root, text = "*", command = lambda: add_to_calculation("*"), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_mul.grid(row = 3, column = 4)

## Divide(/)
btn_div = tk.Button(root, text = "/", command = lambda: add_to_calculation("/"), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_div.grid(row = 2, column = 4)

## Close Bracket (
btn_close_bracket = tk.Button(root, text = "(", command = lambda: add_to_calculation("("), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_close_bracket.grid(row = 5, column = 1)

## Open Bracket )
btn_open_bracket = tk.Button(root, text = ")", command = lambda: add_to_calculation(")"), width = 5, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_open_bracket.grid(row = 5, column = 3)

# Clear Screen
btn_clear = tk.Button(root, text = "C", command = clear_field, width = 11, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_clear.grid(row = 6, column = 1, columnspan = 2)

# Evaluate Answer
btn_equal = tk.Button(root, text = "=", command = evaluate_calculation, width = 11, font = ("Comic Sans MS", 14), bg = "Black", fg  ="White", bd = 10)
btn_equal.grid(row = 6, column = 3, columnspan = 2)

root.mainloop()