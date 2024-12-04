class Obj:
    def __init__(self,name,branch):
        self.name=name;
        self.branch=branch;
    def study(self):
        print("studying"+" "+self.name+" bachelor degree")
Name=Obj("k","cse")
Name.study()
