fn main(){

    // simple while loop using iterating i variable and a comparison to vector length
    let traits = vec!["fear", "anger", "envy", "hate"];
    let mut i = 0;

    while i < traits.len(){
        println!("i: {}, item: {}", i, traits[i]);
        i += 1;
    }

    //using iterators removes need to use or track iterator variables such as i :)
    let traits_iter = traits.iter();

    for item in traits_iter{
        println!("item: {}", item);
    }

    let nums = vec![1,2,3];

    let x = nums.iter()
        .map(|x| x + 1)
        .filter(|x| *x > 2);
    let y: Vec<i32> = x.collect();
}
