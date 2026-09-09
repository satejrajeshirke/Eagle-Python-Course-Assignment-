"""
2. Create a Library Management System using Class and Object in Python. 
What to Do
1. Create a class named Book.  
2. Create a constructor __init__() to initialize:  o Book name  o Book ID  o Author name  o Availability status
3. Create a display_book() method to display book details.
4. Create a issue_book() method: 
      o Check whether the book is available.  
      o If available, issue the book and change its status.  
      o If already issued, display an appropriate message. 
5. Create a return_book() method:  o Return the issued book.  o Change its availability status back to available.
6. Create a check_availability() method to display whether the book is available or issued. 
"""

class Book:
    def ___init__(self,name=" ",id=0,auth_name=" ",avl_status=True):
        self.Book_name=name
        self.Book_id=id
        self.author_name=auth_name
        self.availability_statuz=avl_status


    def dis_play_book():
        
        
        
