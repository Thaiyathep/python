''' #เเบฝึกหัด5.1
class nisit : #กำหนดชื่อ class เป็น nisit
    def __init__(self,name,id,sax,year,subject,province,school) : #กำหนดตัวแปร _ มี2ตัว
        self.name = name      #------------------------
        self.id = id                                #--
        self.sax = sax                              #--
        self.year = year         #กำหนดแล้วเเทนลง    #--
        self.subject = subject                      #--
        self.province = province                    #--
        self.school = school  #--------------------------

    def shownisit(self) :  #เเสดงผล
        print("-------เเนะนำตัว---------")
        print("ชื่อ-นามสกุล :",self.name)
        print("รหัสนักศึกษา :",self.id)
        print("เพศ :",self.sax)
        print("ชั้นปีการศึกษา :",self.year)
        print("คณะ,สาขาวิชา:",self.subject)
        print("จังหวัด :",self.province)
        print("โรงเรียนเดิม :",self.school)

x = nisit("ไทยเทพ พนาวัลย์สมบัติ","633050424-9","ชาย","ปี 1"," ED COM","ขอนแก่น","ศรีกระนวนวิทยาคม")
x.shownisit()
'''
"""
show = [] 
pan = [] 
kum = [] 
i = 1    
def menu(): #ประกาศฟังก์ชันเมนู
    global choice
    print('\nพจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม')
    choice = input('Input Choice: ')

def puss():
    dictionary.insert(0,input("เพิ่มคำศัพท์ ")) #insert() เพื่อเพิ่มสมาชิกไปยังตำแหน่งที่ต้องการ 
    pra.insert(0,input("ชนิดคำศัพท์ (n. ,v. ,adj. ,adv. :) "))
    kum.insert(0,input("ความหมาย "))
    print("เพิ่มคำศัพท์เรียบร้อยแล้ว")
def show():
    print('---------------------\nคำศัพท์มีทั้งหมด ',len(dictionary),"\n---------------------")
    print('คำศัพท์ ประเภท ความหมาย')
    x = 0
    while x < len(dictionary) : #len(ตัวแปรหรือข้อมูล)
        print(dictionary[x],' ',pra[x]," ",kum[x])
        x = x+1

def delete():
    x =str(input("พิมพ์คำศัพท์ที่ต้องการลบ: "))
    x2 =str(input("ต้องการลบ "+x+" ใช่หรือไม่ (y/n) :"))
    if x2 == "y":
        z=0
        while z < len(dictionary): #len(ตัวแปรหรือข้อมูล) คำสั่งสำหรับวัดความยาวของ str,byte,tuple,List,range
            if x == dictionary[z]:
                del pra[z]
                del kum[z]
            z = z+1
        dictionary.remove(x)   #สร้างตัวก๊อบปี้ของList(เอาตัวเลขทุกตัว)เอามาใช้วนลูปแล้วเวลาลบข้อมูลก็ลบใน list ของจริง ผลลัพธ์ก็จะเก็บอยู่ใน list A ตามปกติ
        print("ลบ "+x+" เรียบร้อยแล้ว")
    else:
        print("ยกเลิกการลบคำศัพท์")

while True: #วางเงื่อนไข เลือกchoice
    menu()
    if choice == '1':
        puss()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    else:
        o =str(input("ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) :")) #ข้อมูลชุดข้อความ ว่าใช่หรือไม่
        if o == "y":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break
        else:
            print("กลับเข้าสู่โปรแกรม")
"""
class Manu :
    def __init__(self,product,add,exits) :
        self.product = product
        self.add = add
        self.exits = exits
    def showmanu(self) :
        print("+++++++++โฟลืคเท่++++++")
        print("เเสดงรายการสินค้า        ",self.product)
        print("เพิ่มรายการสินค้า        ",self.add)
        print("ออกจากระบบ           ",self.exits)
x = Manu("กด s","กด a","กด x")
x.showmanu()

