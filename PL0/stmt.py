# 返回第一段语句
def get_stmt(ast):
    return ast[1]

# 返回第二段语句
def get_next_stmt(ast):
    return ast[2]