from ErrorHandler.ErrorHandler import ErrorHandler
from Scanner.Reader import Reader
from Scanner.Recognizer import Recognizer
from Scanner.Token import Token


class Scanner:
    """
    Scanner class to scan the source code.
    """

    def __init__(self, file_name):
        self.reader = Reader(file_name)
        self.source_list = self.reader.read_whole()
        self.token_list = []
        self.curr_index = 0
        self.last_index = len(self.source_list) -1
        self.recognizer = Recognizer()
        self.errors = ErrorHandler(self.reader,self.source_list)
        self.id_name = "IDENTIFIER"
        self.int_name = "INTEGER"
        self.operator_name = "OPERATOR"
        self.string_name = "STRING"
        self.delete_name = "DELETE"
        self.punctuation_name = "PUNCTUATION"
        self.screened = False

    def tokenize(self):
        """
        Read the first character or the second character from the source_list and call a separate function for each
        data type.
        :return: token list of the source code
        """
        while self.curr_index <= self.last_index:
            if self.recognizer.is_letter((self.source_list[self.curr_index])):
                self.handle_identifier()
            elif self.recognizer.is_digit((self.source_list[self.curr_index])):
                self.handle_integer()
            elif self.recognizer.is_single_quote(self.source_list[self.curr_index]):
                if self.curr_index != self.last_index:
                    # self.curr_index += 1
                    self.handle_string()
                    # if self.recognizer.is_single_quote(self.source_list[self.curr_index]):
                    #     self.handle_string()
                    # else:
                    #     self.errors.syntax_error(self.curr_index)
                    #     self.curr_index += 1
                else:
                    self.errors.syntax_error(self.curr_index)
                    self.curr_index += 1

            elif self.recognizer.is_slash(self.source_list[self.curr_index]):
                self.curr_index += 1
                if self.recognizer.is_slash(self.source_list[self.curr_index]):
                    self.curr_index += 1
                    self.handle_comment()
                    
                else:
                    self.curr_index -= 1
                    self.handle_operator()
                    
            elif self.recognizer.is_operator((self.source_list[self.curr_index])):
                self.handle_operator()
            elif self.recognizer.is_space(self.source_list[self.curr_index]) or self.recognizer.is_eol(
                    self.source_list[self.curr_index]) or self.recognizer.is_ht(self.source_list[self.curr_index]):
                self.handle_space()
            elif self.recognizer.is_punctuation(self.source_list[self.curr_index]):
                self.handle_punctuation()
            else:
                self.curr_index += 1
                self.errors.unrecognized_error(self.curr_index)

            if self.curr_index >= self.last_index:
                break

    def handle_identifier(self):
        """
        Handles identifier tokens.
        :return: Add identifier tokens to the token_list
        """
        identifier_value = self.source_list[self.curr_index]
        self.curr_index += 1
        while self.curr_index <= self.last_index and (self.recognizer.is_letter(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_digit(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_underscore(self.source_list[self.curr_index])):
            identifier_value += self.source_list[self.curr_index]
            self.curr_index += 1
            if self.curr_index == self.last_index:
                identifier_value += self.source_list[self.curr_index]
                self.token_list.append((self.id_name, identifier_value))
                return
        else:
            # if self.recognizer.is_space(self.source_list[self.curr_index]) or self.recognizer.is_ht(self.source_list[self.curr_index]) or self.recognizer.is_eol(self.source_list[self.curr_index]):
            self.token_list.append((self.id_name, identifier_value))
            
            # else:
                # self.errors.syntax_error(self.curr_index)

    def handle_integer(self):
        """
        Handles integer tokens.
        :return: Add integer tokens to the token_list
        """
        integer_value = self.source_list[self.curr_index]
        self.curr_index += 1
        while self.curr_index <= self.last_index and self.recognizer.is_digit(self.source_list[self.curr_index]):
            integer_value += self.source_list[self.curr_index]
            self.curr_index += 1
            if self.curr_index == self.last_index:
                integer_value += self.source_list[self.curr_index]
                self.token_list.append((self.int_name, integer_value))
                return
        
        else:
            # if self.recognizer.is_space(self.source_list[self.curr_index]) or self.recognizer.is_ht(self.source_list[self.curr_index]) or self.recognizer.is_eol(self.source_list[self.curr_index]) :
            self.token_list.append((self.int_name, integer_value))
            # else:
            #     self.errors.syntax_error(self.curr_index)
            

    def handle_operator(self):
        """
        Handles operator tokens.
        :return: Add operator tokens to the token_list
        """
        operator_value = self.source_list[self.curr_index]
        self.curr_index += 1
        while self.curr_index <= self.last_index and self.recognizer.is_operator(
                self.source_list[self.curr_index]) and self.curr_index <= self.last_index:
            operator_value += self.source_list[self.curr_index]
            self.curr_index += 1
            if self.curr_index == self.last_index:
                operator_value += self.source_list[self.curr_index]
                break
        else:
            # if self.recognizer.is_space(self.source_list[self.curr_index]) or self.recognizer.is_ht(self.source_list[self.curr_index]) or self.recognizer.is_eol(self.source_list[self.curr_index]) :
            self.token_list.append((self.operator_name, operator_value))
            # else:
            #     self.errors.syntax_error(self.curr_index)

    def handle_comment(self):
        """
        Handles comment tokens.
        :return: Add comment tokens to the token_list
        """
        comment_value = "//"
        while self.curr_index <= self.last_index and (
                self.recognizer.is_double_quote(self.source_list[self.curr_index]) or
                self.recognizer.is_punctuation(self.source_list[self.curr_index]) or
                self.recognizer.is_back_slash(self.source_list[self.curr_index]) or
                self.recognizer.is_space(self.source_list[self.curr_index]) or
                self.recognizer.is_letter(self.source_list[self.curr_index]) or
                self.recognizer.is_digit(self.source_list[self.curr_index]) or
                self.recognizer.is_operator(self.source_list[self.curr_index]) or
                self.recognizer.is_eol(self.source_list[self.curr_index])):

            comment_value += self.source_list[self.curr_index]
            self.curr_index += 1

            if self.recognizer.is_eol(self.source_list[self.curr_index - 1]):
                break

            if self.curr_index == self.last_index and self.recognizer.is_eol(self.source_list[self.curr_index]):
                comment_value += self.source_list[self.curr_index]
                break

        self.token_list.append((self.delete_name, comment_value))

    def handle_space(self):
        """
        Handles space tokens.
        :return: Add space tokens to the token_list
        """
        if self.curr_index > self.last_index:
            return
        space_value = self.source_list[self.curr_index]
        self.curr_index += 1
        while self.curr_index <= self.last_index and (self.recognizer.is_space(self.source_list[self.curr_index]) or 
                                                    self.recognizer.is_eol(self.source_list[self.curr_index]) or
                                                    self.recognizer.is_ht(self.source_list[self.curr_index])):
            space_value += self.source_list[self.curr_index]
            self.curr_index += 1
            if self.curr_index == self.last_index:
                space_value += self.source_list[self.curr_index]
                return
        self.token_list.append((self.delete_name, space_value))

    def handle_string(self):
        """
        Handles string tokens.
        :return: Add string tokens to the token_list
        """
        string_value = ""
        self.curr_index += 1

        while self.curr_index <= self.last_index and (self.recognizer.is_letter(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_digit(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_operator(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_back_slash(
                                                          self.source_list[self.curr_index]) or
                                                      self.recognizer.is_punctuation(
                                                          self.source_list[self.curr_index]) or
                                                      self.recognizer.is_space(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_eol(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_ht(self.source_list[self.curr_index]) or
                                                      self.recognizer.is_single_quote(self.source_list[self.curr_index])
                                                      ):
            if self.curr_index == self.last_index-1:
                if self.recognizer.is_single_quote(self.source_list[self.curr_index]):
                    self.curr_index += 1
                    if self.recognizer.is_single_quote(self.source_list[self.curr_index]):
                        string_value += self.source_list[self.curr_index]
                        self.token_list.append((self.string_name, string_value))
                        return
                    else:
                        self.errors.syntax_error(self.curr_index)
                        return
                else:
                    self.curr_index += 1
                    self.errors.syntax_error(self.curr_index)
                    return


            if self.recognizer.is_eol(self.source_list[self.curr_index]):
                self.errors.syntax_error(self.curr_index-1)
                return

            if self.recognizer.is_back_slash(self.source_list[self.curr_index]):
                string_value += self.source_list[self.curr_index]
                self.curr_index += 1

                if self.curr_index <= self.last_index and self.recognizer.is_after_back_slash(
                        self.source_list[self.curr_index]):
                    string_value += self.source_list[self.curr_index]
                    self.curr_index += 1

            # if self.recognizer.is_single_quote(self.source_list[self.curr_index]):
            #     self.curr_index += 1
            #     if self.recognizer.is_single_quote(self.source_list[self.curr_index]):
            #         self.curr_index += 1
            #         self.token_list.append((self.string_name, string_value))
            #         return
            #     else:
            #         self.errors.syntax_error(self.curr_index-1)
            #         self.curr_index += 1
            #         return

            if self.recognizer.is_single_quote(self.source_list[self.curr_index]):
                self.curr_index += 1
                self.token_list.append((self.string_name, string_value))
                return
                

            string_value += self.source_list[self.curr_index]
            self.curr_index += 1

    def handle_punctuation(self):
        """
        Handles punctuation tokens.
        :return: Add punctuation tokens to the token_list
        """
        self.token_list.append((self.punctuation_name, self.source_list[self.curr_index]))
        self.curr_index += 1
        return

    def screen(self):
        """
        Screening process for the created tokens
        """
        self.screened = True
        new_tokens = []
        # for token in self.token_list:
        #     if self.symbol_table.is_symbol(token[0]):
        #         self.token_list.remove(token)          #TODO: using the remove might not be the best idea. Think about another approch
        for token in self.token_list:
            if token[0] != self.delete_name:
                new_tokens.append(token)

        self.token_list = new_tokens

 
    def print(self, print_token = True):
        """
        Prints the token list
        """
        if self.errors.error_status:
            self.errors.print()
            print(f"\033[1;41m Scanning {'and Screening ' if self.screened else ''}exited with {len(self.errors.error_list)} error{'s' if len(self.errors.error_list) >1 else ''}. \033[0m")
        else:
            if print_token:
                for i in self.token_list:
                    print(i)
            print(f"\033[1;42m Scanning {'and Screening ' if self.screened else ''}finished sucessfullly. \033[0m")


    def get_tokens(self):
        """Returns the scanned and screened token list

        :return :list
        """
        self.tokenize()
        self.screen()
        tokens_list = []
        for i in self.token_list:
            tokens_list.append(Token(i[0],i[1]))
        return tokens_list

