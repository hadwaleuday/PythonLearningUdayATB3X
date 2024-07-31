class Parent:
    gold_parent = "2kg"

    def parent_House(self):
        print("Parent 2BHK")


class Child(Parent):
    gold_child = "1kg"

    def child_House(self):
        print("Child 1BHK")

#child object accessing its class

child_object = Child()
child_object.child_House()
print(child_object.gold_child)


#child object accessing parents class
child_object.parent_House()
print(child_object.gold_parent)

