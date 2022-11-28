use std::fs;

fn main() {
    let contents = fs::read_to_string("depth_readings.txt")
        .expect("Should have been able to read this file");

    println!("File Contents:\n{contents}");
}
