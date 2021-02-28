students=[]
def readModules():
    return []
def doAdd(students):
    currentStudent={}
    currentStudent['name']=input('enter name: ')
    currentStudent['modules']=input('enter module: ')

    students.append(currentStudent)

#test
doAdd(students)
print(students)