from abc import ABC, abstractmethod


class Library:
    def __init__(self):
        self.__member = []
        
    def add_member(self,mem):
        self.__member.append(mem)

    def get_member(self):
        return self.__member


class Member:
    
    def __init__(self,name,id,contact):
        self.__name = name
        self.__id = id
        self.__contact = contact

    def add_member(self , lip):
        lip.add_member(self)
    
    def search_member(self , lip):
        mem_list = lip.get_member()
        for mem in mem_list:
            if mem == self:
                return self
        print('ไม่พบข้อมูล')
       

class Publication(ABC):
     
     def __init__(self , title , author, year):
         self.__title = title
         self.__author = author
         self.__year = year

         

     @abstractmethod
     def method(self):
        pass


class Book(Publication):

    def __init__(self, title, author, year , isbn , genre):
        super().__init__(title, author, year)
        self.__isbn = isbn
        self.__genre = genre

class Loan:
    def __init__(self , member , publication , borrowing_date , due_to):
        self.__member = member
        self.__publication = publication
        self.__borrowing_date = borrowing_date
        self.__due_to = due_to