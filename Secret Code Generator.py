def Encode(msg,shift):
    result =""
    for ch in msg:
        if ch.isalpha():
            base=ord('A') if ch.isupper() else ord('a')
            result+=chr((ord(ch)-base +shift)%26+base)
        else:
            result+=ch
    return result
def decode(msg,shift):
    return(Encode(msg,-shift))

###----main----###

print("1.Encode")
print("2.decode")
print("3.Exit")
num=int(input("Enter a number : "))
if num==1:
    msg=input("Enter input to encode : ") #uppercase = 65 lowercase =97
    shift=int(input("Enter a number for shifting : "))
    enc_msgg=Encode(msg,shift)
    print("Encoded : ",enc_msgg)
elif num==2:
    msg=input("Enter input to decode : ") #uppercase = 65 lowercase =97
    shift=int(input("Enter a number for shifting : "))
    dec_msgg=decode(msg,shift)
    print("Decoded : ",dec_msgg)
elif num==3:
    print("Exiting...")
    exit()
else:
    print("Invalid...")