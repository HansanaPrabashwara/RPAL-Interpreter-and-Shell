
class Recognizer:
    """
    Given A char recognize the class of the char
    """

    def __init__(self):
        self.num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.punctuation = ['(', ')', ';', ',']
        self.letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
                            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.operator_list = ['+', '-', '*', '<', '>', '&', '.', '@', '/', ':', '=', '~', '|', '$', '!', '#', '%', '^',
                              '_', '[', ']', '{', '}', '"', '`', '?']
        self.after_back_slash = ['t', 'n', '\\', '"', ]

    def is_digit(self, char):
        """
        Return True if the character is numeric
        :param char:
        :return: Boolean
        """
        if char in self.num_list:
            return True
        return False

    @staticmethod
    def is_space(char):
        """
        Return True if the char is a space
        :return: Boolean
        """
        if char == " " or char == "\t":
            return True
        return False

    def is_punctuation(self, char):
        """
        Return True if the char is a punctuation
        :param char:
        :return: Boolean
        """
        if char in self.punctuation:
            return True
        return False

    def is_letter(self, char):
        """
        Return True if the character is a letter
        :param char:
        :return: Boolean
        """
        if char in self.letter_list:
            return True
        return False

    def is_operator(self, char):
        """
        Return True if the character is an operator_symbol
        :param self
        :param char
        :return: Boolean
        """
        if char in self.operator_list:
            return True
        return False

    @staticmethod
    def is_eol(char):
        """
        Return True if the chat is the end of the line character
        :param char:
        :return: Boolean
        """
        if char == "\n":
            return True
        return False

    @staticmethod
    def is_underscore(char):
        """
        Return True if the char is an underscore
        :return: Boolean
        """
        if char == "_":
            return True
        return False

    @staticmethod
    def is_slash(char):
        """
        Return True if the char is a slash
        :param char:
        :return: Boolean
        """
        if char == "/":
            return True
        return False

    @staticmethod
    def is_back_slash(char):
        """
        Return True if the char is a backslash
        :param char:
        :return: Boolean
        """
        if char == "\u005c":
            return True
        return False

    def is_after_back_slash(self, char):
        """
        Return True if the char is a
        :return:
        """
        if char in self.after_back_slash:
            return True
        return False

    @staticmethod
    def is_double_quote(char):
        """
        Return True if the char is a double quote
        :param char:
        :return:
        """
        if char == '"':
            return True
        return False

    @staticmethod
    def is_single_quote(char):
        """
        Return True if the char is a double quote
        :param char:
        :return:
        """
        if char == "'":
            return True
        return False
    
    @staticmethod
    def is_ht(char):
        if char == '\t':
            return True
        return False
