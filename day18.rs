fn main() {

    //running parameters for giggles, mutable counter, an array and 
    //an 8bit signed integer 
    let mut counter = 0;
    let array = [10,20,30,40,50];
    let condition: i8 = 5;

    //variable definition defined by a condition, fancy!
    let number = if condition == 5 {5} else {999};

    if number == 5{
        println!("Number is 5");
    } else {
        println!("Number is not 5");
    }

    //a counter loop that returns the count of 10 * 2
    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("{counter} and result {result}");

    //iterating through the array array (nice i know) and printing current element
    for element in array{
        println!("current element is {element}");
    }

    //iterating through numbers 0 to 11 in reverse (hence .rev()) and printing each 
    for number in (0..11).rev(){
        println!("{number}!");
    }
    println!("blast off!!!");

}
