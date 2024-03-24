pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

def population_after_n_years(pop, rate, n):
  for i in range(n):
    pop = pop + pop * rate
  return pop

def maximum_population(pop, rates):
  max_pop = 0
  max_year = 0
  previous_pop = 0
  max_iterations = 10000  
  current_year = int(input())
  for i in range(len(pop)):
    current_pop = population_after_n_years(pop[i], rates[i], current_year)
    total_pop = sum(pop[:i+1]) + current_pop
    if total_pop > max_pop:
      max_pop = total_pop
      max_year = current_year
    elif total_pop < previous_pop:
      
      break
    else:
      previous_pop = total_pop
      current_year += 1
    if current_year > max_iterations:  
      break
  return (max_year, max_pop)


current_total_pop = sum(pop)
print("Current total population:", current_total_pop)


rates = [0.025]
for i in range(1, len(pop)):
  rates.append(rates[i-1] - 0.004)
max_year, max_pop = maximum_population(pop, rates)
print("Years to reach maximum population:", max_year)
print("Maximum population:", max_pop)
