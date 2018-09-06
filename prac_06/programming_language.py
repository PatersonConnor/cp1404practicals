
class ProgrammingLanguage:

    def __init__(self,Typing,Reflection,Year,Name):
        self.Name = Name
        self.typing = Typing
        self.Reflection = Reflection
        self.Year = Year

    def is_dynamic(self):
        if self.typing == "Dynamic":
            return True
        else:
            return False
    def __str__(self):
        return "Language:{}, Type:{}, Refletion:{}, Year:{}".format(self.typing,self.Reflection,self.year)
