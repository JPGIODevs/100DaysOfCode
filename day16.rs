// importing standard io library
use std::io;
use std::cmp::Ordering;
use rand::Rng;

//define special main function
fn main() {

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is {secret_number}");

    //forever loop, super simple
    loop{

    
        println!("Guess the number");
        println!("Enter a guess: ");

        //creating mutable "guess" variable, of the type String(utf8)
        //the ::new syntax indicates a new empty string variable
        let mut guess = String::new();

        //calling io library, can call via std::io::stdin if not imported
        //calling io library, function stdin which is "standard IO in".
        io::stdin()
            //read_line method is called, the &mut guess indicates the arguement
            //responsible for variable location, which read_line writes to
            .read_line(&mut guess)
            .expect("Failed to read line");
            //^^ standard expect, rails function

        //A very wordy way of converting a string to an unsigned 32bit integer
        //unsigned meaning positive numbers only
        //trim removes whitespace, parse converts to alternate type (string to int asked)
        let guess: u32 = match guess.trim().parse(){
            Ok(num) => num,
            Err(_) => continue,
        };
        //^^ used another instance of match to create arms for comparison to ensure safe 
        //error handling

        //basically switch-case, match and its "arms" compares located arguement to arms
        match guess.cmp(&secret_number){
            //using ^cmp from standard libraries, using ordering enum to create instance to compare arguement
            Ordering::Less => println!("too small"),
            Ordering::Greater => println!("too large"),
            Ordering::Equal => {
                println!("Guessed correct!");
                break;
            }
        }
    }
    //println!("you guessed: {guess}")

}
