from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# สร้างคลาส Publication เป็น abstract class
class Publication(ABC):
    #  กำหนด property ต่างๆ
     def __init__(self , title , author, year):
         self.__title = title
         self.__author = author
         self.__year = year

     def get_title(self):
         return self.__title
     def get_author(self):
         return self.__author
     
     def set_title(self,title):
         self.__title = title
     
     def set_author(self,author):
         self.__author = author
    
     def set_year(self,year):
         self.__year = year
    
     def get_year(self):
         return self.__year

    # abstractmethod ต่างๆเพื่อให้คลาสลูกมี method นี้
     @abstractmethod
     def display_detail(self):
        raise NotImplementedError("Subclasses must implement display_detail method.")
     
     
     @abstractmethod
     def search_item(self,lip):
        raise NotImplementedError("Subclasses must implement search_item method.")
     
     @abstractmethod
     def update_item(self,lip):
        raise NotImplementedError("Subclasses must implement update_item method.")

# คลาส library
class Library:
    def __init__(self):
        self.__member = []
        self.__publication = []
        self.__loan = []
    # เพิ่ม member
    def add_member(self,mem):
        for mem_lib in self.__member:
            if mem_lib.get_id() == mem.get_id():
                return False
        self.__member.append(mem)
        return True

    def get_member(self):
        return self.__member
    
    def get_publication(self):
        return self.__publication
    
    def add_publication(self,pub):
        for pub_lip in self.__publication:
            if pub_lip.get_isbn() == pub.get_isbn():
                return False
        self.__publication.append(pub)
        return True
        
    
    def get_publication(self):
        return self.__publication

    def remove_publication(self,pub):
        self.__publication.remove(pub)

    def search_member(self , id):
         mem_list = self.__member
         for mem in mem_list:
             if mem.get_id() == id:
                 return mem
         return False
    
    def search_book(self , title , author , genre):
        pub_list = self.__publication
        for pub in pub_list:
            if pub.get_title() == title and pub.get_author() == author and pub.get_genre() == genre:
                return pub
        return False
    
    def search_book_isbn(self , isbn):
         print(isbn)
         pub_list = self.__publication
         for pub in pub_list:
            print(pub.get_isbn())
            if pub.get_isbn() == isbn:
                return pub
         return False
    
    def add_loan(self , loan):
        self.__loan.append(loan)

    def get_loan(self):
        return self.__loan

    def search_loan(self , mem , pub):
        loan_list =  self.__loan 
        for loan in loan_list:
            if loan.get_member() == mem and loan.get_publication().get_isbn() == pub:
                return loan
        return False
    
    def remove_loan(self ,loan):
        self.__loan.remove(loan)

    def get_most_popular(self):
        pub_list = self.__publication
        if len(pub_list) > 0:
            max_rating = max(pub_list, key=lambda pub: pub.get_rating()).get_rating()
            pub_most = [pub for pub in pub_list if pub.get_rating() == max_rating]
            return pub_most
        return []




# class Member
class Member(Publication):
    # กำหนด property ต่างๆ
    def __init__(self,name,id,contact):
        self.__name = name
        self.__id = id
        self.__contact = contact

    
    def search_item(self , lip):
        mem_list = lip.get_member()
        if self in mem_list:
                return self.display_detail()
        print('ไม่พบข้อมูล')

    def display_detail(self):
         print(f'name : {self.__name}\n id : {self.__id}\n contact : {self.__contact}')
         message = f'name : {self.__name}\n id : {self.__id}\n contact : {self.__contact}'
         return message

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact
    
    def update_item(self,name,contact):
        if name and contact:
            self.__name = name
            self.__contact = contact
        else : 
            print('update ไม่สำเร็จ')
        
    def get_id(self):
        return self.__id
