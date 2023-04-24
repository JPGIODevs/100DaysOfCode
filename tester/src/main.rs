fn main() {

    //let days = vec![36,37,38,39,40,41..83];
    // ^ deprecated :)
    let days: Vec<u32> = (36..83).collect();
      //CHANGE THIS FOR OMISSIONS

    for n in days{
        println!("Day {n} was ommited as I was pushing to other projects!");
    }
}
