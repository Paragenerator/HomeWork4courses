import random
import datetime
#_____________________FUNC_Generate id______________________________________________________________________

def gen_id():
    return int((datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+ str(random.randint(0, 999999)).zfill(6))
#___________________________________________________________________________________________________________

#__________________________________CLASS_____________________________________________
class Product:
    def __init__(self,name,price):
        
        self.name = name
        self.price = price
        self.id = gen_id() #_create id for object
    
    def __str__(self):
        return f"Product (id: {self.id}, name: {self.name}, price: {self.price})"


#____________________________TEST_____________________________________________________
obj_list = [] #__Object list

ids_list = [] #_id's list

for i in range (1000):

    obj_list.append('p'+str(+i)) #__Object name create (хотя можно было бы и числа оставить)

    obj_list[i] = Product(('tovar_'+str(i)), (i)) #__OBJECT CREATE
    

    if obj_list[i].id in ids_list: #__Если айДи нынешнего объекта есть в списке с айДи всех объектов)
        print("\nТЕСТ НЕ ПРОЙДЕН! id объекта",i,obj_list[i],"уже есть в списке")
        break
    else:
        ids_list.append(obj_list[i].id) #__Если его там нет, добавляет нынешний id объекта в список всех id)
    
    
    
    print(obj_list[i]) #_Print current object

print('\n')

print(obj_list[99].id) #_Этими двумя принтами сверяю если списки идентинтичны
print(ids_list[99])