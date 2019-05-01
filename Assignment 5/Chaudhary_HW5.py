import tkinter
import tkinter.messagebox
import math


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Right Triangle Calculator')
        self.main_window.geometry('450x150')
        self.top_frame1 = tkinter.Frame(self.main_window)
        self.top_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label1 = tkinter.Label(self.top_frame1, text='Side A:')
        self.prompt_label2 = tkinter.Label(self.top_frame2, text='Side B:')
        self.entry1 = tkinter.Entry(self.top_frame1, width=50)
        self.entry2 = tkinter.Entry(self.top_frame2, width=50)
        self.prompt_label1.pack(side='left', padx=10, ipadx=10, ipady=10)
        self.entry1.pack(side='left')
        self.prompt_label2.pack(side='left', padx=10, ipadx=10, ipady=10)
        self.entry2.pack(side='left')
        self.des_label = tkinter.Label(self.mid_frame, text='Side C:')
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)
        self.des_label.pack(side='left')
        self.miles_label.pack(side='left')
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.calculate_side)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='right', padx=10, pady=10)
        self.calc_button.pack(side='right')
        self.top_frame1.pack()
        self.top_frame2.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()


    def calculate_side(self):
        side1 = float(self.entry1.get())
        side2 = float(self.entry2.get())
        side3 = format(math.sqrt(side1**2 + side2**2), '.3f')
        self.value.set(side3)


my_gui = MyGUI()