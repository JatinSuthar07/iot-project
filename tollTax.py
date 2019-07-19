#import serial
import smtplib as sm
import xlrd as r
import xlwt as w
#s=serial.Serial('/dev/ttyUSB0')
car=250
truck=450
bus=350
sender="abcx94179@gmail.com"
password="Hello@123"
while(1):
    print("Toll Tax")
    msg=""
    wb=r.open_workbook("ttx.xls")
    d0=wb.sheet_by_index(0)
    l0=d0.col_values(0)
    l1=d0.col_values(1)
    l2=d0.col_values(2)
    l3=d0.col_values(3)
    m=sm.SMTP('smtp.gmail.com',587)
    j=0
    cost=0
    d='11004EA5B64C'
    #s.open()
    #d=str(s.read(12),'utf-8')
    #s.close()
    #print(d)
    wt=w.Workbook()

    ws=wt.add_sheet("Sheet1")
    m.starttls()
    m.login(sender,password)
    if(d in l1):
        for i in range(0,len(l1)):
            if(d==l1[i]):
                j=i
    else:
        print("unable to search your card sir")
        exit(0)
    def fun(c,z):
            print("you have enough amount")
            cost=z-c
            l2[j]=cost
            for i in range(0,len(l0)):
                ws.write(i,0,l0[i])
                ws.write(i,1,l1[i])
                ws.write(i,2,l2[i])
                ws.write(i,3,l3[i])
            wt.save("ttx.xls")
            msg="hello " + d0.cell_value(j,0) +" your accont has deducted rupees " + str(car)+ " for your car available amount is " + str(d0.cell_value(j,2))
            m.sendmail(sender,d0.cell_value(j,3),msg)
            print("mail has send to the given email id")
            del j
            del cost
            del d
            del wb
            del d0
            del l0
            del l1
            del l2
            del l3
            del wt
            del ws
            del msg
            del m        
    v=input("enter the type of vechile : ")
    if(v=="car"):
        if(car<=int(d0.cell_value(j,2))):
            fun(car,int(d0.cell_value(j,2)))
            continue
        else:
            print("you don't have enough amount")
            exit()
    elif(v=="bus"):
        if(bus<=int(d0.cell_value(j,2))):
            print("you have enough amount")
            cost=int(d0.cell_value(j,2))-bus
            l2[j]=cost
            for i in range(0,len(l0)):
                ws.write(i,0,l0[i])
                ws.write(i,1,l1[i])
                ws.write(i,2,l2[i])
                ws.write(i,3,l3[i])
            wt.save("ttx.xls")
            msg="hello " + d0.cell_value(j,0) +" your accont has deducted rupees " + str(car) +" for your bus available amount is " + str(d0.cell_value(j,2))
            m.sendmail(sender,d0.cell_value(j,3),msg)
            print("mail has send to the given email id")
            del j
            del cost
            del d
            del wb
            del d0
            del l0
            del l1
            del l2
            del l3
            del wt
            del ws
            del msg
            del m
            continue
        else:
            print("you don't have enough amount")
            exit()
    elif(v=="truck"):
        if(truck<=int(d0.cell_value(j,2))):
            print("you have enough amount")
            cost=int(d0.cell_value(j,2))-truck
            l2[j]=cost
           
            for i in range(0,len(l0)):
                ws.write(i,0,l0[i])
                ws.write(i,1,l1[i])
                ws.write(i,2,l2[i])
                ws.write(i,3,l3[i])
            wt.save("ttx.xls")
            msg="hello " + d0.cell_value(j,0) +" your accont has deducted rupees " + str(car)+ " for your truck available amount is " + str(d0.cell_value(j,2))
            m.sendmail(sender,d0.cell_value(j,3),msg)
            print("mail has send to the given email id")
            del j
            del cost
            del d
            del wb
            del d0
            del l0
            del l1
            del l2
            del l3
            del wt
            del ws
            del msg
            del m
            continue
        else:
            print("you don't have enough amount")
            exit()
    else:
        print("you have not enterd a valid vehicle")
    
