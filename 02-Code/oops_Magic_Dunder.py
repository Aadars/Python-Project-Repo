class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return '{} by {} of {} Pages'.format(self.title,self.author,self.pages)

mybook = Book('Nagin','Aadarsh',200)
print(mybook)

