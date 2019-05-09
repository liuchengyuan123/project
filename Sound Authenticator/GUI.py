from tkinter import *
from tkinter import ttk
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pylab as plt
from python_speech_features import mfcc
from Resize import resize
from Analyse import analyse


class Window(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('Sound Authenticator  --- By Group 50')
        self.back_left = Label(master=self.root, width=70, height=30, bg='blue')
        self.back_right = Label(master=self.root, width=70, height=30, bg='green')
        self.back_left.pack(side=LEFT)
        self.back_right.pack(side=LEFT)
        self.back_left.pack_propagate(0)
        self.back_right.pack_propagate(0)

        default = "result_png/default.png"
        self.photo = PhotoImage(file=default)
        self.img_label = Label(master=self.back_left, image=self.photo, height=self.photo.height(),
                               width=self.photo.width(), bg='red')
        self.img_label.pack()
        self.new_img_label = Label(master=self.img_label, image=self.photo, height=self.photo.height(),
                               width=self.photo.width(), bg='red')
        self.new_img_label.pack()
        self.text_label = Label(master=self.back_left, height=1, width=70)
        self.text_label.pack_propagate(0)
        self.text_label.pack(side=TOP)
        self.text_area = Text(master=self.text_label, height=1, width=50)
        self.text_area.pack(side=LEFT)
        self.text_area.insert(END, 'file name: ')
        self.file_confirm = Button(master=self.text_label, text='confirm', height=1, width=20)
        self.file_confirm.pack(side=RIGHT)
        args_label = Label(master=self.back_left, height=6, width=70, bg='blue')
        args_label.pack_propagate(0)
        args_label.pack()

        info = Label(args_label, width=30, height=6)
        info.grid_propagate(0)
        info.pack(side=LEFT)
        Label(info, width=10, height=1, text='during time: ', bg='white').grid(row=0, column=0)
        Label(info, width=10, height=1, text='sample rate: ', bg='white').grid(row=1, column=0)
        Label(info, width=10, height=1, text='frames: ', bg='white').grid(row=2, column=0)
        Label(info, width=10, height=1, text='picture: ', bg='white').grid(row=3, column=0)
        self.file_info = []
        for i in range(4):
            self.file_info.append(Text(info, width=18, height=1, bg='white'))
        for i in range(4):
            self.file_info[i].grid(row=i, column=1)

        args = Label(args_label, width=40, height=6)
        args.grid_propagate(0)
        args.pack(side=RIGHT)
        Label(args, width=18, height=1, text='observe from:').grid(row=0, column=0)
        Label(args, width=18, height=1, text='observe till:').grid(row=1, column=0)
        Label(args, width=18, height=1, text='standard value:').grid(row=2, column=0)
        self.time_arg = []
        for i in range(3):
            self.time_arg.append(Text(args, width=20, height=1, bg='white'))
        for i in range(3):
            self.time_arg[i].grid(row=i, column=1)
        self.time_arg[0].insert(END, str(0))
        self.time_arg[1].insert(END, str(0))
        self.time_arg[2].insert(END, str(0.15))
        self.auto_cover = IntVar()
        self.auto_cover.set(1)
        Checkbutton(args, text='auto-cover', variable=self.auto_cover).grid(row=3, column=0)
        Button(args, text='OK', width=10, height=1, bg='white', command=self.plot_time).grid(row=3, column=1)

        self.mfcc_pic = PhotoImage(file=default)
        self.mfcc_label = Label(master=self.back_right, image=self.mfcc_pic,
                           width=self.mfcc_pic.width(), height=self.mfcc_pic.height(), bg='blue')
        self.mfcc_label.pack(side=TOP)
        self.mfcc_label.pack_propagate(0)
        self.new_mfcc_label = Label(master=self.mfcc_label, image=self.mfcc_pic,
                                width=self.mfcc_pic.width(), height=self.mfcc_pic.height(), bg='red')
        self.new_mfcc_label.pack(side=TOP)

        vision = Label(master=self.back_right, width=70, height=5)
        vision.grid_propagate(0)
        vision.pack(side=TOP)
        vis_choice = []
        self.vector = []
        for i in range(13):
            self.vector.append(IntVar())
            self.vector[i].set(1)
        for i in range(6):
            vis_choice.append(Checkbutton(master=vision, text='mfcc ' + str(i + 1), variable=self.vector[i], width=7))
            vis_choice[i].grid(row=0, column=i, sticky=W)
        for i in range(6, 12):
            vis_choice.append(Checkbutton(master=vision, text='mfcc ' + str(i + 1), variable=self.vector[i], width=7))
            vis_choice[i].grid(row=1, column=i - 6, sticky=W)
        vis_choice.append(Checkbutton(master=vision, text='energy per frame', variable=self.vector[12], width=14))
        vis_choice[12].grid(row=2, column=0, columnspan=2, sticky=W)
        Label(master=vision, width=10, height=1, text='win function', bg='white').grid(row=2, column=2, columnspan=1)
        self.Winfunc = StringVar()
        self.comboxlist = ttk.Combobox(master=vision, text='winfunc', textvariable=self.Winfunc, width=14)
        self.comboxlist['values'] = ("None", "Hamming")
        self.comboxlist.current(1)
        self.comboxlist.grid(row=2, column=3, columnspan=2, sticky=W)
        Button(master=vision, text='OK', width=10, height=1, command=self.plot_mfcc, bg='white').grid(row=2, column=5)

        result = Label(master=self.back_right, width=70, height=2)
        result.grid_propagate(0)
        result.pack(side=TOP)
        self.res_area = Label(master=result, width=20, height=2, bg='white')
        self.res_area.grid(row=0, column=0, columnspan=3, sticky=W)
        self.res = Text(master=self.res_area, width=18, height=2)
        self.res.grid_propagate(0)
        self.res.grid(row=0, column=0)
        Label(master=result, width=5).grid(row=0, column=3)
        mfcc_add = Label(master=result, width=12, text='mfcc address:', bg='pink')
        mfcc_add.grid(row=0, column=4, columnspan=2)
        self.add_area = Text(master=result, width=25, height=1)
        self.add_area.grid(row=0, column=6, sticky=E)

        self.fs = None
        self.audio = None
        self.lena = None
        self.mfcc = None
        self.xl = None
        self.time = None
        self.x_seq = None
        self.test_cnt = 0
        self.mfcc_cnt = 0
        self.start = 0
        self.end = 0
        self.time_name = ''
        self.mfcc_name = ''
        self.lenb = 0

    def plot_time(self):
        file_name = self.text_area.get('0.0', END)
        if self.xl != file_name[11:-1]:
            self.xl = file_name[11:-1]
            self.fs, self.audio = wav.read(self.xl)
            self.lena = self.audio.__len__()
            self.time = self.lena / self.fs
            self.x_seq = np.arange(0, self.time, 1 / self.fs)
            for i in range(3):
                self.file_info[i].delete('0.0', END)
            self.file_info[0].insert(END, str(self.time))
            self.file_info[1].insert(END, str(self.fs))
            self.file_info[2].insert(END, str(self.lena))

        self.start = int(self.time_arg[0].get('0.0', END))
        self.end = int(self.time_arg[1].get('0.0', END))
        # self.time_arg[0].insert(END, str(0))
        self.end = min(self.lena, self.end)
        self.time_arg[1].delete('0.0', END)
        self.time_arg[1].insert(END, str(self.end))

        if self.auto_cover.get() == 1:
            self.test_cnt -= 1
        self.test_cnt += 1
        self.time_name = 'result_png/' + 'fir ' + str(self.test_cnt) + '.png'
        plt.clf()
        plt.plot(self.x_seq[self.start: self.end], self.audio[self.start: self.end])
        plt.xlabel('time (s)')
        plt.savefig(self.time_name)
        self.file_info[3].delete('0.0', END)
        self.file_info[3].insert(END, self.time_name)
        resize(self.time_name)

        self.photo = PhotoImage(file=self.time_name)
        print('time', self.photo.height(), self.photo.width())
        self.new_img_label.destroy()
        self.new_img_label = Label(master=self.img_label, image=self.photo, height=self.photo.height(),
                               width=self.photo.width(), bg='red')
        self.new_img_label.pack()
        self.plot_mfcc()

    def plot_mfcc(self):
        tmp_win = None
        if self.Winfunc.get() == "Hamming":
            tmp_win = np.hamming
        self.mfcc = mfcc(self.audio, samplerate=self.fs, winfunc=tmp_win)
        plt.clf()
        self.lenb = self.mfcc.__len__()
        lcy = []
        for i in range(self.lenb):
            tab = []
            for dem in range(13):
                if self.vector[dem].get() == 0:
                    continue
                tab.append(self.mfcc[i][dem])
            lcy.append(tab)
        plt.plot(self.x_seq[:self.lenb], lcy)
        if self.auto_cover.get() == 1:
            self.mfcc_cnt -= 1
        self.mfcc_cnt += 1
        self.mfcc_name = 'result_png/sec ' + str(self.mfcc_cnt) + '.png'
        plt.savefig(self.mfcc_name)
        self.add_area.delete('0.0', END)
        self.add_area.insert(END, self.time_name)
        resize(self.mfcc_name)

        self.mfcc_pic = PhotoImage(file=self.mfcc_name)
        print('mfcc', self.mfcc_pic.height(), self.mfcc_pic.width())
        self.new_mfcc_label.destroy()
        self.new_mfcc_label = Label(master=self.mfcc_label, image=self.mfcc_pic, height=self.photo.height(),
                                   width=self.photo.width(), bg='yellow')
        self.new_mfcc_label.pack_propagate(0)
        self.new_mfcc_label.pack(side=TOP)

        str_ans = ''
        arr = []
        for i in range(self.lenb):
            arr.append(self.mfcc[i][0])
        x = analyse(arr, 0, self.lenb, seg=10, std=0.15)
        print('x', x)
        if x < 0.045:
            str_ans = 'music!!!!'
        else:
            str_ans = 'voice!!!!'
        self.res.delete('0.0', END)
        self.res.insert(END, str_ans)
        return
