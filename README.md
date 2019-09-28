# Javascript-Simulation

(1) Javascript Comments And Keywords:  In this exercise you will write token definition rules for all of the tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and STRING. In addition, you will handle // end of line comments as well as /* delimited comments */. We will assume that JavaScript is case sensitive and that keywords like 'if' and 'true' must be written in lowercase. There are 26 possible tokens that you must handle. The 'tokens' variable below has been initialized below, listing each token's formal name (i.e., the value of token.type). In addition, each token has its associated textual string listed in a comment. For example, your lexer must convert && to a token with token.type 'ANDAND' (unless the && is found inside a comment). 

Hint 1: Use an exclusive state for /* comments */. You may want to define t_comment_ignore and t_comment_error as well. 
