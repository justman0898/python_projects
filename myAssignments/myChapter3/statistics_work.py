import statistics

sample_data = [9, 11, 22, 34, 17, 22, 34, 22, 40]
mean_value = statistics.mean(sample_data)
median_value = statistics.median(sample_data)
mode_value = statistics.mode(sample_data)

print(f"The mean is {mean_value}, the median is {median_value}, and the mode is {mode_value}")