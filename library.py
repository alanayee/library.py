

class Library:       
    def __init__(self,listofbooks):
        #this init method is the first method to be invoked when you create an object (INITALIZE LIBRARY)
        self.books=listofbooks
        # listofbooks is an array paramaeter when you initialize the library
    
    def printbooks(self):
        for i in range (0, len(self.books), 1):
            print(self.books[i])
        # iterate through the array (books) to print out all of the available books
    
    def lendbooks(self, bookname):
        if bookname in self.books:
            print("Book is available. You've successfully borrowed it. \n")
            self.books.remove(bookname)
        # removes book from listofbooks array
        else:
            print("Book isn't available. Come back next time! \n")
    
    def addbook(self,bookname):
    # receives the variable (bookname) from returnbook function
        if bookname in self.books:
            print("This book is already in the library or doesn't exist :( \n")
        
        else:
            self.books.append(bookname)
            print("Hooray! You've returned the book. Hope it was a good read \n")




class People:
    def borrowing(self):
        print("What book would you like to borrow? \n")
        bookname = input() 
        return bookname

    def returnbook(self):
        print("What book would you like to return? \n")
        bookname = input()
        return bookname
        # returns bookname from the input of the user
        # passes variable (bookname) to addbook method 

        
    def welcome(self):
        print("\n")
        print("--------------------------------------------------------")
        print("1. Display all available books ")
        print("2. Request a book")
        print("3. Return a book ")
        print("4. Exit \n")

    # # just a sample function not related to library program
    def addTwoNumbers(self, num1, num2):
        sum = num1 + num2
        return sum
    


def main():    
    p1 = People()       
    library = Library(["ABCs", "To Kill a Mockingbird", "A Place for Us", "Romeo and Juliet"])
    # creating object of class Library
    # object.method() it runs the method on the 


    keepGoing = True
    
    while keepGoing == True:
    # makes it loop through rather than stop

        p1.welcome() 
        # person class calls the "welcome" method
        actionNumber = input("Enter the number you want. \n" )
        # assigns input from user to actionNumber variable (tells which action to do)
        if actionNumber == 1:
            print("\n")
            library.printbooks()
        # library object of Library class calls printbooks() method 
            keepGoing = True
        if actionNumber == 2:
            bookname = p1.borrowing()
            # assigns return value from borrowing method to bookname variable that can be used in any class (in main ()) 
            library.lendbooks(bookname)
            # calls lendbook method from library object in Library class 
            # and uses the parameter "bookname" from main method
            keepGoing = True
        if actionNumber == 3:
            bookname = p1.returnbook()
            # assigns return value from returnbook method and assigns it to a variable that can be used in any class (in main())
            library.addbook(bookname)
            # calls addbook method from library object in Library class
            # uses parameter "bookname" from main method
            keepGoing = True

        if actionNumber == 4:
            print("Exiting Program. See you next time! \n")
            keepGoing = False
            # exit()


main() 