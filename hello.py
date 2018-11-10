from tkinter import *
from tkinter import messagebox

root = Tk()
#назване важно
root.geometry("300x500")
root.title("Окно входа")

def registation():
    text = Label(text="Для входа в систему зарегистрируйтесь")
    text_login = Label(text="Введите ваш логин:")
    registr_login = Entry()
    text_password1 = Label(text="Введите пароль")
    registr_password1 = Entry()
    text_password2 = Label(text="Введите повторно пароль")
    registr_password2 = Entry(show="*")
    button_registr = Button(text="Зарегистрироваться")
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

registation()

root.mainloop()