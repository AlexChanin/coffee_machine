# put your python code here
all_grades = input().split()
grades_a = [x for x in all_grades if x == "A"]
print(round(len(grades_a) / len(all_grades), 2))
