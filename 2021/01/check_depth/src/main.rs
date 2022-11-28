use std::fs;

fn main() {
    let contents = fs::read("depth_readings.txt")
        .expect("Should have been able to read this file");

    println!("Contents of file is:\n{contents}");
}
