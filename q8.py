# ask the user for their age and whether they have a valid ID (yes/no).
# Print"Entry allowed" only if age >- 18 and they have a valid ID - using and directly, no nested if.
age = int(input('enter your age: '))
valid_id = input (' do you have valid ID ?(yes/no) : ')
if age >= 18 and valid_id == 'yes':
    print('Entry allowed')
else:
        print('Entry not allowed')
        