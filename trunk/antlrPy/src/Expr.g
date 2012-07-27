grammar Expr;

options {
    language=Python;
    output=AST;
    ASTLabelType=CommonTree;
}

prog	: ( stat //{print $stat.tree.toStringTree();} 
			)+ ;

stat	:	(  expr  FIN       ->  expr )
	    |	(  ID '=' expr  FIN ->  ^('=' ID expr) )
	    ;

expr	:	multExpr (('+'^|'-'^) multExpr)*
	;

multExpr
	:	atom ('*'^ atom)*
	;

atom	:	INT
	|	ID
	|	'('! expr ')'!
	;

ID	:	('a'..'z'|'A'..'Z')+ ;

INT	:	'0'..'9'+ ;

//NEWLINE	:	'\r'? '\n' ;
FIN	:	'%' ;

WS	:	(' '|'\t'|'\n'|'\r')+ {self.skip()} ;