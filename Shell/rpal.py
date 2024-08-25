

from Parser.Parser import Parser
from Scanner.Scanner import Scanner
from ControlStructureBuilder.ControlStructures import ControlSuctureBuilder

from Interpreter.CSEMachine import CSEMachine


file_name = "run.rpal"

def run():
    p = Parser(Scanner(file_name))
    p.parse()

    if p.errors.error_status:
        print(p.errors.get_errors())
        return p.errors.get_errors()
     
    p.standardize()
    c = ControlSuctureBuilder(p.ST)
    c.linerize()
    a = CSEMachine(c.control_structures,p.errors)
    a.apply_rules()

    if a.errors.error_status:
        print(p.errors.get_errors())
        return p.errors.get_errors()
    else:
        return a.get_results()


