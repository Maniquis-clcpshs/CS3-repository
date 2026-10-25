class Patient:
    def __init__(self,name,bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    
    def get_name(self):
        return self.__name
        
    def get_bill_amount(self):
        return self.__bill_amount
        
    def set_name(self,name):
        self.__name=name
        
    def set_bill_amount(self,bill_amount):
        self.__bill_amount = bill_amount
    
    def calculate_bill(self):
        print("Hospital Billing System\n---------------------------")
        print("Patient name: ", self.__name)
        print("Original bill: ₱", self.__bill_amount)
        print("Final bill: ₱", self.__bill_amount)
        
        
class senior_patient(Patient):
    def calculate_bill(self):
        print("Patient name: ", self._Patient__name)
        print("Original bill: ₱", self._Patient__bill_amount)
        print("Final bill: ₱", self._Patient__bill_amount * 0.8)
            
class PhilHealth_patient(Patient):
    def calculate_bill(self):
        print("Patient name: ", self._Patient__name)
        print("Original bill: ₱", self._Patient__bill_amount)
        print("Final bill: ₱", self._Patient__bill_amount * 0.85)
    
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = senior_patient("Maria Santos", 15000)
philhealthpatient = PhilHealth_patient("Pedro Reyes", 15000)
    
regular_patient.calculate_bill()
senior_patient.calculate_bill()
philhealthpatient.calculate_bill()
    
    
    
    
    
    
    
    
    
    
    
    
    