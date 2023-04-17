#!/bin/bash
for((i=1; i<=20; i++)); do
    T=$(bc <<< "scale=4; 0.0002 + ($i-1)*0.0002")
    python3 test_classification.py --log_dir pointnet2_cls_ssg --num_category 10 --T 20 --noiseMagnitude $T
done