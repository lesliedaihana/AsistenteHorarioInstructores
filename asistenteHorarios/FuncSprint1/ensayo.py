class Person(object):
    country = "China"

    @classmethod
    def countryinfo(cls):
        pass

    @classmethod
    def changecountry(cls,newcountry):
        cls.country = newcountry
        print ('La nacionalidad en este momento es:', cls.country)

    def init(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

#if __name__ == '__main__':
