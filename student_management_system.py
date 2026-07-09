while True:
    print("===== Student Management System =====")


    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    students = ["Gavi", "Aman", "Rohan"]

    if choice == "1":
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        Class = input("Enter Student Class: ")

        print("Student Added Successfully!")
    
    if choice == "2":
         print("Students List:")
         print(students)

    if choice == "3":
        search = input("Enter Student Name: ")
        if search in students:
            print("Student Found")
        else:
            print("Student Not Found")
        
    if choice == "4":
        search = input("Enter Student Name: ")
        if search in students:
            print("Student Updated")
        else:
            print("Student Not Found")
            
    if choice == "5":
        search = input("Enter your Name: ")
        if search in students:
            students.remove(search)    
            print("Student Deleted")
            print(students)
        else:
            print("Student Not Found")
           
    if choice == "6":
        print("Good Bye!")
        break
