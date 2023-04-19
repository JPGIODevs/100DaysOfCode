use std::collections::HashMap;

//fn init_morse(){}


//fn morse(){}



fn main() {

    //mutable boolean running function
    let mut running: bool = true;
    
    //closest thing to dictionary in python
    let mut scores = HashMap::new();


    //appending to hashmap, all keys must be same type
    //string in this case
    scores.insert(String::from("Blue"),10);
    scores.insert(String::from("Red"),50);

    let morse_expressions: Vec<String> = vec!["...".to_string(), ".._".to_string(), ".__".to_string()];

    //println!("Second element in vec: {}", morse_expressions[".__"]);

    //^ not working yet, i believe vec to be improperly used


}
