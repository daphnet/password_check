password = 'a123456'

i = 3 #remaing tries
while i > 0:
    pwd = input ('Please enter your password: ')
    if pwd == password:
        print ('Login Successfully')
        break #exit loop
    else:
        i = i - 1
        print ('Wrong password, you can try', i, "times." )
        
