Publication
	- tile: string
	- author: string
	- year: int
	+ getTitle(): string
	+ getAuthor(): string
	+ getYear(): int
	+ setTitle(title: string): void
	+ setAuthor(author: string): void
	+ setYear(year: int): void
	+ displayDetial(): string
	+ searchItem(lip: Library): string
	+ updateItem(lip: Library): string
Book
	- isbn: string
	- genre: string
	+ getIsbn(): string
	+ getGenre(): string
	+ setIsbn(isbn: string): void
	+ setGenre(genre: string): void
Library
	- member: list
	- publication: list
	= loans: list
	+ addMember(member: Member): bool
	+ getMembers(): list
	+ addPublication(publication: Publication): bool
	+ getPublications(): list
	+ removePublication(publication: Publication): void
	+ searchMember(id: int): Member or False
	+ searchBook(title: string, author: string, genre: string): Book or False
	+ searchBookIsbn(isbn: string): Book or False
	+ addLoan(loan: Loan): void
	+ getLoans(): list
	+ searchLoan(member: Member, book: Book): Loan or False
	+ removeLoan(loan: Loan): void
Member
	- name: string
	- id: int
	- contact: string
	+ getName(): string
	+ getId(): int
	+ getContact(): string
	+ displayDetail(): string
	+ updateItem(name: string, contact: string): void
Loan
	- member: Member
	- publication: Book
	- borrowingDate: datetime
	- dueDate: datetime
	+ getMember(): Member
	+ getPublication(): Book
	+ getBorrowingDate(): datetime
	+ getDueDate(): datetime
	+ displayDetail(): void
	+ loanBook(library: Library): string
	+ returnBook(library: Library): void
Book-->Publication
Library--Publication
Member--Library
Loan--Member
