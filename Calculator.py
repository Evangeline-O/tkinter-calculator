#CALCULATOR APPLICATION

#import library
from tkinter import *

#function that execute when the button is clicked

def on_button_clicked(value):
    #code to handle button clicked and update the entry field

    #Get the current state of the entry field (either empty or occupied)
    current = entry_var.get()

    if value == "Clear" :
        entry_var.set("")
        
    elif value == "C":
        entry_var.set(current[:-1])
        
    elif value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception:
            entry_var.set("Syntax error")
            
    elif value =="/":
        current += "/"
        entry_var.set(current)

    elif value == "X":
        current += "*"
        entry_var.set(current)
        
    elif value == "+":
         current += "+"
         entry_var.set(current)

    elif value == "-":
         current += "-"
         entry_var.set(current)
    elif value == "%":
        try:
            result = eval(current)/ 100 
            entry_var.set(result)
        except Exception:
            entry_var.set("Syntax error")

    else:
        #Update the state of the entry var with the value coming from the button argument
        entry_var.set(current + str (value))
    
#Initialise the Window
root = Tk()
root.title("Optimum Calculator")
root.geometry("350x500")
root.configure(bg="#873e23")

font_properties=("Arial", 14)
btn_bg="grey"
btn_fg="#eab676"

entry_var = StringVar()

calc_entry = Entry(root, textvariable = entry_var, font=("Arial",20), bg="#442510", fg="#eab676", justify="right", bd=5)

calc_entry.grid(row=0, column=0, padx=8, pady=8, columnspan=4)

#Row 1 (c-X-())

clear_btn = Button(root, text="C", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", bd=1, command= lambda:on_button_clicked("C"))
clear_btn.grid(row=1, column=0, padx=4, pady=4)

percent_btn = Button(root, text="%", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("%"))
percent_btn.grid(row=1, column=1, padx=4, pady=4)

opening_brac_btn = Button(root, text="(", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("("))
opening_brac_btn.grid(row=1, column=2, padx=4, pady=4)

closing_brac_btn = Button(root, text=")", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked(")"))
closing_brac_btn.grid(row=1, column=3, padx=4, pady=4)

#Row 2 (7-8-9-X)

num_7_btn = Button(root, text="7", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("7"))
num_7_btn.grid(row=2, column=0, padx=4, pady=4)

num_8_btn = Button(root, text="8", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("8"))
num_8_btn.grid(row=2, column=1, padx=4, pady=4)

num_9_btn = Button(root, text="9", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("9"))
num_9_btn.grid(row=2, column=2, padx=4, pady=4)

multi_btn = Button(root, text="X", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("X"))
multi_btn.grid(row=2, column=3, padx=4, pady=4)

#Row 3(4-5-6--)

num_4_btn = Button(root, text="4", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("4"))
num_4_btn.grid(row=3, column=0, padx=4, pady=4)

num_5_btn = Button(root, text="5", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("5"))
num_5_btn.grid(row=3, column=1, padx=4, pady=4)

num_6_btn = Button(root, text="6", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("6"))
num_6_btn.grid(row=3, column=2, padx=4, pady=4)

subtraction_btn = Button(root, text="-", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("-"))
subtraction_btn.grid(row=3, column=3, padx=4, pady=4)

#Row 4(1-2-3-+)

num_1_btn = Button(root, text="1", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("1"))
num_1_btn.grid(row=4, column=0, padx=4, pady=4)

num_2_btn = Button(root, text="2", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("2"))
num_2_btn.grid(row=4, column=1, padx=4, pady=4)

num_3_btn = Button(root, text="3", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("3"))
num_3_btn.grid(row=4, column=2, padx=4, pady=4)

addition_btn = Button(root, text="+", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("+"))
addition_btn.grid(row=4, column=3, padx=4, pady=4)

#Row 5(/-0-.-=)
division_btn = Button(root, text="/", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("/"))
division_btn.grid(row=5, column=0, padx=4, pady=4)

num_0_btn = Button(root, text="0", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("0"))
num_0_btn.grid(row=5, column=1, padx=4, pady=4)

deci_point_btn = Button(root, text=".", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("."))
deci_point_btn.grid(row=5, column=2, padx=4, pady=4)

equal_sign_btn = Button(root, text="=", width=6, height=2, font= font_properties, bg=btn_bg, fg="white", command= lambda:on_button_clicked("="))
equal_sign_btn.grid(row=5, column=3, padx=4, pady=4)

#Row 6 (clear)

clear_btn = Button(root, text="Clear", width=24, height=2, font= font_properties, bg=btn_bg, fg="white", bd=1, command= lambda:on_button_clicked("Clear"))
clear_btn.grid(row=6, column=0, padx=4, pady=4, columnspan=4)

root.mainloop()
