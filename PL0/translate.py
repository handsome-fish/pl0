#! /usr/bin/python
#coding: utf-8

class Translater(object):
    """docstring for Translater"""
    printn_proc = """
printn  proc
    push    ax
    push    bx
    push    cx
    push     dx

    mov     bx,sp
    mov     cl,10

printn_lop1:
    div     cl
    push    ax
    xor     ah,ah


    cmp     al,0
    jnz     printn_lop1

printn_lop2:
    pop     ax
    mov     dl,ah
    add     dl,30h
    mov     ah,2
    int     21h
    cmp     bx,sp
    jnz     printn_lop2

    pop     dx
    pop     cx
    pop     bx
    pop     ax

    ret
printn  endp
"""
    def __init__(self, in_file_name, out_file_name):
        self.fin = open(in_file_name, "r")
        self.fout = open(out_file_name, "w")
        self.temp = 0

    def gen_label(self, string):
        return "__label_" + string

    def write(self, string):
        self.fout.write(string + "\n")

    def lit_code(self, l, a):
        if int(l) != 0 :
            raise ValueError("Level in LIT instruction can only be ZERO.")
        self.write("  MOV AX, {0}".format(a))
        self.write("  PUSH AX")
        return

    def opr_code(self, l, a):
        if int(l) != 0 :
            raise ValueError("Level in OPR instruction can only be ZERO.")
        #a = int(a)
        if a == 'OPR_RET':
            # 返回地址
            self.write("  MOV  CX, SS:[BP-4]")
            self.write("  MOV  BX, BP")
            # 取动态链
            self.write("  MOV  AX, SS:[BP-2]")
            self.write("  MOV  BP, AX")
            # 建立SP
            self.write("  ADD  BX, 2")
            self.write("  MOV  SP, BX")
            # 函数返回
            self.write("  JMP  CX")
        elif a == 'OPR_NEG':
            self.write("  POP  AX")
            self.write("  NEG  AX")
            self.write("  PUSH AX")
        elif a == 'OPR_ADD':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  ADD  AX, BX")
            self.write("  PUSH AX")
        elif a == 'OPR_SUB':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  SUB  AX, BX")
            self.write("  PUSH AX")
        elif a == 'OPR_MUL':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  IMUL BX")
            self.write("  PUSH AX")
        elif a == 'OPR_DIV':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  MOV  DX, 0")
            self.write("  IDIV BX")
            self.write("  PUSH AX")
        elif a == 'OPR_ODD':
            self.write("  POP  AX")
            self.write("  AND  AX, 1")
            self.write("  PUSH AX")
        elif a == 'OPR_MOD':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  MOV  DX, 0")
            self.write("  IDIV BX")
            self.write("  PUSH DX")
        elif a == 'OPR_EQL':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  CMP  AX, BX")
            self.write("  JE   " + "__temp_lable" + str(self.temp))
            self.write("  PUSH 0")
            self.write("  JMP  " + "__temp_lable_next" + str(self.temp))
            self.write("__temp_lable" + str(self.temp) + ":")
            self.write("  PUSH 1")
            self.write("__temp_lable_next" + str(self.temp) + ":")
            self.temp += 1
        elif a == 'OPR_NEQ':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  CMP  AX, BX")
            self.write("  JNE   " + "__temp_lable" + str(self.temp))
            self.write("  PUSH 0")
            self.write("  JMP  " + "__temp_lable_next" + str(self.temp))
            self.write("__temp_lable" + str(self.temp) + ":")
            self.write("  PUSH 1")
            self.write("__temp_lable_next" + str(self.temp) + ":")
            self.temp += 1
        elif a == 'OPR_LSS':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  CMP  AX, BX")
            self.write("  JL    " + "__temp_lable" + str(self.temp))
            self.write("  PUSH 0")
            self.write("  JMP  " + "__temp_lable_next" + str(self.temp))
            self.write("__temp_lable" + str(self.temp) + ":")
            self.write("  PUSH 1")
            self.write("__temp_lable_next" + str(self.temp) + ":")
            self.temp += 1
        elif a == 'OPR_LEQ':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  CMP  AX, BX")
            self.write("  JLE  " + "__temp_lable" + str(self.temp))
            self.write("  PUSH 0")
            self.write("  JMP  " + "__temp_lable_next" + str(self.temp))
            self.write("__temp_lable" + str(self.temp) + ":")
            self.write("  PUSH 1")
            self.write("__temp_lable_next" + str(self.temp) + ":")
            self.temp += 1
        elif a == 'OPR_GTR':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  CMP  AX, BX")
            self.write("  JG   " + "__temp_lable" + str(self.temp))
            self.write("  PUSH 0")
            self.write("  JMP  " + "__temp_lable_next" + str(self.temp))
            self.write("__temp_lable" + str(self.temp) + ":")
            self.write("  PUSH 1")
            self.write("__temp_lable_next" + str(self.temp) + ":")
            self.temp += 1
        elif a == 'OPR_GEQ':
            self.write("  POP  BX")
            self.write("  POP  AX")
            self.write("  CMP  AX, BX")
            self.write("  JGE  " + "__temp_lable" + str(self.temp))
            self.write("  PUSH 0")
            self.write("  JMP  " + "__temp_lable_next" + str(self.temp))
            self.write("__temp_lable" + str(self.temp) + ":")
            self.write("  PUSH 1")
            self.write("__temp_lable_next" + str(self.temp) + ":")
            self.temp += 1
        else:
            raise ValueError("OPR code can't support this function: {0}.".format(a))
        return

    def lod_code(self, l, a):
        self.write("  MOV  CX, {0}".format(l))
        self.write("  MOV  BX, BP")
        self.write("__temp_lable" + str(self.temp) + ":")
        self.write("  CMP  CX, 0")
        self.write("  JE   " + "__temp_lable" + str(self.temp + 1))
        self.write("  DEC  CX")
        self.write("  MOV  BX, SS:[BX]")
        self.write("  JMP  " + "__temp_lable" + str(self.temp))
        self.write("__temp_lable" + str(self.temp + 1) + ":")
        self.write("  MOV  AX, {0}".format(int(a) * 2))
        self.write("  SUB  BX, AX")
        self.write("  PUSH SS:[BX]")
        self.temp += 2
        return

    def sto_code(self, l, a):
        self.write("  MOV  CX, {0}".format(l))
        self.write("  MOV  BX, BP")
        self.write("__temp_lable" + str(self.temp) + ":")
        self.write("  CMP  CX, 0")
        self.write("  JE   " + "__temp_lable" + str(self.temp + 1))
        self.write("  DEC  CX")
        self.write("  MOV  BX, SS:[BX]")
        self.write("  JMP  " + "__temp_lable" + str(self.temp))
        self.write("__temp_lable" + str(self.temp + 1) + ":")
        self.write("  MOV  AX, {0}".format(int(a) * 2))
        self.write("  SUB  BX, AX")
        self.write("  POP  AX")
        self.write("  MOV  SS:[BX], AX")
        self.temp += 2
        return

    def call_code(self, l, a, ret):
        self.write("  MOV  CX, {0}".format(l))
        self.write("  MOV  BX, BP")
        self.write("__temp_lable" + str(self.temp) + ":")
        self.write("  CMP  CX, 0")
        self.write("  JE   " + "__temp_lable" + str(self.temp + 1))
        self.write("  DEC  CX")
        self.write("  MOV  BX, SS:[BX]")
        self.write("  JMP  " + "__temp_lable" + str(self.temp))
        self.write("__temp_lable" + str(self.temp + 1) + ":")
        self.temp += 2
        self.write("  MOV  DX, BX")
        # DX <- 静态链地址
        self.write("  MOV  CX, BP")
        # CX <- 动态链地址
        # 建立BP
        self.write("  MOV  AX, SP")
        self.write("  SUB  AX, 2")
        self.write("  MOV  BP, AX")
        self.write("  MOV  SS:[BP], DX")
        self.write("  MOV  SS:[BP-2], CX")
        self.write("  MOV  SS:[BP-4], {0}".format(self.gen_label((str)(ret + 1))))
        self.write("  JMP  " + self.gen_label((str)(a)))
        return

    def int_code(self, l, a):
        if int(l) != 0:
            raise ValueError("INC code only support level 0.")
        self.write("  MOV  AX, BP")
        self.write("  SUB  AX, {0}".format(int(a) * 2 - 2))
        self.write("  MOV  SP, AX")
        return

    def jmp_code(self, l, a):
        if int(l) != 0:
            raise ValueError("JMP code only support level 0.")
        self.write("  JMP  " + self.gen_label(str(a)))
        return

    def jpc_code(self, l, a):
        if int(l) != 0:
            raise ValueError("JPC code only support level 0.")
        self.write("  POP  AX")
        self.write("  CMP  AX, 0")
        self.write("  JE   " + self.gen_label(str(a)))
        return

    def write_code(self, l, a):
        if int(l) != 0:
            raise ValueError("SIO_OUT code only support level 0.")
        self.write("  MOV  AH, 09H")
        self.write("  LEA  DX, out_str")
        self.write("  INT  21H")
        self.write("  POP  AX")
        self.write("  CALL printn")
        return

    def read_code(self, l, a):
        if int(l) != 0:
            raise ValueError("SIO_IN code only support level 0.")
        self.write("  MOV  AH, 09H")
        self.write("  LEA  DX, ret_str")
        self.write("  INT  21H")
        return

    def translate(self):
        self.gen_head()
        for inst in self.fin:
            ins_set = tuple(inst.split(" "))
            self.write(self.gen_label(ins_set[0]))
            if ins_set[1].upper() == "LIT":
                self.lit_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "OPR":
                self.opr_code(ins_set[2], str(ins_set[3]).replace("\n",""))
            elif ins_set[1].upper() == "LOD":
                self.lod_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "STO":
                self.sto_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "CAL":
                self.call_code(ins_set[2], ins_set[3], int(ins_set[0].split(":")[0]))
            elif ins_set[1].upper() == "INC":
                self.int_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "JMP":
                self.jmp_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "JPC":
                self.jpc_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "SIO_OUT":
                self.write_code(ins_set[2], ins_set[3])
            elif ins_set[1].upper() == "SIO_IN":
                self.read_code(ins_set[2], ins_set[3])
            else:
                raise KeyError("Translate Error: Not support instruction.")
        self.write("__end_prog:")
        self.write("  MOV AX, 4C00H")
        self.write("  INT 21H")
        self.write("_TEXT ENDS\n")
        # self.write(Translater.printn_proc)
        self.write("END Start")

    def gen_head(self):
        head_str0 = "_STACK SEGMENT STACK 'STACK'\nDB 65535 DUP(0)\nTOS DW 0\n_STACK ENDS\n"
        head_str1 = '_DATA SEGMENT\nout_str db "Output: $"\nin_str db "Input a number:$"\nret_str db 10, "$"\n_DATA ENDS\n'
        head_str2 = "_TEXT SEGMENT 'CODE'\nASSUME ECS:_TEXT, DS:_DATA, SS:_STACK\nStart:\n"
        head_str3 = "MOV AX, _DATA\nMOV DS, AX\nCLI\nMOV AX, _STACK\nMOV SS, AX\nMOV SP, Offset TOS\nMOV BP, Offset TOS - 2\nSTI\n"
        head_str4 = "MOV SS:[BP-4], __end_prog\nMOV SS:[BP-2], 0\nMOV SS:[BP], 0"
        self.write(head_str0)
        self.write(head_str1)
        self.write(head_str2)
        self.write(head_str3)
        self.write(head_str4)

    def close(self):
        self.fout.close()
