class Patient:
  def __init__(self, name, age,sex, bmi, children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = children
    self.smoker = smoker

  def patient_profile(self):
    patient_information = {}
    patient_information['name'] = self.name 
    patient_information['age'] = self.age 
    patient_information['sex'] = self.sex 
    patient_information['bmi'] =self.bmi 
    patient_information['children'] = self.num_of_children
    patient_information['smoker']= self.smoker
    return patient_information

  def update_age(self,new_age):
    self.age = new_age
    print('{P} is now {a} years old.'.format(P = self.name, a= self.age))
    return self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print('{p} has {n} child.'.format(p=self.name, n=self.num_of_children))
    else:
      print('{p} has {n} children.'.format(p=self.name, n=self.num_of_children))
    return self.estimated_insurance_cost()
  
  def estimated_insurance_cost(self):
    self.estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 1250
    print('{P}\'s estimated insurance cost is {e} dollars.'.format(P = self.name, e = self.estimated_cost))

patient1 = Patient('John Doe', 25,1,22.2,0,0)
print(patient1.name)
patient1.estimated_insurance_cost()

patient1.update_age(26)
patient1.update_num_children(1)

print(patient1.patient_profile())

    
