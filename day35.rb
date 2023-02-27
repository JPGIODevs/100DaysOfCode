class Animal
    
    String name
    Number number_of_legs
    Number age

    @@num_of_animals = 0
    def initialize(name, number_of_legs, age)
        @animal_name = name
        @animal_legs = number_of_legs
        @animal_age = age
    end

end

BEGIN{
    puts("first begin statement")
}

dog = Animal.new("dog", 4, 12)

