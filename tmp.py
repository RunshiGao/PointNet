import calMetric
def main(mag):
    for T in range(1,2):
        metric_path = "./metrics/met_" + str(T) + "_" + str(mag) + "_" + ".txt"
        in_path = in_path = "./softmax_scores/confidence_Our_In_" + str(T) + "_" + str(mag) + "_" + ".txt"
        out_path = "./softmax_scores/confidence_Our_Out_" + str(T) + "_" + str(mag) + "_" + ".txt"
        print(in_path, out_path, metric_path)
        met_out = calMetric.metric(in_path, out_path)
        with open(metric_path, "w") as f:
            f.write(met_out)
def mag():
    T = 20
    for mag in [round(0.0001 * i, 4) for i in range(0,40,2)]:
        metric_path = "./metrics/met_" + str(T) + "_" + str(mag) + "_" + ".txt"
        in_path = in_path = "./softmax_scores/confidence_Our_In_" + str(T) + "_" + str(mag) + "_" + ".txt"
        out_path = "./softmax_scores/confidence_Our_Out_" + str(T) + "_" + str(mag) + "_" + ".txt"
        print(in_path, out_path, metric_path)
        met_out = calMetric.metric(in_path, out_path)
        with open(metric_path, "w") as f:
            f.write(met_out)
mag()