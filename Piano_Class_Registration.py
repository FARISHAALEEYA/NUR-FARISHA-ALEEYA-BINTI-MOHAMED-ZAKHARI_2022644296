import tkinter as tk
from tkinter import ttk
import mysql.connector

def enter_data():
        
        # Student info
        student_name = student_name_entry.get()
        gender = gender_type_combobox.get()
        category = category_type_combobox.get()
        no_phone = int(no_phone_entry.get())
        email = email_entry.get()

        # Connect to MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="piano_class_registration"
        )

        mycursor = mydb.cursor()

        # Inserting data into a table
        sql = "INSERT INTO student_data (Student_Name, Gender, Category, No_Phone, Email) VALUES (%s, %s, %s, %s, %s)"
        val = (student_name, gender, category, no_phone, email)
        mycursor.execute(sql, val)
        mydb.commit()

# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Piano Class Registration Form")
root.geometry('700x500')

# Page title
label = tk.Label(root, text="Piano Class Registration", font=("Roman", 28, "bold"), bg='#FA8072')
label.grid(ipadx=10, ipady=10)

frame = tk.Frame(root)
frame.grid()

# Student Info Frame
student_info_frame = tk.LabelFrame(frame, text="Student Information", bg='#FFA07A')
student_info_frame.grid(row=1, column=0, padx=30, pady=50)

# Student Name
student_name_label = tk.Label(student_info_frame, text="Student Name")
student_name_label.grid(row=0, column=0)
student_name_entry = tk.Entry(student_info_frame)
student_name_entry.grid(row=1, column=0)

# Gender
gender_type_label = tk.Label(student_info_frame, text="Gender")
gender_type_combobox = ttk.Combobox(student_info_frame, values=["", "Male", "Female"])
gender_type_label.grid(row=0, column=1)
gender_type_combobox.grid(row=1, column=1)

# Category
category_type_label = tk.Label(student_info_frame, text="Category")
category_type_combobox = ttk.Combobox(student_info_frame, values=["Primary School", "Secondary School"])
category_type_label.grid(row=2, column=0)
category_type_combobox.grid(row=3, column=0)

# No Phone
no_phone_label = tk.Label(student_info_frame, text="No Phone")
no_phone_label.grid(row=2, column=1)
no_phone_entry = tk.Entry(student_info_frame)
no_phone_entry.grid(row=3, column=1)

# Email
email_label = tk.Label(student_info_frame, text="Email")
email_label.grid(row=3, column=2)
email_entry = tk.Entry(student_info_frame)
email_entry.grid(row=3, column=3)

for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Save Button
save_button = tk.Button(root, text="Enter", command=enter_data)
save_button.grid(pady=10)

# Output Label & result
label = tk.Label(root, text='Thank You For Your Registration!', font=("Times New Romans", 17))
label.grid(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.grid()

root.mainloop()