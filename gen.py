alp = "qwertyuiop1234567890asdfghjklzxcvbnm,./;'[]-=\\`~!@#$\%^&*()_+QWEERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"

password = input("Enter a password less than 6 digits: \t")

if len(password) > 6:
    print("Your password is greater than 6 digits!")

for i2 in range(len(alp)):
        file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
        test=""+alp[i2]

        if test == password:
            print("password found! "+test)
            quit()

for i in range(len(alp)):
    test1 = alp[i]
    for i2 in range(len(alp)):
        file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
        test=test1+alp[i2]

        if test == password:
            print("password found! "+test)
            quit()

for i3 in range(len(alp)):
    test2=alp[i3]
    for i in range(len(alp)):
        test1 = alp[i]
        for i2 in range(len(alp)):
            file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
            test=test2+test1+alp[i2]

            if test == password:
                print("password found! "+test)
                quit()

for i4 in range(len(alp)):
    test3=alp[i4]
    for i3 in range(len(alp)):
        test2=alp[i3]
        for i in range(len(alp)):
            test1 = alp[i]
            for i2 in range(len(alp)):
                file = open("/Users/jacob/Desktop/Code_Stuff/Projects/googlepass2/test2.txt", "a")
                test=test3+test2+test1+alp[i2]

                if test == password:
                    print("password found! "+test)
                    quit()
            
    
    