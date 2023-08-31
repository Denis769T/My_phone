#------------------читаем из файла
slovar="C:\Seminarki\Programmir\Python1\Papki\phon.txt"
data = {}
#data_1 =[]
with open(slovar, "r", encoding="utf-8") as fil:
    for line in fil:
        key, value = line.split("-")
        data[key] = value
#---------------------------------стираем файл(save()),подготовка к записи- очистка от символов data
def sss():
    save()
    for key in data:
        text=(f"{str(data[key])}")
        simvol = "'/[]\n-"
        text="".join(([char for char in text if char not in simvol]))#удаление всех спец символов
        save_1(key,text)
#------------------------------- Ввод данных в тел.книгу
def input_data():
    input_1 = (input("Введите данные для сохранения в справочнике (ФИО:Тел:Коментарий)\n"
                     "Пример(Иванюк С.М:+7920909096:Сотовый):").strip())
    index_1 = input_1.find(":")
    key_1 = str(input_1[0:index_1])
    data.setdefault(key_1, input_1)
    save_1(key_1,input_1)
# ------------------------------------------Поиск
def poisk():
    poisk = input("Введите ФИО(Иванов Б.В.):")  # поиск значения по ключу.Нужно
    #simvol = "'n[]\/"
    #data="".join(([char for char in data if char not in simvol]))
    print(data.setdefault(poisk, "Таких данных нет"))
    input("Для продолжения нажмите ввод")  
# ----------------------------------------------------Del удаление строки 
def delete():
    del_1 = input("Введите ФИО удаляемую из справочника (Иванов Б.В.):")
    data.pop(del_1, None)
    input("Удаление успешно.Для продолжения нажмите ввод")
#-------------------------------------------
def save_1(key,text):
    key=key+'-'
    string=key+text+'\n'
    with open("phon.txt", "a",encoding="utf-8")as data:
        data.write(string)
# --------------------------------------Вывод данных из словаря(весь список).
def slovar():
    for key in data:
        a=(f"{str(data[key])}")
        simvol = "'n[]\/"
        a="".join(([char for char in a if char not in simvol]))#удаление всех спец символов
        print(a.strip())
    input("Нажмите ввод.")
def save():
    with open("phon.txt", "w",encoding="utf-8")as sf:
        sf.truncate()
    print(data) 
def inp_0():
    input_1 = input("Поиск значения по Ф.И.О, для изменения данных(пример:Иванов Г.М.):") 
    print(data.get(input_1,"->Not found"))
    input_2 = input("Замена данных в словаре:")
    data[input_1]=input_2
    # for key,value in data.items():
    #     print(key,"-",value.strip())  
                   
while True:
    print("-------------------------------------------------------")
    print(
          "Ввод команды для управления телефонной книгой:\n1-Создать контакт(с сохранением в файл):\n2-Найти контакт:\n3-Удалить контакт(без сохранения в файл):\n"
          "4-Сохранить справочник в файл:\n5-Вывести весь справочник(из памяти):\n6-Изменение данных словоря(в памяти):\n7-Выход:")
    num = int(input("Введите номер:"))
    if num == 1:
        input_data()
    elif num == 2:
        poisk()
    elif num == 3:
        delete ()
    elif num == 4:
        sss()    
    elif num == 5:
        slovar()
    elif num ==6:
        inp_0()    
    elif num ==7:
        break 
    