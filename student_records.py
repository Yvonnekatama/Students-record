def print_waiting(*a_list,**a_dict):
    for person in a_list:
        for student, info in a_dict.items():
            if person==student:
                print( person + ':')
                for key,value in info.items():
                    print(key +'=' + str(value))
                print()

waiting_list=['Eunice','Paul','John','Mary','Popo']
students_dict={'Eunice':{'age':24,'weight':50},
'celine':{'age':23,'weight':58},
'Popoh':{'age':24,'weight':56},
'John':{'age':24,'weight':70}}

print('These students are admited.')
print_waiting(*waiting_list,**students_dict)