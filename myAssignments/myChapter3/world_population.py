# World population estimated to be 8.2 billion people
# Growth rate of around 0.85%

current_population = 8_200_000_000
growth_rate = 0.85 / 100
percentage_growth = 0
growth = 0

for years in range (1, 101):
	percentage_growth = current_population * growth_rate 
	growth = current_population + percentage_growth
	print(f"Population growth at the end of year {years} is {percentage_growth:,.2f}")
	current_population = growth