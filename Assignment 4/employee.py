
class Employee:

    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + self.__id_number + \
               "\nDepartment: " + self.__department + \
               "\nJob Title: " + self.__job_title