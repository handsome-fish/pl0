# 对write后表达式进行解析 write_stmt -> write_token expr
def write_expr(ast):
    return ast[1]