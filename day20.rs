#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
    hobby: String
}

fn main() {
    let age: u8 = 19;
    let jp = Person{
        name: String::from("Jack Gio"),
        age,
        hobby: String::from("powerlifting"),

    };

    dbg!(&jp);
    println!("{:?}", jp);
}
