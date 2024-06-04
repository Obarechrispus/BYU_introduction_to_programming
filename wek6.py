"""
Author: Chnrispus Obare
A simple python script that extract details from a text file
"""
with open(r"C:\Users\obare\byui_schoolwork\BYU_introduction_to_programming\hr_system.txt", "r") as file:
    
    for i in file:
        data_set = i.rstrip()
        data_set= i.split(" ")
        id_num = data_set[2]
        salary = float(data_set[3])
        n_salary = f"{salary:.2f}"
        if data_set[2] == 'Engineer':
            c_d = float(data_set[3])
            salary = float(c_d + 1000)
            n_salary = salary
        else:
            pass
        print(f"{data_set[0]} (ID: {id_num}), {data_set[2]} - ${n_salary}")
