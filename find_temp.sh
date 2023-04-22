#!/bin/bash
for((T=1; T<=20; T+=1)); do
    python3 test_classification.py --log_dir pointnet2_cls_ssg --num_category 10 --T $T
done