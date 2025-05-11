import statistics

sample_data = [9, 11, 22, 34, 17, 22, 34, 22, 40]
mean = statistics.mean(sample_data)
median = statistics.median(sample_data)
mode = statistics.mode(sample_data)

print(f"The mean is {mean}, the median is {median}, and the mode is {mode}")