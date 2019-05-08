from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk

root = Tk()
root.title('Sound Authenticator    -   By Group 50')
back_left = Label(master=root, width=70, height=30, bg='blue')
back_right = Label(master=root, width=70, height=30, bg='green')
back_left.pack(side=LEFT)
back_right.pack(side=LEFT)
back_left.pack_propagate(0)
back_right.pack_propagate(0)
'''
左侧
'''
photo = PhotoImage(file="result_png/500_.png")
img_label = Label(master=back_left, image=photo, height=photo.height(),
                  width=photo.width(), bg='red')
img_label.pack_propagate(0)
img_label.pack(side=TOP)
text_label = Label(back_left, height=1, width=70)
text_label.pack_propagate(0)
text_label.pack(side=TOP)
text_area = Text(text_label, height=1, width=50)
text_area.pack(side=LEFT)
text_area.insert(END, 'file name:')
file_confirm = Button(text_label, text='confirm', height=1, width=20)
file_confirm.pack(side=RIGHT)
args_label = Label(back_left, height=6, width=70, bg='blue')
args_label.pack_propagate(0)
args_label.pack()

'''
文件信息与参数调节
'''
info = Label(args_label, width=30, height=6)
info.grid_propagate(0)
info.pack(side=LEFT)
Label(info, width=10, height=1, text='during time: ', bg='white').grid(row=0, column=0)
Label(info, width=10, height=1, text='sample rate: ', bg='white').grid(row=1, column=0)
Label(info, width=10, height=1, text='frames: ', bg='white').grid(row=2, column=0)
Label(info, width=10, height=1, text='picture: ', bg='white').grid(row=3, column=0)
file_info = []
for i in range(4):
    file_info.append(Text(info, width=18, height=1, bg='white'))
for i in range(4):
    file_info[i].grid(row=i, column=1)

args = Label(args_label, width=40, height=6)
args.grid_propagate(0)
args.pack(side=RIGHT)
Label(args, width=18, height=1, text='observe from:').grid(row=0, column=0)
Label(args, width=18, height=1, text='observe till:').grid(row=1, column=0)
Label(args, width=18, height=1, text='standard value:').grid(row=2, column=0)
time_arg = []
for i in range(3):
    time_arg.append(Text(args, width=20, height=1, bg='white'))
for i in range(3):
    time_arg[i].grid(row=i, column=1)
auto = IntVar()


def write():
    print(auto.get())


Checkbutton(args, text='auto-cover', variable=auto).grid(row=3, column=0)
read = Button(args, width=10, height=1, text='OK', bg='white', command=write)
read.grid(row=3, column=1)

'''
右侧
'''
victory = 'result_png/500.png'
mfcc_pic = PhotoImage(file=victory)
mfcc_label = Label(master=back_right, image=mfcc_pic, width=mfcc_pic.width(),
                   height=mfcc_pic.height(), bg='red')
mfcc_label.pack_propagate(0)
mfcc_label.pack(side=TOP)

vision = Label(master=back_right, width=70, height=5)
vision.grid_propagate(0)
vision.pack(side=TOP)
vis_choice = []
vector = []
for i in range(13):
    vector.append(IntVar())
    vector[i].set(1)
for i in range(6):
    vis_choice.append(Checkbutton(master=vision, text='mfcc ' + str(i + 1)
                                  , variable=vector[i], width=7))
    vis_choice[i].grid(row=0, column=i, sticky=W)
for i in range(6, 12):
    vis_choice.append(Checkbutton(master=vision, text='mfcc ' + str(i + 1)
                                  , variable=vector[i], width=7))
    vis_choice[i].grid(row=1, column=i - 6, sticky=W)

vis_choice.append(Checkbutton(master=vision, text='energy per frame'
                              , variable=vector[12], width=14))
vis_choice[12].grid(row=2, column=0, columnspan=2, sticky=W)
Label(master=vision, width=10, height=1, text='win function', bg='white').grid(row=2, column=2
                                                        , columnspan=1, sticky=E)
Winfunc = StringVar()
comboxlist = ttk.Combobox(master=vision, text='winfunc', textvariable=Winfunc, width=14)
comboxlist['values'] = ("None", "Hamming")
comboxlist.current(1)
comboxlist.grid(row=2, column=3, columnspan=2, sticky=W)


def plot_mfcc():
    print('mfcc_plot')


mfcc_confirm = Button(master=vision, text='OK', width=10, height=1, command=plot_mfcc, bg='white')
mfcc_confirm.grid(row=2, column=5)

result = Label(master=back_right, width=70, height=2)
result.grid_propagate(0)
result.pack(side=TOP)
res_area = Label(master=result, width=20, height=2, bg='white')
res_area.grid(row=0, column=0, columnspan=3, sticky=W)
Label(master=result, width=5).grid(row=0, column=3)
mfcc_add = Label(master=result, width=12, text='mfcc address:', bg='pink')
mfcc_add.grid(row=0, column=4, columnspan=2)
add_area = Text(master=result, width=25, height=1)
add_area.grid(row=0, column=6, sticky=E)

root.mainloop()
