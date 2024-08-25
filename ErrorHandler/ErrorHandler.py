class ErrorHandler:
    """
    Handles errors during scanning screening, parsing and cse matchine executing
    """

    def __init__(self, reader=None ,source_list=None):
        self.reader = reader
        self.error_status = False
        self.source_list = source_list
        self.error_list = []

    def syntax_error(self, index):
        """
        Handles Syntax Errors
        :param index: Error Index
        :return: Adds error message to error_list
        """
        self.error_status = True
        line_no,line_index = self.reader.find_line(index)
        error_string = f"\033[1;31mSyntax Error\033[0m in line {line_no} : {line_index} \n\t{self.reader.get_line(line_no-1)[:line_index]}\033[30;47m{self.reader.get_line(line_no-1)[line_index]}\033[0m{self.reader.get_line(line_no-1)[line_index+1:-1]}"
        self.error_list.append(error_string)

    def unrecognized_error(self, index):
        """
        Handles Unrecognized Characters
        :param index: Error Index
        :return: Adds error message to error_list
        """
        self.error_status = True
        line_no,line_index = self.reader.find_line(index)
        error_string = f"\033[1;31mUnrecognized Character\033[0m in line {line_no} : {line_index} \n\t{self.reader.get_line(line_no-1)[:line_index]}\033[30;47m{self.reader.get_line(line_no-1)[line_index]}\033[0m{self.reader.get_line(line_no-1)[line_index+1:-1]}"
        self.error_list.append(error_string)

    
    def parse_error(self, error):
        """
        Handles Errors During parsing
        :param error: Error string
        :return: Adds error message to error_list
        """

        self.error_status = True
        error_string = f"\033[1;31mParsing Error\033[0m \n\t{error}\033[0m"
        self.error_list.append(error_string)

    def unsupported_operands(self, operation, types):
        """
        Handles errors occur during the binary and unary operations 
        :param 
            operation: Operation name
            :types : Error string including type
        :return: Adds error message to error_list
        """
        self.error_status = True
        error_string = f"\033[1;31mUnsupported Operand Types for {operation}\033[0m \n\t{types}\033[0m"
        self.error_list.append(error_string)

    def zero_division_error(self, operand1):
        """
        Handles division by zero error
        :param 
            :operand1: Operand which get divided by zero
        :return: Adds error message to error_list
        """
        self.error_status = True
        error_string = f"\033[1;31mZero Divison Error\033[0m \n\tCannot divide {operand1} from 0\033[0m"
        self.error_list.append(error_string)
    
    def print(self):
        """
        Print the error list if there are errors.
        :return: Errors
        """
        if self.error_status:
            for error in self.error_list:
                print(error)

    def get_errors(self):
        """
        Get the error list
        :return: Errors
        """
        return self.error_list
