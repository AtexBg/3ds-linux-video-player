#!/bin/sh

while :
do
    i=1
    while [ -f bin_frames/$i.bin ]; do
        cat bin_frames/$i.bin > /dev/fb0 #load each frame into framebuffer
        sleep 0.05 
        i=$((i + 1))
    done
done