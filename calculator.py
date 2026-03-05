import tkinter 

buttom_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(buttom_values)
column_count = len(buttom_values[0])

color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "#FFFFFF"


window = tkinter.Tk()
window.title("Calculator by Shoxrux")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", background=color_black, font=("Arial", 45),
                      foreground=color_white, anchor='e', width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky='we')

for row in range(row_count):
    for col in range(column_count):
        value = buttom_values[row][col]
        buttom = tkinter.Button(frame, text=value, font=('Arial', 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: buttom_clicked(value))
        
        if value in right_symbols:
            buttom.config(foreground=color_white, background=color_orange)
        elif value in top_symbols:
            buttom.config(foreground=color_black, background=color_light_grey)
        else:
            buttom.config(foreground=color_white, background=color_dark_grey)

        buttom.grid(row=row+1, column=col)

frame.pack()

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator

    A = "0"
    operator = None
    B = None

def remove_zero_demical(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def buttom_clicked(value):
    global right_symbols, top_symbols, A, B, operator, label

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_demical(numA + numB)
                elif operator == "-": 
                    label["text"] = remove_zero_demical(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_demical(numA * numB)
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = '0'
                    else:
                        label["text"] = remove_zero_demical(numA / numB)

                clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                operator = value
                label["text"] = "0"
                

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_demical(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_demical(result)
            
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in '0123456789':
            if label["text"] == '0':
                label["text"] = value
            else:
                label["text"] += value
        
        elif value == "√":
            label["text"] = remove_zero_demical(float(label["text"]) ** 0.5)

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()