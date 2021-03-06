
"""
import sqlite3
conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
c = conn.cursor()
c.execute ('''CREATE TABLE student (No integer PRIMARY KEY AUTOINCREMENT, 
    number varchar(30) NOT NULL,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(30) NOT NULL,
    old varchar(30) NOT NULL,
    year varchar(30) NOT NULL)''')
conn.commit()
conn.close()
"""

"""
def insertTousers (number,fname,lname,email,sex,old,year) :
    try :
        conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
        c = conn.cursor()
        sql = '''INSERT INTO student (number,fname,lname,email,sex,old,year) VALUES (?,?,?,?,?,?,?)'''
        data = (number,fname,lname,email,sex,old,year)
        c.execute(sql,data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally :
        if conn :
            conn.close()
"""

def menu(): 
    global choice
    print('\n-----ระบบทะเบียนนักเรียน-----\n',"="*25,'\nเพิ่มนักเรียน กด [a]\nแสดงข้อมูลนักเรียน [s]\nแก้ไขข้อมูลนักเรียน [e]\nลบข้อมูลนักเรียน [d]\nออกจากโปรแกรม [x]')
    choice = input('\nกรุณาเลือกทำรายการ ')

def puss(): 
    print("\n--------เพิ่มนักเรียน--------\n","="*25)
    z = "y"
    while z == "y":
        a1 = str(input("ลำดับที่ "))
        a2 = str(input("ชื่อ "))
        a3 = str(input("นามสกุล "))
        a4 = str(input("อีเมล "))
        a5 = str(input("เพศ ชาย[m] / หญิง[f] "))
        if a5 == "m":
            a5 = "ชาย"
        elif a5 == "f":
            a5 = "หญิง"
        a6 = str(input("อายุ "))
        a7 = str(input("ชั้นปี "))
        import sqlite3
        conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
        c = conn.cursor()
        try :
            data = (str(a1),str(a2),str(a3),str(a4),str(a5),str(a6),str(a7))

            c.execute('INSERT INTO student (number,fname,lname,email,sex,old,year) VALUES (?,?,?,?,?,?,?)',data)
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print('Failed to insert : ',e)
        finally :

            if conn :
                conn.close()
        print("ทำรายการเสร็จสิ้น")
        z = str(input("ต้องการทำรายการต่อหรือไม่ (y/n) : "))

def show(): 
    print("\n------------------------แสดงข้อมูลนักเรียน------------------------\n","="*65)
    print("No---ลำดับที่----ชื่อ------นามสกุล------email-----เพศ----อายุ----ชั้นปี----\n","="*65)
    import sqlite3

    conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM student''')

    result = c.fetchall()
    for x in result :
        print(x)
        
def edit(): 
    print("\n-------แก้ไขข้อมูลนักเรียน-------\n","="*25)
    print("No---ลำดับที่----ชื่อ------นามสกุล------email-----เพศ----อายุ----ชั้นปี----\n","="*65)
    import sqlite3

    conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
    c = conn.cursor()
    c.execute('''SELECT * FROM student''')

    result = c.fetchall()
    for x in result :
        print(x)
    z = "y"
    while z == "y":
            n2 = str(input("\nกด [x] เพื่อยกเลิก \nกรุณาระบุ No ที่ท่านต้องการแก้ไข "))
            if n2 == "x":
                break
            print("แก้ไขเป็น")
            b1 = input("ลำดับที่ ")
            b2 = input("ชื่อ ")
            b3 = input("นามสกุล ")
            b4 = input("อีเมล ")
            b5 = input("เพศ ")
            b6 = input("อายุ ")
            b7 = input("ชั้นปี ")

            import sqlite3
            conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
            c = conn.cursor()
            try :
                data = (str(b1),str(b2),str(b3),str(b4),str(b5),str(b6),str(b7),str(n2))
                conn.commit()
                conn.close()
                

            except sqlite3.Error as e:
                print('Failed to insert : ',e)
            finally :
                if conn :
                    conn.close()
            print("ทำรายการเสร็จสิ้น")
            z = str(input("ต้องการทำรายการต่อหรือไม่ (y/n) : "))

def delete(): 
    z = "y"
    while z == "y":
        print("\n-------ลบข้อมูลนักเรียน-------\n","="*25)
        print("No---ลำดับที่----ชื่อ------นามสกุล------email-----เพศ----อายุ----ชั้นปี----\n","="*65)
        import sqlite3

        conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
        c = conn.cursor()
        c.execute('''SELECT * FROM student''')

        result = c.fetchall()
        for x in result :
            print(x)

        n1 = str(input("\nกด [x] เพื่อยกเลิก \nNo ที่ต้องการลบ "))
        if n1 == "x":
            break
        import sqlite3
        conn = sqlite3.connect(r"D:\Thaiyathep_python\example.db")
        c = conn.cursor()
        try :
            c.execute("DELETE FROM student WHERE No ="+str(n1))
            conn.commit()
            conn.close()

        except sqlite3.Error as e:
            print('Failed to insert : ',e)
        finally :
            if conn :
                conn.close()
        print("ทำรายการเสร็จสิ้น")
        z = str(input("ต้องการทำรายการต่อหรือไม่ (y/n) : "))

while True: # loop choice
    menu()
    if choice == 'a':
        puss()
    elif choice == 's':
        show()
    elif choice == 'e':
        edit()
    elif choice == 'd':
        delete()
    elif choice == 'x':
        o =str(input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :"))
        if o == "y":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กลับเข้าสู่โปรแกรม")



"""
DELETE FROM student; 
DELETE FROM sqlite_sequence WHERE name = 'student';
"""