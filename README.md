# Javascript-Simulation

(1) Javascript Comments And Keywords:  In this exercise you will write token definition rules for all of the tokens in our subset of JavaScript *except* IDENTIFIER, NUMBER and STRING. In addition, you will handle // end of line comments as well as /* delimited comments */. We will assume that JavaScript is case sensitive and that keywords like 'if' and 'true' must be written in lowercase. There are 26 possible tokens that you must handle. The 'tokens' variable below has been initialized below, listing each token's formal name (i.e., the value of token.type). In addition, each token has its associated textual string listed in a comment. For example, your lexer must convert && to a token with token.type 'ANDAND' (unless the && is found inside a comment). 

Hint 1: Use an exclusive state for /* comments */. You may want to define t_comment_ignore and t_comment_error as well. 

(2) Javascript Numbers And Strings:  In this exercise you will finish out the token definitions for JavaScript by handling Numbers, Identifiers and Strings. We have split the lexing of JavaScript into two exercises so that you have a chance to demonstrate your mastery of the concepts independently (i.e., so that you can get one of them right even if the other proves difficult). We could easily make a full JavaScript lexer by putting all of the rules together. For this assignment, a JavaScript IDENTIFIER must start with an upper- or lower-case character. It can then contain any number of upper- or lower-case characters or underscores. Its token.value is the textual string of the identifier. 

      Yes:    my_age
      Yes:    cRaZy
      No:     _starts_with_underscore

For this assignment, a JavaScript NUMBER is one or more digits. A NUMBER can start with an optional negative sign. A NUMBER can contain a decimal point, which can then be followed by zero or more additional digits. Do not worry about hexadecimal (only base 10 is allowed in this problem). The token.value of a NUMBER is its floating point value (NOT a string).
      
      Yes:    123
      Yes:    -456
      Yes:    78.9
      Yes:    10.
      No:     +5
      No:     1.2.3

For this assignment, a JavaScript STRING is zero or more characters contained in double quotes. A STRING may contain escaped characters. Notably, \" does not end a string. The token.value of a STRING is its contents (not including the outer double quotes). 
      
      Yes:    "hello world"
      Yes:    "this has \"escaped quotes\""
      No:     "no"t one string" 

Hint: float("2.3") = 2.3

(3) Euclids Algorithm:  
Format: Submit JavaScript Code
In mathematics, because 8 divides 24 evenly, we say that 8 is a divisor* of 24. When computing, it is often useful to find the largest divisor that two numbers have in common. For example, 36 and 24 are both divisible by 2, 3, 4, and 12: the greatest divisor that they have in common is 12. It turns out that finding common divisors for numbers is critical for modern cryptography, including public-key crypto systems such as RSA: a backbone of internet commerce. Perhaps the oldest algorithm known -- ever! -- is for computing the greatest common divisor of two positive numbers. It is attributed to the Greek mathematician Euclid around 300 BCE. Here's how it goes: 
You are computing the greatest common divisor ("gcd") of two positive integers called "a" and "b". The gcd can be computed recursively (or iteratively) using the following three rules: 

      gcd(a,b) = a                    if a == b
      gcd(a,b) = gcd(a-b,b)           if a > b
      gcd(a,b) = gcd(a,b-a)           if a < b 

Write a JavaScript (_not_ Python) program that declares a function called gcd that accepts two positive integer arguments a and b and returns their greatest common divisor. Store your function in a variable called javascriptcode.

(4) Up To Ten:  Define a JavaScript function that embodies the same functionality as the Python code.
