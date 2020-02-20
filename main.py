import read_file

days = 10
resultLibrerias = []

numDays, librerias, score = read_file.read_file('a_example.txt')

print(librerias)
while numDays > 0:
    print(numDays)
    #select MAx beneficio
    if len(librerias) == 0:
        break
    maxS = librerias[0].calc_score(score)
    index = 0
    i = 0
    for L in librerias:
        if L.calc_score(score) > maxS:
            index = i
            maxS = L.calc_score(score)
        i+= 1
    libSect = librerias[index]
    del librerias[index]
    #todo Eliminar mejores que de tiempo
    [l.del_book_set(libSect.book_set) for l in librerias ]
    resultLibrerias += [libSect]

    numDays -= libSect.register_time


F = open("result.txt", "w")
F.write(str(len(resultLibrerias)) + "\n")

for l in resultLibrerias:
    F.write( str(l.library_index) + " " + str((len(l.book_set))) + "\n")   
    books = ""
    for b in l.book_set:
        books = books + str(b) + " "
    
    F.write(books + "\n")