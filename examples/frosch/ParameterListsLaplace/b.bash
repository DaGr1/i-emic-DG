#!/bin/bash

for i in {1..5}
do
    result=$(mpirun -np 4 ~/Documents/BEP/i-emic-DG/build/src/main/run_frosch_laplace --M=200 --O=6 2>/dev/null | \
    grep "Thyra Laplace Test" | awk '{print $4}')

    echo -n "$result " >> output.txt
done

echo >> output.txt
