#!/bin/bash


for i in {1..30}; do

    filename="${i}.jpg"
    filenameSH="${i}.sh"
    

    if [[ -f "$filename" ]]; then
        file "$filename"
        #xxd "$filename"
        #exiftool "$filename"
        #chmod +x "$filename" 

    else   
        echo "File not found: $filename"
    fi

    ./"${filenameSH}"
done
