from tkinter import Tk as tk
from tkinter import ttk
from tkinter import messagebox

def bells_ras():
    bells = ["Урок безопасности: 8.25 - 8.40", "1 урок: 8.45 - 9.25", "2 урок: 9.35 - 10.15", "3 урок: 10.25 - 11.05",
             "4 урок: 11.15 - 11.55", "5 урок: 12.10 - 12.50", "6 урок: 13.05 - 13.45", "7 урок: 13.55 - 14.35",
             "8 урок: 14.45 - 15.25"]
    messagebox.showinfo("Информация", f"Расписание звонков: \n Урок безопасности: 8.25 - 8.40 \n"
                                      f"1 урок: 8.45 - 9.25 \n 2 урок: 9.35 - 10.15 \n 3 урок: 10.25 - 11.05 \n"
                                      f"4 урок: 11.15 - 11.55 \n 5 урок: 12.10 - 12.50 \n 6 урок: 13.05 - 13.45"
                                      f"\n 7 урок: 13.55 - 14.35 \n 8 урок: 14.45 - 15.25")

def monday_ras():
    monday = ["1 - Разговор о неважном", "2 - Английский язык", "3 - Химия", "4 - История", "5 - Математика", ]
    messagebox.showinfo("Информация", f"Расписание уроков на понедельник: \n 1 - Разговор о неважном"
                                      f"\n 2 - Английский язык \n 3 - Химия \n 4 - История \n 5 - Математика \n 6 - Русский язык"
                                      f"\n 7 - Статистика и вероятность \n 8 - Физическая культура")

def tuesday_ras():
    tuesday = ["1 - Информатика", "2 - Математика", "3 - Обществознание", "4 - Физика", "5 - Литература",
               "6 - Иностранный язык", "7 - Физическая культура"]
    messagebox.showinfo("Информация", f"Расписание уроков на вторник: \n 1 - Русский язык \n 2 - Обществознание"
                                      f"\n 3 - Информатика \n 4 - Математика \n 5 - Литература"
                                      f"\n 6 - Алгоритмика \n 7 - Математика")


def wednesday_ras():
    wednesday = ["1 - Русский язык", "2 - Обществознание", "3 - Информатика", "4 - Математика", "5 - Литература",
                 "6 - Алгоритмика", "7 - Математика"]
    messagebox.showinfo("Информация", f"Расписание уроков на среду: \n 1 - Русский язык \n"
                                      f"2 - Обществознание \n 3 - Информатика \n 4 - Математика \n"
                                      f"5 - Литература \n 6 - Алгоритмика \n 7 - Математика")

def thursday_ras():
    thursday = ["1 - Россия - мои горизонты", "2 - География", "3 - Математика", "4 - Английский язык", "5 - История",
                "6 - Информатика", "7 - Физическая культура"]
    messagebox.showinfo("Информация", f"Расписание уроков на четверг: \n 1 - Россия - мои горизонты"
                                      f"\n 2 - География \n 3 - Математика \n 4 - Английский язык \n"
                                      f"5 - История \n 6 - Информатика  \n 7 - Физическая культура")

def friday_ras():
    friday = ["1 - Математика", "2 - Литература", "3 - Информатика", "4 - ОБЗР", "5 - Биология", "6 - Математика",
              "7 - Физика"]
    messagebox.showinfo("Информация", f"1 - Математика \n 2 - Литература \n"
                                      f"3 - Информатика \n 4 - ОБЗР \n 5 - Биология \n 6 - Математика"
                                      f"\n 7 - Физическая культура")


root = tk()
root.geometry("160x170")
root.title("Расписание")

button_monday = ttk.Button(text="Понедельник", command=monday_ras, width=12)
button_monday.pack()

button_tuesday = ttk.Button(text="Вторник", command=tuesday_ras, width=12)
button_tuesday.pack()

button_wednesday = ttk.Button(text="Среда", command=wednesday_ras, width=12)
button_wednesday.pack(anchor="center")

button_thursday = ttk.Button(text="Четверг", command=thursday_ras, width=12)
button_thursday.pack(anchor="center")

button_friday = ttk.Button(text="Пятница", command=friday_ras, width=12)
button_friday.pack(anchor="center")

button_bells = ttk.Button(text="Звонки", command=bells_ras, width=12)
button_bells.pack(anchor="center")

root.mainloop()

