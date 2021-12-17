# coding=UTF-8
# author: dbZhang
# update: 2021-12-10


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from controller.accountController import AccountController


PARENT_PATH = Path(__file__).parent.parent
IMAGE_PATH = PARENT_PATH / Path("./img/add_page_img")


def relative_to_assets(path: str):
    return IMAGE_PATH / Path(path)


class AddPage:
    def __init__(self):
        self.initMainWindow()
        self.initComponent()
        self.addWindow.resizable(False, False)
        self.addWindow.mainloop()

    # 初始化主界面
    def initMainWindow(self):
        self.addWindow = Toplevel()
        self.addWindow.geometry("300x450+900+180")
        self.addWindow.configure(bg='#FFFFFF')
        self.addWindow.title('添加账号密码')

    # 初始化组件
    def initComponent(self):
        self.initCanvas()
        self.initText()
        self.initEntry()
        self.initBtn()

    # 初始化画布
    def initCanvas(self):
        self.addCanvas = Canvas(
            master=self.addWindow,
            bg="#FFFFFF",
            height=450,
            width=300,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.addCanvas.place(x=0, y=0)

    # 初始化文本
    def initText(self):
        self.addCanvas.create_text(
            21.0,
            61.0,
            anchor="nw",
            text="账号",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )
        self.addCanvas.create_text(
            21.0,
            108.0,
            anchor="nw",
            text="密码",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )
        self.addCanvas.create_text(
            21.0,
            163.0,
            anchor="nw",
            text="标题",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )
        self.addCanvas.create_text(
            21.0,
            225.0,
            anchor="nw",
            text="备注",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )

    # 初始化输入框
    def initEntry(self):
        # 账号输入框
        self.account_img = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.account_bg = self.addCanvas.create_image(
            173.5,
            75.0,
            image=self.account_img
        )
        self.account_entry = Entry(
            master=self.addWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.account_entry.place(
            x=85.0,
            y=65.0,
            width=177.0,
            height=21.0
        )
        # 密码输入框
        self.password_img = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.password_bg = self.addCanvas.create_image(
            173.5,
            120.0,
            image=self.password_img
        )
        self.password_entry = Entry(
            master=self.addWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.password_entry.place(
            x=85.0,
            y=115.0,
            width=150.0,
            height=15.0
        )
        # 标题输入框
        self.caption_img = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.caption_bg = self.addCanvas.create_image(
            173.5,
            175.0,
            image=self.caption_img
        )
        self.caption_entry = Entry(
            master=self.addWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.caption_entry.place(
            x=85.0,
            y=170.0,
            width=160.0,
            height=12.0
        )
        # 备注输入框
        self.note_img = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.note_bg = self.addCanvas.create_image(
            173.5,
            295.0,
            image=self.note_img
        )
        self.note_entry = Text(
            master=self.addWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.note_entry.place(
            x=85.0,
            y=230.0,
            width=170.0,
            height=130.0
        )

        # 初始化按钮

    # 初始化按钮
    def initBtn(self):
        # 确认按钮
        self.confirmBtn_img = PhotoImage(file=relative_to_assets("confirm_btn.png"))
        self.confirmBtn = Button(
            master=self.addWindow,
            image=self.confirmBtn_img,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda:print('确认按钮'),
            relief='flat'
        )
        self.confirmBtn.place(
            x=21.0,
            y=393.0,
            width=75.0,
            height=40.0
        )
        # 取消按钮
        self.cancelBtn_img = PhotoImage(file=relative_to_assets('cancel_btn.png'))
        self.cancelBtn = Button(
            master=self.addWindow,
            image=self.cancelBtn_img,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda:print("取消按钮"),
            relief='flat'
        )
        self.cancelBtn.place(
            x=195.0,
            y=393.0,
            width=75.0,
            height=40.0
        )
        self.bindBtn()

    # 获得输入框内容
    def getAccountText(self):
        return self.account_entry.get()

    def getPasswordText(self):
        return self.password_entry.get()

    def getCaptionText(self):
        return self.caption_entry.get()

    def getNoteText(self):
        return self.note_entry.get('0.0', 'end').strip('\n')

    def setPasswordText(self, text):
        self.password_entry.insert(0, text)

    # 返回四个输入框的内容
    def getallmessage(self):
        msg = [self.getCaptionText(), self.getAccountText(), self.getPasswordText(), self.getNoteText()]
        return msg

    # 绑定按钮和监听事件
    def bindBtn(self):
        self.confirmBtn.bind('<Button-1>', self.confirmBtnClicked)
        self.cancelBtn.bind('<Button-1>', self.cancelBtnClicked)

    # 确认按钮响应事件
    def confirmBtnClicked(self, event):
        controller = AccountController(self.getCaptionText(),self.getAccountText(),self.getPasswordText(),self.getNoteText())
        if controller.addAccount():
            messagebox.showinfo(title='添加账号', message='添加成功!')
            self.addWindow.destroy()
        else:
            messagebox.showinfo(title='添加账号', message='添加失败！')

    # 取消按钮响应事件
    def cancelBtnClicked(self, event):
        self.addWindow.destroy()


# test
if __name__ == '__main__':
    s = AddPage()
