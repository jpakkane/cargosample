# Demo project to compile Crate dependencies with Meson

This project builds a Rust program that uses the
[itoa crate](https://github.com/dtolnay/itoa). It uses Cargo but
this script downloads and converts it on the fly to build
and integrate with Meson instead.

To run it do the following:

```shell
./get_cargo_deps.py itoa 0.3.4
meson build
ninja -C build
build/prog
```

Running the final program should give you the following output:

```shell
Converted number: [49, 50, 56]
```
