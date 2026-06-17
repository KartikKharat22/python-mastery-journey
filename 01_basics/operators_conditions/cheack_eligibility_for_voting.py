person_age = int(input('Enter the age of person: '))
if person_age >= 18:
    voter_id = input('Do you have a voter id card (y/n) : ')
    if voter_id == 'y':
        print('You can do vote.')
    else:
        print("You can't vote.\nyou need a voting id !")
else:
    print("You can't vote \nYou are under age ")

