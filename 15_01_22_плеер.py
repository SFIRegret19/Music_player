from tkinter import *
from pygame import mixer
from tkinter import filedialog as fd

root = Tk()


frame1 = Frame()
frame2 = Frame()

#frame1
song_state_label = Label(frame1,width=60,text = 'Остановлено')

song_state_label.pack()
frame1.pack()

#frame2
track_list_box = Listbox(frame2,width=60,height=10,selectmode=SINGLE)
frame3 = Frame(frame2)
open_file_button = Button(frame3,text='Open file',width=15,height=2,)
close_file_button = Button(frame3,text='Open folder',width=15,height=2)

open_file_button.pack()
close_file_button.pack()
track_list_box.pack(side=LEFT)
frame3.pack(side=LEFT)
frame2.pack()
#frame4
frame4 = Frame()
B_play = Button(frame4,text='▶',width=5,height=2)
B_pause = Button(frame4,text='❚❚',width=5,height=2)
B_next = Button(frame4,text='▷▷',width=5,height=2)
B_previous = Button(frame4,text='◁◁',width=5,height=2)
B_stop = Button(frame4,text='▢',width=5,height=2)

B_previous.pack(side=LEFT)
B_play.pack(side=LEFT)
B_pause.pack(side=LEFT)
B_next.pack(side=LEFT)
B_stop.pack(side=LEFT)
frame4.pack()

root.mainloop()