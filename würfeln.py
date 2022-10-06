#Alle Werte sammeln
number_of_Students = input("Wie viele Schüler gibt es: ")
best_grade = input("Was ist die beste Note: ")
badest_grade = input("Was ist die schlechteste Note: ")
print("Gib die Namen der Schüler in einer neuen Zeile an.")
array_of_names = []
array_of_grades = []
array_of_results = []
def ask_names():
    name_of_student = input("")
    array_of_names.append(str(name_of_student))
for x in range(0,int(number_of_Students)):
    ask_names()
#Notengenerieren
def calculateMiddle():
    t = 0
    for x in array_of_grades:
        t += int(x)
    x = float(number_of_Students)
    result = t / x
    print("Der Durchschnitt ist: " + str(result))
import random
def printList():
    X = 0
    while X < len(array_of_names):
        print(array_of_results[X])
        X += 1
    calculateMiddle()
def writeList():
    i = 0
    print("Die Noten sind:")
    while i < len(array_of_names):
        array_of_results.append(array_of_names[i] + ", Note: " + array_of_grades[i])
        i += 1
    printList()
for x in range(0,int(number_of_Students)):
    x = int(best_grade)
    y = int(badest_grade)
    grade = random.randint(x, y)
    array_of_grades.append(str(grade))
writeList()
