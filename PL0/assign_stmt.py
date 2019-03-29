# 对赋值语句进行分析 assign_stmt -> ident_token become_token expr

# 返回赋值左部标识符
def assign_left(ast):
    return ast[1]

# 返回赋值右部表达式
def assign_right(ast):
    return ast[2]