#Write a program to convert an unsigned number in one radix ‘A’ to the equivalent number in another radix ‘B’, where  A and B can be any positive integer(vice versa of radix Base)

print(" Choices: \n a- Decimal to others\n b- Binary to others\n c- Hexadecimal to others\n c- Octal to others.\n e- exit")

hex_values=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def decimal_conv(n,a):
    conv=list()
    while n>0:
        rem=n%a
        conv.append(hex_values[rem])
        n=n//a
    return " ".join(conv[::-1])

def bin_conv(num,n):
    if len(str(num))%n!=0:
        num=abs((len(str(num))%n)-n)*'0'+str(num)
    ls=list(num)
    final = list(zip(*[iter(ls)] * n))
    converted, bin_converted=list(), list()
    for i in final:
        l_sum=0;bin_sum=0;
        count=len(i)-1
        for j,k in zip(i,range(count,-1,-1)):
            l_sum+=int(j)*(2**k)
        bin_sum=l_sum
        if n<=4:
            converted.append(hex_values[l_sum])
    return "".join(converted), bin_sum

def hex_conv(num,n):
    l_num=list(num)
    count=len(l_num)-1
    sum_val=0
    for i,j in zip(l_num,range(count,-1,-1)):
        sum_val+=(hex_values.index(i))*(n**j)
    return sum_val

def oct_conv(num,n):
    l_num=list(num)
    count=len(l_num)-1
    sum_val=0
    for i,j in zip(l_num,range(count,-1,-1)):
        sum_val+=(n**j)*int(i)
    return sum_val
    

while True:
    ch=input("Enter choice: ")
    if ch not in ['a','b','c','d','e']:
        print("Enter valid options only")
        continue

    if ch=='a':
        try:
            num=int(input("Enter number in decimal form: "))
        except ValueError:
            print("Enter integer value only")
            continue
        
        #decimal to binary 
        bin_form=decimal_conv(num,2)
        print("Binary form: ",bin_form,"\n")
        
        #decimal to octal
        oct_form=decimal_conv(num,8)
        print("Octal form: ",oct_form,"\n")
        
        #decimal to hexadecimal
        hex_form=decimal_conv(num,16)
        print("Hexadecimal form: ",hex_form,"\n")
        print("---------------------------------\n")
        
    elif ch=='b':
       try: 
        binarry=input("Enter number in binary form: ")
        for i in binarry:
            if i not in ['0','1']:
                print("Invalid binary format")
                break
        
        #binary to decimal
        _, dec_form=bin_conv(binarry,len(list(binarry)))
        print("Decimal form: ",dec_form,"\n")
        
        #binary to octal
        oct_form, _=bin_conv(binarry,3)
        print("Octal form: ",oct_form,"\n")
        
        #binary to hexadecimal
        hex_form, _=bin_conv(binarry,4)
        print("Hexadecimal form: ",hex_form,"\n")
        print("---------------------------------\n")
       except:
           None
        
    elif ch=='c':
       try:
        hexa=input("Enter number in hexadecimal form: ")
        
        #hexadecimal to decimal
        dec_form=hex_conv(hexa,16)
        print("Decimal form: ",dec_form,"\n")
        
        #hexadecimal to binary
        bin_form=decimal_conv(dec_form,2)
        print("Binary form: ",bin_form,"\n")
        
        #hexadecimal to octal
        oct_form=decimal_conv(dec_form,8)
        print("Octal form: ",oct_form,"\n")
        print("---------------------------------\n")
       except:
           print("Invaid hexadecimal format")
        
    elif ch=='d':
       try:
        octa=input("Enter number in octal form: ")
        
        #octal to decimal
        dec_form=oct_conv(octa,8)
        print("Decimal form: ",dec_form,"\n")
        
        #octal to binary
        bin_form=decimal_conv(dec_form,2)
        print("Binary form: ",bin_form,"\n")
        
        #octal to hexadecimal
        hex_form=decimal_conv(dec_form,16)
        print("Hexadecimal form: ",hex_form,"\n")
        print("---------------------------------\n")
       except:
           print("Invalid octal format")
        
        
    
    elif ch=='e':
        print("Program Terminated, HEHE")
        break
