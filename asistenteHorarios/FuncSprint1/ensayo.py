class Person:
    @classmethod
    def datos(cls,name,age,gender):
        cls.name = name
        cls.age = age
        cls.gender = gender

    country = "Venezuela"
    name = "Juana"
    age = int(20)
    gender = "Femenino"

    @classmethod
    def countryinfo(cls):
        pass

    @classmethod
    def changecountry(cls,newcountry):
        cls.country = newcountry
        print ('La nacionalidad en este momento es:', cls.country)




#if __name__ == '__main__':
