correct_password = 'a123456'

x = 3
while x <= 3 and x > 0:
    password = input ('Please enter your password: ')
    if password == correct_password:
        print ('Login Successfully')
        break
    else:
        x = x - 1
        print ('Wrong password, you can try', x, "times." )
        
