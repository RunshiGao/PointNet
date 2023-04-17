#!/bin/bash
out_file="out.txt"
for((T=1000; T<=2000; T+=100)); do
    py_out=$(python3 calMetric.py)
    echo "$T, $py_out" >> $out_file
done