# create the initial variables below
# age: age of the individual in years 
age = 28
# sex: 0 for female, 1 for male*
sex = 0
# bmi: individual's body mass index
bmi = 26.2
# num_of_children: number of children the individual has
num_of_children = 3
# smoker: 0 for a non-smoker, 1 for a smoker
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500


# print insurance cost estimate
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# Age Factor
age += 4

# New Insurance cost with added age
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

#calculate the difference in insurance costs
change_in_insurance_cost = new_insurance_cost - insurance_cost

#print the change in cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")
# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# Male vs. Female Factor 
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + ' dollars.')
# Extra Practice
sex = 0
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being a smoker instead of a non-smoker is " + str(change_in_insurance_cost) + ' dollars.')
