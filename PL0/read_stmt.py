# 对read后语句进行解析 read_stmt -> read_token ident_token

def read_ident(ast):
    return ast[1]