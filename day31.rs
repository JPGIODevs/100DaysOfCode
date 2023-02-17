fn said_10_times(saying: String){

    for n in 1..11{

        println!("{saying} said {n} times");
    }

}


fn main(){

    said_10_times(String::from("I made a tauri app earlier, will be on github soon :)"));

}