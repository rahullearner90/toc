import re
#Regular expression for string containing exactly 3 b's in string
data=input('Enter string containing a and b only :')
result=re.match(r'a*ba*ba*ba*',data)
if result:
    print(data, ' is accepted.')
else:
    print(data,' is not accepted.')


#Regular expression for string containing starting with a followed by any number b and ending in a
data=input('Enter string containing a and b only :')
result=re.match(r'ab*a$',data)
if result:
    print(data, ' is accepted.')
else:
    print(data,' is not accepted.')

#regular expression for the language accepting all the string which are starting with 1 and ending with 0, over ∑ = {0, 1}.
#1(0/1)*0
#the regular expression for the language containing the string in which every 0 is immediately followed by 11
#^(011)(0/1)*