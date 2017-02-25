CREATE TABLE book_loans (
   BookId INT PRIMARY KEY,
   BranchId INT,
   CardNo INT,
   DateOut VARCHAR(20),
   DueDate VARCHAR(20),
   FOREIGN KEY (BookId) REFERENCES book(BookId),
   FOREIGN KEY (BranchId) REFERENCES library_branch(BranchId),
   FOREIGN KEY (CardNo) REFERENCES borrower(CardNo)   
  );