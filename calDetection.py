from calMetric import detection


in_soft_file = "./softmax_scores/confidence_Our_In_" + str(7500) + "_" + str(0.0) + "_.txt"
out_soft_file = "./softmax_scores/confidence_Our_Out_" + str(7500) + "_" + str(0.0) + "_.txt"
detection_error = detection(in_soft_file, out_soft_file)
print(detection_error)