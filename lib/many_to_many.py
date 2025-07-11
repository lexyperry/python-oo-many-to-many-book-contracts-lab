class Author:
    all = []

    def __init__(self, name):
       self.name = name 
       Author.all.append(self)
       
    def contracts(self):
       return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})   
   
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    



class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return list({contract.author for contract in self.contracts()})
    
    

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.validate()
        Contract.all.append(self)

    def validate(self):
        if not isinstance(self.author, Author):
            raise TypeError("Auther must be an instance of Author class")
        if not isinstance(self.book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(self.date, str):
            raise TypeError("Date must be a string")
        if not isinstance(self.royalties, int):
            raise TypeError("Royalties must be an integer")
        
    @classmethod
    def contracts_by_date(cls, target_date):
        return [contract for contract in cls.all if contract.date == target_date]
        

      