fn main(){

    enum DogBreed{
        Pug(String),
        Husky(String),
        Lab(String),
    }

    struct Dog {

        breed: DogBreed,
        name: String,

    }

    let nelly = Dog{
        breed: DogBreed::Pug(String::from("Pug")),
        name: String::from("Nelly"),
    };

   
    println!("{}", nelly.name);
}