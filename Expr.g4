grammar Expr;
SPACES
 : [ \t] -> skip;
FUN: 'fun';
MAIN: 'main';
NEWLINE : [\r\n]+ ;

INT     : [0-9]+ ;
BOOL : ('true'|'false');
STRING: '"' .*? '"';

IDENT   : [a-zA-Z]+ ;

prog:  FUN MAIN '(' ')' '{' NEWLINE ((stmt NEWLINE)*) '}'
    ;
stmt: 'print' '(' printexp=expr ')'
    | 'if' if_condition=expr '{' NEWLINE ((stmt NEWLINE)*) '}'
    | 'while' while_condition=expr '{' NEWLINE ((stmt NEWLINE)*) '}'
    | ident=IDENT ('=') assign=expr
    ;
expr:   left=expr op=('*'|'/') right=expr // MulExpression | DivExpression
    |   left=expr op=('+'|'-') right=expr // AddExpression | SubExpression
    |   left=expr op=('<' | '>' | '==' | '!=') right=expr // LessExp | MoreExp | EqualExp | NotEqualExp
    |   value=INT // NumberExpression
    |   '(' exp=expr ')' // BraceExpression
    |   bool=BOOL // BoolExpression
    |   string=STRING // StrExpression
    |   ident=IDENT // IdentExpression
    ;