from tkinter import *
from tkinter import messagebox
import pickle

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
    button_registr = Button(text="Зарегистрироваться", command=lambda: save())
    text.pack()
    text_login.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

    def save():
        login_pass_save = {}#создаем словарь
        login_pass_save[registr_login.get()]=registr_password1.get()
        doc = open("login.txt", "wb")
        pickle.dump(login_pass_save, doc)
        doc.close()
        login()

def login():
    text_log = Label(text="Теперь можно работать в системе")
    text_enter_login = Label(text="Введите ваш логин")
    enter_login = Entry()
    text_enter_password = Label(text="Введите ваш пароль")
    enter_password = Entry(show="*")
    button_enter = Button(text="Войти", command = lambda: password_true())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    button_enter.pack()

    def password_true():
        doc = open("login.txt", "rb")
        file_doc = pickle.load(doc)
        doc.close()
        if enter_login.get() in file_doc:
            if enter_password.get() == file_doc[enter_login.get()]:
                messagebox.showinfo("Вход выполнен успешно!")
            else:
                messagebox.showerror("Ощибка")
        else:
            messagebox.showerror("Ошибка")

registation()


root.mainloop()