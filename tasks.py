
from tkinter import *

# чтние файла
with open("tasks.txt", "r",encoding="UTF-8") as f:
    tasks= f.read().splitlines()


# функция перезапуска
def restart():
    global tasks
    tasks=["Зарядка для глаз","Зарядка для рук","Рисование","Медитация","Программирование"]
    with open("tasks.txt", "w", encoding="UTF-8") as f:
        #f.write("\n".join(a).join("\n"))
        for i in tasks:
            f.write("%s\n" % i)

    new_day()


# создание окна
root = Tk()
root.title("Tasks")
txt_hello=Label(root,text="Хорошего дня,Илья")


# проверка нужна ли кнопка перезапуска
if len(tasks)==0 or tasks[0]=="":
    button_new_day= Button(root, text="начать новый день", padx=60, pady=20,command=lambda: [restart(),button_new_day.destroy()])
    button_new_day.grid(row=7, column=1)


# функция удаления
def delete(task):
    global tasks

    tasks.remove(task)
    with open("tasks.txt", "w", encoding="UTF-8") as f:
        for i in tasks:
            f.write("%s\n" % i)


# функция отображения спсиска дел
def new_day():
    global tasks
    if "Зарядка для глаз" in tasks:
        txt_task_1=Label(root,text="Зарядка для глаз")
        button_1 = Button(root, text="сделал", padx=60, pady=20, command=lambda: [button_1.destroy(),
                                                                                  txt_task_1.destroy(),delete("Зарядка для глаз")])
        txt_task_1.grid(row=2, column=1)
        button_1.grid(row=2, column=2)


    if "Зарядка для рук" in tasks:
        txt_task_2 = Label(root, text="Зарядка для рук")
        button_2 = Button(root, text="сделал", padx=60, pady=20,
                          command=lambda: [button_2.destroy(), txt_task_2.destroy(),delete("Зарядка для рук")])
        txt_task_2.grid(row=3, column=1)
        button_2.grid(row=3, column=2)

    if "Рисование" in tasks:
        txt_task_3 = Label(root, text="Рисование")
        button_3 = Button(root, text="сделал", padx=60, pady=20,
                          command=lambda: [button_3.destroy(), txt_task_3.destroy(),delete("Рисование")])
        txt_task_3.grid(row=4, column=1)
        button_3.grid(row=4, column=2)



    if "Медитация" in tasks:
        txt_task_4 = Label(root, text="Медитация")
        button_4 = Button(root, text="сделал", padx=60, pady=20,
                          command=lambda: [button_4.destroy(), txt_task_4.destroy(),delete("Медитация")])
        txt_task_4.grid(row=5, column=1)
        button_4.grid(row=5, column=2)


    if "Программирование" in tasks:
        txt_task_5 = Label(root, text="Программирование")
        button_5 = Button(root, text="сделал", padx=60, pady=20,
                          command=lambda: [button_5.destroy(), txt_task_5.destroy(),delete("Программирование")])
        txt_task_5.grid(row=6, column=1)
        button_5.grid(row=6, column=2)


    txt_hello.grid(row=1,column=1)

new_day()
root.mainloop()
