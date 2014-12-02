#!/usr/bin/env python

""" Various custom AST node types that contain LLVM code generation methods. """

import antlr3
import antlr3.tree
from llvm.core import Module, Constant, Type, Value, Function, Builder, FCMP_ULT

from simpleLexer import *

# GLOBALS (directly from tutorials)
g_llvm_module = Module.new('simple')  # Holds all of the IR code.
g_llvm_builder = None  # Builder created any time a function is entered.
tp_int = Type.int()


class EmitNode(antlr3.tree.CommonTree):
    def __str__(self):
        return str(self.emit())

    def emit(self):
        print "TYPE " + str(self.type) + " UNIMPLEMENTED"

    def getScope(self):
        """
        This will return the nearest BLOCK's scope. This is useful for updating
        a blocks scope from assignments.
        :rtype: dict[str, Value]
        """
        return self.parent.getScope()

    def getClosure(self):
        """
        Only Block nodes have variable scopes. Default behavior is to just ask
        for the parents closure. The root of the AST will always be a BLOCK, so
        it should always return from there.
        :rtype: dict[str, Value]
        """
        return self.parent.getClosure()


class BlockNode(EmitNode):
    def __init__(self, payload):
        super(BlockNode, self).__init__(payload)

        self.scope = {}
        """ The local scope for this block. """

        self.closure = list(self.parent.getClosure()).append(self.scope)
        """ :type : list[dict] """

    def __str__(self):
        return '\n'.join([str(node) for node in self.children])

    def emit(self):
        for child in self.children:
            child.emit()
            # NOTE: Blocks do not have a return value!

    def getScope(self):
        return self.scope

    def getClosure(self):
        return self.closure


class SkipNode(EmitNode):
    def __str__(self):
        return "SKIP"

    def emit(self):
        # Emit useless instruction as a no-op.
        zero = Constant.int(tp_int, 0)
        return g_llvm_builder.add(zero, zero, "addtmp")


class IntegerNode(EmitNode):
    def __str__(self):
        return self.text

    def emit(self):
        return Constant.int(tp_int, self.text)


class IdentifierNode(EmitNode):
    def __str__(self):
        return self.text

    def emit(self):
        c = self.getClosure()
        if self.text in c:
            return c[self.text]
        else:
            raise RuntimeError("Unknown variable name: " + self.text)


class UnaryNode(EmitNode):
    def __str__(self):
        return "".join(self.children)

    def emit(self):
        expr = self.children[0].emit()
        return g_llvm_builder.neg(expr.name, "negated_" + expr.name)


class BooleanNode(EmitNode):
    def __str__(self):
        return self.text

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
        # Check for the name in the current scope closure. If it does not exist,
        # add it. If it does exist TODO
        closure = self.getScope()
        name = self.children[0]


        right = self.children[1].emit()


        return


class ArithmeticNode(EmitNode):
    def emit(self):
        left = self.children[0].emit()
        right = self.children[1].emit()

        if self.getText() == '*':
            return g_llvm_builder.mul(left, right, 'multmp')
        elif self.getText() == '+':
            return g_llvm_builder.add(left, right, 'addtmp')
        elif self.getText() == '-':
            return g_llvm_builder.sub(left, right, 'subtmp')
        else:
            raise RuntimeError("Unrecognized arithmetic operator.")


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
        conditional_bool = "conditional_bool = [" + str(
            conditional) + " == 0.0]"
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
        elif t == UNARY:
            return UnaryNode(payload)
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