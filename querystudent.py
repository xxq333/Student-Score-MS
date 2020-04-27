#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 02, 2020 10:28:16 PM CST  platform: Windows NT

import sys
import pymysql

try:
    import Tkinter as tk
    import Tkinter.messagebox as v
except ImportError:
    import tkinter as tk
    import tkinter.messagebox as v

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import querystudent_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    querystudent_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    querystudent_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1023x591+524+129")
        top.minsize(152, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("学生信息查询")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(top,show = 'headings')
        self.Scrolledtreeview1.place(relx=0.117, rely=0.389, relheight=0.469
                , relwidth=0.812)
        self.Scrolledtreeview1.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0",text="Tree")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="40")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="center")
        self.Scrolledtreeview1.heading("Col1",text="学号")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="191")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="center")
        self.Scrolledtreeview1.heading("Col2",text="姓名")
        self.Scrolledtreeview1.heading("Col2",anchor="center")
        self.Scrolledtreeview1.column("Col2",width="95")
        self.Scrolledtreeview1.column("Col2",minwidth="20")
        self.Scrolledtreeview1.column("Col2",stretch="1")
        self.Scrolledtreeview1.column("Col2",anchor="center")
        self.Scrolledtreeview1.heading("Col3",text="性别")
        self.Scrolledtreeview1.heading("Col3",anchor="center")
        self.Scrolledtreeview1.column("Col3",width="97")
        self.Scrolledtreeview1.column("Col3",minwidth="20")
        self.Scrolledtreeview1.column("Col3",stretch="1")
        self.Scrolledtreeview1.column("Col3",anchor="center")
        self.Scrolledtreeview1.heading("Col4",text="年龄")
        self.Scrolledtreeview1.heading("Col4",anchor="center")
        self.Scrolledtreeview1.column("Col4",width="93")
        self.Scrolledtreeview1.column("Col4",minwidth="20")
        self.Scrolledtreeview1.column("Col4",stretch="1")
        self.Scrolledtreeview1.column("Col4",anchor="center")
        self.Scrolledtreeview1.heading("Col5",text="学院")
        self.Scrolledtreeview1.heading("Col5",anchor="center")
        self.Scrolledtreeview1.column("Col5",width="196")
        self.Scrolledtreeview1.column("Col5",minwidth="20")
        self.Scrolledtreeview1.column("Col5",stretch="1")
        self.Scrolledtreeview1.column("Col5",anchor="w")
        self.Scrolledtreeview1.heading("Col6",text="班级")
        self.Scrolledtreeview1.heading("Col6",anchor="center")
        self.Scrolledtreeview1.column("Col6",width="96")
        self.Scrolledtreeview1.column("Col6",minwidth="20")
        self.Scrolledtreeview1.column("Col6",stretch="1")
        self.Scrolledtreeview1.column("Col6",anchor="center")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.117, rely=0.102, height=32, width=131)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {等线} -size 15")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''姓名查询：''')

        self.fname = tk.Entry(top)
        self.fname.place(relx=0.244, rely=0.102,height=31, relwidth=0.18)
        self.fname.configure(background="white")
        self.fname.configure(disabledforeground="#a3a3a3")
        self.fname.configure(font="TkFixedFont")
        self.fname.configure(foreground="#000000")
        self.fname.configure(highlightbackground="#d9d9d9")
        self.fname.configure(highlightcolor="black")
        self.fname.configure(insertbackground="black")
        self.fname.configure(selectbackground="#c4c4c4")
        self.fname.configure(selectforeground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.117, rely=0.203, height=32, width=131)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {等线} -size 15")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''学号查询：''')

        self.fsno = tk.Entry(top)
        self.fsno.place(relx=0.244, rely=0.203,height=31, relwidth=0.18)
        self.fsno.configure(background="white")
        self.fsno.configure(disabledforeground="#a3a3a3")
        self.fsno.configure(font="TkFixedFont")
        self.fsno.configure(foreground="#000000")
        self.fsno.configure(highlightbackground="#d9d9d9")
        self.fsno.configure(highlightcolor="black")
        self.fsno.configure(insertbackground="black")
        self.fsno.configure(selectbackground="#c4c4c4")
        self.fsno.configure(selectforeground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.459, rely=0.102, height=32, width=62)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=querystudent_support.namefind)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {等线} -size 13")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''查询''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.459, rely=0.203, height=37, width=61)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=querystudent_support.snofind)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {等线} -size 13")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''查询''')

        self.Label2_12 = tk.Label(top)
        self.Label2_12.place(relx=0.117, rely=0.288, height=32, width=131)
        self.Label2_12.configure(activebackground="#f9f9f9")
        self.Label2_12.configure(activeforeground="black")
        self.Label2_12.configure(background="#d9d9d9")
        self.Label2_12.configure(disabledforeground="#a3a3a3")
        self.Label2_12.configure(font="-family {等线} -size 15")
        self.Label2_12.configure(foreground="#000000")
        self.Label2_12.configure(highlightbackground="#d9d9d9")
        self.Label2_12.configure(highlightcolor="black")
        self.Label2_12.configure(text='''全部查询：''')

        self.Button2_13 = tk.Button(top)
        self.Button2_13.place(relx=0.254, rely=0.288, height=37, width=281)
        self.Button2_13.configure(activebackground="#ececec")
        self.Button2_13.configure(activeforeground="#000000")
        self.Button2_13.configure(background="#d9d9d9")
        self.Button2_13.configure(command=querystudent_support.allfind)
        self.Button2_13.configure(disabledforeground="#a3a3a3")
        self.Button2_13.configure(font="-family {等线} -size 13")
        self.Button2_13.configure(foreground="#000000")
        self.Button2_13.configure(highlightbackground="#d9d9d9")
        self.Button2_13.configure(highlightcolor="black")
        self.Button2_13.configure(pady="0")
        self.Button2_13.configure(text='''查询''')

        self.Button2_14 = tk.Button(top)
        self.Button2_14.place(relx=0.626, rely=0.102, height=37, width=281)
        self.Button2_14.configure(activebackground="#ececec")
        self.Button2_14.configure(activeforeground="#000000")
        self.Button2_14.configure(background="#d9d9d9")
        self.Button2_14.configure(command=querystudent_support.deletes)
        self.Button2_14.configure(disabledforeground="#a3a3a3")
        self.Button2_14.configure(font="-family {等线} -size 13")
        self.Button2_14.configure(foreground="#000000")
        self.Button2_14.configure(highlightbackground="#d9d9d9")
        self.Button2_14.configure(highlightcolor="black")
        self.Button2_14.configure(pady="0")
        self.Button2_14.configure(text='''删除''')

        self.Button2_15 = tk.Button(top)
        self.Button2_15.place(relx=0.626, rely=0.196, height=37, width=281)
        self.Button2_15.configure(activebackground="#ececec")
        self.Button2_15.configure(activeforeground="#000000")
        self.Button2_15.configure(background="#d9d9d9")
        self.Button2_15.configure(command=querystudent_support.updates)
        self.Button2_15.configure(disabledforeground="#a3a3a3")
        self.Button2_15.configure(font="-family {等线} -size 13")
        self.Button2_15.configure(foreground="#000000")
        self.Button2_15.configure(highlightbackground="#d9d9d9")
        self.Button2_15.configure(highlightcolor="black")
        self.Button2_15.configure(pady="0")
        self.Button2_15.configure(text='''修改''')

        self.Button2_16 = tk.Button(top)
        self.Button2_16.place(relx=0.626, rely=0.288, height=37, width=281)
        self.Button2_16.configure(activebackground="#ececec")
        self.Button2_16.configure(activeforeground="#000000")
        self.Button2_16.configure(background="#d9d9d9")
        self.Button2_16.configure(command=querystudent_support.adds)
        self.Button2_16.configure(disabledforeground="#a3a3a3")
        self.Button2_16.configure(font="-family {等线} -size 13")
        self.Button2_16.configure(foreground="#000000")
        self.Button2_16.configure(highlightbackground="#d9d9d9")
        self.Button2_16.configure(highlightcolor="black")
        self.Button2_16.configure(pady="0")
        self.Button2_16.configure(text='''添加''')

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Microsoft YaHei UI} 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





