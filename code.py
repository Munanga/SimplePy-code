
class Baby:

    def __init__(self):
        self.fname = "Jane"
        self.lname = "Anderson"
        self.salary = 90000
        self._id = 334912310


    def set(self,value):
        self.salary = value

    @property
    def email(self):
        return self.fname + self.lname + "@ggu.com"

    def __str__(self):
        return self.fname + " " + "$" + str(self.salary)

Instance = Baby()
print(Instance.fname)
print(Instance.lname)
print(Instance.email)

Instance.lname = "Cooper"

print(Instance.fname)
print(Instance.lname)
print(Instance.email)
