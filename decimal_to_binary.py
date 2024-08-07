def decimal_to_binary(num,out = "", cutoff = 15):
    #Extracting integral and decimal parts of the number
    sign = ""
    integral_part = ""
    decimal_part = "0"
    flag = False
    for i in str(num):
        if i == "-":
            sign = i
            continue
        if i == ".":
            flag = True
        if flag:
            decimal_part+=i
        else:
            integral_part+=i
    integral_part = int(integral_part)
    decimal_part = float(decimal_part)

    #Converting integral part to binary
    temp = integral_part
    out1 = ""
    while temp!=1:
        out1 = str(temp%2) + out1
        temp = temp//2
    out1 = "1" + out1
    
    #Converting decimal part to binary, will terminate after (cutoff = 15) places.
    out2 = "."
    temp = decimal_part
    for i in range(cutoff):
        out2 += str( int(2*temp) )
        if 2*temp == 1:
            break
        temp = 2*temp - int(2*temp)
    return sign+out1+out2

print(decimal_to_binary(-6.19))       