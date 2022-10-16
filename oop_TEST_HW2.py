import random
import datetime
import re

#_____________________FUNC_Generate id______________________________________________________________________

def gen_id():
    return int((datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+ str(random.randint(0, 999999)).zfill(6))
#___________________________________________________________________________________________________________

#__________________________________CLASS PRODUCT_____________________________________________
class Product:
    def __init__(self,name,price):
        
        self.name = name
        self.setPrice(price)
        self.id = gen_id() #_create id for object
    
    def __str__(self):

        return f"Product (id: {self.id}, name: {self.name}, price pr: {self.__price})"

    def __repr__(self):
        return self.__str__()

    def getPrice(self):
        return self.__price
    def setPrice(self,price):
        if price >=0:
            self.__price = price
        else:
            print("такой цены быть не может, сделай положительную")
            self.setPrice(input("price for object can be only >0 :"))
            


#__________________________________CLASS CLIENT_____________________________________________
class Client:
    

    def __init__(self,FullName,PhysicalAddress):
        
        self.setFullName(FullName)

        self.setPhysicalAddress(PhysicalAddress)

        self.id = gen_id() #_create id for object
    

    def __str__(self):
        return f"PClient (id: {self.id}, name: {self.__FullName}, address : {self.__PhysicalAddress})"

    def __repr__(self):
        return self.__str__()
      
  
            #_________________________get/set FullName_________________________________

    def getFullName(self):
            return self.__FullName
        
    def setFullName(self,FullName):
        if len(FullName) >=3 and (re.compile("^[a-zA-Zа-яА-ЯёЁ ]+$").search(FullName) is not None)\
                and FullName.count(' ') == 1\
                    and FullName[0].isupper()\
                       and FullName[FullName.find(' ')+1].isupper() :
            self.__FullName = FullName
        else:
            print("\nВы дали параметру FullName неверное значение, введите праметр по примеру.")
            self.setFullName(input("example for Client(Full Name) - 'John Smith'. Input: "))
    #__________________________________________________________



            #_________________________get/set PhysicalAddress_________________________________

    def getPhysicalAddress(self):
            return self.__PhysicalAddress
        
    def setPhysicalAddress(self,PhysicalAddress):
        if len(PhysicalAddress) >=5 and (re.compile("^[\da-zA-Zа-яА-ЯёЁ ,/-]+$").search(PhysicalAddress) is not None)\
                and PhysicalAddress[0].isupper()\
                    and PhysicalAddress.count(' ') >= 2 and PhysicalAddress.count(',') ==1\
                        and (PhysicalAddress[PhysicalAddress.find(',')+1]==' ' and PhysicalAddress[PhysicalAddress.find(',')+2].isupper()):
            self.__PhysicalAddress = PhysicalAddress
        else:
            print("\nВы дали параметру PhysicalAddress неверное значение, введите праметр по примеру.")
            self.setPhysicalAddress(input("example for Client(PhysicalAddress) - 'City, Street 100'.\nInput: "))
#__________________________________________________________




#__________________________________CLASS BAG_____________________________________________
class Bag:
    def __init__(self,client,products):
        self.id = gen_id() #_create id for object
        self.client = client
        self.products = products
        self.cost = self.fullCost()
    
    def fullCost(self):
        bagCost = 0
        for i in range (len(self.products)):
            bagCost = bagCost + (self.products[i].getPrice())
        return bagCost

#_________________________________________________________________________________________





cl1 = Client("Li_Nu", "Lobnya, Lenina 19")


print('\n',cl1.getFullName(),'\n')

print(cl1)

print("\n НИЖЕ БУДЕТ ВЫВОД ИЗ ОБЪЕКТА класса 'Bag' \n")





bag1 = Bag(Client("John Doe", "Chisinau, Puskin 1"), products=[Product("hleb", 10), Product("meat", 100), Product("milk", 15)])


print("\n",bag1.client)

print('\n','Тут продукты из объекта BAG \n',bag1.products)

print('\n','тут общая стоимость объектов из списка "roducts" : ',bag1.cost)

































print("last PRiiiiiiiiiiiiint")