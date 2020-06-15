class People:
    __id1 = 0
    __name = ""
    __age = 0

    def __init__(self, id1, name, age):
        self.__id1 = id1
        self.__name = name
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def __getAge(self):
        return self.__age


class Chinese:
    __language = "chinese"
    __feature = "chopsticks"
    __a = 0

    def __init__(self, a):
        self.__a = a

    def getLanguage(self):
        return self.__language

    def getFeature(self):
        return self.__feature

    def getA(self):
        return self.__a


class Germany:
    __language = "german"
    __feature = "fork"

    def getLanguage(self):
        return self.__language

    def getFeature(self):
        return self.__feature


class Student(People, Chinese):
    __school = ""

    def __init__(self, id1, name, age, school, a):
        People.__init__(self, id1, name, age)
        Chinese.__init__(self, a)
        self.__school = school

    def getSchool(self):
        return self.__school


class Worker(People, Germany):
    __site = ""

    def __init__(self, id1, name, age, site):
        super().__init__(id1, name, age)
        self.__site = site

    def getSite(self):
        return self.__site


if __name__ == "__main__":
    student = Student(1, "xfk", 20, "cuiYun", 999)
    worker = Worker(2, "dfk", 35, "yuBei")
    print(student.getName())
    print(student.getSchool())
    print(student.getLanguage())
    print(student.getFeature())
    print(student.getA())
    print(worker.getName())
    print(worker.getSite())
    print(worker.getLanguage())
    print(worker.getFeature())
