class Person(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, graduateyear):
        self.graduateyear = graduateyear
        Person.__init__(self, fname, lname)


x = Student('Shatakshi', 'Shivhare', 2029)
x.display()
print(x.graduateyear)
