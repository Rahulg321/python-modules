 

class Employee:
    raise_amt = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def fullname(self):
        return f'{self.first}.{self.last}'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'
    
    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"
    

# emp_1 = Employee('Lin','Dan', 98000)
# emp_2 = Employee('norman', 'sandhu', 845623)


# print(emp_1)

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname)

