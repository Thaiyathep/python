#Functions
"""
width = 4
legth = 4
height = 2
box_area = width * length * height

โครงสร้าง def ชื่อฟังก์ชัน():
            ...คำสั่งข้างใน
def get_box_area():
    width = 4
    length = 4
    height = 2
    box_area = width * length * height
    print(box_area)

get_box_area()

    โครงสร้างที่เรากำหนดค่าได้ def ชื่อฟังก์ชัน(พรารา1, พรารา2, พารา3):
                                    ...คำสั่งข้างใน
def get_box_area(width, length, height):
    box_area = width * length * height
    print(box_area)

get_box_area(4, 4, 2)
get_box_area(width=1, length=1, height=1)

เราไม่อยากเเสดงผลลัพธ์ แต่เราอยากได้เเค่คำนวณเเล้วคืนค่ากลับไปที่เรียกใช้ฟัง์ชัน
ซึ่งมีคำสั่งหนึ่งคือ return
def get_box_area(width, length, height):
    box_area = width * length * height
    return box_area

box1 = get_box_area(4, 4, 2)
box2 = get_box_area(width=1, length=1, height=1)

print(box1)

มีอีกอย่าง เมื่อเจอ return มันจะหยุดการทำงานของฟังก์ชันนั้นทันนที
def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0
    box_area = width * length * height
    return box_area

box1 = get_box_area(4, -4, 2)
box2 = get_box_area(width=1, length=1, height=1)

print(box1)
"""