def benefit(t, n ,k):
    #Tiền lãi
    m = n*(t/100) * k
    print("Tiền lai:",m)
    #Tiền nhận được
    s= n+m
    print("số tiền nhận được:",s)

t= int(input("lãi suất hàng tháng ="))
n= int(input("số tiền ban đầu ="))
k = int(input("số tháng gửi ="))
benefit(t, n, k)