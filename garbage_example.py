class Employee:
    def __init__(self):
        print('Ctor called, Employee created')
    
    def __del__(self):
        print('Dtor called, Employee deleted')

obj = Employee()
#obj = 1

print('End of program')