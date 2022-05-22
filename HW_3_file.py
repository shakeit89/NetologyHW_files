import os


DIR_NAME = 'files'
BASE_PATH = os.getcwd()
file_names = os.listdir(DIR_NAME)

file_dict = {}

for file in file_names:
    with open(os.path.join(BASE_PATH, DIR_NAME, file)) as f_txt:
        count = 0
        for line in f_txt: #подсчет строк
            count += 1
        if count in file_dict.keys(): #на случай совпадения количества строк у разных файлов
            file_dict[count].append(file) #создаем словарь, где ключи - кол-во строк, значения - список из файлов
        else:
            file_dict[count] = [file]

file_dict = dict(sorted(file_dict.items())) #сортируем словарь по ключам

with open(os.path.join(BASE_PATH, DIR_NAME, 'new_txt'), 'a') as new_txt:
    for count, files in file_dict.items():
        for i in files:
            with open(os.path.join(BASE_PATH, DIR_NAME, i)) as read_txt:
                a = read_txt.read()
                new_txt.write(i+'\n'+ f'{str(count)}\n')
                new_txt.write(a +'\n')


