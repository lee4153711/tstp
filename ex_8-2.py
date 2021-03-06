with open('ex_8-2.txt','w') as f:
    name = input('what your name?: ')
    age = input('how old are you?: ')
    gender = input('what is gender?: ')
    f.write(f'name:{name}\nage:{age}\ngender:{gender}')
    
