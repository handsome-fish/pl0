# 对块进行分析 <block> → [<condecl>][<vardecl>][<proc>]<body>

# 常量声明
def const_dec(ast):
    return ast[1]

# 变量声明
def var_dec(ast):
    return ast[2]

# 过程说明
def proc_dec(ast):
    return ast[3]

# 语句说明
def block_stmts(ast):
    return ast[4]