import csv
import datetime
import doctest

def open_csv(filename):
    try:
        with open(filename) as csvfile:
            file_reader = csv.reader(csvfile, delimiter=";")
            for line in file_reader:
                for column in line:
                    print(column, '| ', end='')
                print()
    except OSError as err :
        print("Error {} "{}"".format(type(err).__name__, filename))

#remplacer la ligne 'print("Error {} ...)' par 'raise NameError("The file cannot be read")'

# Lecture d'un date au format jour/mois/année
def read_date(s):
    return datetime.datetime.strptime(s, "%d/%m/%Y")

# Lecture d'un flottant en supprimant les caractères indésirables
# et en transformant les virgules en points.
def read_float(s) :
    """
    Converts a string into a float
    >>> read_float("1 234,5€")
    1234.5
    """
    clean = ""
    for c in s :
        if c in "0123456789." :
            clean += c
        elif c == ',' :
            clean += '.'
    return float(clean)

# Lecture d'un booléen
def read_bool(s):
    return s.lower() in ["true", "yes", "1", "ok", "oui"]

# Chargement des données depuis le fichier CSV
def load_data(filename):
    try:
        students = []
        with open(filename) as csvfile:
            file_reader = csv.reader(csvfile, delimiter=";")
            headers = next(file_reader)  # read headers
            headers = [item.lower() for item in headers]
            for line in file_reader:
                student = {}
                for i in range(len(headers)):
                    if i == 3 :
                        student[headers[i]] = read_float(line[i])
                    elif i == 4 :
                        student[headers[i]] = read_bool(line[i])
                    elif i == 5 :
                        student[headers[i]] = read_date(line[i])
                    else :
                        student[headers[i]] = line[i]
                students.append(student)
        return students
    except OSError as err :
        print("Error {} "{}"".format(type(err).__name__, filename))


def remove_duplicates(data) :
    kept = []         # list of kept entries
    already_seen = {} # dictionary of already seen email addresses
    for student in data :
        if "mail" not in student or len(student["mail"]) == 0 :
            print("No email in " + str(student))
            kept.append(student)   # We keep students with no e-mail
        else :
            # If a student has already been seen, we check the registration date
            # and replace the former entry if the current one has an older registration date
            if student["mail"] in already_seen :
                stud_idx = already_seen[student["mail"]]
                if student["registration_date"] < kept[stud_idx]["registration_date"] :
                    kept[stud_idx] = student
            else:
                # We append the student to the list of kept student
                # and put its index in the list in the dictionary of already seen students
                already_seen[student["mail"]] = len(kept)
                kept.append(student)
    return kept

import operator

def  remove_participants(students, n) :
    # Build the list of students who have paid
    paid = [stud for stud in students if stud['paid']]
    # Build the list of students who have not paid yet
    not_paid = [stud for stud in students if not stud['paid']]
    # Sort the lists by increasing registration dates
    paid.sort(key = operator.itemgetter('registration_date'))
    not_paid.sort(key = operator.itemgetter('registration_date'))
    # Build the total list with paid first, then not paid, but ordered by registration date
    total = paid+not_paid
    # Keep only the n first students
    return total[0:n]

# If the file is run as a python script, run the tests in the docstrings
if __name__ == '__main__' :
    print(doctest.testmod())





# Ski lengths
#skis = {'s1':155, 's2':160, 's3':170, 's4':170, 's5':175, 's6':175, 's7':180, 's8':190}
skis = {'s1':155, 's2':190, 's3':170, 's4':175, 's5':170, 's6':175, 's7':180, 's8':160}
# skiers heights
#customers = {'c1':150, 'c2':173, 'c3':186, 'c4':200}
customers = {'c1':150, 'c2':200, 'c3':186, 'c4':173}

def alloc(skis, customers) :
    mapping = {c:None for c in customers}
    custset = set(customers)
    skiset = set(skis)
    delta_sum = 0
    while len(custset) > 0 :
        min_delta = None
        for c in custset :
            for s in skiset :
                delta = abs(skis[s] - customers[c])
                if min_delta == None or delta < min_delta :
                    min_delta = delta
                    bestclient = c
                    bestski = s
        custset.remove(bestclient)
        skiset.remove(bestski)
        mapping[bestclient] = bestski
        delta_sum += min_delta
    mapping['delta_sum'] = delta_sum
    return mapping

print(alloc(skis, customers))

# Not optimal: c1:s2, c2:s1 has a delta_sum of 50
print(alloc({'s1':160, 's2':200}, {'c1':170, 'c2':140}))

import math
# Optimal solution
def alloc_opt(skis, customers) :
    skilist = ['_'] + sorted([(skis[s], s) for s in skis])
    custlist = ['_'] + sorted([(customers[c], c) for c in customers])
    sol = [ [0 for _ in range(1, len(customers)+2)] for _ in range(1, len(skis)+2) ]
    for i in range(len(skis)+1) :
        sol[i][0] = 0
    for j in range(len(customers)+1) :
        sol[0][j] = math.inf
    for i in range(1, len(skis)+1) :
        for j in range(1, len(customers)+1) :
            sol[i][j] = min(sol[i-1][j], sol[i-1][j-1] + abs(skilist[i][0] - custlist[j][0]))
    i = len(skis)
    j = len(customers)
    alloc = {}
    while j > 0 :
        if sol[i][j] < sol[i-1][j] :
            alloc[custlist[j][1]] = skilist[i][1]
            j -= 1
        i -= 1
    alloc['delta_sum'] = sol[len(skis)][len(customers)]
    return alloc

print(alloc_opt(skis, customers))
