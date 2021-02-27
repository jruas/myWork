def menu():
    print('What would you like to do?')
    print('(a) Add new Student')
    print('(v) View Students')
    print('(q) Quit')
    choice=input('Type one letter a/v/q: ').strip()
    return choice

def toAdd():
    print('in adding')

def toView():
    print('in viewing')

choice=menu()
while (choice !='q'):
    if choice=="a":
        toAdd()
    elif choice=="v":
        doView()
    elif choice!="q":
     print('please select either a,v,q: ')
     choice=menu()



