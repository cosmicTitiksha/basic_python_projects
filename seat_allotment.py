# Seat Allotment Software
# Say out of total 7 seats, 3 are open category, 1 obc girl, 1 obc, 1 SC, 1 EWS
number_of_available_seats = int(input("Total number of available seats : "))
number_of_students_appeared = int(input("Total number of students appeared : "))

raw_list = []
selected_students = []

for i in range(1, number_of_students_appeared+1):
  name = input("Enter your name : ")
  marks = float(input("Number of marks obtained : "))
  category = input("Category : ").lower()
  gender = input("Gender (M/F/O) : ").upper()
  raw_list.append([name , marks , category, gender])

# Sorting of nested list based on marks obtained
raw_list.sort(key = lambda x : x[1] , reverse = True)

selected_students = raw_list[:3]


obc_girl_filled = False
obc_filled = False
sc_filled = False
ews_filled = False

for student in raw_list[3:]:
    name, marks, category, gender = student

    if not obc_girl_filled and category == 'obc' and gender == 'F' and student not in selected_students:
        selected_students.append(student)
        obc_girl_filled = True

    elif not obc_filled and category == 'obc' and student not in selected_students:
        selected_students.append(student)
        obc_filled = True

    elif not sc_filled and category == 'sc' and student not in selected_students:
        selected_students.append(student)
        sc_filled = True

    elif not ews_filled and category == 'ews' and student not in selected_students:
        selected_students.append(student)
        ews_filled = True

print("\nSelected Students:")
for student in selected_students:
    print(student)