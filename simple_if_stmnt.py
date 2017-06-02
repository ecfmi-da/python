
tu_xlsm = "EXCEL_UI_TU.xlsm"

print("Hi, would you like to use >> {} <<<, y or n".format(tu_xlsm))
y_n = input().lower()
if y_n == "y":
    print("Thanks, I will use that file")
else:
    other_answ = input("What is the name of the file you would like to use?\n")
    print("Ok, I will use the file {}".format(other_answ))
