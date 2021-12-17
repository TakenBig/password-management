# coding=utf-8
# author: dbZhang
# update: 2021-12-16

# otherPage.py
# class OtherPage
# provide some simple funcitons about password

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox, END
from controller.accountController import AccountController
import pyperclip
from addPage import AddPage


PARENT_PATH = Path(__file__).parent.parent
IMAGE_PATH = PARENT_PATH / Path("./img/other_page_img")


def relative_to_assets(path):
    return IMAGE_PATH / Path(path)


class OtherPage:
    def __init__(self):
        self.initMainWindow()
        self.initCompoent()
        self.otherWindow.resizable(False,False)
        self.otherWindow.mainloop()

    def initMainWindow(self):
        self.otherWindow = Toplevel()
        self.otherWindow.geometry('300x450+900+180')
        self.otherWindow.configure(bg='#FFFFFF')
        self.otherWindow.title('其他功能')

    def initCompoent(self):
        self.initCanvas()
        self.initText()
        self.initButton()
        self.initEntry()

    def initCanvas(self):
        self.otherCanvas = Canvas(
            master=self.otherWindow,
            bg="#FFFFFF",
            height=450,
            width=300,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.otherCanvas.place(x=0, y=0)
        self.otherCanvas.create_rectangle(
            0.0,
            0.0,
            300.0016784667969,
            450.0,
            fill="#FFFFFF",
            outline=""
        )

    def initEntry(self):
        # 密码强度检测
        self.passwordDetection_img= PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.passwordDetection_bg = self.otherCanvas.create_image(
            116.0,
            61.5,
            image=self.passwordDetection_img
        )
        self.passwordDetectionEntry = Entry(
            master=self.otherWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.passwordDetectionEntry.place(
            x=16.0,
            y=48.0,
            width=200.0,
            height=27.0
        )
        # 密码生成
        self.passwordProduce_img = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.passwordProduce_bg = self.otherCanvas.create_image(
            116.0,
            146.5,
            image=self.passwordProduce_img
        )
        self.passwordProduceEntry = Entry(
            master=self.otherWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.passwordProduceEntry.place(
            x=16.0,
            y=133.0,
            width=200.0,
            height=27.0
        )

    def initButton(self):
        # 密码生成
        self.passwordProduceBtn_img= PhotoImage(file=relative_to_assets("button_1.png"))
        self.passwordProduceBtn = Button(
            master=self.otherWindow,
            image=self.passwordProduceBtn_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.passwordProduceBtn.place(
            x=240.0,
            y=131.0,
            width=42.0,
            height=31.0
        )
        # 开发人员
        self.aboutMeBtn_img = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.aboutMeBtn = Button(
            master=self.otherWindow,
            image=self.aboutMeBtn_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.aboutMeBtn.place(
            x=114.0,
            y=419.0,
            width=72.0,
            height=21.0
        )
        # 密码强度检测self.aboutMeBtn_img
        self.passwordDetectionBtn_img = PhotoImage(file=relative_to_assets("button_3.png"))
        self.passwordDetectionBtn = Button(
            master=self.otherWindow,
            image=self.passwordDetectionBtn_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.passwordDetectionBtn.place(
            x=240.0,
            y=46.0,
            width=42.0,
            height=31.0
        )
        # 事件绑定
        self.bindBtn()

    def initText(self):
        self.otherCanvas.create_text(
            11.0,
            18.0,
            anchor="nw",
            text="密码强度检测：",
            fill="#000000",
            font=("Roboto", 18 * -1)
        )
        self.otherCanvas.create_text(
            11.0,
            103.0,
            anchor="nw",
            text="密码生成：",
            fill="#000000",
            font=("Roboto", 18 * -1)
        )

    def bindBtn(self):
        self.passwordDetectionBtn.bind('<Button-1>', self.passwordDetectionBtnClicked)
        self.passwordProduceBtn.bind('<Button-1>', self.passwordProduceBtnClicked)
        self.aboutMeBtn.bind('<Button-1>', self.aboutMeBtnClicked)

    # 密码强度检测
    def passwordDetectionBtnClicked(self, event):
        controller = AccountController(password=self.passwordDetectionEntry.get())
        res = controller.passwordDetection()
        messagebox.showinfo(title='强度检测', message=res)

    # 密码生成
    def passwordProduceBtnClicked(self, event):
        controller = AccountController()
        res = controller.passwordProduce()
        self.passwordProduceEntry.delete(0,END)
        self.passwordProduceEntry.insert(0, res)
        pyperclip.copy(res)
        response = messagebox.askquestion(title='询问', message='是否创建并存储一个新账户 \n 密码已经复制')
        if response == 'yes':
            page = AddPage()
            # page.setPasswordText(res)
            # self.otherWindow.destroy()

    # 开发人员
    def aboutMeBtnClicked(self, event):
        messagebox.showinfo(title='介绍', message='作者: dbZhang \n 有问题可以发送邮件到：1508256957@qq.com')


if __name__ == '__main__':
    page = OtherPage()

