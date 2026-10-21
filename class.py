class animal:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def get_name(self,name):
        self.name=name
        name=input("Enter your name:")
    def get_height(self,height):
        self.height=height
        height=input("Enter your height:")

    def display_info(self):
        print(f"Name:{self.name},Height:{self.height}")
animal1=animal("Dog",20)
animal1.display_info()