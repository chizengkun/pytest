class person():
    def walk(self):
        print('walk')
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def age(self):
        return 23

class student(person):
    #__slots__ = ('name','age')
    pass


s = student()
s.name = 'jpython'
#s.age = 10
print( s.age)