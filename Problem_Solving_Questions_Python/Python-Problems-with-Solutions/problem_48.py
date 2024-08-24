'''Create a class “Programmer” for storing information of few programmers
working at Microsoft.'''

class progammer :
    def __init__(self, name ,employee_id , language):
        self.name = name 
        self.employee_id = employee_id
        self.language = language

    def get_details(self):
        return f"Programmer Name : {self.name} ,Employee ID  : {self.employee_id , Language : {self.language}}"    
