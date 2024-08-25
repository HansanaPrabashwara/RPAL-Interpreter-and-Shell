#!/usr/bin/env python

"""RPAL Programming Language Implementation for Group 0820 """

__author__ = "PERERA I.T.M. 210460V, PRABASHWARA D.G.H. 210483T"
__version__ = "0.0.1"
__status__ = "Draft"



import sys

from Parser.Parser import Parser
from Scanner.Scanner import Scanner
from ControlStructureBuilder.ControlStructures import ControlSuctureBuilder

from Interpreter.CSEMachine import CSEMachine


file_name = sys.argv[1]
AST = True if len(sys.argv) == 3 and sys.argv[2] == "-ast" else False
ST = True if len(sys.argv) == 3 and sys.argv[2] == "-st" else False
CS = True if len(sys.argv) == 3 and sys.argv[2] == "-cs" else False
STACK = True if len(sys.argv) == 3 and sys.argv[2] == "-stack" else False
ENV = True if len(sys.argv) == 3 and sys.argv[2] == "-env" else False


p = Parser(Scanner(file_name))
p.parse()

if p.errors.error_status:
    p.errors.print()
    sys.exit(1)
else:
    if AST:
        p.printAST()
    else:
        if ST:
            p.printST()
        else:
            p.standardize()
            c = ControlSuctureBuilder(p.ST)
            if CS:
                c.printCS()
            else:
                c.linerize()
                a = CSEMachine(c.control_structures,p.errors)
                a.apply_rules()
                if a.errors.error_status:
                    p.errors.print()
                    sys.exit(1)
                else:
                    if STACK:
                        for stack_instance in a.stack_log:
                            print(stack_instance.get_items())
                    elif ENV:
                        for i in a.environments:
                            print(i)
                    else:
                        a.print()

                        



