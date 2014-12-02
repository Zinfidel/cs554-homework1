#!/usr/bin/env python

""" Converts an abstract syntax tree (AST) produced by ANTLR3 into LLVM code,
    and produces an executable.
"""
from nodes import LlvmAdaptor, tp_int, g_llvm_builder, g_llvm_module

# ANTLR
import antlr3
import antlr3.tree
from simpleLexer import simpleLexer
from simpleParser import simpleParser

# LLVM
from llvm.core import Type, Constant, Builder


# Read an input file, lex, parse, and produce a tree.
test_input = open("input/input1.txt").read()
charStream = antlr3.StringStream(test_input)
lexer = simpleLexer(charStream)
tokenStream = antlr3.CommonTokenStream(lexer)
parser = simpleParser(tokenStream)
llvmAdaptor = LlvmAdaptor()
parser.setTreeAdaptor(llvmAdaptor)
ast = parser.program().tree

# print ast

# Create main function.
#
# Create the main function signature and add it to the module.
# Signature: int main()
tp_main = Type.function(tp_int, [])
f_main = g_llvm_module.add_function(tp_main, "main")

# Set up the entry block for the main function and create a builder for it.
entry_block = f_main.append_basic_block("entry")
g_llvm_builder = Builder.new(entry_block)

ast.emit()
# TODO: Have to do something with blocks here?

# Exit with return code 0 (RET_SUCCESS).
g_llvm_builder.ret(Constant.int(tp_int, 0))

print g_llvm_module