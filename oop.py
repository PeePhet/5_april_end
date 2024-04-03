from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Publication(ABC):
     
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

     @abstractmethod
     def display_detail(self):
        raise NotImplementedError("Subclasses must implement display_detail method.")
     
     @abstractmethod
     def add_item(self,lip):
        raise NotImplementedError("Subclasses must implement add_item method.")
     
     @abstractmethod
     def search_item(self,lip):
        raise NotImplementedError("Subclasses must implement search_item method.")
     
     @abstractmethod
     def update_item(self,lip):
        raise NotImplementedError("Subclasses must implement update_item method.")

     
class Library:
    def __init__(self):
        self.__member = []
        self.__publication = []
        
    def add_member(self,mem):
        self.__member.append(mem)

    def get_member(self):
        return self.__member
    
    def get_publication(self):
        return self.__publication
    
    def add_publication(self,pub):
        self.__publication.append(pub)
    
    def get_publication(self):
        return self.__publication
    
    def display_member(self):
        pass

    def remove_publication(self,pub):
        self.__publication.remove(pub)





class Member(Publication):
    
    def __init__(self,name,id,contact):
        self.__name = name
        self.__id = id
        self.__contact = contact

    def add_item(self , lip):
        lip.add_member(self)
    
    def search_item(self , lip):
        mem_list = lip.get_member()
        if self in mem_list:
                return self.display_detail()
        print('ไม่พบข้อมูล')

    def display_detail(self):
        print(f'name : {self.__name}\n id : {self.__id}\n contact : {self.__contact}')
    
    def update_item(self,name,contact):
        if name and contact:
            self.__name = name
            self.__contact = contact
        else : 
            print('update ไม่สำเร็จ')
        


class Book(Publication):

    def __init__(self, title =None, author=None, year=None , isbn=None , genre=None):
        super().__init__(title, author, year)
        self.__isbn = isbn
        self.__genre = genre

    def add_item(self , lip):
        lip.add_publication(self)
        
    def search_item(self,lip):
        pub_list = lip.get_publication()
        if self in pub_list:
            return self.display_detail()
        else:
            print('ไม่พบหนังสือที่ท่านต้องการ')
       
    def display_detail(self):
        print(f'title : {super().get_author()}\nauthor : {super().get_title()}\ngenre : {self.__genre}')

    def set_genre(self,genre):
        self.__genre = genre

    def update_item(self,title,author,genre):
        super().set_title(title)
        super().set_author(author)
        self.set_genre(genre)

    def set_book(self,book):
        self = book
        
    

class Loan:
    def __init__(self , member , publication , borrowing_date , due_to):
        self.__member = member
        self.__publication = publication
        self.__borrowing_date = borrowing_date
        self.__due_to = due_to

    def display_detail(self):
        print(f'member : {self.__member.display_detail()}\n -- -- -- \npublication : {self.__publication.display_detail()}\n -- -- -- \nborrowing_date : {self.__borrowing_date}\n -- --- --\ndue to : {self.__due_to}')

    def loan_book(self,lip):
        pub_list = lip.get_publication()
        if self.__publication in pub_list:
            lip.remove_publication(self.__publication)
            print('เสร็จสิ้นครับ')
        else:
            print('กำลังถูกยืม')

    def return_booK(self,lip):
        lip.add_publication(self.__publication)
        print('คืนสำเร็จ')
        

current_time = datetime.now()
seven_days_later = current_time + timedelta(days=7)

# สร้าง object library 
Library1 = Library()
#  สร้าง object user
user1 = Member('jack' , 1 , '++0985154')
user2 = Member('goat' , 2 , '++8548156')
user3 = Member('jojo' , 3 , '++4515312')


#  สร้าง book
book1 = Book('harry' ,'micheal' ,1997 ,'105g' ,'avenger')
book2 = Book('spider_man' ,'jack dobson' ,1989 ,'fg45' ,'comic')
book3 = Book('titanic' ,'duchman' ,2001 ,'dds4' ,'drama')


# เพื่มสมาชิก 
user1.add_item(Library1)
user2.add_item(Library1)

# ค้นหา สมาชิก ที่เป็น member
user1.search_item(Library1)
# ค้นหา สมาชิก ที่ไม่เป็น member
user3.search_item(Library1)

# แสดงข้อมูล
user1.display_detail()
# อัพเดทข้อมูล
user1.update_item('pep','++888221')




# เพิ่ม book
book1.add_item(Library1)
book2.add_item(Library1)


# ค้นหา book ใน lip
book1.search_item(Library1)

# ค้นหา book ที่ไม่มีใน lip
book3.search_item(Library1)

# แสดงข้อมูล book 
book1.display_detail()
# อัพแดท  book 
book1.update_item('jurassic','arthur' , 'comic')


# สร้าง object loan
loan1 = Loan(user1,book1 , current_time , seven_days_later)
loan2 = Loan(user2 , book1 , current_time, seven_days_later)
# ยืมหนังสือที่หนังสือมีอยูในระบบ
loan1.loan_book(Library1)
# ยืมหนังสือที่ไม่มีหนังสือมีอยูในระบบ
loan2.loan_book(Library1)
# คืนหนังสือ 
loan1.return_booK(Library1)
# loan2 ยืมต่อ
loan2.loan_book(Library1)

