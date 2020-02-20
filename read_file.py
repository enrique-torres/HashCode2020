class Library:
    library_index = 0
    register_time = 0
    books_per_day = 0
    book_set = set([])
    def __init__(self, register_time, books_per_day, library_index):
        self.register_time = register_time
        self.books_per_day = books_per_day
        self.library_index = library_index

    def put_book_set(self, book_set):
        self.book_set = book_set

    def del_book(self, book_index):
        self.book_set.remove(book_index)

    def del_book_set(self, book_set):
        self.book_set = self.book_set.difference(book_set)

    def subtract_register_day(self):
        self.register_time = self.register_time - 1

    def calc_score(self, book_score_list):
        score_calculated = 0
        for book in self.book_set:
            try:
                score_calculated = score_calculated + book_score_list[book]
            except:
                print("Problem calculating score for library " + str(self.library_index + "\n"))
        return float(score_calculated) / (self.register_time + len(self.book_set))

    def a_string(self):
        return "{Indice: " + str(self.library_index) + ", Set de libros: " + str(self.book_set) + "}"

    def __str__(self):
        representation = self.a_string()
        return representation
    def __repr__(self):
        representation = self.a_string()
        return representation

    
def read_file(file_name):
    file_in = open(file_name)
    lines = file_in.readlines()

    num_books = 0
    num_libraries = 0
    num_max_days = 0

    libraries = []
    scores = []

    index = 0
    library_index = 0
    for line in lines:
        #First line of file, general information about input data
        if index == 0:
            data = line.split()
            try:
                num_books = int(data[0])
                num_libraries = int(data[1])
                num_max_days = int(data[2])
            except:
                print("Error in first line of input file:\n")
                print(data)
        #Second line of file, book score in order
        elif index == 1:
            data = line.split()
            try:
                for book_score in data:
                    scores.append(int(book_score))
            except Exception as e:
                print("Error in second line of input file:\n")
                print(data)
                print(e)
        #Rest of lines of input data
        else:
            #This line is a library general information line
            if index % 2 == 0:
                data = line.split()
                try:
                    libraries.append(Library(int(data[1]), int(data[2]), library_index))
                except:
                    print("Problem reading library number " + str(library_index) + "\n")
                    print(data)
            if index % 2 == 1:
                data = line.split()
                try:
                    library_book_set = set([])
                    for book_index in data:
                        library_book_set.add(int(book_index))
                    libraries[library_index].put_book_set(library_book_set)
                    library_index = library_index + 1
                except:
                    print("Problem reading books for library " + str(library_index) + "\n")
                    print(data)
        index = index + 1
    return num_max_days, libraries, scores