# @classmethod
# @staticmethod

class MyClass:
    value = 10  # class attribute

    def __init__(self, name: str):
        self.name = name  # instance attribute

    # instance method
    def instance_method(self):
        return f"Instance method called for {self.name}"


obj = MyClass('Python')
