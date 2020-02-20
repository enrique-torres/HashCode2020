class Library:
    register_time = 0
    books_per_day = 0
    book_set = set([])
    has_been_registered = False
    total_score = 0
    def __init__(self, register_time, books_per_day, book_set):
        self.register_time = register_time
        self.book_set = book_set
        self.books_per_day = books_per_day

    def calc_score():
        return self.total_score / ()

    


file_in = open('b_read_on.txt')
lines = file_in.readlines()

num_books = 0
num_libraries = 0
num_max_days = 0

libraries = []
scores = []

index = 0
for line in lines:
    if index == 0:
        data = line.split()
        