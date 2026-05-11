import json
import os

class GradeManager:
    def __init__(self,filename="grades.json"):
        self.filename = filename
        self.students = self.load_data()
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as f:
                return json.load(f)
            
        return {}
    
    def save_data(self):
        with open(self.filename,"w") as f:
            json.dump(self.students,f,indent=4)
    
    def add_student(self,name,grade):
        self.students[name] = grade
        self.save_data()
    def get_grade(self,name):
        return self.students.get(name,"Student not found")
    def delete_student(self,name):
        if name in self.students:
            del self.students[name]
            self.save_data()
        else:
            return "Student not found"
    def list_students(self):
        return self.students
if __name__ == "__main__":
    manager = GradeManager()
    manager.add_student("Alice",85)
    manager.add_student("Bob",90)
    print(manager.get_grade("Alice"))
    print(manager.list_students())
    manager.delete_student("Bob")
    print(manager.list_students())
    