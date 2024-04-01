# @classmethod
# @staticmethod

class MyClass:
    value: int = 10  # class attribute

    def __init__(self, name: str):
        self.name = name  # instance attribute

    # instance method
    def instance_method(self):
        return f"Instance method called for {self.name}"

    # class method
    @classmethod
    def class_method(cls):
        return f"Class method called for {cls.value}"

    # static method
    @staticmethod
    def static_method():
        return f"Static method called"


obj = MyClass('Python')
print(obj.instance_method())
print(obj.class_method())
print(MyClass.class_method())
