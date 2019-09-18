from tkinter import *
from Recognizer import Recognizer, Talker
import speech
import talk_online
'''
GUI window:
1.welcome window -> click 'Get Start'
2.left -> words recognize
3.top right -> mfcc picture
4.bottom right -> speak to robot
'''


class Window(object):
    def __init__(self):
        '''
        variables clarification
        definition of variables in this class
        '''
        self.root = Tk()
        self.welcome_label = Label(master=self.root, width=80, height=30)
        self.photo = PhotoImage(file='new_welc.png')
        self.back_right = Label(master=self.root, width=50, height=30, bg='green')
        self.back_left = Label(master=self.root, width=30, height=30, bg='blue')
        self.img_label = Label(master=self.welcome_label, image=self.photo, height=self.photo.height(),
                               width=self.photo.width())
        self.welc_over_but = Button(master=self.img_label,
                                    text='Get Start', width=20, height=1, command=self.come_in)
        self.mfcc_label = Label(master=self.back_right, width=50, height=16, bg='yellow')
        self.word_label = Label(master=self.back_left, width=30, height=30, bg='pink')
        self.word_list = Listbox(master=self.word_label, width=30, height=10)
        self.word_rec_label = Label(master=self.word_label, height=1, width=30, bg='red')
        self.word_rec_but = Button(master=self.word_rec_label, height=1, width=10,
                                   text='Listen to me', command=self.listen_word)
        self.auto_cover = IntVar()
        self.word_args = Label(master=self.word_label, width=30, height=6, bg='blue')
        self.word_rec_time = Text(master=self.word_args, width=30, height=1)
        self.word_file = Text(master=self.word_args, width=30, height=1)
        self.word_listen_status = Label(master=self.word_args, width=30, height=4, bg='white')
        self.word_result = Listbox(master=self.word_label, height=13, width=30)
        self.mfcc_pic_label = Label(master=self.mfcc_label, height=16, width=50)
        self.mfcc_pic = None
        self.talk_label = Label(master=self.back_right, width=50, height=14, bg='purple')
        self.talk_arg = Label(master=self.talk_label, width=50, height=2)
        self.lcy = Label(master=self.talk_arg, width=20, height=3)
        self.fjw = Label(master=self.talk_arg, width=30, height=3, bg='green')
        self.talk_rec_but = Button(master=self.lcy, width=10, height=2,
                                   command=self.listen_talk, text="Let's chat!")
        self.talk_auto_cover = IntVar()
        self.talk_rec_time = Text(master=self.fjw, width=30, height=1)
        self.talk_file = Text(master=self.fjw, width=30, height=1)
        self.talk_area = Label(master=self.talk_label, width=50, height=12)
        self.talk_history = Text(master=self.talk_area, width=50, height=12)
        self.speech_content = Text(master=self.talk_area, width=50, height=2)
        self.rc = Recognizer()
        self.talker = Talker()

        self.root.title('Speech Recognizer')
        self.welcome()

    def come_in(self):
        print('in come_in')
        self.welcome_label.destroy()
        self.back_left.pack(side=LEFT)
        self.back_right.pack(side=LEFT)
        self.back_left.pack_propagate(0)
        self.back_right.pack_propagate(0)
        self.mfcc_label.pack(side=TOP)
        self.mfcc_label.pack_propagate(0)
        self.word_label.pack()
        self.word_label.pack_propagate(0)
        self.words_section()
        self.mfcc_section()
        self.talk_section()
        self.rc.welcome()

    def welcome(self):
        print('in welcome')
        self.welcome_label.pack()
        self.welcome_label.pack_propagate(0)
        self.img_label.pack()
        self.img_label.pack_propagate(0)
        self.welc_over_but.pack()

    '''
    the input parameter is the name of the mfcc_picture
    this function only update mfcc_pic_label
    '''
    def show_mfcc(self, filename):
        self.mfcc_pic = PhotoImage(file=filename)
        self.mfcc_pic_label.destroy()
        self.mfcc_pic_label = Label(master=self.mfcc_label, image=self.mfcc_pic, height=400, width=400)
        self.mfcc_pic_label.pack()
        return

    def talk_section(self):
        self.talk_label.pack()
        self.talk_label.pack_propagate(0)
        self.talk_arg.pack()
        self.talk_arg.pack_propagate(0)
        self.lcy.pack(side=LEFT)
        self.lcy.pack_propagate(0)
        self.fjw.pack(side=RIGHT)
        self.fjw.pack_propagate(0)
        self.talk_rec_but.pack(side=LEFT)
        self.talk_rec_but.pack_propagate(0)
        self.talk_auto_cover.set(1)
        Checkbutton(self.lcy, text='cover', variable=self.talk_auto_cover, width=10, height=2).pack()
        self.talk_rec_time.pack()
        self.talk_rec_time.insert(END, 'Record time: 2s')
        self.talk_file.pack()
        self.talk_file.insert(END, 'File: ')
        self.talk_area.pack()
        self.talk_area.pack_propagate(0)
        self.talk_history.pack(side=TOP)
        self.talk_history.pack_propagate(0)
        self.speech_content.pack(side=BOTTOM)
        self.speech_content.pack_propagate(0)

    '''
    called when you hit 'Let's chat' button
    using self.talker to chat
    
    '''
    def listen_talk(self):
        ret, name = self.talker.work((self.talk_auto_cover.get() == 1))
        # print(ret)
        self.talk_file.delete('0.0', END)
        self.talk_file.insert(END, 'File: ' + name)
        data = self.rc.get_wav_mfcc(name)
        filename = 'Oldboy.png'
        self.rc.plot_save(filename, data)
        self.show_mfcc(filename=filename)

        '''
        react to the ret
        '''
        self.word_result.delete(0, END)
        for xx in ret:
            self.word_result.insert(END, xx)

        self.speech_content.delete('0.0', END)
        try:
            self.speech_content.insert(END, ret[0])
        except:
            self.speech_content.insert(END, '你说话了吗')
        self.talk_react(ret[0])
        return

    '''
    for message translated by API
    react some words
    '''
    def talk_react(self, msg):
        print('get message', msg)
        if msg.find('天气') != -1:
            ans = talk_online.weather()
            speech.say('为你找到今天的天气')
            self.talk_history.insert(END, '\n------------------\n')
            for ww in ans:
                self.talk_history.insert(END, ww + '\n')
            return
        if msg.find('笑话') != -1:
            ans = talk_online.joke()
            speech.say('我想到一个好笑的笑话')
            self.talk_history.insert(END, '\n------------------\n')
            self.talk_history.insert(END, ans + '\n')
            return
        if msg.find('成绩') != -1:
            ans = talk_online.grade()
            speech.say('正在查询你的成绩')
            self.talk_history.insert(END, '\n------------------\n')
            for line in ans:
                self.talk_history.insert(END, line + '\n')
            return


    def mfcc_section(self):
        self.mfcc_pic_label.pack()

    def prep_word_list(self):
        for a_word in [
            'rich',
            'flash',
            'blog',
            'mathematics',
            'hard',
            'twenty',
            'love',
            'girl',
            'banana',
            'apple'
        ]:
            self.word_list.insert(END, a_word)

    def words_section(self):
        self.prep_word_list()
        self.word_list.pack()
        self.word_rec_label.pack(side=TOP)
        self.word_rec_label.pack_propagate(0)
        self.word_rec_but.pack(side=LEFT)
        self.auto_cover.set(1)
        Checkbutton(self.word_rec_label, text='auto-cover', variable=self.auto_cover, width=20).pack(side=LEFT)
        self.word_args.pack()
        self.word_args.pack_propagate(0)
        self.word_rec_time.grid(row=0, column=0)
        self.word_rec_time.insert(END, 'Record time: 2s')
        self.word_file.grid(row=1, column=0)
        self.word_file.insert(END, 'File: ')
        self.word_listen_status.grid(row=2, column=0)
        self.word_listen_status.pack_propagate(0)
