import calMetric
for T in range(100, 1000, 100):
    metric_path = "./metrics/met_" + str(T) + "_" + str(0.0014) + "_" + ".txt"
    in_path = in_path = "./softmax_scores/confidence_Our_In_" + str(T) + "_" + str(0.0014) + "_" + ".txt"
    out_path = "./softmax_scores/confidence_Our_Out_" + str(T) + "_" + str(0.0014) + "_" + ".txt"
    print(in_path, out_path, metric_path)
    met_out = calMetric.detection(in_path, out_path)
    with open(metric_path, "w") as f:
        f.write("Detection error:" + str(met_out))