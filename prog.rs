extern crate itoa;

fn main() {
    // write to a vector or other io::Write
    let mut buf = Vec::new();
    let result = itoa::write(&mut buf, 128u64);
    match result {
        Err(e) => {
            println!("Could not convert number: {}", e);
        }
        Ok(_f) =>  {
            println!("Converted number: {:?}", buf);
        }
    }
}
