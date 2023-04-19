#class stuff, see how much easier it is compared to rust?
class Person():
    
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby


def main():


    age = 19
    name = "Jack Gio"
    hobby = "Powerlifting"

    jp = Person(name, age, hobby)

    print(f"name is {jp.name}, age of {jp.age}yrs and hobby is {jp.hobby}")


main()

