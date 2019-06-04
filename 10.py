
import math
def Tinh(R):
    if R<0:
        print ("R không hợp lệ")
    else:
        c = 2*R*math.pi
        s = R*R*math.pi
        print("chu vi là:", c)
        print("diện tích là:", s)

R= float(input("nhập bán kính hình tròn:"))
Tinh (R)