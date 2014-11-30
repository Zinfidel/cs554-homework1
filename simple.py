#!/usr/bin/env python

""" Converts an abstract syntax tree (AST) produced by ANTLR3 into LLVM code,
    and produces an executable.
"""
from nodes import LlvmAdaptor

import antlr3
import antlr3.tree
from simpleLexer import simpleLexer
from simpleParser import simpleParser


# Read an input file, lex, parse, and produce a tree.
test_input = open("input/input1.txt").read()
charStream = antlr3.StringStream(test_input)
lexer = simpleLexer(charStream)
tokenStream = antlr3.CommonTokenStream(lexer)
parser = simpleParser(tokenStream)
llvmAdaptor = LlvmAdaptor()
parser.setTreeAdaptor(llvmAdaptor)
ast = parser.program().tree

ast.emit()
