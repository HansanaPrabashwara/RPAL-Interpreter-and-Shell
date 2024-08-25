class Reader:
    """Read the source file 
    """
    def __init__(self, filename):
        self.file = filename
        self.str = ""
        self.lines = []
        try:
            source = open(filename, 'r')
            self.lines = source.readlines()
            self.lines[-1] += " "
            for line in self.lines:
                self.str += line
        except:
            # print(f"{colored("Unknown File ", color="red")} \n\t{colored(f"{filename}", color="black", on_color="on_white")}")
            print(f"\033[1;31mUnknown File\033[0m \n\t \033[30;47m{filename}\033[0m")
        
    def read_whole(self):
        """Read the whole file as a string

        Returns:
            String : All lines in the file
        """
        return self.str
    
    def find_line(self, index):
        """Given a index find the corresponding line and the corresponding line index of a character

        Args:
            index (int): index of the carater

        Returns:
            int, int: line number, linne index 
        """
        line = 0
        cummutative_index = len(self.lines[line])
        while(index > cummutative_index):
            line += 1
            cummutative_index += len(self.lines[line])
        return line+1, index-cummutative_index + len(self.lines[line])
    
    def read_lines(self):
        """Return the lined of the file as a list

        Returns:
            List: lines of the list
        """
        return self.lines

    def get_line(self, line_number):
        """Given the line number returns the line

        Args:
            line_number (int): line number 

        Returns:
            String: the correspondding line 
        """
        return self.lines[line_number]
