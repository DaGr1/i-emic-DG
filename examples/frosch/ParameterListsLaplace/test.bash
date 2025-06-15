#!/bin/bash

target="ParameterList.xml"

for file in *.xml; do
    if [[ "$file" != "$target" ]]; then
        echo "Replacing $target with contents of $file"
        cp "$file" "$target"
        sleep 1 
    else
	echo "before"
	continue  
    fi
    echo "after"
done

