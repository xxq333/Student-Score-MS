#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 03, 2020 02:47:59 PM CST  platform: Windows NT

import sys
import xlwt
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

def grade_out():
    conn = pymysql.connect(host='localhost', user='root', passwd='809144', db='mydb', port=3306)
    cur = conn.cursor()
    cur.execute('select student.*,class.*,grade.grade from student,class,grade where student.sno = grade.sno and grade.cno = class.cno')
    r = cur.fetchall()
    filename = "gradeout.xls"
    w.Entry1.insert(0, 'D:/python1/'+filename)
    wbk = xlwt.Workbook()
    sheet1 = wbk.add_sheet('sheet1',cell_overwrite_ok=True)
    fileds = [u'学号',u'姓名',u'性别',u'年龄',u'学院',u'班级',u'课程号',u'课程名称',u'学分',u'成绩']
    conn.commit()
    i = 0
    for filed in range(0,len(fileds)):
        sheet1.write(0,filed,fileds[i])
        i +=1
    for r1 in range(1,len(r)+1):
        for col in range(0,len(fileds)):
            sheet1.write(r1,col,r[r1-1][col])
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = '等线'
    font.colour_index = 4
    font.height = 11
    style.font = font
    alignment = xlwt.Alignment()#居中
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment
    wbk.save(filename)
    cur.close()
    conn.close()
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import daochugrade
    daochugrade.vp_start_gui()




