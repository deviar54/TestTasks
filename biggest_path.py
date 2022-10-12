#Объявляем глобальную переменную для хранения самого длинного пути в дереве
biggest_path_var = []
#Объявляем счетчик для всех узлов и листьев
counter = 0

path = eval(input())

#Основная функция для возвращения самого длинного пути
def biggest_path(X: dict)->str:
    dfs_tree(X)
    #если счетчик узлов меньше или равен двум, то выводим /
    return '/'+'/'.join(biggest_path_var) if counter>2 else '/'
    

#Функция поиска в глубину для дерева
def dfs_tree(X: dict, path=[]):
    #Проверка на пустой словарь
    if len(X)!=0:
        nodes = list(X.keys()) #Добавляем верхний уровень вершин дерева из словаря
        
        global biggest_path_var
        global counter

        #Делаем обход по узлам
        for node in nodes:
            #Наращиваем счетчик узлов
            counter+=1

            #Создаем временный путь для нахождения остальных узлов в ветке
            temp_path = path.copy()
            temp_path.append(node)
            
            #Проверка на существование вершин дерева на уровне ниже
            if type(X[node]) is dict:
                dfs_tree(X[node], temp_path)
            else: #если нет вершин значит вложенный уровень состоит из листьев
                #Объявляем переменную для листьев и записываем туда уникальные значения
                leafs = list(set(X[node]))
                #Наращиваем счетчик узлов по количеству листьев
                counter+=len(leafs)
                #Добавляем во временный путь первый лист
                temp_path.append(leafs[0])                
               
            #Сравниваем самый длинный путь и временный путь по длине, если временный путь длиннее,
            #то присваиваем глобальной переменной новое значение
            if len(temp_path)>len(biggest_path_var):
                biggest_path_var=temp_path.copy()


print(biggest_path(path))

