# 对条件语句分析 if <lexp> then <statement>[else <statement>]
# if_stmt -> if_token cond then_token stmt else_token stmt


# 返回if语句的条件
def get_if_cond(ast):
    return ast[1]

# 返回then后语句
def get_if_then(ast):
    return ast[2]

# 返回else后语句
def get_if_else(ast):
    return ast[3]