# 对call语句进行分析 call_stmt -> call_token ident_token

# 返回call后标识符
def call_proc(ast):
    return ast[1]