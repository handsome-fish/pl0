
from tkinter import *
import hashlib
import time
from tkinter import filedialog
LOG_LINE_NUM = 0

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
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=13, rowspan=15, columnspan=9)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)#grid函数可将页面按row,column分割
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="PL/0转汇编", bg="lightblue", width=10,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=5, column=12)
        self.fileinput = Button(self.init_window_name,text="打开文件",bg="lightblue",width=10,command=self.openfiles2)
        self.fileinput.grid(row=3, column=12)
        # 滚动条
        self.init_data_scrollbar_y = Scrollbar(self.init_window_name)                #创建纵向滚动条
        self.init_data_scrollbar_y.config(command=self.init_data_Text.yview)       #将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.init_data_Text.config(yscrollcommand=self.init_data_scrollbar_y.set)   #Text反向绑定滚动条
        self.init_data_scrollbar_y.grid(row=1, column=11, rowspan=10, sticky='NS')
        self.result_data_scrollbar_y = Scrollbar(self.init_window_name)                #创建纵向滚动条
        self.result_data_scrollbar_y.config(command=self.result_data_Text.yview)       #将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.result_data_Text.config(yscrollcommand=self.result_data_scrollbar_y.set)   #Text反向绑定滚动条
        self.result_data_scrollbar_y.grid(row=1, column=23, rowspan=15, sticky='NS')

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
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")


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

if __name__ ==  '__main__':
    gui_start()
