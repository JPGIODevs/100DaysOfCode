use std::io;

fn main() {

    let maybe: bool = false;
    let months = [1,2,3,4,5];
    let number = if maybe {0} else {999};

    println!("Enter a number 1-5: \n");

    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("incorrect input");

    let input: usize = input
        .trim()
        .parse()
        .expect("no number entered"); 

    let chosen_num = months[input];

    if chosen_num < 3{
        println!("Chosen number is lower than 3");
    } else if chosen_num > 3{
        println!("Chosen number is greater than 3");
    } else {
        println!("What did you chose?? {chosen_num}??")
    }

    println!("You have chose {chosen_num}");    

    //cba to type this again lol \/
    //let test_num: u32 = input.trim().parse().expect("Not a number");

    other_function("hello", number);

}

fn other_function(input: &str, maybe: i32){

    println!("other function called, string is {input} and maybe number is {maybe}");

}