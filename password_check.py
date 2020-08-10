password = 'a123456'

i = 3 #remaing tries
while i > 0:
    i = i - 1
    pwd = input ('Please enter your password: ')
    if pwd == password:
        print ('Login Successfully')
        break #exit loop
    else:
        print ('Wrong password.')
        if i > 0:
            print ('You can try', i, 'times.')
        else:
            print ('Your password has been locked.')
