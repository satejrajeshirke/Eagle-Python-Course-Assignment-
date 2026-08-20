"""
1. Create a Student Management System using Class and Object in Python. 
What to Do
 1. Create a class named Student.
 2. Create a constructor __init__() to initialize:  o Student name  o Roll number  o Age  o Marks of 3 subjects  
 3. Create a display_details() method to display all student information.  
 4. Create a calculate_total() method to calculate the total marks.  
 5. Create a calculate_percentage() method to calculate the percentage.  
 6. Create a check_result() method:  o Student passes if marks in every subject are 35 or above.  o Otherwise, display FAIL. 
 7. Create an update_marks() method to update the marks of a selected subject.  

"""

class Student:
    def __init__(self,name=" ",roll_no=0,age=0,sub1=0,sub2=0,sub3=0):
        self.Student_name=name
        self.Roll_number=roll_no
        self.age=age
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def menu(self):
        print("1.Please Enter 1 add Information")
        print("2.Please Enter 2 display Information")
        print("3.please Enter 3 To Calculate Total")
        print("4.please Enter 4 To Calculate Percentage")
        print("5.Student passes if marks in every subject are 35 or above or fail")
        print("6.Update marks of subjects")

        self.Choice=int(input("Enter Your Choice"))

        match self.Choice:
            case 1:
                self.get_info()

            case 2:
                self.dis_info()

            case 3:
                self.cal_total()

            case 4:
                self.cal_percentage()

            case 5:
                self.check_res()

            case 6:
                self.update_marks()

        

    def get_info(self):
        self.Student_name=input("Please Enter Your Name")
        self.Roll_number=int(input("Enter Roll Number"))
        self.age=int(input("Enter Age:"))
        self.sub1=int(input("Enter Marks Of Subject 1"))
        self.sub2=int(input("Enter Marks Of Subject 2"))
        self.sub3=int(input("Enter Marks Of Subject 3"))

        self.menu()


    def dis_info(self):
        print("Student Name:,",self.Student_name)
        print("Student Roll Number:",self.Roll_number)
        print("Student Age:",self.age)
        print("Subject 1 marks:",self.sub1)
        print("Subject 2 Marks:",self.sub2)
        print("Subject 3 Marks:",self.sub3)

        self.menu()

    def cal_total(self):
        total=self.sub1+self.sub2+self.sub3

        print("Total Of the Three Subjectsis:",total)

        self.menu()

    def cal_percentage(self):
        total=self.sub1+self.sub2+self.sub3
        percentage = (total / 300) * 100
        print("Percenatge:",percentage)

        self.menu()

    def check_res(self):
        if self.sub1 >=35 and self.sub2 >=35 and self.sub3 >=35:
            print("Stundet Is Passed")
        else:
            print("Student is failed")

        self.menu()


    def update_marks(self):
        self.sub1=int(input("Enter Subject 1 new Marks"))
        self.sub2=int(input("Enter subject 2 new Marks"))
        self.sub3=int(input("Enter new subject 3 marks"))

        self.menu()

    

    


obj=Student()
obj.menu()

