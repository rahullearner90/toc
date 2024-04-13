zeros=0
ones=0
count=0
def stateq0(str):
    global zeros
    global ones
    global count
    if count<len(str):
        n=str[count]
        if len(n)==0:
            print('string is not accepted')
        else:
            if n=='0':
                count=count+1
                zeros=zeros+1
                stateq0(str)
            if n=='1':
                count=count+1
                ones=ones+1
                stateq0(str)
    else:
        print(zeros)
        print(ones)
str=input("Enter a string accepting 1 and 0 only: ")
stateq0(str)