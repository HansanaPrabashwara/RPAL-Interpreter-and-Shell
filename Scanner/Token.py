
class Token:
    """Token class to create token instances
    """
    def __init__(self, typeClass, value):
        self.keywords = ['let','in','fn','where','aug','or','not','gr','ge','ls','le','eq','ne','true','false','nil','dummy','within','and','rec']
        
        if value in self.keywords:
            self.key = "KEYWORD"
        else:
            # if typeClass == "PUNCTUATION":
            #     if value == "(":
            #         self.key = "("
            #     elif value == ")":
            #         self.key = ")"
            #     elif value == ",":
            #         self.key = ","
            #     elif value == ";":
            #         self.key = ";"
            # else:    
            self.key = typeClass
        self.val = value

    def __str__(self):
        return f"(<{self.key}>, {self.val})" 
    
    def __repr__(self):
        return f"(<{self.key}>, {self.val})" 