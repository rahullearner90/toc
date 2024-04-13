global str
def stateq0(str):
    global count
    print("Entered q0",count)
    if count<len(str):
        n=str[count]
        if len(n)==0:
            print('string is not accepted')
        else:
            if n=='0':
                count=count+1
                stateq0(str)
            if n=='1':
                count=count+1
                stateq1(str)
    else:
        print('not a valid string')
            
def stateq1(str):
    global count
    print("Entered q1",count)
    if count<len(str):
        n=str[count]
        if len(n)==0:
            print('string is not accepted')
        else:
            if n=='0':
                count=count+1
                stateq2(str)
            if n=='1':
                count=count+1
                stateq1(str)
    else:
        print('not a valid string')
def stateq2(str):
    global count
    print("Entered q2",count)
    if count<len(str):
        n=str[count]
        if len(n)==0:
            print('string is not accepted')
        else:
            if n=='0':
                count=count+1
                stateq0(str)
            if n=='1':
                count=count+1
                stateq3(str)
    else:
        print('not a valid string')
def stateq3(str):
    global count
    print("Entered q3",count)
    if count<len(str):
        n=str[count]
        if len(n)==0:
            print('string is not accepted')
        else:
            if n=='0':
                count=count+1
                stateq0(str)
            if n=='1':
                count=count+1
                stateq0(str)
    else:
        print("String is accepted")
str=input("Enter a string accepting 1 and 0 only: ")
count=-1
stateq0(str)