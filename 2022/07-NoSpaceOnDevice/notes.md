Good article about class methods (especially their inheritance).  
    - See:  https://pynative.com/python-class-method/#:~:text=Delete%20Class%20Methods-,What%20is%20Class%20Method%20in%20Python,the%20object%20of%20the%20class.


From:  https://stackoverflow.com/questions/30105134/initialize-child-class-with-parent

---
class Parent(object):
    def __init__(self, *args, **kwargs):
        self.init_args = {'args':args, 'kwargs':kwargs}
        self.children = list()
        ...  # whatever else a Parent does

    def make_child(self, child_cls, *args, **kwargs):
        if args is None:
            args = self.init_args['args']
        if kwargs is None:
            kwargs = self.init_args['kwargs']
        child = child_cls(self, *args, **kwargs)
        self.children.append(child)
        return child


class Child(Parent):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        ...  # whatever else a Child does
 DEMO

>>> p = Parent()
>>> c = p.make_child(Child)
>>> c in p.children
True
---