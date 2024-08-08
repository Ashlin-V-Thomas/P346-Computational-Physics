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
    if decimal_part==0.0:
        return sign + out1
    out2 = "."
    temp = decimal_part
    for i in range(cutoff):
        out2 += str( int(2*temp) )
        if 2*temp == 1:
            break
        temp = 2*temp - int(2*temp)
    return sign+out1+out2

def binary_to_decimal(binary_string):
    sign = 1
    if "-" in binary_string:
        sign = -1
        binary_string = binary_string[1:]
    if "." not in binary_string:
        integral_part = binary_string
        fractional_part = ""
    else:
        integral_part = binary_string[:binary_string.index(".")]
        fractional_part = binary_string[binary_string.index(".") + 1:]

    out = 0
    for i in range(len(integral_part)):
        out += int(integral_part[i])*2**(len(integral_part)-1-i)
    for i in range(1,len(fractional_part)+1):
        out += int(fractional_part[i-1])/2**i
    return sign*out

print(decimal_to_binary(-65.324))
print(binary_to_decimal('101011.1101'))
print(binary_to_decimal(decimal_to_binary(-645.15789)))
 
