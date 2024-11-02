#!/bin/bash

for i in {1..30}; do

    filename="${i}.jpg"
    
    

    if [[ -f "$filename" ]]; then
        strings "$filename"
    else   
        echo "File not found: $filename"
    fi


done
