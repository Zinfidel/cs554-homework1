#!/usr/bin/env python

import antlr3
import antlr3.tree
from simpleLexer import *


""" Various custom AST node types that contain LLVM code generation methods.
"""


class EmitNode(antlr3.tree.CommonTree):
    def emit(self):
        print "UNIMPLEMENTED"
        for child in self.getChildren():
            print child.emit()


class BlockNode(EmitNode):
    def emit(self):
        for child in self.getChildren():
            print child.emit()


class IntegerNode(EmitNode):
    def emit(self):
        return self.getText()


class IdentifierNode(EmitNode):
    def emit(self):
        return self.getText()


class BooleanNode(EmitNode):
    def emit(self):
        if self.getText().lower() == "true":
            return "True"
        elif self.getText().lower() == "false":
            return "False"
        else:
            raise Exception("Unrecognized boolean value.")


class AssignmentNode(EmitNode):
    def emit(self):
        children = self.getChildren()
        left = children[0].emit()
        right = children[1].emit()
        return left + " := " + right


class ArithmeticNode(EmitNode):
    def emit(self):
        children = self.getChildren()
        left = children[0].emit()
        right = children[1].emit()

        if self.getText() == '*':
            return left + ' * ' + right
        elif self.getText() == '+':
            return left + ' + ' + right
        elif self.getText() == '-':
            return left + ' - ' + right
        else:
            raise Exception("Unrecognized arithmetic operator.")


class RelationalNode(EmitNode):
    def emit(self):
        children = self.getChildren()
        left = children[0].emit()
        right = children[1].emit()

        if self.getText() == '=':
            return left + ' = ' + right
        elif self.getText() == '<':
            return left + ' < ' + right
        elif self.getText() == '<=':
            return left + ' <= ' + right
        elif self.getText() == '>':
            return left + ' > ' + right
        elif self.getText() == '>=':
            return left + ' >= ' + right
        else:
            raise Exception("Unrecognized relational operator.")


class IfElseThenNode(EmitNode):
    def emit(self):
        children = self.getChildren()
        conditional = children[0].emit()
        then_block = children[1].emit()
        else_block = children[2].emit()

        # Convert conditional to a boolean
        # TODO


class LlvmAdaptor(antlr3.tree.CommonTreeAdaptor):
    def createWithPayload(self, payload):
        if payload is None:
            return EmitNode(payload)

        t = payload.type
        if t == BLOCK:
            return BlockNode(payload)
        elif t == INTEGER:
            return IntegerNode(payload)
        elif t == IDENT:
            return IdentifierNode(payload)
        elif t in (MULT, PLUS, MINUS):
            return ArithmeticNode(payload)
        elif t == RELOP:
            return RelationalNode(payload)
        elif t == BOOLEAN:
            return BooleanNode(payload)
        elif t == GETS:
            return AssignmentNode(payload)
        elif t == IF:
            return IfElseThenNode(payload)
        else:
            return EmitNode(payload)