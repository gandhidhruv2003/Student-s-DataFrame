import pandas as pd
def students():
    name_list = []
    mark_list = []
    roll_no_list = []

    n = int(input("Enter the number of students: "))

    for i in range(n):
        name = str(input("Enter the name: "))
        mark = int(input("Enter the marks: "))
        roll_no = int(input("Enter the Roll number: "))
        name_list.append(name)
        mark_list.append(mark)
        roll_no_list.append(roll_no)

    df = pd.DataFrame({
        "Name": name_list,
        "Mark": mark_list,
        "Roll number": roll_no_list
    })

    print(df)
students()