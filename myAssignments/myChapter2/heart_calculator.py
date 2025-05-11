
age = int(input("Enter your age: "))

maximumHeartRate = 220 - age

minimumRange = (maximumHeartRate * 50 // 100)

maximumRange = (maximumHeartRate * 85 // 100)

print ("The maximum heart rate is", maximumHeartRate)
print(f"The range is {maximumRange} - {maximumRange}")