# age = 19 
# password = True

# if age >= 29 and password:
#     print("Krisish mumkin")
# else:
#     print("sizga mumkkin emas")

# stundent = True
# pensioner = True

# if stundent or pensioner:
#     print("sizga chegirma bor")
# else:
#     print("afsuski sizga chegirma yo'q")

# ligin = False

# if not ligin:
#     print("avval login qiling")

# s = "Hi my Name is Mirjalol"
# print(s.upper())


# words=["Hi", "Mother", "Father"]
# print("Brother".join(words))
# print(len(s))

# age = 18
# if age >= 18:
#     print ("katta")
# else:
#     print("kichik")

# ball = 70

# if ball >= 90:
#     print("A")
# elif ball >= 70:
#     print("B")
# elif ball >= 60:
#     print("C")
# else:
#     print("you feiled")

# age = 10
# password = True

# if age >= 18:
#     if password:
#         print("kirishingiz mumkin")
#     else:
#         print("password yo'q")
# else:
#     print("yosh yetmaydi")

# age = 19
# password = False

# if age >= 18 and password:
#     print("krishingiz mumkin")
# elif age >= 18 and not password:
#     print("password yo'q")
# else:
#     print("yosh yetarli emas")

# x = 8

# if x >= 0:
#     print("musbat")
# elif x == 0:
#     print("Nol")
# else:
#     print("manfiy")

# nums = [1,2,3,4,5]
# i = nums
# for i in range(5):
#     print(i)

# for i in range(10):
#     print(i)

# i = 10
# while i <= 5:
#     print(i)
#     i += 1 

# parol = "1234"
# k = input("Parol kriting: ")

# while k != parol:
#     k =input("Qayta ter ")
# print("Kirdi")
# for i in range(10):
#     if i == 8:
#         break
#     print(i) 

# for i in range(1,15):
#     if i == 3:
#         continue
#     print(i)

# for i in range(100):
#     if i % 2 == 0:
#         print("Juft son", i)
    
# s = 0

# for i in range(1,101):
#     s += i 
# print(s)

# num = [1,3,4,6,-9,1,3,-3,4,2]

# for i in num:
#     if i < 0:
#         print("Musbat sonlar topildi" , i)
#         break

# class animal:
#     def sound(self):
#         print("ovoz chiqaradi")
# class dog(animal):
#     pass

# Dog = dog ()
# Dog.sound()


# class car:
#     def drive(self):
#         print("yuradi")
# class malibu(car):
#     pass


# cars = malibu()
# cars.d

# class Student:
#     def __init__(self, name , surname, ball ):
#         self.name=name
#         self.suname=surname
#         self.ball=ball
#     def baho(self):
#         if self.ball>0:
#             return "Good"
# student = Student("Mirjalol", "Abdulzizov", 28)
# print(student.baho())


# class student:
#     def __init__(self, name,surname,baho):
#         self.name=name
#         self.surname=surname
#         self.baho=baho
#     def check(self):
#         if self.baho <= 80:
#             return "Mirjalol"
#         else:
#             return "Ibrohim"
# talaba = student("Mirjalol","Abdulazizov",90)
# print(talaba.check())
    

# class student:
#     def __init__(self,name,surname,gread):
#         self.name = name
#         self.surname = surname
#         self.gread = gread
#     def bahosi(self):
#         if self.gread >= 80:
#             return "good"
#         else:
#             return "bad"
# talaba = student("Mirjalol", "Abdulazizov", 90)
# print(talaba.bahosi())
        
# class student:
#     def __init__(self,name,baho):
#         self.name = name
#         self.baho = baho
#     def bahosi(self):
#         if self.baho >= 90:
#             return "pass"
# talaba = student ('mirjalol',100)
# print(talaba.bahosi())


# class player:
#     def __init__(self,name,age,position):
#         self.name = name 
#         self.age = age
#         self.position = position

#     def cost(self):
#         if self.position == "struker":
#             return 90000
#         elif self.position == "midle":
#             return 20000
#         else:
#             return 10000
        
# b = player("Mirjalol",18,"struker")
# print(b.cost())

# class Yukmashinaasi:
#     def __init__(self,yuk,km,yuk_narx,narx_km):
#         self.yuk = yuk
#         self.km = km
#         self.yuk_narx = yuk_narx
#         self.narx_km = narx_km
        
        
#     def umimiy(self):
#         y = self.yuk * self.yuk_narx
#         k = self.km * self.narx_km
#         return k + y 
    
# som = Yukmashinaasi (10,100,100,10)
# print(f"Yetkazib berish narxi {som.umimiy()} dollor narxi")

# def qoshish(a , b):
#     natija = a + b
#     return natija

# m = qoshish(2,6)
# print(m)

# def son ( f ,d ):
#     natija = f + d
#     return natija
# javob = son(1,99)
# print(javob)


# class Telefon:
#     def __init__(self,model,ram,xotira):
#         self.model = model
#         self.ram = ram 
#         self.xotira = xotira
        
#     def get_info(self):
#         return f'nomi {self.model} {self.ram} ram {self.xotira} xotira'

# telfon = Telefon ("17 pro max",32,"1 TB")
# print(telfon.get_info())


# class yuk:
#     def __init__(self,km,kg):
#         self.km = km

#         self.kg = kg
#     def info(self):
#         return (self.km * 1000) + (self.kg * 1000)
        
# natija = yuk(10,20)
# print("yetkazib berish narxi", natija.info(), "so'm")


# list = [1,2,3,4,5,55]

# eng_katta = list[0]

# for son in list:
#     if son > eng_katta:
#         eng_katta = son
# print("eng katta", eng_katta,"son")



# class univer:
#     def __init__(self,name):
#         self.name = name
        
#     def son(self):
#         if self.name == "pdp":
#             return "1000 o'quvchi"
#         elif self.name == "amaliy":
#             return "1500 o'qvchi"


#         elif self.name == "tatu":
#             return "2000 o'quvchi"
# natija = univer("pdp")
# print(natija.son())


# class univer:
#     def __init__(self,name):
#         self.name = name 
#     def son(self):
#         if self.name == "pdp":
#             return "3500 o'quvchi"
#         elif self.name == "tatu":
#             return "4000 o'quvchi"
# natija = univer("pdp")
# print(natija.son(),"bor")



# class univer:
#     def __init__(self,name):
#         self.name = name 

#     def son(self):
#         if self.name == "PDP":
#             return "4000 talaba"
#         elif self.name == "TATU":
#             return "5000 talaba"
#         elif self.name == "UBS":
#             return "3000 talaba"
#         else:
#             return "xato name"
# natija = univer("PDP")
# print(natija.son())


class yuk:
    def __init__(self,kg,km):
        self.km = km
        self.kg = kg

    def result(self):
        return (self.km * 1000) + (self.kg * 4000) 

answer = yuk(100,300)        
print("Ydtkazib beish narxi" , answer.result(), "so'm")