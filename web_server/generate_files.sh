#! /bin/bash

for n in {0..2047}; do
    dd if=/dev/urandom of=./static/image_$n.png bs=2M count=1
done
