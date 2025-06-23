#!/bin/bash

target="ParameterList.xml"
> Data.txt

for file in *.xml; do
    if [[ "$file" != "$target" ]]; then
        echo "Replacing $target with contents of $file"
        cp "$file" "$target"
        sleep 1
    else
        continue
    fi

    > output.txt
    for i in {0..10}; do
        echo --O=$i >> output.txt
        for j in {1..2}; do
            # Run the simulation and extract iteration count
            iterations=$(mpirun -np 4 ~/Documents/BEP/i-emic-DG/build/src/main/run_frosch_laplace --M=10 --O=$i 2>/dev/null | \
                grep -Eo 'returned a solve status.*in [0-9]+ iterations' | \
                grep -Eo '[0-9]+' | tail -1)

            # Handle cases where grep doesn't find the pattern
            if [[ -z "$iterations" ]]; then
                iterations="N/A"
            fi

            echo -n "$iterations " >> output.txt
        done
        echo >> output.txt
    done

    echo "$file" >> Data.txt
    cat output.txt >> Data.txt
done

