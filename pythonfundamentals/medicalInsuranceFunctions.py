# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  #return "The estimated insurance cost for " + name +" is " + str(estimated_cost) + " dollars."
  return estimated_cost
# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0) 
# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)
# Estimate your own insurance cost
duncan_insurance_cost = calculate_insurance_cost("Duncan", 25, 1, 22.1, 0, 0)

def calculate_cost_difference(num1, num2):
  difference = num1 - num2
  print("The difference in insurance cost is "+str(difference)+" dollars." )
  return difference
difference1 = calculate_cost_difference(maria_insurance_cost, omar_insurance_cost)
