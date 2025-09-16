# from student import {
#     create_student,
#     read_all_students,
#     read_student_by_id,
#     update_stedent,
#     delete_student,
#     search_students,
#     sert_students

# }

def menu_loop():
    while True:
        print("/n=== Student Management(Modular) ===")
        print("1. Create")
        print("2. Read All")
        print("3. Read By ID")
        print("4. Update By ID")
        print("5. Delete by ID")
        print("6. Exit")
        print("7. Search")
        print("8. Sort")
        choice = input("เลือกเมนู: ").strip()

        try:
            if choice == "1":
               name = input("ชื่อ: ")
               dept = input("สาขา: ")
               year = int(input("เกรดเฉลี่ย: "))
               print("เพื่มเเล้ว:", create_student(name, dept, year, gpa))

            elif choice == "2":
                for s in read_all_students():
                    print(s)

            elif choice == "3":
                sid = int(input("ID: ").strip())
                s = read_student_by_id(sid)
                    print(s or "ไม่พบข้อมูล")

            elif choice == "4":
                sia
                    print(s)

            