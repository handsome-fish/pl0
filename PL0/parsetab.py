
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'become_token begin_token call_token comma_token const_token divide_token do_token else_token end_token eql_token geq_token grt_token ident_token if_token leq_token les_token lparent_token minus_token mul_token neq_token number_token odd_token period_token plus_token proc_token read_token rparent_token semicolom_token then_token var_token while_token write_tokenprogram : block period_tokenblock : con_dec var_dec proc_dec stmtcon_dec : const_token ident_token eql_token number_token con_dec_cdr semicolom_token\n               | empty\n    con_dec_cdr : comma_token ident_token eql_token number_token con_dec_cdr\n                   | empty\n    var_dec : var_token ident_token var_dec_cdr semicolom_token\n               | empty\n    var_dec_cdr : comma_token ident_token var_dec_cdr\n                   | empty\n    proc_dec : proc_token ident_token semicolom_token block semicolom_token proc_dec_cdr\n                | empty\n    proc_dec_cdr : proc_token ident_token semicolom_token block semicolom_token proc_dec_cdr\n                    | empty\n    stmt : assign_stmt\n            | call_stmt\n            | begin_stmt\n            | if_stmt\n            | while_stmt\n            | read_stmt\n            | write_stmt\n            | empty\n    assign_stmt : ident_token become_token exprcall_stmt : call_token ident_tokenbegin_stmt : begin_token stmt begin_stmt_cdr end_tokenbegin_stmt_cdr : semicolom_token stmt begin_stmt_cdr\n                      | empty\n    if_stmt : if_token cond then_token stmt\n               | if_token cond then_token stmt else_token stmt\n    while_stmt : while_token cond do_token stmtread_stmt : read_token ident_tokenwrite_stmt : write_token exprcond : odd_token expr\n            | expr cmp expr\n    cmp : eql_token\n           | les_token\n           | leq_token\n           | grt_token\n           | geq_token\n           | neq_token\n    expr : flag no_flag_expr\n            | no_flag_expr\n    no_flag_expr : term plus_token term\n       no_flag_expr : term minus_token term\n       no_flag_expr : term\n    flag : plus_token\n            | minus_token\n    term : factorterm : factor mul_token term\n       term : factor divide_token term\n    factor : ident_tokenfactor : number_tokenfactor : lparent_token expr rparent_tokenempty : '
    
