# coding=UTF-8
# author: dbZhang
# update: 2021-12-11

from pathlib import Path
from tkinter import Frame, Label, Listbox, Scrollbar, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, messagebox
from tkinter import END, Menu
from tkinter.constants import BOTH, END, FLAT, GROOVE, LEFT, RIGHT, X, Y
import addPage
from controller.accountController import AccountController
import detailPage
import otherPage

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("./img/home_page_img")


def relative_to_assets(path: str):
    return ASSETS_PATH / Path(path)


class HomePage:

    def __init__(self):
        self.initMainWindow()
        self.initComponent()
        self.homeWindow.resizable(False, False)
        self.initAccountContents()
        self.homeWindow.mainloop()

    # 初始化主窗口
    def initMainWindow(self):
        self.homeWindow = Tk()
        self.homeWindow.geometry('300x450+600+180')
        self.homeWindow.configure(bg='#FFFFFF')
        self.homeWindow.title('密码本')

    # 初始化组件们
    def initComponent(self):
        self.initCanvas()
        self.initButton()
        self.initEntry()
        self.initInnerWin()

    # 初始化画板
    def initCanvas(self):
        # 画板
        self.homeCanvas = Canvas(
            self.homeWindow,
            bg="#FFFFFF",
            height=450,
            width=300,
            bd=0,
            highlightthickness=0,
            relief="ridge"
            # yscrollcommand=self.scrollBar
        )
        self.homeCanvas.place(x=0, y=0)
        self.homeCanvas.create_rectangle(
            0.0,
            0.0,
            300.02667236328125,
            450.0,
            fill="#FFFFFF",
            outline="")
        # 在画板上添加一个图片
        self.search_icon_img = PhotoImage(file=relative_to_assets('image_1.png'))
        self.serch_icon = self.homeCanvas.create_image(
            26.013336181640625,
            22.0,
            image=self.search_icon_img
        )

    # 初始化按钮
    def initButton(self):
        # 设置按钮
        self.setBtn_img = PhotoImage(file=relative_to_assets('button_1.png'))
        self.setBtn = Button(
            image=self.setBtn_img,
            borderwidth=0,
            highlightthickness=0,
            relief='flat'
        )
        self.setBtn.place(
            x=8.013336181640625,
            y=422.0,
            width=49.0,
            height=25.0
        )
        # 其他按钮
        self.otherBtn_img = PhotoImage(file=relative_to_assets('button_2.png'))
        self.otherBtn = Button(
            image=self.otherBtn_img,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.otherBtn.place(
            x=219.01333618164062,
            y=424.0,
            width=49.98666763305664,
            height=21.0
        )
        # 添加按钮
        self.addBtn_img = PhotoImage(file=relative_to_assets('button_3.png'))
        self.addBtn = Button(
            image=self.addBtn_img,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.addBtn.place(
            x=261.0133361816406,
            y=8.0,
            width=30.0,
            height=30.0
        )
        # 刷新按钮
        self.refreshBtn_img = PhotoImage(file=relative_to_assets('refresh_btn.png'))
        self.refreshBtn = Button(
            image=self.refreshBtn_img,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.refreshBtn.place(
            x=100,
            y=420,
            width=78,
            height=30
        )
        # 事件绑定
        self.bindBtn()

    # 初始化输入框
    def initEntry(self):
        self.search_entry_img = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.homeCanvas.create_image(
            150.01333618164062,
            22.5,
            image=self.search_entry_img
        )
        self.search_entry = Entry(
            bd=0,
            bg="#C4C4C4",
            highlightthickness=0
        )
        self.search_entry.place(
            x=52.013336181640625,
            y=7.0,
            width=196.0,
            height=29.0
        )
        # 响应事件绑定
        self.search_entry.bind('<Return>', self.searchEntryEntered)

    # 初始化内层窗口
    def initInnerWin(self):
        # 内层窗口
        self.innerWin = Frame(
            master=self.homeCanvas,
            borderwidth=5,
            relief=GROOVE
        )
        self.innerWin.place(
            x=8,
            y=50,
            width=284,
            height=370
        )
        self.myScrollBar = Scrollbar(
            master=self.innerWin
        )
        self.myScrollBar.pack(
            side=RIGHT,
            fill=Y
        )
        self.listbox = Listbox(
            master=self.innerWin,
            yscrollcommand=self.myScrollBar.set
        )
        self.listbox.config(
            font=("Roboto Bold", 24 * -1)
        )

        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.myScrollBar.config(
            command=self.listbox.yview
        )
        self.bindListBox()

    # 绑定按钮响应事件
    def bindBtn(self):
        self.setBtn.bind('<Button-1>', self.setBtnClicked)
        self.otherBtn.bind('<Button-1>', self.otherBtnClicked)
        self.addBtn.bind('<Button-1>', self.addBtnClicked)
        self.refreshBtn.bind('<Button-1>', self.refreshClicked)

    # 绑定列表框点击事件
    def bindListBox(self):
        # self.listbox.bind('<<ListboxSelect>>', self.itemSelected)
        self.listbox.bind('<Double-Button-1>', self.itemSelected)
        self.listbox.bind('<Button-3>', self.showPopUpMenu)

    # 设置按钮响应事件
    def setBtnClicked(self, event):
        # print('set button clicked')
        messagebox.showinfo(title='设置页面', message='由于时间原因，此页面暂时未开发')

    # 其他按钮响应事件
    def otherBtnClicked(self, event):
        page = otherPage.OtherPage()

    # 添加按钮响应事件
    def addBtnClicked(self, event):
        page = addPage.AddPage()

    # 刷新按钮响应事件
    def refreshClicked(self, event):
        self.deleteAllItems()
        self.initAccountContents()

    # 列表框点击事件
    def itemSelected(self, event):
        self.listbox.update()
        itemIndex = self.listbox.curselection()
        caption = self.listbox.get(itemIndex)
        detail_page = detailPage.Detail(caption=caption)

    # 搜索栏ENTER响应事件
    def searchEntryEntered(self, event):
        content = self.search_entry.get()
        controller = AccountController(caption=content)
        captions = controller.searchLikesCaption()
        self.deleteAllItems()
        for item in captions:
            self.addSingleItemToListBox(item.pop())

    # 往列表框添加一组元素
    def addItemToListBox(self, accountInfoList):
        for i in accountInfoList:
            self.listbox.insert(END, i)

    # 往列表框添加一个元素
    def addSingleItemToListBox(self, account):
        self.listbox.insert(END, account)

    # 面板内容初始化
    def initAccountContents(self):
        controller = AccountController()
        captions = controller.queryCaptions()
        for item in captions:
            self.addSingleItemToListBox(item.pop())

    # 删除listbox的所有选项
    def deleteAllItems(self):
        self.listbox.delete(0, END)

    # 弹出框
    def showPopUpMenu(self, event):
        popupmenu = Menu(
            master=self.listbox,
            tearoff=False
        )
        popupmenu.add(itemType='cascade', label='删除', command=self.deleterAccount)
        popupmenu.post(event.x_root, event.y_root)

    # 删除事件
    def deleterAccount(self):
        res = messagebox.askquestion(title='删除', message='是否删除')
        if res == 'yes':
            itemindex = self.listbox.curselection()
            caption = self.listbox.get(itemindex)
            # print(caption)
            controller = AccountController(caption=caption)
            flag = controller.deleteAccount()
            if flag:
                messagebox.showinfo(title='删除', message='删除成功')
            else:
                messagebox.showinfo(title='删除', message='删除失败')


if __name__ == '__main__':
    s = HomePage()
