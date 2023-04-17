#!/bin/bash
for((T=100; T<=1000; T+=50)); do
    python3 test_classification.py --log_dir pointnet2_cls_ssg --num_category 10 --T $T
done