# class Book
class Book(Publication):

    def __init__(self, title =None, author=None, year=None , isbn=None , genre=None):
        super().__init__(title, author, year)
        self.__isbn = isbn
        self.__genre = genre
        self.__rating = 0
        
    def search_item(self,lip):
        pub_list = lip.get_publication()
        if self in pub_list:
            return self.display_detail()
        else:
            print('ไม่พบหนังสือที่ท่านต้องการ')
       
    def display_detail(self):
        message = f'title : {super().get_author()}\nauthor : {super().get_title()}\ngenre : {self.__genre}'
        return message

    def set_genre(self,genre):
        self.__genre = genre

    def update_item(self,title,author,genre):
        super().set_title(title)
        super().set_author(author)
        self.set_genre(genre)

    def set_book(self,book):
        self = book

    def get_genre(self):
        return self.__genre
    
    def get_isbn(self):
        return self.__isbn
    
    def get_author(self):
        return super().get_author()
    
    def get_title(self):
        return super().get_title()
    
    def get_year(self):
        return super().get_year()
    
    def get_rating(self):
        return self.__rating
    
    def add_rating(self):
        self.__rating += 1
        
    

class Loan:
    def __init__(self , member , publication , borrowing_date , due_to):
        self.__member = member
        self.__publication = publication
        self.__borrowing_date = borrowing_date
        self.__due_to = due_to

    def display_detail(self):
        print(f'member : {self.__member.display_detail()}\n -- -- -- \npublication : {self.__publication.display_detail()}\n -- -- -- \nborrowing_date : {self.__borrowing_date}\n -- --- --\ndue to : {self.__due_to}')

    # method ยืมหนังสือ ถ้าหนังสื่อมีใน lib จะสามารถยืมได้
    def loan_book(self,lip):
        pub_list = lip.get_publication()
        if self.__publication in pub_list:
            lip.remove_publication(self.__publication)
            lip.add_loan(self)
            self.__publication.add_rating()
            message ='Loan successfully'
            return message
        else:
             message ='Failed to loan'

    # คินหนังสือกลับ lib 
    def return_booK(self,lip):
        lip.add_publication(self.__publication)
        lip.remove_loan(self)
        print('คืนสำเร็จ')

    def get_member(self):
        return self.__member
    
    def get_publication(self):
        return self.__publication
    
    def get_borrow_date(self):
        return self.__borrowing_date
    
    def get_due_date(self):
        return self.__due_to
    
   

# # สร้าง object library 
# Library1 = Library()
# #  สร้าง object user
# user1 = Member('jack' , 1 , '++0985154')
# user2 = Member('goat' , 2 , '++8548156')
# user3 = Member('jojo' , 3 , '++4515312')


# #  สร้าง book
# book1 = Book('harry' ,'micheal' ,1997 ,'105g' ,'avenger')
# book2 = Book('spider_man' ,'jack dobson' ,1989 ,'fg45' ,'comic')
# book3 = Book('titanic' ,'duchman' ,2001 ,'dds4' ,'drama')


# # เพื่มสมาชิก 
# user1.add_item(Library1)
# user2.add_item(Library1)

# # ค้นหา สมาชิก ที่เป็น member
# user1.search_item(Library1)
# # ค้นหา สมาชิก ที่ไม่เป็น member
# user3.search_item(Library1)

# # แสดงข้อมูล
# user1.display_detail()
# # อัพเดทข้อมูล
# user1.update_item('pep','++888221')




# # เพิ่ม book
# book1.add_item(Library1)
# book2.add_item(Library1)


# # ค้นหา book ใน lip
# book1.search_item(Library1)

# # ค้นหา book ที่ไม่มีใน lip
# book3.search_item(Library1)

# # แสดงข้อมูล book 
# book1.display_detail()
# # อัพแดท  book 
# book1.update_item('jurassic','arthur' , 'comic')


# # สร้าง object loan
# loan1 = Loan(user1,book1 , current_time , seven_days_later)
# loan2 = Loan(user2 , book1 , current_time, seven_days_later)
# # ยืมหนังสือที่หนังสือมีอยูในระบบ
# loan1.loan_book(Library1)
# # ยืมหนังสือที่ไม่มีหนังสือมีอยูในระบบ
# loan2.loan_book(Library1)
# # คืนหนังสือ 
# loan1.return_booK(Library1)
# # loan2 ยืมต่อ
# loan2.loan_book(Library1)

