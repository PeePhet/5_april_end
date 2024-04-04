from PyQt6.QtCore import QSize, Qt, QRectF
from PyQt6.QtGui import QImage, QPalette, QBrush , QPainter , QColor ,QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QInputDialog , QLineEdit , QDialog ,QMessageBox ,QComboBox
from library_system import Library, Member, Book, Loan
from datetime import datetime, timedelta
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library")
        self.showFullScreen()
        # สร้าง class lib
        self.library = Library()
        

        # กำหนดพื้นหลังเป็นรูปภาพ
        palette = self.palette()
        image = QImage("classic.png")
        palette.setBrush(QPalette.ColorRole.Window, QBrush(image))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # สร้าง QVBoxLayout และ QHBoxLayout สำหรับปุ่มและ Label
        vbox = QVBoxLayout(self)
        vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        label_layout = QHBoxLayout()
        label_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_layout.setContentsMargins(0, 20, 0, 20)  # กำหนดระยะห่างด้านบนและด้านล่าง

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.setSpacing(20)

        vbox.addLayout(label_layout)
        vbox.addLayout(button_layout)

        # เพิ่ม QLabel ด้านบน
        label = QLabel("Library")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background-color: rgba(0, 0, 0, 0.5);")
        label_layout.addWidget(label)

        # สร้างและแสดงปุ่ม
        self.display_button("Add new member", button_layout)
        self.display_button("Search member", button_layout)
        self.display_button("Add new book", button_layout)
        self.display_button("Search book", button_layout)
        self.display_button("Borrow a book", button_layout)
        self.display_button("Return the book", button_layout)
        self.display_button("Check The book is overdue", button_layout)

        
        


    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # กำหนดสีและความโปร่งแสงของสี่เหลี่ยม
        painter.setPen(Qt.GlobalColor.black)
            # กำหนดสีของพื้นหลัง
        painter.setBrush(Qt.GlobalColor.white)  # เลือกสีเขียวเป็นตัวอย่าง

        # วาดสี่เหลี่ยมที่ 1
        rect1 = QRectF(60, 180, 400, 600)
        painter.drawRect(rect1)
         # ปรับพิกัดของสี่เหลี่ยมเล็กลงเพื่อทำให้ข้อความอยู่ในตำแหน่งที่ต้องการ
        margin = 10
        text_rect1 = QRectF(rect1.x() + margin, rect1.y() + margin, rect1.width() - 2 * margin, rect1.height() - 2 * margin)
        # เขียนข้อความ
        painter.setFont(QFont("Arial", 12))
        painter.drawText(text_rect1, Qt.AlignmentFlag.AlignHCenter, "MEMBER")
        # display member
        self.display_detail_member(painter , rect1)
        
        rect2 = QRectF(55*9, 180, 550, 600)
        painter.drawRect(rect2)
        margin = 10
        text_rect2 = QRectF(rect2.x() + margin, rect2.y() + margin, rect2.width() - 2 * margin, rect2.height() - 2 * margin)
        # เขียนข้อความ
        painter.setFont(QFont("Arial", 12))
        painter.drawText(text_rect2, Qt.AlignmentFlag.AlignHCenter, "BOOK")
        # display book ใน lip 
        self.display_detail_book(painter , rect2)

        rect3 = QRectF(60*18, 180, 400, 600)
        painter.drawRect(rect3)
        margin = 10
        text_rect3 = QRectF(rect3.x() + margin, rect3.y() + margin, rect3.width() - 2 * margin, rect3.height() - 2 * margin)
        # เขียนข้อความ
        painter.setFont(QFont("Arial", 12))
        painter.drawText(text_rect3, Qt.AlignmentFlag.AlignHCenter, "BORROWING")
        self.display_detail_borrow(painter , rect3)

        rect4 = QRectF(60*25, 180, 400, 600)
        painter.drawRect(rect4)
        margin = 10
        text_rect4 = QRectF(rect4.x() + margin, rect4.y() + margin, rect4.width() - 2 * margin, rect4.height() - 2 * margin)
        # เขียนข้อความ
        painter.setFont(QFont("Arial", 12))
        painter.drawText(text_rect4, Qt.AlignmentFlag.AlignHCenter, "OVERDUE")
        self.display_detail_over_due(painter,rect4)

        rect5 = QRectF(60, 200 *4, 1500, 150)
        painter.drawRect(rect5)
        margin = 10
        text_rect5 = QRectF(rect5.x() + margin, rect5.y() + margin, rect5.width() - 2 * margin, rect5.height() - 2 * margin)
        # เขียนข้อความ
        painter.setFont(QFont("Arial", 12))
        painter.drawText(text_rect5, Qt.AlignmentFlag.AlignHCenter, "Overdue")
        self.display_detail_popular(painter ,rect5)





    # แสดงข้อมูล member ภายใน lib
    def display_detail_member(self , painter , rect):
         mem_list = self.library.get_member()
         for index, mem in enumerate(mem_list):
            margin = 10
            text_rect = QRectF(rect.x() + margin , rect.y() + (margin*5 * (index+1)), rect.width() - 2 * margin, rect.height() - 2 * margin)
            painter.setFont(QFont("Arial", 12))
            # ตัวอย่างการแสดงข้อมูลสมาชิก
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft, f"{index+1}   Name: {mem.get_name()}, Contact: {mem.get_contact()} , ID : {mem.get_id()}")
    # แสดงข้อมูล book ภายใน lib
    def display_detail_book(self , painter , rect):
       pub_list = self.library.get_publication()
       for index, pub in enumerate(pub_list):
         margin = 10
         text_rect = QRectF(rect.x() + margin , rect.y() + (margin*5 * (index+1)), rect.width() - 2 * margin, rect.height() - 2 * margin)
         painter.setFont(QFont("Arial", 12))
         # ตัวอย่างการแสดงข้อมูลสมาชิก
         painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft, f"{index+1}  Title: {pub.get_title()}, Author: {pub.get_author()} , Genre : {pub.get_genre()} , Year : {pub.get_year()} ,  ISBN : {pub.get_isbn()}")
    # แสดงข้อมูล borrow ภายใน lib
    def display_detail_borrow(self , painter , rect):
       loan_list = self.library.get_loan()
       for index, loan in enumerate(loan_list):
         margin = 10
         text_rect = QRectF(rect.x() + margin , rect.y() + (margin*5 * (index+1)), rect.width() - 2 * margin, rect.height() - 2 * margin)
         painter.setFont(QFont("Arial", 12))
         # ตัวอย่างการแสดงข้อมูลสมาชิก
         painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft, f"{index+1}  Name: {loan.get_member().get_name()}, Title: {loan.get_publication().get_title()} , ISBN : {loan.get_publication().get_isbn()}\nBorrowing date :{loan.get_borrow_date()}\nDue to :{loan.get_due_date()}")

    def display_detail_over_due(self , painter , rect):
         current_time = datetime.now()
         loan_list = self.library.get_loan()
         for index, loan in enumerate(loan_list):
            if loan.get_due_date() < current_time:
                margin = 10
                text_rect = QRectF(rect.x() + margin , rect.y() + (margin*5 * (index+1)), rect.width() - 2 * margin, rect.height() - 2 * margin)
                painter.setFont(QFont("Arial", 12))
                # ตัวอย่างการแสดงข้อมูลสมาชิก
                painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft, f"{index+1}  Name: {loan.get_member().get_name()}, Title: {loan.get_publication().get_title()} , ISBN : {loan.get_publication().get_isbn()}\nBorrowing date :{loan.get_borrow_date()}\nDue to :{loan.get_due_date()}")
            
    def display_detail_popular(self , painter , rect):
         most_list = self.library.get_most_popular()
         if len(most_list) > 0:
            for index, most in enumerate(most_list):
                    margin = 10
                    text_rect = QRectF(rect.x() + margin , rect.y() + (margin*5 * (index+1)), rect.width() - 2 * margin, rect.height() - 2 * margin)
                    painter.setFont(QFont("Arial", 12))
                    # ตัวอย่างการแสดงข้อมูลสมาชิก
                    painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft, f"{index+1}  Title: {most.get_title()}, Author: {most.get_author()} , Genre : {most.get_genre()} , Year : {most.get_year()} ,  ISBN : {most.get_isbn()}")
         else:
             most_list  = self.library.get_loan()
             for index, most in enumerate(most_list):
                    margin = 10
                    text_rect = QRectF(rect.x() + margin , rect.y() + (margin*5 * (index+1)), rect.width() - 2 * margin, rect.height() - 2 * margin)
                    painter.setFont(QFont("Arial", 12))
                    # ตัวอย่างการแสดงข้อมูลสมาชิก
                    if most.get_due_date():
                        painter.drawText(text_rect, Qt.AlignmentFlag.AlignLeft, f"{index+1}  Title: {most.get_publication().get_title()}, Author: {most.get_publication().get_author()} , Genre : {most.get_publication().get_genre()} , Year : {most.get_publication().get_year()} ,  ISBN : {most.get_publication().get_isbn()}")

    # สร้างปุ่มต่างๆ
    def display_button(self, text, layout):
        btn = QPushButton(text)
        btn.setFixedSize(QSize(150, 50))
        layout.addWidget(btn)
        if text == "Add new member":
            btn.clicked.connect(self.box_add_new_member)
        if text == "Search member":
            btn.clicked.connect(self.box_search_member)
        if text == "Add new book":
            btn.clicked.connect(self.box_add_new_book)
        if text == "Search book":
            btn.clicked.connect(self.box_search_book)
        if text == "Borrow a book":
            btn.clicked.connect(self.box_borrow_book)
        if text == "Return the book":
            btn.clicked.connect(self.box_return)

    # หน้าต่าง ของ add member
    def box_add_new_member(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Member")

        layout = QVBoxLayout()

        name_label = QLabel("Name:")
        layout.addWidget(name_label)
        name_input = QLineEdit()
        layout.addWidget(name_input)


        id_label = QLabel("Id:")
        layout.addWidget(id_label)
        id_input = QLineEdit()
        layout.addWidget(id_input)



        contact_label = QLabel("Contact:")
        layout.addWidget(contact_label)
        contact_input = QLineEdit()
        layout.addWidget(contact_input)



        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_ok_mem(dialog, name_input.text(), contact_input.text() , id_input.text()))
        layout.addWidget(btn_ok)

        dialog.setLayout(layout)
        dialog.exec()
    # method เมื่อกดตกลง add member
    def on_ok_mem(self, dialog, name, contact , id):
        if name and contact and id:
            new_user = Member(name , id , contact)
            status =  self.library.add_member(new_user)
            if not status:
                self.display_messagebox(dialog,'This ID has already been used.')
                return
            dialog.accept()
        else:
            print("Please enter both name and ID.")
  
    # หน้าต่าง ของ add book
    def box_add_new_book(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Add New Book")

        layout = QVBoxLayout()

        title_label = QLabel("Title:")
        layout.addWidget(title_label)
        title_input = QLineEdit()
        layout.addWidget(title_input)

        author_label = QLabel("Author:")
        layout.addWidget(author_label)
        author_input = QLineEdit()
        layout.addWidget(author_input)

        year_label = QLabel("Year:")
        layout.addWidget(year_label)
        year_input = QLineEdit()
        layout.addWidget(year_input)

        genre_label = QLabel("Genre:")
        layout.addWidget(genre_label)
        genre_input = QLineEdit()
        layout.addWidget(genre_input)

        isbn_label = QLabel("Isbn:")
        layout.addWidget(isbn_label)
        isbn_input = QLineEdit()
        layout.addWidget(isbn_input)



        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_ok_book(dialog, title_input.text(), author_input.text() , genre_input.text(), year_input.text() ,isbn_input.text()))
        layout.addWidget(btn_ok)

        dialog.setLayout(layout)
        dialog.exec()

    # method เมื่อกดตกลง add book
    def on_ok_book(self ,dialog ,title , author , genre , year , isbn):
        if title and author and genre and year and isbn:
            new_pub = Book(title , author , year , isbn , genre)
            status = self.library.add_publication(new_pub)
            if not status:
                self.display_messagebox(dialog, 'This isbn is already in use.')
                return
            dialog.accept()
        else:
            print("Please enter both name and ID.")

    # method เมื่อกดตกลง search mem
    def on_ok_search_mem(self , dialog, id ):
        if id:
            self.search_message_box(dialog ,id)
        else:
            pass
      # หน้าต่าง ของ search_member
    def box_search_member(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Search member")

        layout = QVBoxLayout()

        ID_member_label = QLabel("ID_member:")
        layout.addWidget(ID_member_label)
        ID_member_input = QLineEdit()
        layout.addWidget(ID_member_input)


        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_ok_search_mem(dialog,ID_member_input.text()))
        layout.addWidget(btn_ok)

        dialog.setLayout(layout)
        dialog.exec()
    
    
   # หน้าต่าง ของ search_book
    def box_search_book(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Search book")

        layout = QVBoxLayout()

        title_label = QLabel("Title:")
        layout.addWidget(title_label)
        title_input = QLineEdit()
        layout.addWidget(title_input)

        author_label = QLabel("Author:")
        layout.addWidget(author_label)
        author_input = QLineEdit()
        layout.addWidget(author_input)

        genre_label = QLabel("Genre:")
        layout.addWidget(genre_label)
        genre_input = QLineEdit()
        layout.addWidget(genre_input)


        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_ok_search_book(dialog,title_input.text() , author_input.text() , genre_input.text()))
        layout.addWidget(btn_ok)

        dialog.setLayout(layout)
        dialog.exec()
    # เมื่อกดตกลงของ search_book
    def on_ok_search_book(self,dialog , title , author , genre): 
        lib = self.library
        book =lib.search_book(title,author , genre)
        if book:
            message = book.display_detail()
            print(message)
            # สร้าง QMessageBox
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Search result")
            msg_box.setText(book.display_detail())
            msg_box.setInformativeText("Do you want to close this message box?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)

            # แสดง Message Box และรอผลลัพธ์
            result = msg_box.exec()

            # ตรวจสอบผลลัพธ์
            if result == QMessageBox.StandardButton.Yes:
                dialog.accept()
            elif result == QMessageBox.StandardButton.No:
                print("Message box closed with 'No' button.")
        else:
            # สร้าง QMessageBox
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Result")
            msg_box.setIcon(QMessageBox.Icon.Information)  # กำหนดไอคอนให้เป็น Info
            msg_box.setText('There is no information for this book in the system.')
            msg_box.setInformativeText("Do you want to search again?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
            # แสดง Message Box และรอผลลัพธ์
            result = msg_box.exec()

            # ตรวจสอบผลลัพธ์
            if result == QMessageBox.StandardButton.Yes:
               pass
            elif result == QMessageBox.StandardButton.No:
               dialog.accept()
    # แสดงผลลัพธ์ การ ค้นหา member
    def search_message_box(self , dialog , id):
        lib = self.library
        mem =  lib.search_member(id)
        if mem:
            # สร้าง QMessageBox
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Search result")
            msg_box.setText(mem.display_detail())
            msg_box.setInformativeText("Do you want to close this message box?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)

            # แสดง Message Box และรอผลลัพธ์
            result = msg_box.exec()

            # ตรวจสอบผลลัพธ์
            if result == QMessageBox.StandardButton.Yes:
                dialog.accept()
            elif result == QMessageBox.StandardButton.No:
                print("Message box closed with 'No' button.")
        else:
            # สร้าง QMessageBox
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Result")
            msg_box.setIcon(QMessageBox.Icon.Information)  # กำหนดไอคอนให้เป็น Info
            msg_box.setText('There is no information for this person in the system.')
            msg_box.setInformativeText("Do you want to search again?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
            # แสดง Message Box และรอผลลัพธ์
            result = msg_box.exec()

            # ตรวจสอบผลลัพธ์
            if result == QMessageBox.StandardButton.Yes:
               pass
            elif result == QMessageBox.StandardButton.No:
               dialog.accept()

    # หน้าต่างของ borrow_book
    def box_borrow_book(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Borrow a Book")

        layout = QVBoxLayout(dialog)

        # QComboBox สำหรับเลือก Member ID
        member_id_label = QLabel("Member ID:")
        layout.addWidget(member_id_label)
        self.member_id_combo = QComboBox()
        layout.addWidget(self.member_id_combo)
        # เพิ่มรหัสสมาชิกใน ComboBox
        mem_list = self.library.get_member()
        for mem in mem_list:
             self.member_id_combo.addItem(mem.get_id())


        # QComboBox สำหรับเลือก Book ISBN
        book_isbn_label = QLabel("Book ISBN:")
        layout.addWidget(book_isbn_label)
        self.book_isbn_combo = QComboBox()
        layout.addWidget(self.book_isbn_combo)

        # เพิ่มรหัสสมาชิกใน ComboBox
        pub_list = self.library.get_publication()
        for pub in pub_list:
             self.book_isbn_combo.addItem(pub.get_isbn())

        # QPushButton เพื่อยืนยันการยืม
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_ok_borrow(dialog, self.member_id_combo.currentText(), self.book_isbn_combo.currentText()))
        layout.addWidget(btn_ok)

        dialog.exec()
    # เมื่อกดตกลง borrow_book
    def on_ok_borrow(self , dialog , member_id , book_isbn):
        lib = self.library
        member = lib.search_member(member_id)
        book = lib.search_book_isbn(book_isbn)
        current_time = datetime.now()
        seven_days_later = current_time + timedelta(days=7)
        new_loan = Loan(member , book ,current_time, seven_days_later)
        message = new_loan.loan_book(lib)
        
        if message:
            # สร้าง QMessageBox
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Search result")
            msg_box.setText(message)
            msg_box.setInformativeText("Do you want to close this message box?")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)

            # แสดง Message Box และรอผลลัพธ์
            result = msg_box.exec()

            # ตรวจสอบผลลัพธ์
            if result == QMessageBox.StandardButton.Yes:
                dialog.accept()
            elif result == QMessageBox.StandardButton.No:
                print("Message box closed with 'No' button.")
    # แสดง message_box    
    def display_messagebox(self , dialog , message):
         # สร้าง QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Search result")
        msg_box.setText(message)
        msg_box.setInformativeText("Do you want to close this message box?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)

        # แสดง Message Box และรอผลลัพธ์
        result = msg_box.exec()

        # ตรวจสอบผลลัพธ์
        if result == QMessageBox.StandardButton.Yes:
            dialog.accept()
        elif result == QMessageBox.StandardButton.No:
            print("Message box closed with 'No' button.")
        
    # หน้าต่างของ return box
    def box_return(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Return Book")

        layout = QVBoxLayout(dialog)

        # QComboBox สำหรับเลือก Member ID
        member_id_label = QLabel("Member ID:")
        layout.addWidget(member_id_label)
        self.member_id_combo = QComboBox()
        layout.addWidget(self.member_id_combo)
        


        # QComboBox สำหรับเลือก Book ISBN
        book_isbn_label = QLabel("Book ISBN:")
        layout.addWidget(book_isbn_label)
        self.book_isbn_combo = QComboBox()
        layout.addWidget(self.book_isbn_combo)

        # เพิ่มรหัสสมาชิกใน ComboBox
        loan_list = self.library.get_loan()
        for loan in loan_list:
            self.member_id_combo.addItem(loan.get_member().get_id())
            self.book_isbn_combo.addItem(loan.get_publication().get_isbn())

        # QPushButton เพื่อยืนยันการยืม
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(lambda: self.on_return_borrow(dialog, self.member_id_combo.currentText(), self.book_isbn_combo.currentText()))
        layout.addWidget(btn_ok)
        dialog.exec()
       

     # เมื่อกดตกลง   return box
    def on_return_borrow(self ,dialog, member_id, book_isbn):
        if member_id and book_isbn:
            lib = self.library
            mem = lib.search_member(member_id)
            loan_info = lib.search_loan(mem , book_isbn)
            if loan_info:
                self.display_messagebox(dialog,'return book successfully')
                loan_info.return_booK(lib)
                dialog.accept()
            else:
                pass
           



# รันแอปพลิเคชัน
app = QApplication([])
window = MainWindow()
window.show()
app.exec()

