from pyleri import *

class MyGrammar(Grammar):
    n=input('enter n')
    m=input('enter m')
    r_name=Regex('a{'+n+'}b{'+m+'}cb{'+m+'}a{'+n+'}')
#'i([\+ \* \-]i)*')
#[0-9]*( ){0,}([\+\-\/\*]( ){0,}[0-9]*( ){0,})*')
#'i[\+ \* \-]i')
#a*b*')
    k_hi=Keyword('E')
    START = Sequence(k_hi, r_name)
    
# Compile your grammar by creating an instance of the Grammar Class.
my_grammar = MyGrammar()
# Use the compiled grammar to parse 'strings'
print(my_grammar.parse('E i+i/i').is_valid) # => True