# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 simple.g 2014-11-29 20:23:06

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INTEGER=26
WHILE=16
ELSE=13
DO=17
NOT=7
MINUS=6
MULT=4
AND=8
EOF=-1
SEMI=20
LPAREN=21
IF=11
SKIP=15
RPAREN=22
WS=27
BOOLEAN=24
THEN=12
BLOCK=23
OR=9
ENDIF=14
IDENT=25
PLUS=5
GETS=19
ENDWHILE=18
RELOP=10

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "MULT", "PLUS", "MINUS", "NOT", "AND", "OR", "RELOP", "IF", "THEN", 
    "ELSE", "ENDIF", "SKIP", "WHILE", "DO", "ENDWHILE", "GETS", "SEMI", 
    "LPAREN", "RPAREN", "BLOCK", "BOOLEAN", "IDENT", "INTEGER", "WS"
]




class simpleParser(Parser):
    grammarFileName = "simple.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(simpleParser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)


    class program_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.program_return, self).__init__()

            self.tree = None




    # $ANTLR start "program"
    # simple.g:48:1: program : block ;
    def program(self, ):

        retval = self.program_return()
        retval.start = self.input.LT(1)

        root_0 = None

        block1 = None



        try:
            try:
                # simple.g:49:3: ( block )
                # simple.g:49:5: block
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_block_in_program311)
                block1 = self.block()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, block1.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "program"

    class block_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.block_return, self).__init__()

            self.tree = None




    # $ANTLR start "block"
    # simple.g:52:1: block : ( statement )+ -> ^( BLOCK ( statement )+ ) ;
    def block(self, ):

        retval = self.block_return()
        retval.start = self.input.LT(1)

        root_0 = None

        statement2 = None


        stream_statement = RewriteRuleSubtreeStream(self._adaptor, "rule statement")
        try:
            try:
                # simple.g:53:5: ( ( statement )+ -> ^( BLOCK ( statement )+ ) )
                # simple.g:53:7: ( statement )+
                pass 
                # simple.g:53:7: ( statement )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == IF or (SKIP <= LA1_0 <= WHILE) or LA1_0 == IDENT) :
                        alt1 = 1


                    if alt1 == 1:
                        # simple.g:0:0: statement
                        pass 
                        self._state.following.append(self.FOLLOW_statement_in_block326)
                        statement2 = self.statement()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            stream_statement.add(statement2.tree)


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1

                # AST Rewrite
                # elements: statement
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                if self._state.backtracking == 0:

                    retval.tree = root_0

                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 54:9: -> ^( BLOCK ( statement )+ )
                    # simple.g:54:12: ^( BLOCK ( statement )+ )
                    root_1 = self._adaptor.nil()
                    root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(BLOCK, "BLOCK"), root_1)

                    # simple.g:54:20: ( statement )+
                    if not (stream_statement.hasNext()):
                        raise RewriteEarlyExitException()

                    while stream_statement.hasNext():
                        self._adaptor.addChild(root_1, stream_statement.nextTree())


                    stream_statement.reset()

                    self._adaptor.addChild(root_0, root_1)



                    retval.tree = root_0



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "block"

    class arith_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.arith_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "arith_expr"
    # simple.g:58:1: arith_expr : mult_expr ;
    def arith_expr(self, ):

        retval = self.arith_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        mult_expr3 = None



        try:
            try:
                # simple.g:59:2: ( mult_expr )
                # simple.g:59:4: mult_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_mult_expr_in_arith_expr360)
                mult_expr3 = self.mult_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, mult_expr3.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arith_expr"

    class mult_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.mult_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "mult_expr"
    # simple.g:61:1: mult_expr : add_expr ( MULT add_expr )* ;
    def mult_expr(self, ):

        retval = self.mult_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MULT5 = None
        add_expr4 = None

        add_expr6 = None


        MULT5_tree = None

        try:
            try:
                # simple.g:62:2: ( add_expr ( MULT add_expr )* )
                # simple.g:62:4: add_expr ( MULT add_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_add_expr_in_mult_expr370)
                add_expr4 = self.add_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, add_expr4.tree)
                # simple.g:62:13: ( MULT add_expr )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == MULT) :
                        alt2 = 1


                    if alt2 == 1:
                        # simple.g:62:14: MULT add_expr
                        pass 
                        MULT5=self.match(self.input, MULT, self.FOLLOW_MULT_in_mult_expr373)
                        if self._state.backtracking == 0:

                            MULT5_tree = self._adaptor.createWithPayload(MULT5)
                            root_0 = self._adaptor.becomeRoot(MULT5_tree, root_0)

                        self._state.following.append(self.FOLLOW_add_expr_in_mult_expr376)
                        add_expr6 = self.add_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, add_expr6.tree)


                    else:
                        break #loop2



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "mult_expr"

    class add_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.add_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "add_expr"
    # simple.g:64:1: add_expr : sub_expr ( PLUS sub_expr )* ;
    def add_expr(self, ):

        retval = self.add_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        PLUS8 = None
        sub_expr7 = None

        sub_expr9 = None


        PLUS8_tree = None

        try:
            try:
                # simple.g:65:2: ( sub_expr ( PLUS sub_expr )* )
                # simple.g:65:4: sub_expr ( PLUS sub_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_sub_expr_in_add_expr389)
                sub_expr7 = self.sub_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, sub_expr7.tree)
                # simple.g:65:13: ( PLUS sub_expr )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == PLUS) :
                        alt3 = 1


                    if alt3 == 1:
                        # simple.g:65:14: PLUS sub_expr
                        pass 
                        PLUS8=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_add_expr392)
                        if self._state.backtracking == 0:

                            PLUS8_tree = self._adaptor.createWithPayload(PLUS8)
                            root_0 = self._adaptor.becomeRoot(PLUS8_tree, root_0)

                        self._state.following.append(self.FOLLOW_sub_expr_in_add_expr395)
                        sub_expr9 = self.sub_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, sub_expr9.tree)


                    else:
                        break #loop3



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "add_expr"

    class sub_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.sub_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "sub_expr"
    # simple.g:67:1: sub_expr : arith_atom ( MINUS arith_atom )* ;
    def sub_expr(self, ):

        retval = self.sub_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        MINUS11 = None
        arith_atom10 = None

        arith_atom12 = None


        MINUS11_tree = None

        try:
            try:
                # simple.g:68:2: ( arith_atom ( MINUS arith_atom )* )
                # simple.g:68:4: arith_atom ( MINUS arith_atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_arith_atom_in_sub_expr408)
                arith_atom10 = self.arith_atom()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, arith_atom10.tree)
                # simple.g:68:15: ( MINUS arith_atom )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == MINUS) :
                        alt4 = 1


                    if alt4 == 1:
                        # simple.g:68:16: MINUS arith_atom
                        pass 
                        MINUS11=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_sub_expr411)
                        if self._state.backtracking == 0:

                            MINUS11_tree = self._adaptor.createWithPayload(MINUS11)
                            root_0 = self._adaptor.becomeRoot(MINUS11_tree, root_0)

                        self._state.following.append(self.FOLLOW_arith_atom_in_sub_expr414)
                        arith_atom12 = self.arith_atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, arith_atom12.tree)


                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "sub_expr"

    class arith_atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.arith_atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "arith_atom"
    # simple.g:70:1: arith_atom : ( ( IDENT | INTEGER ) | LPAREN arith_expr RPAREN );
    def arith_atom(self, ):

        retval = self.arith_atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set13 = None
        LPAREN14 = None
        RPAREN16 = None
        arith_expr15 = None


        set13_tree = None
        LPAREN14_tree = None
        RPAREN16_tree = None

        try:
            try:
                # simple.g:71:2: ( ( IDENT | INTEGER ) | LPAREN arith_expr RPAREN )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((IDENT <= LA5_0 <= INTEGER)) :
                    alt5 = 1
                elif (LA5_0 == LPAREN) :
                    alt5 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # simple.g:71:4: ( IDENT | INTEGER )
                    pass 
                    root_0 = self._adaptor.nil()

                    set13 = self.input.LT(1)
                    if (IDENT <= self.input.LA(1) <= INTEGER):
                        self.input.consume()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set13))
                        self._state.errorRecovery = False

                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        mse = MismatchedSetException(None, self.input)
                        raise mse




                elif alt5 == 2:
                    # simple.g:72:4: LPAREN arith_expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN14=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_arith_atom437)
                    self._state.following.append(self.FOLLOW_arith_expr_in_arith_atom440)
                    arith_expr15 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr15.tree)
                    RPAREN16=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_arith_atom442)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "arith_atom"

    class bool_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.bool_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "bool_expr"
    # simple.g:76:1: bool_expr : and_expr ;
    def bool_expr(self, ):

        retval = self.bool_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        and_expr17 = None



        try:
            try:
                # simple.g:77:2: ( and_expr )
                # simple.g:77:4: and_expr
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_and_expr_in_bool_expr457)
                and_expr17 = self.and_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, and_expr17.tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bool_expr"

    class and_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.and_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "and_expr"
    # simple.g:79:1: and_expr : or_expr ( AND or_expr )* ;
    def and_expr(self, ):

        retval = self.and_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        AND19 = None
        or_expr18 = None

        or_expr20 = None


        AND19_tree = None

        try:
            try:
                # simple.g:80:3: ( or_expr ( AND or_expr )* )
                # simple.g:80:5: or_expr ( AND or_expr )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_or_expr_in_and_expr469)
                or_expr18 = self.or_expr()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, or_expr18.tree)
                # simple.g:80:13: ( AND or_expr )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == AND) :
                        alt6 = 1


                    if alt6 == 1:
                        # simple.g:80:14: AND or_expr
                        pass 
                        AND19=self.match(self.input, AND, self.FOLLOW_AND_in_and_expr472)
                        if self._state.backtracking == 0:

                            AND19_tree = self._adaptor.createWithPayload(AND19)
                            root_0 = self._adaptor.becomeRoot(AND19_tree, root_0)

                        self._state.following.append(self.FOLLOW_or_expr_in_and_expr475)
                        or_expr20 = self.or_expr()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, or_expr20.tree)


                    else:
                        break #loop6



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "and_expr"

    class or_expr_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.or_expr_return, self).__init__()

            self.tree = None




    # $ANTLR start "or_expr"
    # simple.g:82:1: or_expr : bool_atom ( OR bool_atom )* ;
    def or_expr(self, ):

        retval = self.or_expr_return()
        retval.start = self.input.LT(1)

        root_0 = None

        OR22 = None
        bool_atom21 = None

        bool_atom23 = None


        OR22_tree = None

        try:
            try:
                # simple.g:83:3: ( bool_atom ( OR bool_atom )* )
                # simple.g:83:5: bool_atom ( OR bool_atom )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_bool_atom_in_or_expr489)
                bool_atom21 = self.bool_atom()

                self._state.following.pop()
                if self._state.backtracking == 0:
                    self._adaptor.addChild(root_0, bool_atom21.tree)
                # simple.g:83:15: ( OR bool_atom )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == OR) :
                        alt7 = 1


                    if alt7 == 1:
                        # simple.g:83:16: OR bool_atom
                        pass 
                        OR22=self.match(self.input, OR, self.FOLLOW_OR_in_or_expr492)
                        if self._state.backtracking == 0:

                            OR22_tree = self._adaptor.createWithPayload(OR22)
                            root_0 = self._adaptor.becomeRoot(OR22_tree, root_0)

                        self._state.following.append(self.FOLLOW_bool_atom_in_or_expr495)
                        bool_atom23 = self.bool_atom()

                        self._state.following.pop()
                        if self._state.backtracking == 0:
                            self._adaptor.addChild(root_0, bool_atom23.tree)


                    else:
                        break #loop7



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "or_expr"

    class bool_atom_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.bool_atom_return, self).__init__()

            self.tree = None




    # $ANTLR start "bool_atom"
    # simple.g:85:1: bool_atom : ( BOOLEAN | NOT bool_atom | LPAREN bool_expr RPAREN | arith_expr RELOP INTEGER );
    def bool_atom(self, ):

        retval = self.bool_atom_return()
        retval.start = self.input.LT(1)

        root_0 = None

        BOOLEAN24 = None
        NOT25 = None
        LPAREN27 = None
        RPAREN29 = None
        RELOP31 = None
        INTEGER32 = None
        bool_atom26 = None

        bool_expr28 = None

        arith_expr30 = None


        BOOLEAN24_tree = None
        NOT25_tree = None
        LPAREN27_tree = None
        RPAREN29_tree = None
        RELOP31_tree = None
        INTEGER32_tree = None

        try:
            try:
                # simple.g:86:3: ( BOOLEAN | NOT bool_atom | LPAREN bool_expr RPAREN | arith_expr RELOP INTEGER )
                alt8 = 4
                LA8 = self.input.LA(1)
                if LA8 == BOOLEAN:
                    alt8 = 1
                elif LA8 == NOT:
                    alt8 = 2
                elif LA8 == LPAREN:
                    LA8_3 = self.input.LA(2)

                    if (self.synpred11_simple()) :
                        alt8 = 3
                    elif (True) :
                        alt8 = 4
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 8, 3, self.input)

                        raise nvae

                elif LA8 == IDENT or LA8 == INTEGER:
                    alt8 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # simple.g:86:5: BOOLEAN
                    pass 
                    root_0 = self._adaptor.nil()

                    BOOLEAN24=self.match(self.input, BOOLEAN, self.FOLLOW_BOOLEAN_in_bool_atom509)
                    if self._state.backtracking == 0:

                        BOOLEAN24_tree = self._adaptor.createWithPayload(BOOLEAN24)
                        self._adaptor.addChild(root_0, BOOLEAN24_tree)



                elif alt8 == 2:
                    # simple.g:87:4: NOT bool_atom
                    pass 
                    root_0 = self._adaptor.nil()

                    NOT25=self.match(self.input, NOT, self.FOLLOW_NOT_in_bool_atom514)
                    if self._state.backtracking == 0:

                        NOT25_tree = self._adaptor.createWithPayload(NOT25)
                        root_0 = self._adaptor.becomeRoot(NOT25_tree, root_0)

                    self._state.following.append(self.FOLLOW_bool_atom_in_bool_atom517)
                    bool_atom26 = self.bool_atom()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_atom26.tree)


                elif alt8 == 3:
                    # simple.g:88:4: LPAREN bool_expr RPAREN
                    pass 
                    root_0 = self._adaptor.nil()

                    LPAREN27=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_bool_atom522)
                    self._state.following.append(self.FOLLOW_bool_expr_in_bool_atom525)
                    bool_expr28 = self.bool_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_expr28.tree)
                    RPAREN29=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_bool_atom527)


                elif alt8 == 4:
                    # simple.g:89:4: arith_expr RELOP INTEGER
                    pass 
                    root_0 = self._adaptor.nil()

                    self._state.following.append(self.FOLLOW_arith_expr_in_bool_atom533)
                    arith_expr30 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr30.tree)
                    RELOP31=self.match(self.input, RELOP, self.FOLLOW_RELOP_in_bool_atom535)
                    if self._state.backtracking == 0:

                        RELOP31_tree = self._adaptor.createWithPayload(RELOP31)
                        root_0 = self._adaptor.becomeRoot(RELOP31_tree, root_0)

                    INTEGER32=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_bool_atom538)
                    if self._state.backtracking == 0:

                        INTEGER32_tree = self._adaptor.createWithPayload(INTEGER32)
                        self._adaptor.addChild(root_0, INTEGER32_tree)



                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "bool_atom"

    class statement_return(ParserRuleReturnScope):
        def __init__(self):
            super(simpleParser.statement_return, self).__init__()

            self.tree = None




    # $ANTLR start "statement"
    # simple.g:92:1: statement : ( IDENT GETS arith_expr SEMI | SKIP SEMI | IF bool_expr THEN block ELSE block ENDIF SEMI | WHILE bool_expr DO block ENDWHILE SEMI );
    def statement(self, ):

        retval = self.statement_return()
        retval.start = self.input.LT(1)

        root_0 = None

        IDENT33 = None
        GETS34 = None
        SEMI36 = None
        SKIP37 = None
        SEMI38 = None
        IF39 = None
        THEN41 = None
        ELSE43 = None
        ENDIF45 = None
        SEMI46 = None
        WHILE47 = None
        DO49 = None
        ENDWHILE51 = None
        SEMI52 = None
        arith_expr35 = None

        bool_expr40 = None

        block42 = None

        block44 = None

        bool_expr48 = None

        block50 = None


        IDENT33_tree = None
        GETS34_tree = None
        SEMI36_tree = None
        SKIP37_tree = None
        SEMI38_tree = None
        IF39_tree = None
        THEN41_tree = None
        ELSE43_tree = None
        ENDIF45_tree = None
        SEMI46_tree = None
        WHILE47_tree = None
        DO49_tree = None
        ENDWHILE51_tree = None
        SEMI52_tree = None

        try:
            try:
                # simple.g:93:5: ( IDENT GETS arith_expr SEMI | SKIP SEMI | IF bool_expr THEN block ELSE block ENDIF SEMI | WHILE bool_expr DO block ENDWHILE SEMI )
                alt9 = 4
                LA9 = self.input.LA(1)
                if LA9 == IDENT:
                    alt9 = 1
                elif LA9 == SKIP:
                    alt9 = 2
                elif LA9 == IF:
                    alt9 = 3
                elif LA9 == WHILE:
                    alt9 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 9, 0, self.input)

                    raise nvae

                if alt9 == 1:
                    # simple.g:93:9: IDENT GETS arith_expr SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    IDENT33=self.match(self.input, IDENT, self.FOLLOW_IDENT_in_statement554)
                    if self._state.backtracking == 0:

                        IDENT33_tree = self._adaptor.createWithPayload(IDENT33)
                        self._adaptor.addChild(root_0, IDENT33_tree)

                    GETS34=self.match(self.input, GETS, self.FOLLOW_GETS_in_statement556)
                    if self._state.backtracking == 0:

                        GETS34_tree = self._adaptor.createWithPayload(GETS34)
                        root_0 = self._adaptor.becomeRoot(GETS34_tree, root_0)

                    self._state.following.append(self.FOLLOW_arith_expr_in_statement559)
                    arith_expr35 = self.arith_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, arith_expr35.tree)
                    SEMI36=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement561)


                elif alt9 == 2:
                    # simple.g:94:9: SKIP SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    SKIP37=self.match(self.input, SKIP, self.FOLLOW_SKIP_in_statement572)
                    if self._state.backtracking == 0:

                        SKIP37_tree = self._adaptor.createWithPayload(SKIP37)
                        self._adaptor.addChild(root_0, SKIP37_tree)

                    SEMI38=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement574)


                elif alt9 == 3:
                    # simple.g:95:9: IF bool_expr THEN block ELSE block ENDIF SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    IF39=self.match(self.input, IF, self.FOLLOW_IF_in_statement585)
                    if self._state.backtracking == 0:

                        IF39_tree = self._adaptor.createWithPayload(IF39)
                        root_0 = self._adaptor.becomeRoot(IF39_tree, root_0)

                    self._state.following.append(self.FOLLOW_bool_expr_in_statement588)
                    bool_expr40 = self.bool_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_expr40.tree)
                    THEN41=self.match(self.input, THEN, self.FOLLOW_THEN_in_statement590)
                    self._state.following.append(self.FOLLOW_block_in_statement593)
                    block42 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block42.tree)
                    ELSE43=self.match(self.input, ELSE, self.FOLLOW_ELSE_in_statement595)
                    self._state.following.append(self.FOLLOW_block_in_statement598)
                    block44 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block44.tree)
                    ENDIF45=self.match(self.input, ENDIF, self.FOLLOW_ENDIF_in_statement600)
                    SEMI46=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement603)


                elif alt9 == 4:
                    # simple.g:96:9: WHILE bool_expr DO block ENDWHILE SEMI
                    pass 
                    root_0 = self._adaptor.nil()

                    WHILE47=self.match(self.input, WHILE, self.FOLLOW_WHILE_in_statement614)
                    if self._state.backtracking == 0:

                        WHILE47_tree = self._adaptor.createWithPayload(WHILE47)
                        root_0 = self._adaptor.becomeRoot(WHILE47_tree, root_0)

                    self._state.following.append(self.FOLLOW_bool_expr_in_statement617)
                    bool_expr48 = self.bool_expr()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, bool_expr48.tree)
                    DO49=self.match(self.input, DO, self.FOLLOW_DO_in_statement619)
                    self._state.following.append(self.FOLLOW_block_in_statement622)
                    block50 = self.block()

                    self._state.following.pop()
                    if self._state.backtracking == 0:
                        self._adaptor.addChild(root_0, block50.tree)
                    ENDWHILE51=self.match(self.input, ENDWHILE, self.FOLLOW_ENDWHILE_in_statement624)
                    SEMI52=self.match(self.input, SEMI, self.FOLLOW_SEMI_in_statement627)


                retval.stop = self.input.LT(-1)

                if self._state.backtracking == 0:

                    retval.tree = self._adaptor.rulePostProcessing(root_0)
                    self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "statement"

    # $ANTLR start "synpred11_simple"
    def synpred11_simple_fragment(self, ):
        # simple.g:88:4: ( LPAREN bool_expr RPAREN )
        # simple.g:88:4: LPAREN bool_expr RPAREN
        pass 
        self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_synpred11_simple522)
        self._state.following.append(self.FOLLOW_bool_expr_in_synpred11_simple525)
        self.bool_expr()

        self._state.following.pop()
        self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_synpred11_simple527)


    # $ANTLR end "synpred11_simple"




    # Delegated rules

    def synpred11_simple(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred11_simple_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_block_in_program311 = frozenset([1])
    FOLLOW_statement_in_block326 = frozenset([1, 11, 15, 16, 25])
    FOLLOW_mult_expr_in_arith_expr360 = frozenset([1])
    FOLLOW_add_expr_in_mult_expr370 = frozenset([1, 4])
    FOLLOW_MULT_in_mult_expr373 = frozenset([21, 25, 26])
    FOLLOW_add_expr_in_mult_expr376 = frozenset([1, 4])
    FOLLOW_sub_expr_in_add_expr389 = frozenset([1, 5])
    FOLLOW_PLUS_in_add_expr392 = frozenset([21, 25, 26])
    FOLLOW_sub_expr_in_add_expr395 = frozenset([1, 5])
    FOLLOW_arith_atom_in_sub_expr408 = frozenset([1, 6])
    FOLLOW_MINUS_in_sub_expr411 = frozenset([21, 25, 26])
    FOLLOW_arith_atom_in_sub_expr414 = frozenset([1, 6])
    FOLLOW_set_in_arith_atom426 = frozenset([1])
    FOLLOW_LPAREN_in_arith_atom437 = frozenset([21, 25, 26])
    FOLLOW_arith_expr_in_arith_atom440 = frozenset([22])
    FOLLOW_RPAREN_in_arith_atom442 = frozenset([1])
    FOLLOW_and_expr_in_bool_expr457 = frozenset([1])
    FOLLOW_or_expr_in_and_expr469 = frozenset([1, 8])
    FOLLOW_AND_in_and_expr472 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_or_expr_in_and_expr475 = frozenset([1, 8])
    FOLLOW_bool_atom_in_or_expr489 = frozenset([1, 9])
    FOLLOW_OR_in_or_expr492 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_bool_atom_in_or_expr495 = frozenset([1, 9])
    FOLLOW_BOOLEAN_in_bool_atom509 = frozenset([1])
    FOLLOW_NOT_in_bool_atom514 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_bool_atom_in_bool_atom517 = frozenset([1])
    FOLLOW_LPAREN_in_bool_atom522 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_bool_expr_in_bool_atom525 = frozenset([22])
    FOLLOW_RPAREN_in_bool_atom527 = frozenset([1])
    FOLLOW_arith_expr_in_bool_atom533 = frozenset([10])
    FOLLOW_RELOP_in_bool_atom535 = frozenset([26])
    FOLLOW_INTEGER_in_bool_atom538 = frozenset([1])
    FOLLOW_IDENT_in_statement554 = frozenset([19])
    FOLLOW_GETS_in_statement556 = frozenset([21, 25, 26])
    FOLLOW_arith_expr_in_statement559 = frozenset([20])
    FOLLOW_SEMI_in_statement561 = frozenset([1])
    FOLLOW_SKIP_in_statement572 = frozenset([20])
    FOLLOW_SEMI_in_statement574 = frozenset([1])
    FOLLOW_IF_in_statement585 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_bool_expr_in_statement588 = frozenset([12])
    FOLLOW_THEN_in_statement590 = frozenset([11, 15, 16, 25])
    FOLLOW_block_in_statement593 = frozenset([13])
    FOLLOW_ELSE_in_statement595 = frozenset([11, 15, 16, 25])
    FOLLOW_block_in_statement598 = frozenset([14])
    FOLLOW_ENDIF_in_statement600 = frozenset([20])
    FOLLOW_SEMI_in_statement603 = frozenset([1])
    FOLLOW_WHILE_in_statement614 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_bool_expr_in_statement617 = frozenset([17])
    FOLLOW_DO_in_statement619 = frozenset([11, 15, 16, 25])
    FOLLOW_block_in_statement622 = frozenset([18])
    FOLLOW_ENDWHILE_in_statement624 = frozenset([20])
    FOLLOW_SEMI_in_statement627 = frozenset([1])
    FOLLOW_LPAREN_in_synpred11_simple522 = frozenset([7, 21, 24, 25, 26])
    FOLLOW_bool_expr_in_synpred11_simple525 = frozenset([22])
    FOLLOW_RPAREN_in_synpred11_simple527 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("simpleLexer", simpleParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
