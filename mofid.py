import csv



def add_user():
    User = input("Username: ")
    Pass = input("Password: ")
    fields = [User, Pass]
    with open('Users', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
add_user()
def read_user():
    with open('Users', 'r') as Users:
        Users = csv.reader(Users, delimiter=',')
        n = 0
        for row in Users:
            print(row[0])

read_user()