#        for i in self.word_list.get(0, END):
#            self.word_result.insert(END, str(i) + ' with probability of ')
        self.word_result.pack()

    '''
    listen_word function, when you hit 'Listen to me' Button,
    print 'in listen word', then the machine record the word you say for the next 2 seconds,
    record filename will be sent by rec_word function from Recognizer
    use show_mfcc to plot the picture of wav_file 'filename'
    submit data to word_react'''
    def listen_word(self):
        print('in listen_word')
        Label(master=self.word_listen_status, text="I'm listening~", width=30, height=4).pack()
        wav_file = self.rc.record((self.auto_cover.get() == 1))  # start to record
        self.word_file.delete('0.0', END)
        self.word_file.insert(END, 'File: ' + wav_file)
        filename = 'Oldboy.png' # mfcc picture filename
        data = self.rc.rec_word(wav_file)   # recognize word data
        mfcc_data = self.rc.get_wav_mfcc(wav_file)  # mfcc data
        self.rc.plot_save(filename, mfcc_data)  # plot the data
        self.show_mfcc(filename)    # show the plot picture
        # not complete
        # complete
        self.word_react(data)   # update result on GUI

    '''
    word_react get recognition data from listen_word
    use the data to update the content in word_result list and voice speech
    '''
    def word_react(self, data):
        self.word_result.delete(0, END)
        usu = []
        for word in data:
            if word not in usu:
                self.word_result.insert(END, word)
                usu.append(word)
        try:
            speech.say('我认为你刚才说了' + data[0])
        except:
            speech.say('你发音不太标准哦')
        return


if __name__ == '__main__':
    win = Window()
    win.root.mainloop()
