from codegen import *
import sys
from tkinter import *
import hashlib
import time
from tkinter import filedialog
import translate
import pickle
LOG_LINE_NUM = 0

def get_op(code):
    return code[0]

def get_l(code):
    return code[1]

def get_m(code):
    return code[2]

def code_cope():
    f = open('code.txt', 'r')
    s = open("code_cope.txt", 'w')
    i = 1
    for low in f:
        low_new = str(low[1:-2]).split(',')
        low_newer = str(i) + ' ' + low_new[0] + low_new[1] + low_new[2]
        s.write(low_newer.replace('\'', '') + '\n')
        i += 1
    f.close()
    s.close()

def pl0(codes):
    def base(bar):
        b = bp
        for i in range(0,bar):
            b = stack[b-1]
        return b

    pc,sp,ar,bp = 0,0,0,1
    flag = False
    stack = [0] * 1000
    lever = [-1] * 20
    lever[0] = 0
    while pc < len(codes) and  ar >= 0:
        code = codes[pc]
        #解释器写入文件
        f=open('interpreter.txt', 'a')
        f.write(str(code)+'\n')
        f.close()
        #print (code)
        pc += 1
        op,l,m = get_op(code),get_l(code),get_m(code)
        if op == 'LIT':
            stack[sp] = m
            sp += 1
        elif op == 'OPR':
            if m == 'OPR_RET':
                sp = bp - 1
                bp,pc = stack[sp+1],stack[sp+2]
                lever[ar] = -1
                ar -= 1
            elif m == 'OPR_NEG':
                stack[sp - 1] = - stack[sp - 1]
            elif m == 'OPR_ADD':
                sp -= 1
                stack[sp - 1] += stack[sp]
            elif m == 'OPR_SUB':
                sp -= 1
                stack[sp - 1] -= stack[sp]
            elif m == 'OPR_MUL':
                sp -= 1
                stack[sp - 1] *= stack[sp]
            elif m == 'OPR_DIV':
                sp -= 1
                stack[sp - 1] /= stack[sp]
            elif m == 'OPR_ODD':
                stack[sp - 1] = int(stack[sp - 1])%2
            elif m == 'OPR_MOD':
                sp -= 1
                stack[sp - 1] %= stack[sp]
            elif m == 'OPR_EQL':
                sp -= 1
                if stack[sp] == stack[sp -1]:
                    stack[sp - 1] = 1
                else:
                    stack[sp - 1] = 0
            elif m == 'OPR_NEQ':
                sp -= 1
                if stack[sp] == stack[sp - 1]:
                    stack[sp - 1] = 0
                else:
                    stack[sp - 1] = 1
            elif m == 'OPR_LSS':
                sp -= 1
                if stack[sp - 1] < stack[sp]:
                    stack[sp - 1] = 1
                else:
                    stack[sp - 1] = 0
            elif m == 'OPR_LEQ':
                sp -= 1
                if stack[sp - 1] <= stack[sp]:
                    stack[sp - 1] = 1
                else:
                    stack[sp - 1] = 0
            elif m == 'OPR_GTR':
                sp -= 1
                if stack[sp - 1] > stack[sp]:
                    stack[sp - 1] = 1
                else:
                    stack[sp - 1] = 0
            elif m == 'OPR_GEQ':
                sp -= 1
                if stack[sp - 1] >= stack[sp]:
                    stack[sp - 1] = 1
                else:
                    stack[sp - 1] = 0
            else:
                pass
        elif op == 'LOD':
            stack[sp] = stack[base(l)-1+m]
            sp +=1
        elif op == 'STO':
            sp -= 1
            stack[base(l)-1+m] = stack[sp]
        elif op == 'CAL':
            stack[sp] = base(l)
            stack[sp+1],stack[sp+2] = bp,pc
            bp,pc = sp + 1,m
            lever[ar] = sp
            for i in range(0,ar):
                lever[ar] -= lever[i]
            ar += 1
            lever[ar] = 3
        elif op == 'INC':
            sp += m
        elif op == 'JMP':
            pc = m
        elif op == 'JPC':
            sp -= 1
            if stack[sp] == 0:
                pc = m
        elif op == 'SIO_OUT':
            flag = True
        elif op == 'SIO_IN':
            flag = True
        else:
            print ("Error in code {0}".format(pc))
        f=open('interpreter.txt', 'a')
        f.write(str(pc)+' '+str(bp)+' '+str(sp)+' '+str(ar)+' '+str(stack[0:sp])+'\n')
        f.close()
        print (pc,bp,sp,ar,stack[0:sp])
        if flag == True:
            if op == 'SIO_OUT':
                sp -= 1
                print ("write : " + str(int(stack[sp])))
            if op == 'SIO_IN':
                stack[sp] = int(input("read: "))
                sp += 1
            flag =False

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("我的编译器")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.lex_data_label = Label(self.init_window_name, text="词法处理结果")
        self.lex_data_label.grid(row=7, column=0)
        self.result_data_label = Label(self.init_window_name, text="中间代码")
        self.result_data_label.grid(row=3, column=13)
        self.interpreter_data_label = Label(self.init_window_name, text="解释器")
        self.interpreter_data_label.grid(row=8, column=13)
        self.error_data_label = Label(self.init_window_name, text="错误")
        self.error_data_label.grid(row=12, column=13)
        self.parse_data_label = Label(self.init_window_name, text="语法分析")
        self.parse_data_label.grid(row=0, column=13)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=20)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=6, columnspan=10)
        self.lex_data_Text = Text(self.init_window_name, width=67, height=15)  #lex结果展示
        self.lex_data_Text.grid(row=8, column=0, rowspan=4, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)                #grid函数可将页面按row,column分割
        self.code_data_Text = Text(self.init_window_name, width=67, height=15)  #code结果展示
        self.code_data_Text.grid(row=4, column=13, rowspan=4, columnspan=8)
        self.parse_data_Text = Text(self.init_window_name, width=67, height=10)  #parse结果展示
        self.parse_data_Text.grid(row=1, column=13, rowspan=2, columnspan=8)
        self.interpreter_data_Text = Text(self.init_window_name, width=67, height=10)  #interpreter结果展示
        self.interpreter_data_Text.grid(row=9, column=13, rowspan=3, columnspan=8)
        self.error_data_Text = Text(self.init_window_name, width=67, height=8)  #error结果展示
        self.error_data_Text.grid(row=13, column=13,columnspan=8)

        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="生成中间代码", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=5, column=12)
        self.fileinput = Button(self.init_window_name,text="打开文件",bg="lightblue",width=10,command=self.openfiles2)
        self.fileinput.grid(row=3, column=12)
        # 滚动条
        self.init_data_scrollbar_y = Scrollbar(self.init_window_name)                #创建纵向滚动条输入
        self.init_data_scrollbar_y.config(command=self.init_data_Text.yview)       #将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.init_data_Text.config(yscrollcommand=self.init_data_scrollbar_y.set)   #Text反向绑定滚动条
        self.init_data_scrollbar_y.grid(row=1, column=11, rowspan=6, sticky='NS')
        self.result_data_scrollbar_y = Scrollbar(self.init_window_name)                #code滚动条
        self.result_data_scrollbar_y.config(command=self.code_data_Text.yview)
        self.code_data_Text.config(yscrollcommand=self.result_data_scrollbar_y.set)
        self.result_data_scrollbar_y.grid(row=4, column=23, rowspan=4, sticky='NS')
        self.lex_data_scrollbar_y = Scrollbar(self.init_window_name)                #lex滚动条
        self.lex_data_scrollbar_y.config(command=self.lex_data_Text.yview)
        self.lex_data_Text.config(yscrollcommand=self.lex_data_scrollbar_y.set)
        self.lex_data_scrollbar_y.grid(row=8, column=11, rowspan=4, sticky='NS')
        self.parse_data_scrollbar_y = Scrollbar(self.init_window_name)                #parse滚动条
        self.parse_data_scrollbar_y.config(command=self.parse_data_Text.yview)
        self.parse_data_Text.config(yscrollcommand=self.parse_data_scrollbar_y.set)
        self.parse_data_scrollbar_y.grid(row=1, column=23, rowspan=2, sticky='NS')
        self.interpreter_data_scrollbar_y = Scrollbar(self.init_window_name)                #interpreter滚动条
        self.interpreter_data_scrollbar_y.config(command=self.interpreter_data_Text.yview)
        self.interpreter_data_Text.config(yscrollcommand=self.interpreter_data_scrollbar_y.set)
        self.interpreter_data_scrollbar_y.grid(row=9, column=23, rowspan=4, sticky='NS')

    #打开文件按钮command
    def openfiles2(self):
        self.filename = filedialog.askopenfilename()
        try:
            with open(self.filename) as f:
                for each_line in f:
                    self.init_data_Text.insert(INSERT,each_line)
        except OSError as reason:
            self.init_data_Text.insert(INSERT,"文件不存在")


    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()#get(1.0,EnD)指从第1行读到最后一行

        # f=open('code.txt', 'w')
        # f.write("")
        # f.close()
        #print("src =",src)
        if src:
            try:
                ast = pl0_parse(self.filename)
                f=open('parse.txt', 'w')
                f.write(str(ast)+'\n')
                f.close()
                codegen(ast)
                pl0(code)
                #清空屏幕
                self.code_data_Text.delete(1.0,END)
                # self.init_data_Text.delete(1.0,END)
                self.parse_data_Text.delete(1.0,END)
                self.lex_data_Text.delete(1.0,END)
                self.error_data_Text.delete(1.0,END)
                self.interpreter_data_Text.delete(1.0,END)
                #print(len(code))
                #将结果存入文件
                f=open('code.txt', 'w')
                for ins in code:
                     f.write(str(ins)+'\n')
                f.close()
                # 生成汇编代码assemble_code.txt
                code_cope()
                translate.Translater('code_cope.txt', 'assemble_code.txt').translate()
                #写入code_text
                try:
                    with open('code.txt') as f:
                        for each_line in f:
                            self.code_data_Text.insert(INSERT,each_line)
                        f.close()
                except OSError as reason:
                    self.code_data_Text.insert(INSERT,"文件不存在")
                    f.close()
                #写入lex_text
                try:
                    with open('lex.txt') as f:
                        for each_line in f:
                            self.lex_data_Text.insert(INSERT,each_line)
                        f.close()
                except OSError as reason:
                    self.lex_data_Text.insert(INSERT,"文件不存在")
                    f.close()
                #写入parse_text
                try:
                    with open('parse.txt') as f:
                        for each_line in f:
                            self.parse_data_Text.insert(INSERT,each_line)
                        f.close()
                except OSError as reason:
                    self.parse_data_Text.insert(INSERT,"文件不存在")
                    f.close()
                #写入error_text
                try:
                    with open('error.txt') as f:
                        for each_line in f:
                            self.error_data_Text.insert(INSERT,each_line)
                        f.close()
                except OSError as reason:
                    self.error_data_Text.insert(INSERT,"文件不存在")
                    f.close()
                #写入interpreter_text
                try:
                    with open('interpreter.txt') as f:
                        for each_line in f:
                            self.interpreter_data_Text.insert(INSERT,each_line)
                        f.close()
                except OSError as reason:
                    self.interpreter_data_Text.insert(INSERT,"文件不存在")
                    f.close()

                #输出到界面
                self.write_log_to_Text("INFO:pl0_translate success")
            except:
                self.write_log_to_Text("ERROR:pl0_translate failed")
        else:
            self.write_log_to_Text("ERROR:pl0_translate failed")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        #实现日志满的时候更新
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
if __name__ == '__main__':

    #print(len(sys.argv))
    '''
    if len(sys.argv) != 2:
        print('Usage: python pl0.py filepath!')
        exit(1)
    '''
    f=open('error.txt', 'w')
    f.write('\n')
    f.close()
    f=open('interpreter.txt', 'w')
    f.write('\n')
    f.close()
    gui_start()

