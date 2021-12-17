# coding=UTF-8
# author: dbZhang
# updata: 2021-12-12

# detail.py
# class Detail
# create the interface contains the detail of concrete acoount
# provide the function of modify account
# direct copy account or password

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox, END
from controller.accountController import AccountController
import pyperclip

PARENT_PATH = Path(__file__).parent.parent
IMAGE_PATH = PARENT_PATH / Path("./img/detail_page_img")


def relative_to_assets(path: str):
    return IMAGE_PATH / Path(path)


class Detail:
    def __init__(self, caption=None, account=None, password=None, note=None):
        self.caption = caption
        self.account = account
        self.password = password
        self.note = note
        self.status = True
        self.initMainWindow()
        self.initCompoent()
        self.quertByCaption()
        self.detailWindow.resizable(False, False)
        self.detailWindow.mainloop()

    # 初始化主界面
    def initMainWindow(self):
        self.detailWindow = Toplevel()
        self.detailWindow.geometry('300x450+900+180')
        self.detailWindow.configure(bg='#FFFFFF')
        self.detailWindow.title('查看详情')

    # 初始化组件
    def initCompoent(self):
        self.initCanvas()
        self.initText()
        self.initEntry()
        self.initButton()

    # 初始化画布
    def initCanvas(self):
        self.detailCanvas = Canvas(
            self.detailWindow,
            bg='#FFFFFF',
            height=450,
            width=300,
            bd=0,
            highlightthickness=0,
            relief='ridge'
        )
        self.detailCanvas.place(x=0, y=0)
        self.detailCanvas.create_rectangle(
            9.0,
            6.0,
            292.0,
            444.0,
            fill="#FFFFFF",
            outline=""
        )

    # 初始化文本
    def initText(self):
        self.detailCanvas.create_text(
            27.0,
            170.0,
            anchor="nw",
            text="备注：",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )

        self.detailCanvas.create_text(
            27.0,
            124.0,
            anchor="nw",
            text="标题：",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )

        self.detailCanvas.create_text(
            27.0,
            32.0,
            anchor="nw",
            text="账号：",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )

        self.detailCanvas.create_text(
            27.0,
            78.0,
            anchor="nw",
            text="密码：",
            fill="#000000",
            font=("Roboto Bold", 24 * -1)
        )

    # 初始化输入框
    def initEntry(self):
        # 账号输入框
        self.account_entry_img = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.detailCanvas.create_image(
            176.5,
            46.0,
            image=self.account_entry_img
        )
        self.account_entry = Entry(
            self.detailWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.account_entry.place(
            x=102.0,
            y=37.0,
            width=149.0,
            height=18.0
        )
        # 密码输入框
        self.password_entry_img = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.detailCanvas.create_image(
            176.5,
            89.0,
            image=self.password_entry_img
        )
        self.password_entry = Entry(
            self.detailWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            show='*'
        )
        self.password_entry.place(
            x=102.0,
            y=80.0,
            width=149.0,
            height=18.0
        )
        # 标题输入框
        self.caption_entry_img = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.detailCanvas.create_image(
            176.5,
            132.0,
            image=self.caption_entry_img
        )
        self.caption_entry = Entry(
            self.detailWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.caption_entry.place(
            x=102.0,
            y=123.0,
            width=149.0,
            height=18.0
        )
        # 备注输入框
        self.note_entry_img = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.detailCanvas.create_image(
            176.5,
            226.0,
            image=self.note_entry_img
        )
        self.note_entry = Text(
            self.detailWindow,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.note_entry.place(
            x=102.0,
            y=174.0,
            width=149.0,
            height=105.0
        )

    # 初始化按钮
    def initButton(self):
        # 账号一键复制按钮
        self.account_copy_img = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.account_copy_btn = Button(
            self.detailWindow,
            image=self.account_copy_img,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.account_copy_btn.place(
            x=57.0,
            y=304.0,
            width=190.0,
            height=37.0
        )
        # 密码一键复制按钮
        self.password_copy_img = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.password_copy_btn = Button(
            self.detailWindow,
            image=self.password_copy_img,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.password_copy_btn.place(
            x=57.0,
            y=351.0,
            width=190.0,
            height=37.0
        )
        # 修改按钮
        self.modify_img = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.modify_btn = Button(
            self.detailWindow,
            image=self.modify_img,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.modify_btn.place(
            x=57.0,
            y=396.0,
            width=190.0,
            height=37.0
        )
        # 确定按钮
        self.confirm_btn_img = PhotoImage(file=relative_to_assets('confirm_btn.png'))

        # 按钮响应事件绑定
        self.bindBtn()

        # 绑定按钮事件

    # 事件绑定
    def bindBtn(self):
        self.account_copy_btn.bind('<Button-1>', self.accountCopyBtnClicked)
        self.password_copy_btn.bind('<Button-1>', self.passwordCopyBtnClicked)
        self.modify_btn.bind('<Button-1>', self.mofifyBtnClicked)

    # 标题输入框
    def setCaptionEntry(self, string):
        self.caption_entry.insert(0, string=string)
        self.caption_entry.config(state='disable')

    # 账号输入框
    def setAccountEntry(self, string):
        self.account_entry.insert(0, string)
        self.account_entry.config(state='disable')

    # 密码输入框
    def setPasswordEntry(self, string):
        self.password_entry.insert(0, string)
        self.password_entry.config(state='disable')

    # 备注输入框
    def setNoteEntry(self, string):
        self.note_entry.insert("1.0", string)
        self.note_entry.config(state='disabled')

    # 账号复制按钮响应事件
    def accountCopyBtnClicked(self, event):
        account = self.account_entry.get()
        pyperclip.copy(account)
        messagebox.showinfo(title='复制', message='账号复制成功')

    # 密码复制按钮响应事件
    def passwordCopyBtnClicked(self, event):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo(title='复制', message='密码复制成功')

    # 修改按钮响应事件
    def mofifyBtnClicked(self, event):
        if self.status:  # 修改按钮状态
            self.modify_btn.config(
                image=self.confirm_btn_img
            )
            self.modifiedEntryNormal()
            self.status = False
        else:   # 确认修改状态
            self.modify_btn.config(
                image=self.modify_img
            )
            caption = self.caption_entry.get()  # 获得标签内容
            account = self.account_entry.get()
            password = self.password_entry.get()
            note = self.note_entry.get('0.0', 'end').strip('\n')
            self.caption_entry.delete(0, END)   # 标签内容清空
            self.account_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.note_entry.delete('0.0', 'end')
            controller = AccountController(caption, account, password, note)
            flag = controller.updateAccount()  # 更新账户信息
            if flag:
                messagebox.showinfo(title='修改', message='修改成功')
            else:
                messagebox.showinfo(title='修改', message='修改失败')
            self.status = True
            self.quertByCaption()
        self.detailCanvas.update()

    # 传入caption参数
    def quertByCaption(self):
        # self.caption = caption
        controller = AccountController(caption=self.caption)
        query_res = controller.queryByCaption()
        print(query_res)
        for item in query_res:
            self.setCaptionEntry(item[0])
            self.setAccountEntry(item[1])
            self.setPasswordEntry(item[2])
            self.setNoteEntry(item[3])

    # 修改输入框的属性为可修改
    def modifiedEntryNormal(self):
        self.caption_entry.config(state='normal')
        self.password_entry.config(state='normal')
        self.note_entry.config(state='normal')
