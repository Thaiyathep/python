#เเบบฝึกหัดที่3.1
"""
print('เลือกเมนูเพื่อทำรายการ\n#################')
print('กด 1 เลิอกเหมาจ่าย')
print('กด 2 เลือกจ่ายเพิ่ม')
ch = int(input('')) #กำหนดวางให้เลือก
if ch == 1 :  #ส่วนที่ 1(ตัวเลือก)
    km1 = int(input('กรุณาบอกระยะทาง')) #กำหนดตัวkm1 เข้ามา
    if km1 <= 25 : #น้อยกว่าหรือเท่ากับ 25
        print('ค่าใช้จ่ายรวมทั้งหมด 25 บาท')
    else:
        print('ค่าใช้จ่ายรวมทั้งหมด 55 บาท') #สิ้นสุดส่วนที่ 1
elif ch == 2 : #ส่วนที่ 2 (ตัวเลือก)
    km2 = int(input('กรุณาบอกระยะทาง')) #กำหนดตัวkm2 เข้ามา
    if km2 < 25 : #ไม่เกิน 25
            print('ค่าใช้จ่ายทั้งหมด 25 บาท')
    else:
        print('ค่าใช้จ่ายรวมทั้งหมด 80 บาท') #สิ้นสุดส่วนที่ 2
"""
#เเบบฝึกหัดที่3.3
"""
print('กรุณากรอกจำนวนครั้งการรับค่า')
n = int(input(' ')) #รับค่ามาจากภายนอก
i = 1
sum = 0
while(i <= n) :  
    a =int(input('กรอกตัวเลข ')) 
    i+= 1
    sum = sum+a #
print('ผลรวมของค่าทั้งหมด    ',sum) #นอกลูป
"""
"""
print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ  exit เพื่ออออกจากโปรเเกรม')
i = 1
name = []
for 
"""
#เเบฝึกหัดที่3.4
"""
print('ป้อนชื่ออาหารสุดโปรดของคุณ หรือ  exit เพื่ออออกจากโปรเเกรม')
foodlist = []
a = 0
while(True) :
    a = a + 1
    print('อาหารสุดโปรดลำดับที่',a,end= '')
    choose = input('คือ\t')
    foodlist.append(choose)
    if choose == 'exit' :
        break
print('รายการอาหารสุดโปรดของคุณ มีดังนี้',end= '')
for x in range(1,a) :
        print(x,' ',foodlist[x-1],end= '')
"""
#อาจารย์พาทำ
"""
a = []
while True:
    b = input('-----ร้านน้องโฟล์คการบาส-----\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]\n')
    b = b.lower()
    if b=='a':
        c = input('ป้อนรายการลุกค้า(รหัส:ชื่อ:จังหวัด)')
        a.append(c)
        print('\n*******ข้อมูลได้เข้าสู่ระบบแล้ว*******\n')
    elif b == 's':
        print('{0:-<30}'.format(""))
        print('{0:-<8}{1:-<10}{2:10}'.format('รหัส','ชื่อ','จังหวัด'))
        print('{0:-<6}{0:-<10}{0:-<10}'.format(""))
        for d in a:
              e = d.split(":")
              print('{0[0]:<6} {0[1]:<10}({0[2]:<10})'.format(e))
              continue
    elif b == 'x':
        break
print('ทำคำสั่งต่อไป')
"""
#เเบบฝึกหัดที่ 3.5
""" 
studer = int(input('Please enter student: '))
print('-'*30)
total = [0 , 0 , 0 , 0 , 0 , 0]
score = ['90 - 100 : ','80 - 89 : ','70 - 79 : ','60 - 69 : ','50 - 59 : ','0 - 49 : ']
x = 1
while x <= studer :
    point = int(input('Please enter score : '))
    if point <= 100 and point >= 90 :
        total[0] +=1
    elif point < 90 and point >= 80 :
        total[1] +=1
    elif point < 80 and point >= 70 :
        total[2] +=1
    elif point < 70 and point >= 60 :
        total[3] +=1
    elif point < 60 and point >= 50 :
        total[4] +=1
    elif point < 50 and point >= 0 :
        total[5] +=1
    x = x+1
for x in range(0,6) :
    print(score[x],'*'*total[x])
    """