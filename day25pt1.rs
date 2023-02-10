
fn said_ten_times(input_word: String){

    for n in 1..10{

        println!("{input_word} said {n} times");
    }

}


fn main() {

    let list_of_stuff = vec!["tree", "oinge", "boberry"];

    for element in list_of_stuff.iter(){
        println!("{}",element);
    }


    said_ten_times("frog".to_string())
    
}
