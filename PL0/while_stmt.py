# 对循环语句分析 while <lexp> do <statement>

def get_while_cond(ast):
    return ast[1]

def get_while_stmt(ast):
    return ast[2]