_lr_action_items = {'const_token':([0,55,106,],[4,4,4,]),'var_token':([0,3,5,55,83,106,],[-54,8,-4,-54,-3,-54,]),'proc_token':([0,3,5,7,9,55,56,83,95,106,108,],[-54,-54,-4,12,-8,-54,-7,-3,99,-54,99,]),'ident_token':([0,3,4,5,7,8,9,11,12,13,26,27,28,29,30,31,34,37,41,43,45,46,51,55,56,59,63,65,67,68,69,70,71,72,73,75,76,77,78,80,83,95,98,99,100,101,106,108,109,],[-54,-54,10,-4,-54,14,-8,25,32,-12,38,25,49,49,53,49,57,49,49,49,-46,-47,49,-54,-7,84,25,25,49,-35,-36,-37,-38,-39,-40,49,49,49,49,25,-3,-54,25,104,-11,-14,-54,-54,-13,]),'call_token':([0,3,5,7,9,11,13,27,55,56,63,65,80,83,95,98,100,101,106,108,109,],[-54,-54,-4,-54,-8,26,-12,26,-54,-7,26,26,26,-3,-54,26,-11,-14,-54,-54,-13,]),'begin_token':([0,3,5,7,9,11,13,27,55,56,63,65,80,83,95,98,100,101,106,108,109,],[-54,-54,-4,-54,-8,27,-12,27,-54,-7,27,27,27,-3,-54,27,-11,-14,-54,-54,-13,]),'if_token':([0,3,5,7,9,11,13,27,55,56,63,65,80,83,95,98,100,101,106,108,109,],[-54,-54,-4,-54,-8,28,-12,28,-54,-7,28,28,28,-3,-54,28,-11,-14,-54,-54,-13,]),'while_token':([0,3,5,7,9,11,13,27,55,56,63,65,80,83,95,98,100,101,106,108,109,],[-54,-54,-4,-54,-8,29,-12,29,-54,-7,29,29,29,-3,-54,29,-11,-14,-54,-54,-13,]),'read_token':([0,3,5,7,9,11,13,27,55,56,63,65,80,83,95,98,100,101,106,108,109,],[-54,-54,-4,-54,-8,30,-12,30,-54,-7,30,30,30,-3,-54,30,-11,-14,-54,-54,-13,]),'write_token':([0,3,5,7,9,11,13,27,55,56,63,65,80,83,95,98,100,101,106,108,109,],[-54,-54,-4,-54,-8,31,-12,31,-54,-7,31,31,31,-3,-54,31,-11,-14,-54,-54,-13,]),'period_token':([0,2,3,5,7,9,11,13,16,17,18,19,20,21,22,23,24,38,44,47,48,49,50,53,54,56,61,65,74,80,83,85,87,89,90,91,92,93,94,95,98,100,101,103,108,109,],[-54,6,-54,-4,-54,-8,-54,-12,-2,-15,-16,-17,-18,-19,-20,-21,-22,-24,-42,-45,-48,-51,-52,-31,-32,-7,-23,-54,-41,-54,-3,-25,-28,-43,-44,-49,-50,-53,-30,-54,-54,-11,-14,-29,-54,-13,]),'$end':([1,6,],[0,-1,]),'semicolom_token':([3,5,7,9,11,13,14,16,17,18,19,20,21,22,23,24,27,32,33,35,36,38,39,44,47,48,49,50,53,54,55,56,57,58,60,61,63,65,74,80,81,82,83,85,86,87,89,90,91,92,93,94,95,98,100,101,102,103,104,105,106,107,108,109,],[-54,-4,-54,-8,-54,-12,-54,-2,-15,-16,-17,-18,-19,-20,-21,-22,-54,55,56,-10,-54,-24,63,-42,-45,-48,-51,-52,-31,-32,-54,-7,-54,83,-6,-23,-54,-54,-41,-54,95,-9,-3,-25,63,-28,-43,-44,-49,-50,-53,-30,-54,-54,-11,-14,-54,-29,106,-5,-54,108,-54,-13,]),'eql_token':([10,42,44,47,48,49,50,74,84,89,90,91,92,93,],[15,68,-42,-45,-48,-51,-52,-41,96,-43,-44,-49,-50,-53,]),'comma_token':([14,36,57,102,],[34,59,34,59,]),'number_token':([15,28,29,31,37,41,43,45,46,51,67,68,69,70,71,72,73,75,76,77,78,96,],[36,50,50,50,50,50,50,-46,-47,50,50,-35,-36,-37,-38,-39,-40,50,50,50,50,102,]),'end_token':([17,18,19,20,21,22,23,24,27,38,39,44,47,48,49,50,53,54,61,62,63,64,65,74,80,85,86,87,89,90,91,92,93,94,97,98,103,],[-15,-16,-17,-18,-19,-20,-21,-22,-54,-24,-54,-42,-45,-48,-51,-52,-31,-32,-23,85,-54,-27,-54,-41,-54,-25,-54,-28,-43,-44,-49,-50,-53,-30,-26,-54,-29,]),'else_token':([17,18,19,20,21,22,23,24,38,44,47,48,49,50,53,54,61,65,74,80,85,87,89,90,91,92,93,94,98,103,],[-15,-16,-17,-18,-19,-20,-21,-22,-24,-42,-45,-48,-51,-52,-31,-32,-23,-54,-41,-54,-25,98,-43,-44,-49,-50,-53,-30,-54,-29,]),'become_token':([25,],[37,]),'odd_token':([28,29,],[41,41,]),'plus_token':([28,29,31,37,41,47,48,49,50,51,67,68,69,70,71,72,73,91,92,93,],[45,45,45,45,45,75,-48,-51,-52,45,45,-35,-36,-37,-38,-39,-40,-49,-50,-53,]),'minus_token':([28,29,31,37,41,47,48,49,50,51,67,68,69,70,71,72,73,91,92,93,],[46,46,46,46,46,76,-48,-51,-52,46,46,-35,-36,-37,-38,-39,-40,-49,-50,-53,]),'lparent_token':([28,29,31,37,41,43,45,46,51,67,68,69,70,71,72,73,75,76,77,78,],[51,51,51,51,51,51,-46,-47,51,51,-35,-36,-37,-38,-39,-40,51,51,51,51,]),'then_token':([40,44,47,48,49,50,66,74,88,89,90,91,92,93,],[65,-42,-45,-48,-51,-52,-33,-41,-34,-43,-44,-49,-50,-53,]),'les_token':([42,44,47,48,49,50,74,89,90,91,92,93,],[69,-42,-45,-48,-51,-52,-41,-43,-44,-49,-50,-53,]),'leq_token':([42,44,47,48,49,50,74,89,90,91,92,93,],[70,-42,-45,-48,-51,-52,-41,-43,-44,-49,-50,-53,]),'grt_token':([42,44,47,48,49,50,74,89,90,91,92,93,],[71,-42,-45,-48,-51,-52,-41,-43,-44,-49,-50,-53,]),'geq_token':([42,44,47,48,49,50,74,89,90,91,92,93,],[72,-42,-45,-48,-51,-52,-41,-43,-44,-49,-50,-53,]),'neq_token':([42,44,47,48,49,50,74,89,90,91,92,93,],[73,-42,-45,-48,-51,-52,-41,-43,-44,-49,-50,-53,]),'do_token':([44,47,48,49,50,52,66,74,88,89,90,91,92,93,],[-42,-45,-48,-51,-52,80,-33,-41,-34,-43,-44,-49,-50,-53,]),'rparent_token':([44,47,48,49,50,74,79,89,90,91,92,93,],[-42,-45,-48,-51,-52,-41,93,-43,-44,-49,-50,-53,]),'mul_token':([48,49,50,93,],[77,-51,-52,-53,]),'divide_token':([48,49,50,93,],[78,-51,-52,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,55,106,],[2,81,107,]),'con_dec':([0,55,106,],[3,3,3,]),'empty':([0,3,7,11,14,27,36,39,55,57,63,65,80,86,95,98,102,106,108,],[5,9,13,24,35,24,60,64,5,35,24,24,24,64,101,24,60,5,101,]),'var_dec':([3,],[7,]),'proc_dec':([7,],[11,]),'stmt':([11,27,63,65,80,98,],[16,39,86,87,94,103,]),'assign_stmt':([11,27,63,65,80,98,],[17,17,17,17,17,17,]),'call_stmt':([11,27,63,65,80,98,],[18,18,18,18,18,18,]),'begin_stmt':([11,27,63,65,80,98,],[19,19,19,19,19,19,]),'if_stmt':([11,27,63,65,80,98,],[20,20,20,20,20,20,]),'while_stmt':([11,27,63,65,80,98,],[21,21,21,21,21,21,]),'read_stmt':([11,27,63,65,80,98,],[22,22,22,22,22,22,]),'write_stmt':([11,27,63,65,80,98,],[23,23,23,23,23,23,]),'var_dec_cdr':([14,57,],[33,82,]),'cond':([28,29,],[40,52,]),'expr':([28,29,31,37,41,51,67,],[42,42,54,61,66,79,88,]),'flag':([28,29,31,37,41,51,67,],[43,43,43,43,43,43,43,]),'no_flag_expr':([28,29,31,37,41,43,51,67,],[44,44,44,44,44,74,44,44,]),'term':([28,29,31,37,41,43,51,67,75,76,77,78,],[47,47,47,47,47,47,47,47,89,90,91,92,]),'factor':([28,29,31,37,41,43,51,67,75,76,77,78,],[48,48,48,48,48,48,48,48,48,48,48,48,]),'con_dec_cdr':([36,102,],[58,105,]),'begin_stmt_cdr':([39,86,],[62,97,]),'cmp':([42,],[67,]),'proc_dec_cdr':([95,108,],[100,109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block period_token','program',2,'p_program','pl0yacc.py',9),
  ('block -> con_dec var_dec proc_dec stmt','block',4,'p_block','pl0yacc.py',18),
  ('con_dec -> const_token ident_token eql_token number_token con_dec_cdr semicolom_token','con_dec',6,'p_con_dec','pl0yacc.py',22),
  ('con_dec -> empty','con_dec',1,'p_con_dec','pl0yacc.py',23),
  ('con_dec_cdr -> comma_token ident_token eql_token number_token con_dec_cdr','con_dec_cdr',5,'p_con_dec_cdr','pl0yacc.py',31),
  ('con_dec_cdr -> empty','con_dec_cdr',1,'p_con_dec_cdr','pl0yacc.py',32),
  ('var_dec -> var_token ident_token var_dec_cdr semicolom_token','var_dec',4,'p_var_dec','pl0yacc.py',40),
  ('var_dec -> empty','var_dec',1,'p_var_dec','pl0yacc.py',41),
  ('var_dec_cdr -> comma_token ident_token var_dec_cdr','var_dec_cdr',3,'p_var_dec_cdr','pl0yacc.py',49),
  ('var_dec_cdr -> empty','var_dec_cdr',1,'p_var_dec_cdr','pl0yacc.py',50),
  ('proc_dec -> proc_token ident_token semicolom_token block semicolom_token proc_dec_cdr','proc_dec',6,'p_proc_dec','pl0yacc.py',58),
  ('proc_dec -> empty','proc_dec',1,'p_proc_dec','pl0yacc.py',59),
  ('proc_dec_cdr -> proc_token ident_token semicolom_token block semicolom_token proc_dec_cdr','proc_dec_cdr',6,'p_proc_dec_cdr','pl0yacc.py',68),
  ('proc_dec_cdr -> empty','proc_dec_cdr',1,'p_proc_dec_cdr','pl0yacc.py',69),
  ('stmt -> assign_stmt','stmt',1,'p_stmt','pl0yacc.py',78),
  ('stmt -> call_stmt','stmt',1,'p_stmt','pl0yacc.py',79),
  ('stmt -> begin_stmt','stmt',1,'p_stmt','pl0yacc.py',80),
  ('stmt -> if_stmt','stmt',1,'p_stmt','pl0yacc.py',81),
  ('stmt -> while_stmt','stmt',1,'p_stmt','pl0yacc.py',82),
  ('stmt -> read_stmt','stmt',1,'p_stmt','pl0yacc.py',83),
  ('stmt -> write_stmt','stmt',1,'p_stmt','pl0yacc.py',84),
  ('stmt -> empty','stmt',1,'p_stmt','pl0yacc.py',85),
  ('assign_stmt -> ident_token become_token expr','assign_stmt',3,'p_assign_stmt','pl0yacc.py',90),
  ('call_stmt -> call_token ident_token','call_stmt',2,'p_call_stmt','pl0yacc.py',94),
  ('begin_stmt -> begin_token stmt begin_stmt_cdr end_token','begin_stmt',4,'p_begin_stmt','pl0yacc.py',98),
  ('begin_stmt_cdr -> semicolom_token stmt begin_stmt_cdr','begin_stmt_cdr',3,'p_begin_stmt_cdr','pl0yacc.py',102),
  ('begin_stmt_cdr -> empty','begin_stmt_cdr',1,'p_begin_stmt_cdr','pl0yacc.py',103),
  ('if_stmt -> if_token cond then_token stmt','if_stmt',4,'p_if_stmt','pl0yacc.py',109),
  ('if_stmt -> if_token cond then_token stmt else_token stmt','if_stmt',6,'p_if_stmt','pl0yacc.py',110),
  ('while_stmt -> while_token cond do_token stmt','while_stmt',4,'p_while_stmt','pl0yacc.py',118),
  ('read_stmt -> read_token ident_token','read_stmt',2,'p_read_stmt','pl0yacc.py',122),
  ('write_stmt -> write_token expr','write_stmt',2,'p_write_stmt','pl0yacc.py',126),
  ('cond -> odd_token expr','cond',2,'p_cond','pl0yacc.py',130),
  ('cond -> expr cmp expr','cond',3,'p_cond','pl0yacc.py',131),
  ('cmp -> eql_token','cmp',1,'p_cmp','pl0yacc.py',139),
  ('cmp -> les_token','cmp',1,'p_cmp','pl0yacc.py',140),
  ('cmp -> leq_token','cmp',1,'p_cmp','pl0yacc.py',141),
  ('cmp -> grt_token','cmp',1,'p_cmp','pl0yacc.py',142),
  ('cmp -> geq_token','cmp',1,'p_cmp','pl0yacc.py',143),
  ('cmp -> neq_token','cmp',1,'p_cmp','pl0yacc.py',144),
  ('expr -> flag no_flag_expr','expr',2,'p_expr_flag','pl0yacc.py',149),
  ('expr -> no_flag_expr','expr',1,'p_expr_flag','pl0yacc.py',150),
  ('no_flag_expr -> term plus_token term','no_flag_expr',3,'p_expr_no_flag','pl0yacc.py',160),
  ('no_flag_expr -> term minus_token term','no_flag_expr',3,'p_expr_no_flag','pl0yacc.py',161),
  ('no_flag_expr -> term','no_flag_expr',1,'p_expr_no_flag','pl0yacc.py',162),
  ('flag -> plus_token','flag',1,'p_flag','pl0yacc.py',172),
  ('flag -> minus_token','flag',1,'p_flag','pl0yacc.py',173),
  ('term -> factor','term',1,'p_term_factor','pl0yacc.py',178),
  ('term -> factor mul_token term','term',3,'p_term_mul','pl0yacc.py',182),
  ('term -> factor divide_token term','term',3,'p_term_mul','pl0yacc.py',183),
  ('factor -> ident_token','factor',1,'p_factor_ident','pl0yacc.py',191),
  ('factor -> number_token','factor',1,'p_factor_number','pl0yacc.py',195),
  ('factor -> lparent_token expr rparent_token','factor',3,'p_factor_expr','pl0yacc.py',199),
  ('empty -> <empty>','empty',0,'p_empty','pl0yacc.py',203),
]
