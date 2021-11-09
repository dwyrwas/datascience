# Add your code here
medical_costs ={} 
medical_costs["Marina"] = 6607.0
medical_costs['Vinay'] = 3225.0
medical_costs.update({'Connie': 8886.0, 'Isaac':16444.0, 'Valentina': 6420.0})
print(medical_costs)
medical_costs['Vinay'] = 3325.0
print(medical_costs)
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
average_cost = total_cost/len(medical_costs)
print('Average Insurance Cost: {average_cost}'.format(average_cost=average_cost))
# list comprehension to dictionary
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)
marina_age = names_to_ages.get('Marina', None)
print('Marina\'s age is {marina_age}'.format(marina_age=marina_age))
medical_records = {}
medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records.update({'Vinay':{'Age':24, 'Sex':'Male','BMI':26.9, 'Children':0, 'Smoker':'Non-Smoker','Insurance_cost':3225.0}, 'Connie': {'Age':43, 'Sex':'Female','BMI':25.3, 'Children':3, 'Smoker':'Non-Smoker','Insurance_cost':8886.0}, 'Isaac':{'Age':35, 'Sex':'Male','BMI':20.6, 'Children':4, 'Smoker':'Smoker','Insurance_cost':16444.0}, 'Valentina':{'Age':52, 'Sex':'Female','BMI':18.7,'Children':1, 'Smoker':'Non-Smoker','Insurance_cost':6420.0}})
print(medical_records)
connie_cost = medical_records['Connie'].get('Insurance_cost')
print('Connie\'s insurance cost is {x} dollars.'.format(x=connie_cost))
medical_records.pop('Vinay')
for customer, value in medical_records.items():
  Name = customer
  Age = customer['Age']
  print('{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}'.format(Name = 'Name')) 
