grammar simple;

options{
	language=Python;
	output=AST;
	ASTLabelType=CommonTree;
	backtrack=true;
}
/* Arithmetic operators, in order of precedence. */
MULT	:	'*';
PLUS	:	'+';
MINUS	:	'-';

/* Boolean operators, in order of precedence. */
NOT     :	'not';
AND	:	'&';
OR	:	'|';
RELOP	:	('=' | '<' | '<=' | '>' | '>=');

/* If / else. */
IF	:	'if';
THEN	:	'then';
ELSE	:	'else';
ENDIF	:	'fi';
SKIP	:	'skip';

/* Do while. */
WHILE	:	'while';
DO	:	'do';
ENDWHILE:	'od';

/* Misc. */
GETS	:	':=';
SEMI	:	';';
LPAREN	:	'(';
RPAREN	:	')';
BLOCK	:	'block';

/* Atoms. */
BOOLEAN	:	('true' | 'false');
IDENT	:	('a'..'z' | 'A'..'Z')('a'..'z' | 'A'..'Z' | '0'..'9')*;
INTEGER	:	('0'..'9')+;

/* Ignore whitespace. */
WS	:	(' ' | '\t' | '\n' | '\r' | '\f')+ {$channel = HIDDEN;};


program
 	:	block
 	;

block
    :	statement+
        -> ^(BLOCK statement+)
    ;

/* Arithmetic expressions - craziness due to precendence! */
arith_expr
	:	mult_expr
	;
mult_expr
	:	add_expr (MULT^ add_expr)*
	;
add_expr 
	:	sub_expr (PLUS^ sub_expr)*
	;
sub_expr 
	:	arith_atom (MINUS^ arith_atom)*
	;
arith_atom
	:	(IDENT | INTEGER)
	|	LPAREN! arith_expr RPAREN!
	;

/* Boolean expressions - craziness due to precedence! */
bool_expr 
	:	and_expr
	;
and_expr 
 	:	or_expr (AND^ or_expr)*
 	;
or_expr
 	:	bool_atom (OR^ bool_atom)*
 	;
bool_atom
 	:	BOOLEAN
	|	NOT^ bool_atom
	|	LPAREN! bool_expr RPAREN!
	|	arith_expr RELOP^ INTEGER
	;

statement
    :   IDENT GETS^ arith_expr SEMI!
    |   SKIP SEMI!
    |   IF^ bool_expr THEN! block ELSE! block ENDIF! SEMI!
    |   WHILE^ bool_expr DO! block ENDWHILE! SEMI!
    ;