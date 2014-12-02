#!/usr/bin/env python

import antlr3
import antlr3.tree
from simpleLexer import *


""" Various custom AST node types that contain LLVM code generation methods.
"""


class EmitNode(antlr3.tree.CommonTree):
    def __str__(self):
        return self.emit()

    def emit(self):
        print "TYPE " + str(self.type) + " UNIMPLEMENTED"
        # for child in self.getChildren():
        #     print child.emit()


class BlockNode(EmitNode):
    def emit(self):
        # for child in self.getChildren():
        #     print child.emit()
        return '\n'.join([str(node) for node in self.getChildren()])


class SkipNode(EmitNode):
    def emit(self):
        return "SKIP"


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


class UnaryBoolOpNode(EmitNode):
    def emit(self):
        b = self.getChild(0)
        return self.text + " " + b.emit()


class BinaryBoolOpNode(EmitNode):
    def emit(self):
        children = self.getChildren()
        left = children[0].emit()
        right = children[1].emit()

        if self.getText().lower() == '&':
            return left + ' & ' + right
        elif self.getText().lower() == '|':
            return left + ' | ' + right
        else:
            raise Exception("Unrecognized binary boolean operator.")


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
        temp = ""  # TODO: TEMP VAR FOR STRING RETURN DEBUGGING
        children = self.getChildren()
        conditional = children[0]
        then_branch = children[1]
        else_branch = children[2]

        # Convert conditional to a boolean.
        conditional_bool = "conditional_bool = [" + str(conditional) + " == 0.0]"
        temp = '\n'.join([temp, conditional_bool])

        # Create blocks for the if/then cases.
        # TODO: Create branch function
        then_block = ""
        else_block = ""
        merge_block = ""

        # Emit conditional instruction.
        temp = '\n'.join([temp, "if conditional_bool GOTO THEN else GOTO ELSE"])

        # Emit THEN instructions at end of ELSE block.
        then_block = then_block + then_branch.emit()
        temp = '\n'.join([temp, then_block])
        temp = '\n'.join([temp, "GOTO merge block"])

        # Emitting then can change block, update then block to the block the
        # builder is currently in (for the Phi function).
        # TODO: Set then_block to current block

        # Emit ELSE instructions at end of ELSE block.
        else_block = else_block + else_branch.emit()
        temp = '\n'.join([temp, else_block])
        temp = '\n'.join([temp, "GOTO merge block"])

        # Emitting else can change block, update else block to the block the
        # builder is currently in (for the Phi function).
        # TODO: Set else_block to current block

        # Emit merge block.
        # TODO: Create phi node

        # TODO: return phi
        return temp


class WhileNode(EmitNode):
    def emit(self):
        return '\n'.join([str(node) for node in self.getChildren()])


class LlvmAdaptor(antlr3.tree.CommonTreeAdaptor):
    def createWithPayload(self, payload):
        if payload is None:
            return EmitNode(payload)

        t = payload.type
        if t == BLOCK:
            return BlockNode(payload)
        if t == SKIP:
            return SkipNode(payload)
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
        elif t == NOT:
            return UnaryBoolOpNode(payload)
        elif t in (AND, OR):
            return BinaryBoolOpNode(payload)
        elif t == GETS:
            return AssignmentNode(payload)
        elif t == IF:
            return IfElseThenNode(payload)
        elif t == WHILE:
            return WhileNode(payload)
        else:
            return EmitNode(payload)