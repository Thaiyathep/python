#ฟังก์ชัน
"""
import os
choice = 0
filename = ''

def menu():
    global choice
    print('Menu\n 1.open calculator\n 2.Open Notepad\n 3.Exit ')
    choice = input('Select Menu :')


def opennotepad():
    filename = 'C:\Windows\\SysWoW64\\notepad.exe'
    print('Memorandum writing %s' %filename)
    os.system(filename)

def opencalculator():
    filename = 'C:\\Windows\\System32\\calc.exe'
    print('Calculate Number %s' %filename)
    os.system(filename)

while True:
    menu()
    if choice == '1':
        opencalculator()
    elif choice == '2':
        opennotepad()
    else:
        break
"""
#เเบบฝึกหัดที่ 4.1
choice = 0
i=1
lt=[0,0,0,0,0]
def menu():
    global choice 
    print('โปรแกรมร้านค้า\n 1.แสดงรายการสินค้า\n 2.หยิบสินค้าใส่ตะกร้า\n 3.แสดงจำนวนและราคาของสินค้าที่หยิบ\n 4.หยิบสินค้าออกจากตะกร้า\n 5.ปิดโปรแกรม\n')
    choice = input('Select Menu : ')

def openproduct():
    print('รายการสินค้า\n 1.เสือดำ ราคา 50000000 บาท\n 2.เก้ง ราคา 30000000  บาท\n 3.กระชู่ ราคา 200000000 บาท\n 4.ม้านิลมังกร ราคา 450000000 บาท\n 5.ยูนิคอร์น ราคา 5000000000 บาท\n')

def puss():
    print('กรุณาเลือกรายการสินค้า\n 1.เสือดำ ราคา 50000000 บาท\n 2.เก้ง ราคา 30000000  บาท\n 3.กระชู่ ราคา 200000000 บาท\n 4.ม้านิลมังกร ราคา 450000000 บาท\n 5.ยูนิคอร์น ราคา 5000000000 บาท\n')
    while(i>0):
        a=int(input("เลือกสินค้าหมายเลข :"))
        if a==1:
            lt[0] +=1
        elif a==2:
            lt[1] +=1
        elif a==3:
            lt[2] +=1
        elif a==4:
            lt[3] +=1
        elif a==5:
            lt[4] +=1
        elif a==6:
            break
def show():
    print("สินค้าของคุณมีดังนี้")
    print('สินค้า..........จำนวน............ราคา')
    print('1.เสือดำ.......',lt[0],'.....',lt[0]*15,'....')
    print('2.เก้ง.........',lt[1],'.....',lt[1]*10,'....')
    print('3.กระชู่........',lt[2],'.....',lt[2]*6,'.....')
    print('4.ม้านิลมังกร....',lt[3],'.....',lt[3]*30,'....')
    print('5.ยูนิคอร์น......',lt[4],'.....',lt[4]*25,'....')

def delete():
    print('กรุณาเลือกรายการสินค้า\n 1.เสือดำ ราคา 50000000 บาท\n 2.เก้ง ราคา 30000000  บาท\n 3.กระชู่ ราคา 200000000 บาท\n 4.ม้านิลมังกร ราคา 450000000 บาท\n 5.ยูนิคอร์น ราคา 5000000000 บาท\n')
    while(i>0):
        a=int(input("เลือกสินค้าหมายเลข :"))
        if a==1:
            lt[0] -=1
        elif a==2:
            lt[1] -=1
        elif a==3:
            lt[2] -=1
        elif a==4:
            lt[3] -=1
        elif a==5:
            lt[4] -=1
        elif a==6:
            break

while True:
    menu()
    if choice == '1':
        openproduct()
    elif choice == '2':
        puss()
    elif choice == '3':
        show()
    elif choice == '4':
        delete()
    else : 
        break





















