struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}

fn main(){
    let user1 = User {
        active: true,
        username: String::from("jackygmp"),
        email: String::from("marzy.m.p@gmail.com"),
        sign_in_count: 1,
    };

    let user2 = build_user(String::from("emailz"), String::from("username2"));

    println!("{}", user1.email);

}