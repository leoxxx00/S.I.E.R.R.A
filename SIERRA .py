import tkinter.messagebox
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter import Entry, Tk
import sqlite3
import tkinter
from tkinter import ttk
import docx
from docx.shared import Inches
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
from docxtpl import DocxTemplate
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import os
import datetime
import pandas as pd
from docx import Document
from docx.shared import Inches
import glob
import os
import qrcode
import numpy as np
w=Tk()
w.title('Welcome from S.I.E.R.R.A')
w.geometry('300x280')
pic=PhotoImage(file='sierra.png')
con = sqlite3.connect("activation.db")
c = con.cursor()
c.execute("""Create table IF NOT EXISTS activation(
        email text,
        password text
        )""")
def activate():
    wa = Tk()
    wa.title('S.I.E.R.R.A')
    wa.geometry('166x200')
    con = sqlite3.connect("activation.db")
    c = con.cursor()
    c.execute("""
            INSERT INTO activation (email, password) VALUES ("000@gmail.com", "000")
            """)
    print('S.I.E.R.R.A is now activated')
    def RA():
        wam = Tk()
        wam.title('Request to Register an Account')
        wam.geometry("666x202")
        con = sqlite3.connect('DATA.db')
        c = con.cursor()
        c.execute("""CREATE TABLE if not exists requestacc (
                          	email text,
                          	password text,
                          	type text,
                          	id integer)
                          	""")
        con.commit()
        con.close()
        d_fr = LabelFrame(wam, text="Entries")
        d_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
        e_l = Label(d_fr, text="Email")
        e_l.grid(row=2, column=0, padx=10, pady=10)
        e_e = Entry(d_fr)
        e_e.grid(row=2, column=1, padx=10, pady=10)
        p_l = Label(d_fr, text="Password")
        p_l.grid(row=2, column=2, padx=10, pady=10)
        p_e = Entry(d_fr)
        p_e.grid(row=2, column=3, padx=10, pady=10)
        ty_l = Label(d_fr, text="Account Type")
        ty_l.grid(row=3, column=0, padx=10, pady=10)
        ty_e = Entry(d_fr)
        ty_e.grid(row=3, column=1, padx=10, pady=10)
        id_l = Label(d_fr, text="ID")
        id_l.grid(row=3, column=2, padx=10, pady=10)
        id_e = Entry(d_fr)
        id_e.grid(row=3, column=3, padx=10, pady=10)
        def remove_ent():
            e_e.delete(0, END)
            p_e.delete(0, END)
            ty_e.delete(0, END)
            id_e.delete(0, END)
        def recadd():
            con = sqlite3.connect('DATA.db')
            c = con.cursor()
            c.execute("INSERT INTO requestacc VALUES (:first, :last,:type, :id)",
                      {
                          'first': e_e.get(),
                          'last': p_e.get(),
                          'type': ty_e.get(),
                          'id': id_e.get()
                      })
            con.commit()
            con.close()
            e_e.delete(0, END)
            p_e.delete(0, END)
            ty_e.delete(0, END)
            id_e.delete(0, END)
            tkinter.messagebox.showinfo("blah", "Account Requested")
            wam.destroy()
            wa.destroy()
        b_fr = LabelFrame(wam, text="Commands")
        b_fr.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
        add_b = Button(b_fr, text="Request to Register", command=recadd)
        add_b.grid(row=0, column=1, padx=10, pady=10)
        select_rec_b = Button(b_fr, text="Clear Entries", command=remove_ent)
        select_rec_b.grid(row=0, column=7, padx=10, pady=10)
        wam.mainloop()
    def admin():
        wad = Tk()
        wad.title('Admin login')
        wad.geometry('390x111')
        wa.destroy()
        def adminsubmit():
            con = sqlite3.connect("activation.db")
            c = con.cursor()
            c.execute("SELECT * FROM activation where email=? AND password=?", (email.get(), password.get()))
            row = c.fetchone()
            if row:
                tkinter.messagebox.showinfo("blah", "Hello Admin")
                wadmin = Tk()
                wadmin.title('Admin Managenemt')
                wadmin.geometry('300x155')
                w.destroy()
                wad.destroy()
                def am():
                    wam = Tk()
                    wam.title('Manage Accounts')
                    wam.geometry("1122x444")
                    def RQ():
                        wam = Tk()
                        wam.title('Requested Accounts')
                        wam.geometry("1111x444")
                        def q_data():
                            for rec in tree.get_children():
                                tree.delete(rec)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("SELECT rowid, * FROM requestacc")
                            rcs = c.fetchall()
                            global cnt
                            cnt = 0
                            for rec in rcs:
                                if cnt % 2 == 0:
                                    tree.insert(parent='', index='end', iid=cnt, text='',
                                                values=(rec[1], rec[2],rec[3], rec[0]), tags=('evenrow',))
                                else:
                                    tree.insert(parent='', index='end', iid=cnt, text='',
                                                values=(rec[1], rec[2], rec[3],rec[0]), tags=('oddrow',))
                                cnt += 1
                            con.commit()
                            con.close()
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists requestacc (
                        	email text,
                        	password text,
                        	type text,
                        	id integer)
                        	""")
                        con.commit()
                        con.close()
                        tree_f = Frame(wam)
                        tree_f.pack(pady=10)
                        tree_scr = Scrollbar(tree_f)
                        tree_scr.pack(side=RIGHT, fill=Y)
                        tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                        tree.pack()
                        tree_scr.config(command=tree.yview)
                        tree['columns'] = ("Email", "Password", "type","ID")
                        tree.column("#0", width=0, stretch=NO)
                        tree.column("Email", anchor=W, width=250)
                        tree.column("Password", anchor=W, width=250)
                        tree.column("type", anchor=W, width=250)
                        tree.column("ID", anchor=CENTER, width=250)
                        tree.heading("#0", text="", anchor=W)
                        tree.heading("Email", text="Email", anchor=W)
                        tree.heading("Password", text="Password", anchor=W)
                        tree.heading("type", text="Account Type", anchor=W)
                        tree.heading("ID", text="ID", anchor=CENTER)
                        d_fr = LabelFrame(wam, text="Entries")
                        d_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                        e_l = Label(d_fr, text="Email")
                        e_l.grid(row=2, column=0, padx=10, pady=10)
                        e_e = Entry(d_fr)
                        e_e.grid(row=2, column=1, padx=10, pady=10)
                        p_l = Label(d_fr, text="Password")
                        p_l.grid(row=2, column=2, padx=10, pady=10)
                        p_e = Entry(d_fr)
                        p_e.grid(row=2, column=3, padx=10, pady=10)
                        id_l = Label(d_fr, text="ID")
                        id_l.grid(row=2, column=4, padx=10, pady=10)
                        id_e = Entry(d_fr)
                        id_e.grid(row=2, column=5, padx=10, pady=10)
                        def r1():
                            z = tree.selection()[0]
                            tree.delete(z)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("DELETE from requestacc WHERE oid=" + id_e.get())
                            con.commit()
                            con.close()
                            remove_ent()
                            messagebox.showinfo("!!!", "The selected Account has been deleated!")
                        def remove_ent():
                            e_e.delete(0, END)
                            p_e.delete(0, END)
                            id_e.delete(0, END)
                        def sel_rec(e):
                            e_e.delete(0, END)
                            p_e.delete(0, END)
                            id_e.delete(0, END)
                            select = tree.focus()
                            assign = tree.item(select, 'values')
                            e_e.insert(0, assign[0])
                            p_e.insert(0, assign[1])
                            id_e.insert(0, assign[3])
                            con.commit()
                            con.close()
                            e_e.delete(0, END)
                            p_e.delete(0, END)
                            id_e.delete(0, END)
                            tree.delete(*tree.get_children())
                            q_data()
                        def table_loop():
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("""CREATE TABLE if not exists requestacc (
                        		email text,
                        		password text,
                        		type text,
                        		id integer)
                        		""")
                            con.commit()
                            con.close()
                        b_fr = LabelFrame(wam, text="Commands")
                        b_fr.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                        rm_1_b = Button(b_fr, text="Delete Selected One", command=r1)
                        rm_1_b.grid(row=0, column=3, padx=10, pady=10)
                        select_rec_b = Button(b_fr, text="Clear Entries", command=remove_ent)
                        select_rec_b.grid(row=0, column=4, padx=10, pady=10)
                        tree.bind("<ButtonRelease-1>", sel_rec)
                        q_data()
                        wam.mainloop()
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM acc")
                        rcs = c.fetchall()
                        global cnt
                        cnt = 0
                        for rec in rcs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[0]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[0]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists acc (
                    	email text,
                    	password text,
                    	id integer)
                    	""")
                    con.commit()
                    con.close()
                    tree_f = Frame(wam)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Email", "Password", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Email", anchor=W, width=350)
                    tree.column("Password", anchor=W, width=350)
                    tree.column("ID", anchor=CENTER, width=310)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Email", text="Email", anchor=W)
                    tree.heading("Password", text="Password", anchor=W)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    d_fr = LabelFrame(wam, text="Entries")
                    d_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                    e_l = Label(d_fr, text="Email")
                    e_l.grid(row=2, column=0, padx=10, pady=10)
                    e_e = Entry(d_fr)
                    e_e.grid(row=2, column=1, padx=10, pady=10)
                    p_l = Label(d_fr, text="Password")
                    p_l.grid(row=2, column=2, padx=10, pady=10)
                    p_e = Entry(d_fr)
                    p_e.grid(row=2, column=3, padx=10, pady=10)
                    id_l = Label(d_fr, text="ID")
                    id_l.grid(row=2, column=4, padx=10, pady=10)
                    id_e = Entry(d_fr)
                    id_e.grid(row=2, column=5, padx=10, pady=10)
                    def r1():
                        z = tree.selection()[0]
                        tree.delete(z)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("DELETE from acc WHERE oid=" + id_e.get())
                        con.commit()
                        con.close()
                        remove_ent()
                        messagebox.showinfo("!!!", "The selected Account has been deleated!")
                    def r_all():
                        resp = messagebox.askyesno("!!!", "This Will Delete every Accounts\nAre You Sure?!")
                        if resp == 1:
                            for rec in tree.get_children():
                                tree.delete(rec)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("DROP TABLE acc")
                            con.commit()
                            con.close()
                            remove_ent()
                            table_loop()
                    def remove_ent():
                        e_e.delete(0, END)
                        p_e.delete(0, END)
                        id_e.delete(0, END)
                    def sel_rec(e):
                        e_e.delete(0, END)
                        p_e.delete(0, END)
                        id_e.delete(0, END)
                        select = tree.focus()
                        assign = tree.item(select, 'values')
                        e_e.insert(0, assign[0])
                        p_e.insert(0, assign[1])
                        id_e.insert(0, assign[2])
                    def up_rec():
                        select = tree.focus()
                        tree.item(select, text="", values=(e_e.get(), p_e.get(), id_e.get()))
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""UPDATE acc SET
                    		email = :first,
                    		password = :last,
                    		id=:id
                    		WHERE oid = :oid""",
                                  {
                                      'first': e_e.get(),
                                      'last': p_e.get(),
                                      'id': id_e.get(),
                                      'oid': id_e.get()
                                  })
                        con.commit()
                        con.close()
                        e_e.delete(0, END)
                        p_e.delete(0, END)
                        id_e.delete(0, END)
                    def recadd():
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("INSERT INTO acc VALUES (:first, :last, :id)",
                                  {
                                      'first': e_e.get(),
                                      'last': p_e.get(),
                                      'id': id_e.get()
                                  })
                        con.commit()
                        con.close()
                        e_e.delete(0, END)
                        p_e.delete(0, END)
                        id_e.delete(0, END)
                        tree.delete(*tree.get_children())
                        q_data()
                    def table_loop():
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists acc (
                    		email text,
                    		password text,
                    		id integer)
                    		""")
                        con.commit()
                        con.close()
                    b_fr = LabelFrame(wam, text="Commands")
                    b_fr.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    up_b = Button(b_fr, text="Update an Account", command=up_rec)
                    up_b.grid(row=0, column=0, padx=10, pady=10)
                    add_b = Button(b_fr, text="Register an Account", command=recadd)
                    add_b.grid(row=0, column=1, padx=10, pady=10)
                    rm_all_b = Button(b_fr, text="Delete all Accounts ", command=r_all)
                    rm_all_b.grid(row=0, column=2, padx=10, pady=10)
                    rm_1_b = Button(b_fr, text="Delete only one Selected", command=r1)
                    rm_1_b.grid(row=0, column=3, padx=10, pady=10)
                    select_rec_b = Button(b_fr, text="Clear Entries", command=remove_ent)
                    select_rec_b.grid(row=0, column=7, padx=10, pady=10)
                    request_b = Button(b_fr, text="Requested Accounts", command=RQ)
                    request_b.grid(row=1, column=0, padx=10, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_rec)
                    q_data()
                    wam.mainloop()
                def R():
                    wim = Tk()
                    wim.title('Sold List')
                    wim.geometry("1200x333")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM sold")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                            rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                            rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def findr():
                        look_data = find_e.get()
                        look_data_name = find_e.get()
                        find.destroy()
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM sold WHERE t like ? or t like ?  ", (look_data, look_data_name))
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def find_rcs():
                        global find_e, find
                        find = Toplevel(wim)
                        find.title("Find Items")
                        find.geometry("400x200")
                        find_fr = LabelFrame(find, text="Search by Recepit No.")
                        find_fr.pack(padx=10, pady=10)
                        find_e = Entry(find_fr, font=("Helvetica", 18))
                        find_e.pack(pady=20, padx=20)
                        find_b = Button(find, text="Search List", command=findr)
                        find_b.pack(padx=20, pady=20)
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists sold (
                                                                    item_name text,
                                                                    item_code text,
                                                                    quantity text,
                                                                    price text,
                                                                    email text,
                                                                    date text,
                                                                    t text,
                                                                    id integer)
                                                                    """)
                    con.commit()
                    con.close()
                    def rall():
                        resp = messagebox.askyesno("!!!!", "Every item from the DATA will be Erased\nAre You Sure?!")
                        if resp == 1:
                            for rec in tree.get_children():
                                tree.delete(rec)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("DROP TABLE sold")
                            con.commit()
                            con.close()
                            del_ent()
                            table_loop()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "email", "t", "date", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=160)
                    tree.column("Item Code", anchor=W, width=160)
                    tree.column("Quantity", anchor=CENTER, width=160)
                    tree.column("Price", anchor=CENTER, width=80)
                    tree.column("email", anchor=CENTER, width=160)
                    tree.column("ID", anchor=CENTER, width=80)
                    tree.column("date", anchor=CENTER, width=80)
                    tree.column("t", anchor=CENTER, width=160)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Sold Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("email", text="Email", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    tree.heading("date", text="Date", anchor=CENTER)
                    tree.heading("t", text="Recepit", anchor=CENTER)
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    search_b = Button(b_f, text="Reset", command=q_data)
                    search_b.grid(row=0, column=1, padx=20, pady=10)
                    search_b = Button(b_f, text="Search Old Transactions", command=find_rcs)
                    search_b.grid(row=0, column=2, padx=20, pady=10)
                    search_b = Button(b_f, text="Remove All", command=rall)
                    search_b.grid(row=0, column=3, padx=20, pady=10)
                    q_data()
                    wim.mainloop()
                def G():
                    con = sqlite3.connect("DATA.db")
                    c = con.cursor()
                    c.execute("SELECT  * FROM acc")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Registred Accounts.csv', index=False, header=True)
                    c.execute("SELECT  * FROM item")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Items.csv', index=False, header=True)
                    c.execute("SELECT  * FROM requestacc")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Requested Accounts.csv', index=False, header=True)
                    c.execute("SELECT  * FROM return")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Rturn Items.csv', index=False, header=True)
                    c.execute("SELECT  * FROM sold")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Purchased Items.csv', index=False, header=True)
                    c.execute("SELECT  * FROM shopping")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('In Purchasing.csv', index=False, header=True)
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Stock Trackings.csv', index=False, header=True)
                    c.execute("SELECT  * FROM tcheck")
                    recs = c.fetchall()
                    raw_datas = pd.DataFrame(recs)
                    raw_datas.to_csv('Transactions Check.csv', index=False, header=True)
                    messagebox.showinfo("!", "Report Generated")
                def T():
                    wim = Tk()
                    wim.title('In Purchasing List')
                    wim.geometry("1111x333")
                    def im():
                        wim = Tk()
                        wim.title('Inventory Management')
                        wim.geometry("1200x444")
                        def q_data():
                            for rec in tree.get_children():
                                tree.delete(rec)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("SELECT rowid, * FROM item")
                            recs = c.fetchall()
                            global count
                            cnt = 0
                            for rec in recs:
                                if cnt % 2 == 0:
                                    tree.insert(parent='', index='end', iid=cnt, text='',
                                                values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]),
                                                tags=('evenrow',))
                                else:
                                    tree.insert(parent='', index='end', iid=cnt, text='',
                                                values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]),
                                                tags=('oddrow',))
                                cnt += 1
                            con.commit()
                            con.close()
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists item (
                           	item_name text,
                           	item_code text,
                           	quantity text,
                           	price text,
                           	discount text,
                           	id integer)
                           	""")
                        con.commit()
                        con.close()
                        tree_f = Frame(wim)
                        tree_f.pack(pady=10)
                        tree_scr = Scrollbar(tree_f)
                        tree_scr.pack(side=RIGHT, fill=Y)
                        tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                        tree.pack()
                        tree_scr.config(command=tree.yview)
                        tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "Discount", "ID")
                        tree.column("#0", width=0, stretch=NO)
                        tree.column("Item Name", anchor=W, width=250)
                        tree.column("Item Code", anchor=W, width=250)
                        tree.column("Quantity", anchor=CENTER, width=250)
                        tree.column("Price", anchor=CENTER, width=110)
                        tree.column("Discount", anchor=CENTER, width=110)
                        tree.column("ID", anchor=CENTER, width=110)
                        tree.heading("#0", text="", anchor=W)
                        tree.heading("Item Name", text="Item Name", anchor=W)
                        tree.heading("Item Code", text="Item Code", anchor=W)
                        tree.heading("Quantity", text="Quantity", anchor=CENTER)
                        tree.heading("Price", text="Price", anchor=CENTER)
                        tree.heading("Discount", text="Discount", anchor=CENTER)
                        tree.heading("ID", text="ID", anchor=CENTER)
                        rec_fr = LabelFrame(wim, text="Entries")
                        rec_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                        in_l = Label(rec_fr, text="Item Name")
                        in_l.grid(row=2, column=0, padx=1, pady=10)
                        in_e = Entry(rec_fr)
                        in_e.grid(row=2, column=1, padx=1, pady=10)
                        ic_l = Label(rec_fr, text="Item Code")
                        ic_l.grid(row=2, column=2, padx=1, pady=10)
                        ic_e = Entry(rec_fr)
                        ic_e.grid(row=2, column=3, padx=1, pady=10)
                        qty_l = Label(rec_fr, text="Quantity")
                        qty_l.grid(row=2, column=4, padx=1, pady=10)
                        qty_e = Entry(rec_fr)
                        qty_e.grid(row=2, column=5, padx=1, pady=10)
                        p_l = Label(rec_fr, text="Price")
                        p_l.grid(row=3, column=0, padx=1, pady=10)
                        p_e = Entry(rec_fr)
                        p_e.grid(row=3, column=1, padx=1, pady=10)
                        d_l = Label(rec_fr, text="Discount")
                        d_l.grid(row=3, column=2, padx=1, pady=10)
                        di_e = Entry(rec_fr)
                        di_e.grid(row=3, column=3, padx=1, pady=10)
                        id_l = Label(rec_fr, text="ID")
                        id_l.grid(row=3, column=4, padx=1, pady=10)
                        id_e = Entry(rec_fr)
                        id_e.grid(row=3, column=5, padx=1, pady=10)
                        def r1():
                            z = tree.selection()[0]
                            tree.delete(z)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("DELETE from item WHERE oid=" + id_e.get())
                            con.commit()
                            con.close()
                            del_ent()
                            messagebox.showinfo("!", "An Item has Been Removed!")
                        def rall():
                            resp = messagebox.askyesno("!!!!", "Every item from the DATA will be Erased\nAre You Sure?!")
                            if resp == 1:
                                for rec in tree.get_children():
                                    tree.delete(rec)
                                con = sqlite3.connect('DATA.db')
                                c = con.cursor()
                                c.execute("DROP TABLE item")
                                con.commit()
                                con.close()
                                del_ent()
                                table_loop()
                        def del_ent():
                            in_e.delete(0, END)
                            ic_e.delete(0, END)
                            qty_e.delete(0, END)
                            p_e.delete(0, END)
                            di_e.delete(0, END)
                            id_e.delete(0, END)
                        def sel_data(e):
                            in_e.delete(0, END)
                            ic_e.delete(0, END)
                            qty_e.delete(0, END)
                            p_e.delete(0, END)
                            di_e.delete(0, END)
                            id_e.delete(0, END)
                            sel = tree.focus()
                            val = tree.item(sel, 'val')
                            in_e.insert(0, val[0])
                            ic_e.insert(0, val[1])
                            qty_e.insert(0, val[2])
                            p_e.insert(0, val[3])
                            di_e.insert(0, val[4])
                            id_e.insert(0, val[5])
                        def up_rec():
                            sel = tree.focus()
                            tree.item(sel, text="",
                                      values=(in_e.get(), ic_e.get(), qty_e.get(), p_e.get(), di_e.get(), id_e.get()))
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("""UPDATE item SET
                        		item_name = :1,
                        		item_code = :2,
                        		quantity = :3,
                        		price = :4,
                        		discount = :5
                        		WHERE oid = :oid""",
                                      {
                                          '1': in_e.get(),
                                          '2': ic_e.get(),
                                          '3': qty_e.get(),
                                          '4': p_e.get(),
                                          '5': di_e.get(),
                                          'oid': id_e.get()
                                      })
                            con.commit()
                            con.close()
                            in_e.delete(0, END)
                            ic_e.delete(0, END)
                            qty_e.delete(0, END)
                            p_e.delete(0, END)
                            di_e.delete(0, END)
                            id_e.delete(0, END)
                        def add_data():
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("INSERT INTO item VALUES (:first, :last, :quantity,:price,:discount, :id)",
                                      {
                                          'first': in_e.get(),
                                          'last': ic_e.get(),
                                          'quantity': qty_e.get(),
                                          'price': p_e.get(),
                                          'discount': di_e.get(),
                                          'id': id_e.get(),
                                      })
                            con.commit()
                            con.close()
                            in_e.delete(0, END)
                            ic_e.delete(0, END)
                            qty_e.delete(0, END)
                            p_e.delete(0, END)
                            di_e.delete(0, END)
                            id_e.delete(0, END)
                            tree.delete(*tree.get_children())
                            q_data()

                        def table_loop():
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("""CREATE TABLE if not exists item (
                        		item_name text,
                        		item_code text,
                        		quantity text,
                        		price text,
                        		discount text,
                        		id integer
                        		)""")
                            con.commit()
                            con.close()
                        b_f = LabelFrame(wim, text="Commands")
                        b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                        up_b = Button(b_f, text="Update an Item", command=up_rec)
                        up_b.grid(row=0, column=0, padx=20, pady=10)
                        add_b = Button(b_f, text="Add an item to database", command=add_data)
                        add_b.grid(row=0, column=1, padx=20, pady=10)
                        r_all_b = Button(b_f, text="Remove All Items ", command=rall)
                        r_all_b.grid(row=0, column=2, padx=20, pady=10)
                        r_1_b = Button(b_f, text="Remove only one Item", command=r1)
                        r_1_b.grid(row=0, column=3, padx=20, pady=10)
                        sel_rec_b = Button(b_f, text="Clear Entries", command=del_ent)
                        sel_rec_b.grid(row=0, column=7, padx=20, pady=10)
                        tree.bind("<ButtonRelease-1>", sel_data)
                        q_data()
                        wim.mainloop()
                    def wimsold():
                        wim = Tk()
                        wim.title('Return Inventory List')
                        wim.geometry("1111x232")

                        def q_data():
                            for rec in tree.get_children():
                                tree.delete(rec)
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("SELECT rowid, * FROM return")
                            recs = c.fetchall()
                            global count
                            cnt = 0
                            for rec in recs:
                                if cnt % 2 == 0:
                                    tree.insert(parent='', index='end', iid=cnt, text='',
                                                values=(
                                                    rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8],
                                                    rec[0]),
                                                tags=('evenrow',))
                                else:
                                    tree.insert(parent='', index='end', iid=cnt, text='',
                                                values=(
                                                    rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8],
                                                    rec[0]),
                                                tags=('oddrow',))
                                cnt += 1
                            con.commit()
                            con.close()

                        tree_f = Frame(wim)
                        tree_f.pack(pady=10)
                        tree_scr = Scrollbar(tree_f)
                        tree_scr.pack(side=RIGHT, fill=Y)
                        tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                        tree.pack()
                        tree_scr.config(command=tree.yview)
                        tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "email", "t", "date", "ID")
                        tree.column("#0", width=0, stretch=NO)
                        tree.column("Item Name", anchor=W, width=140)
                        tree.column("Item Code", anchor=W, width=140)
                        tree.column("Quantity", anchor=CENTER, width=140)
                        tree.column("Price", anchor=CENTER, width=100)
                        tree.column("email", anchor=CENTER, width=140)
                        tree.column("ID", anchor=CENTER, width=100)
                        tree.column("date", anchor=CENTER, width=100)
                        tree.column("t", anchor=CENTER, width=140)
                        tree.heading("#0", text="", anchor=W)
                        tree.heading("Item Name", text="Item Name", anchor=W)
                        tree.heading("Item Code", text="Item Code", anchor=W)
                        tree.heading("Quantity", text="Quantity", anchor=CENTER)
                        tree.heading("Price", text="Price", anchor=CENTER)
                        tree.heading("email", text="Email", anchor=CENTER)
                        tree.heading("ID", text="ID", anchor=CENTER)
                        tree.heading("date", text="Date", anchor=CENTER)
                        tree.heading("t", text="Recepit", anchor=CENTER)
                        q_data()
                        wim.mainloop()
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM shopping")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                                rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                                rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "email", "t", "date", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=140)
                    tree.column("Item Code", anchor=W, width=140)
                    tree.column("Quantity", anchor=CENTER, width=140)
                    tree.column("Price", anchor=CENTER, width=100)
                    tree.column("email", anchor=CENTER, width=140)
                    tree.column("ID", anchor=CENTER, width=100)
                    tree.column("date", anchor=CENTER, width=100)
                    tree.column("t", anchor=CENTER, width=140)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("email", text="Email", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    tree.heading("date", text="Date", anchor=CENTER)
                    tree.heading("t", text="Recepit", anchor=CENTER)
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    sold_b = Button(b_f, text="Check Return list", command=wimsold)
                    sold_b.grid(row=0, column=3, padx=20, pady=10)
                    sold_b = Button(b_f, text="Inventory Management", command=im)
                    sold_b.grid(row=0, column=4, padx=20, pady=10)
                    q_data()
                    wim.mainloop()
                activation = Button(wadmin, text="Account Management  ", command=am)
                activation.grid(row=1, column=0, columnspan=1, pady=5, padx=0, ipadx=60)
                activation = Button(wadmin, text="Review Sales Data   ", command=R)
                activation.grid(row=2, column=0, columnspan=1, pady=5, padx=0, ipadx=70)
                activation = Button(wadmin, text="Inventory Tracking   ", command=T)
                activation.grid(row=3, column=0, columnspan=1, pady=5, padx=0, ipadx=70)
                activation = Button(wadmin, text="Generate Reports    ", command=G)
                activation.grid(row=4, column=0, columnspan=1, pady=5, padx=0, ipadx=70)
                con.commit()
                con.close()
                wadmin.mainloop()
            else:
                tkinter.messagebox.showinfo("blah", "Email or Password is incorrect")
            email.delete(0, END)
            password.delete(0, END)
        email = Entry(wad, width=30)
        email.grid(row=0, column=1, padx=1, pady=(10, 0))
        password = Entry(wad, width=30, show="*")
        password.grid(row=1, column=1)
        email_label = Label(wad, text="Email")
        email_label.grid(row=0, column=0, pady=(10, 0))
        passport_label = Label(wad, text="Password")
        passport_label.grid(row=1, column=0)
        submit_btn = Button(wad, text='Login', command=adminsubmit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=10, ipadx=10)
        wad.mainloop()
    def staff():
        ws = Tk()
        ws.title('Staff login')
        ws.geometry('390x111')
        wa.destroy()
        def staffsubmit():
            con = sqlite3.connect("DATA.db")
            c = con.cursor()
            c.execute("SELECT * FROM acc where email=? AND password=?", (email.get(), password.get()))
            row = c.fetchone()
            if row:
                tkinter.messagebox.showinfo("blah", "Hello")
                ws1 = Tk()
                ws1.title('Welcome')
                ws1.geometry('300x90')
                w.destroy()
                ws.destroy()
                def wim():
                    wim = Tk()
                    wim.title('Item Avability')
                    wim.geometry("1200x333")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM item")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def findr():
                        look_data = find_e.get()
                        look_data_name = find_e.get()
                        find.destroy()
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM item WHERE item_name like ? or item_code like ?  ",(look_data, look_data_name))
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def find_rcs():
                        global find_e, find
                        find = Toplevel(wim)
                        find.title("Find Items")
                        find.geometry("400x200")
                        find_fr = LabelFrame(find, text="Search by Name or Code")
                        find_fr.pack(padx=10, pady=10)
                        find_e = Entry(find_fr, font=("Helvetica", 18))
                        find_e.pack(pady=20, padx=20)
                        find_b = Button(find, text="Search an Item", command=findr)
                        find_b.pack(padx=20, pady=20)
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists item (
                              	item_name text,
                              	item_code text,
                              	quantity text,
                              	price text,
                              	discount text,
                              	id integer)
                              	""")
                    con.commit()
                    con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "Discount", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=250)
                    tree.column("Item Code", anchor=W, width=250)
                    tree.column("Quantity", anchor=CENTER, width=250)
                    tree.column("Price", anchor=CENTER, width=110)
                    tree.column("Discount", anchor=CENTER, width=110)
                    tree.column("ID", anchor=CENTER, width=110)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("Discount", text="Discount", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    def sel_data(e):
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        id_e.delete(0, END)
                        da_e.delete(0, END)
                        sel = tree.focus()
                        val = tree.item(sel, 'val')
                        in_e.insert(0, val[0])
                        ic_e.insert(0, val[1])
                        p_e.insert(0, val[3])
                        d._einsert(0, val[4])
                        id_e.insert(0, val[5])
                        qty_e.insert(0, val[6])
                        tree.delete(*tree.get_children())
                        q_data()
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    search_b= Button(b_f, text="Search", command=find_rcs)
                    search_b.grid(row=0, column=3, padx=20, pady=10)
                    search_b = Button(b_f, text="Reset", command=q_data)
                    search_b.grid(row=0, column=4, padx=20, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_data)
                    q_data()
                    wim.mainloop()
                def purchase():
                    wim = Tk()
                    wim.title('Purchase list')
                    wim.geometry("1200x444")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM shopping")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[0]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7],rec[0]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists shopping (
                                 	item_name text,
                                 	item_code text,
                                 	quantity text,
                                 	price text,
                                 	discount text,
                                 	email text,
                                 	date text,
                                 	id integer)
                                 	""")
                    con.commit()
                    con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "Discount","Email", "date","ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=220)
                    tree.column("Item Code", anchor=W, width=220)
                    tree.column("Quantity", anchor=CENTER, width=120)
                    tree.column("Price", anchor=CENTER, width=80)
                    tree.column("Discount", anchor=CENTER, width=150)
                    tree.column("Email", anchor=CENTER, width=180)
                    tree.column("date", anchor=CENTER, width=100)
                    tree.column("ID", anchor=CENTER, width=80)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("Discount", text="Discount", anchor=CENTER)
                    tree.heading("Email", text="Email", anchor=CENTER)
                    tree.heading("date", text="Date", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    rec_fr = LabelFrame(wim, text="Entries")
                    rec_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                    in_l = Label(rec_fr, text="Item Name")
                    in_l.grid(row=2, column=0, padx=1, pady=10)
                    in_e = Entry(rec_fr)
                    in_e.grid(row=2, column=1, padx=1, pady=10)
                    ic_l = Label(rec_fr, text="Item Code")
                    ic_l.grid(row=2, column=2, padx=1, pady=10)
                    ic_e = Entry(rec_fr)
                    ic_e.grid(row=2, column=3, padx=1, pady=10)
                    qty_l = Label(rec_fr, text="Quantity")
                    qty_l.grid(row=2, column=4, padx=1, pady=10)
                    qty_e = Entry(rec_fr)
                    qty_e.grid(row=2, column=5, padx=1, pady=10)
                    p_l = Label(rec_fr, text="Price")
                    p_l.grid(row=3, column=0, padx=1, pady=10)
                    p_e = Entry(rec_fr)
                    p_e.grid(row=3, column=1, padx=1, pady=10)
                    d_l = Label(rec_fr, text="Discount")
                    d_l.grid(row=3, column=2, padx=1, pady=10)
                    d_e = Entry(rec_fr)
                    d_e.grid(row=3, column=3, padx=1, pady=10)
                    id_l = Label(rec_fr, text="ID")
                    id_l.grid(row=3, column=4, padx=1, pady=10)
                    id_e = Entry(rec_fr)
                    id_e.grid(row=3, column=5, padx=1, pady=10)
                    e_l = Label(rec_fr, text="Email")
                    e_l.grid(row=3, column=6, padx=1, pady=10)
                    e_e = Entry(rec_fr)
                    e_e.grid(row=3, column=7, padx=1, pady=10)
                    da_l = Label(rec_fr, text="Date")
                    da_l.grid(row=2, column=6, padx=1, pady=10)
                    da_e = Entry(rec_fr)
                    da_e.grid(row=2, column=7, padx=1, pady=10)
                    def sel_data(e):
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        id_e.delete(0, END)
                        e_e.delete(0, END)
                        da_e.delete(0, END)
                        sel = tree.focus()
                        val = tree.item(sel, 'val')
                        in_e.insert(0, val[0])
                        ic_e.insert(0, val[1])
                        qty_e.insert(0, val[2])
                        p_e.insert(0, val[3])
                        d_e.insert(0, val[4])
                        e_e.insert(0, val[5])
                        id_e.insert(0, val[7])
                        da_e.insert(0,val[6])
                    tree.bind("<ButtonRelease-1>", sel_data)
                    def checkout():
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists sold (
                                                                        item_name text,
                                                                        item_code text,
                                                                        quantity text,
                                                                        price text,
                                                                        email text,
                                                                        date text,
                                                                        t text,
                                                                        id integer)
                                                                        """)
                        con.commit()
                        con.close()
                        def clear_entries():
                            q_spin.delete(0, tkinter.END)
                            q_spin.insert(0, "1")
                            d_en.delete(0, tkinter.END)
                            p_spin.delete(0, tkinter.END)
                            p_spin.insert(0, "0.0")
                            ic_entry.delete(0, tkinter.END)
                        i_list = []
                        def add_item():
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute("""CREATE TABLE if not exists tcheck (
                                                                	email text,
                                                                	t text,
                                                                	d text,
                                                                	id integer)
                                                                	""")
                            c.execute("INSERT INTO tcheck VALUES (:email,:t ,:id,:d)",
                                      {
                                          'email': e_e.get(),
                                          't': ph_e.get(),
                                          'id': id_e.get(),
                                          'd': da_e.get(),
                                      })
                            con.commit()
                            con.close()
                            q = int(q_spin.get())
                            d = d_en.get()
                            p = float(p_spin.get())
                            ic = ic_entry.get()
                            da=da_e.get()
                            total = q * p
                            invoice_item = [q, d, p, total, ic,da]
                            tree.insert('', 0, values=invoice_item)
                            clear_entries()
                            i_list.append(invoice_item)
                        def make_invoice():
                            d = DocxTemplate("invoice_t.docx")
                            email = e_e.get()
                            date=da_e.get()
                            tcode = ph_e.get()
                            subtot = sum(item[3] for item in i_list)
                            saletx = 0.1
                            tot = subtot * (1 - saletx)
                            d.render({"name": email,
                                      "tcode": tcode,
                                      "invoice_list": i_list,
                                      "subtotal": subtot,
                                      "salestax": str(saletx * 100) + "%",
                                      "total": tot,
                                      "date":date
                                      })
                            d_name = "new_invoice" + email + datetime.datetime.now().strftime(
                                "%Y-%m-%d-%H%M%S") + ".docx"
                            d.save(d_name)
                            messagebox.showinfo("Invoice Created", "Invoice Created")
                            w.destroy()
                            wim.destroy()
                        w = tkinter.Tk()
                        w.title("Invoice Generator Form")
                        fra = tkinter.Frame(w)
                        fra.pack(padx=1, pady=5)
                        e_label = tkinter.Label(fra, text="Email")
                        e_label.grid(row=1, column=0)
                        e_e = tkinter.Entry(fra)
                        e_e.grid(row=2, column=0)
                        ph_lab = tkinter.Label(fra, text="Recepit number")
                        ph_lab.grid(row=3, column=0)
                        ph_e = tkinter.Entry(fra)
                        ph_e.grid(row=4, column=0)
                        q_lab = tkinter.Label(fra, text="Qty")
                        q_lab.grid(row=1, column=1)
                        q_spin = tkinter.Spinbox(fra, from_=1, to=100)
                        q_spin.grid(row=2, column=1)
                        ic_lab = tkinter.Label(fra, text="Item Code")
                        ic_lab.grid(row=3, column=1)
                        ic_entry = tkinter.Entry(fra)
                        ic_entry.grid(row=4, column=1)
                        da_lab = tkinter.Label(fra, text="Date")
                        da_lab.grid(row=5, column=0)
                        da_e = tkinter.Entry(fra)
                        da_e.grid(row=6, column=0)
                        d_lab = tkinter.Label(fra, text="Item Name")
                        d_lab.grid(row=1, column=2)
                        d_en = tkinter.Entry(fra)
                        d_en.grid(row=2, column=2)
                        p_lab = tkinter.Label(fra, text="Unit Price")
                        p_lab.grid(row=3, column=2)
                        p_spin = tkinter.Entry(fra)
                        p_spin.grid(row=4, column=2)
                        add_it_b = tkinter.Button(fra, text="Add an Item", command=add_item)
                        add_it_b.grid(row=8, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                        columns = ('qty', 'name', 'code', 'total', 'icode','d')
                        tree = ttk.Treeview(fra, columns=columns, show="headings")
                        tree.heading('qty', text='Quantity')
                        tree.heading('name', text='Item Name')
                        tree.heading('code', text='Unit Price')
                        tree.heading('total', text="Total")
                        tree.heading('icode', text="Item Code")
                        tree.heading('d', text="Date")
                        tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
                        save_inv_b = tkinter.Button(fra, text="Create an Invoice", command=make_invoice)
                        save_inv_b.grid(row=9, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                        con.commit()
                        con.close()
                        tree.delete(*tree.get_children())
                        q_data()
                        w.mainloop()
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    add_b = Button(b_f, text="Go To Invoice", command=checkout)
                    add_b.grid(row=0, column=1, padx=20, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_data)
                    q_data()
                    wim.mainloop()
                def R():
                    wim = Tk()
                    wim.title('Purchase History')
                    wim.geometry("1200x444")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM sold")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                            rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                            rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def findr():
                        look_data = find_e.get()
                        look_data_name = find_e.get()
                        find.destroy()
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM sold WHERE t like ? or t like ?  ", (look_data, look_data_name))
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                                rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                                rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def find_rcs():
                        global find_e, find
                        find = Toplevel(wim)
                        find.title("Find Items")
                        find.geometry("400x200")
                        find_fr = LabelFrame(find, text="Search by Recepit No.")
                        find_fr.pack(padx=10, pady=10)
                        find_e = Entry(find_fr, font=("Helvetica", 18))
                        find_e.pack(pady=20, padx=20)
                        find_b = Button(find, text="Search List", command=findr)
                        find_b.pack(padx=20, pady=20)
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists sold (
                                                                                   item_name text,
                                                                                   item_code text,
                                                                                   quantity text,
                                                                                   price text,
                                                                                   email text,
                                                                                   date text,
                                                                                   t text,
                                                                                   id integer)
                                                                                   """)
                    con.commit()
                    con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "email", "t", "date", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=160)
                    tree.column("Item Code", anchor=W, width=160)
                    tree.column("Quantity", anchor=CENTER, width=160)
                    tree.column("Price", anchor=CENTER, width=120)
                    tree.column("email", anchor=CENTER, width=160)
                    tree.column("ID", anchor=CENTER, width=120)
                    tree.column("date", anchor=CENTER, width=120)
                    tree.column("t", anchor=CENTER, width=160)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("email", text="Email", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    tree.heading("date", text="Date", anchor=CENTER)
                    tree.heading("t", text="Recepit", anchor=CENTER)
                    rec_fr = LabelFrame(wim, text="Entries")
                    rec_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                    in_l = Label(rec_fr, text="Item Name")
                    in_l.grid(row=2, column=0, padx=1, pady=10)
                    in_e = Entry(rec_fr)
                    in_e.grid(row=2, column=1, padx=1, pady=10)
                    ic_l = Label(rec_fr, text="Item Code")
                    ic_l.grid(row=2, column=2, padx=1, pady=10)
                    ic_e = Entry(rec_fr)
                    ic_e.grid(row=2, column=3, padx=1, pady=10)
                    qty_l = Label(rec_fr, text="Quantity")
                    qty_l.grid(row=2, column=4, padx=1, pady=10)
                    qty_e = Entry(rec_fr)
                    qty_e.grid(row=2, column=5, padx=1, pady=10)
                    p_l = Label(rec_fr, text="Price")
                    p_l.grid(row=3, column=0, padx=1, pady=10)
                    p_e = Entry(rec_fr)
                    p_e.grid(row=3, column=1, padx=1, pady=10)
                    d_l = Label(rec_fr, text="Email")
                    d_l.grid(row=3, column=2, padx=1, pady=10)
                    d_e = Entry(rec_fr)
                    d_e.grid(row=3, column=3, padx=1, pady=10)
                    id_l = Label(rec_fr, text="ID")
                    id_l.grid(row=3, column=4, padx=1, pady=10)
                    id_e = Entry(rec_fr)
                    id_e.grid(row=3, column=5, padx=1, pady=10)
                    e_l = Label(rec_fr, text="Recepit")
                    e_l.grid(row=3, column=6, padx=1, pady=10)
                    e_e = Entry(rec_fr)
                    e_e.grid(row=3, column=7, padx=1, pady=10)
                    da_l = Label(rec_fr, text="Date")
                    da_l.grid(row=2, column=6, padx=1, pady=10)
                    da_e = Entry(rec_fr)
                    da_e.grid(row=2, column=7, padx=1, pady=10)
                    def sel_data(e):
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        e_e.delete(0, END)
                        da_e.delete(0, END)
                        id_e.delete(0, END)
                        sel = tree.focus()
                        val = tree.item(sel, 'val')
                        in_e.insert(0, val[0])
                        ic_e.insert(0, val[1])
                        qty_e.insert(0, val[2])
                        p_e.insert(0, val[3])
                        d_e.insert(0, val[4])
                        e_e.insert(0, val[5])
                        da_e.insert(0, val[6])
                        id_e.insert(0, val[7])
                    def retu():
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists return (
                                                                                  	item_name text,
                                                                                  	item_code text,
                                                                                  	quantity text,
                                                                                  	price text,
                                                                                  	email text,
                                                                                  	t text,
                                                                                  	date text,
                                                                                  	id integer)
                                                                                  	""")

                        def clear_entries():
                            q_spin.delete(0, tkinter.END)
                            q_spin.insert(0, "1")
                            d_en.delete(0, tkinter.END)
                            p_spin.delete(0, tkinter.END)
                            p_spin.insert(0, "0.0")
                            ic_entry.delete(0, tkinter.END)
                        i_list = []
                        def add_item():
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute(
                                "INSERT INTO return VALUES (:first, :last, :quantity,:price,:email,:t ,:date,:id)",
                                {
                                    'first': d_en.get(),
                                    'last': ic_entry.get(),
                                    'quantity': q_spin.get(),
                                    'price': p_spin.get(),
                                    'email': e_e.get(),
                                    't': da_e.get(),
                                    'date': ph_e.get(),
                                    'id': id_e.get(),
                                })
                            c.execute("DELETE from sold WHERE oid=" + id_e.get())
                            con.commit()
                            con.close()
                            q = int(q_spin.get())
                            d = d_en.get()
                            p = float(p_spin.get())
                            ic = ic_entry.get()
                            da = da_e.get()
                            total = q * p
                            invoice_item = [q, d, p, total, ic, da]
                            tree.insert('', 0, values=invoice_item)
                            clear_entries()
                            i_list.append(invoice_item)
                        def make_invoice():
                            d = DocxTemplate("return_t.docx")
                            email = e_e.get()
                            date = da_e.get()
                            tcode = ph_e.get()
                            subtot = sum(item[3] for item in i_list)
                            saletx = 0.1
                            tot = subtot * (1 - saletx)
                            d.render({"name": email,
                                      "tcode": tcode,
                                      "invoice_list": i_list,
                                      "subtotal": subtot,
                                      "salestax": str(saletx * 100) + "%",
                                      "total": tot,
                                      "date": date
                                      })
                            d_name = "new_return" + email + datetime.datetime.now().strftime(
                                "%Y-%m-%d-%H%M%S") + ".docx"
                            d.save(d_name)
                            messagebox.showinfo("Return Created", "Return Created")
                            w.destroy()
                            wim.destroy()
                        w = tkinter.Tk()
                        w.title("Return Generator Form")
                        fra = tkinter.Frame(w)
                        fra.pack(padx=1, pady=5)
                        e_label = tkinter.Label(fra, text="Email")
                        e_label.grid(row=1, column=0)
                        e_e = tkinter.Entry(fra)
                        e_e.grid(row=2, column=0)
                        ph_lab = tkinter.Label(fra, text="Recepit number")
                        ph_lab.grid(row=3, column=0)
                        ph_e = tkinter.Entry(fra)
                        ph_e.grid(row=4, column=0)
                        q_lab = tkinter.Label(fra, text="Qty")
                        q_lab.grid(row=1, column=1)
                        q_spin = tkinter.Spinbox(fra, from_=1, to=100)
                        q_spin.grid(row=2, column=1)
                        ic_lab = tkinter.Label(fra, text="Item Code")
                        ic_lab.grid(row=3, column=1)
                        ic_entry = tkinter.Entry(fra)
                        ic_entry.grid(row=4, column=1)
                        da_lab = tkinter.Label(fra, text="Date")
                        da_lab.grid(row=5, column=0)
                        da_e = tkinter.Entry(fra)
                        da_e.grid(row=6, column=0)
                        d_lab = tkinter.Label(fra, text="Item Name")
                        d_lab.grid(row=1, column=2)
                        d_en = tkinter.Entry(fra)
                        d_en.grid(row=2, column=2)
                        p_lab = tkinter.Label(fra, text="Unit Price")
                        p_lab.grid(row=3, column=2)
                        p_spin = tkinter.Entry(fra)
                        p_spin.grid(row=4, column=2)
                        add_it_b = tkinter.Button(fra, text="Add an Item", command=add_item)
                        add_it_b.grid(row=8, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                        columns = ('qty', 'name', 'code', 'total', 'icode', 'd')
                        tree = ttk.Treeview(fra, columns=columns, show="headings")
                        tree.heading('qty', text='Quantity')
                        tree.heading('name', text='Item Name')
                        tree.heading('code', text='Unit Price')
                        tree.heading('total', text="Total")
                        tree.heading('icode', text="Item Code")
                        tree.heading('d', text="Date")
                        tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
                        save_inv_b = tkinter.Button(fra, text="Create a Return", command=make_invoice)
                        save_inv_b.grid(row=9, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                        con.commit()
                        con.close()
                        tree.delete(*tree.get_children())
                        q_data()
                        w.mainloop()
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    add_b = Button(b_f, text="Make Returns", command=retu)
                    add_b.grid(row=0, column=0, padx=20, pady=10)
                    search_b = Button(b_f, text="Reset", command=q_data)
                    search_b.grid(row=0, column=1, padx=20, pady=10)
                    search_b = Button(b_f, text="Search Old Transactions", command=find_rcs)
                    search_b.grid(row=0, column=2, padx=20, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_data)
                    q_data()
                    wim.mainloop()
                activation = Button(ws1, text="Check Item Avability", command=wim)
                activation.grid(row=1, column=0, columnspan=1, pady=0, padx=0, ipadx=70)
                activation = Button(ws1, text="Create an Invoice    ", command=purchase)
                activation.grid(row=2, column=0, columnspan=1, pady=0, padx=0, ipadx=70)
                activation = Button(ws1, text="Manage Returns      ", command=R)
                activation.grid(row=3, column=0, columnspan=1, pady=0, padx=0, ipadx=70)
                ws1.mainloop()
            else:
                tkinter.messagebox.showinfo("blah", "Email or Password is incorrect")
            con.commit()
            con.close()
            email.delete(0, END)
            password.delete(0, END)
        email = Entry(ws, width=30)
        email.grid(row=0, column=1, padx=20, pady=(10, 0))
        password = Entry(ws, width=30, show="*")
        password.grid(row=1, column=1)
        email_label = Label(ws, text="Email")
        email_label.grid(row=0, column=0, pady=(10, 0))
        passport_label = Label(ws, text="Password")
        passport_label.grid(row=1, column=0)
        submit_btn = Button(ws, text='Login', command=staffsubmit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=10, ipadx=10)
        ws.mainloop()
    def user():
        wu = Tk()
        wu.title('User login')
        wu.geometry('390x111')
        wa.destroy()
        def usersubmit():
            con = sqlite3.connect("DATA.db")
            c = con.cursor()
            c.execute("SELECT * FROM acc where email=? AND password=?", (email.get(), password.get()))
            row = c.fetchone()
            if row:
                tkinter.messagebox.showinfo("blah", "Welcome from SIERRA")
                wu1 = Tk()
                wu1.title('Plese Choose to Proceed')
                wu1.geometry('300x90')
                w.destroy()
                wu.destroy()
                def wim():
                    wim = Tk()
                    wim.title('Search and Purchase')
                    wim.geometry("1200x444")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM item")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5],rec[6],rec[0]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5],rec[6],rec[0]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def findr():
                        look_data = find_e.get()
                        look_data_name = find_e.get()
                        find.destroy()
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM item WHERE item_name like ? or item_code like ?  ",(look_data, look_data_name))
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[0]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def find_rcs():
                        global find_e, find
                        find = Toplevel(wim)
                        find.title("Find Items")
                        find.geometry("400x200")
                        find_fr = LabelFrame(find, text="Search by Name or Code")
                        find_fr.pack(padx=10, pady=10)
                        find_e = Entry(find_fr, font=("Helvetica", 18))
                        find_e.pack(pady=20, padx=20)
                        find_b = Button(find, text="Search an Item", command=findr)
                        find_b.pack(padx=20, pady=20)
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists item (
                              	item_name text,
                              	item_code text,
                              	quantity text,
                              	price text,
                              	discount text,
                              	id integer)
                              	""")
                    con.commit()
                    con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "Discount", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=250)
                    tree.column("Item Code", anchor=W, width=250)
                    tree.column("Quantity", anchor=CENTER, width=250)
                    tree.column("Price", anchor=CENTER, width=120)
                    tree.column("Discount", anchor=CENTER, width=120)
                    tree.column("ID", anchor=CENTER, width=120)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("Discount", text="Discount", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    rec_fr = LabelFrame(wim, text="Entries")
                    rec_fr.pack(anchor=S, fill="x", expand="yes", padx=10)
                    in_l = Label(rec_fr, text="Item Name")
                    in_l.grid(row=2, column=0, padx=1, pady=10)
                    in_e = Entry(rec_fr)
                    in_e.grid(row=2, column=1, padx=1, pady=10)
                    ic_l = Label(rec_fr, text="Item Code")
                    ic_l.grid(row=2, column=2, padx=1, pady=10)
                    ic_e = Entry(rec_fr)
                    ic_e.grid(row=2, column=3, padx=1, pady=10)
                    qty_l = Label(rec_fr, text="Quantity")
                    qty_l.grid(row=2, column=4, padx=1, pady=10)
                    qty_e = Entry(rec_fr)
                    qty_e.grid(row=2, column=5, padx=1, pady=10)
                    p_l = Label(rec_fr, text="Price")
                    p_l.grid(row=3, column=0, padx=1, pady=10)
                    p_e = Entry(rec_fr)
                    p_e.grid(row=3, column=1, padx=1, pady=10)
                    d_l = Label(rec_fr, text="Discount")
                    d_l.grid(row=3, column=2, padx=1, pady=10)
                    d_e = Entry(rec_fr)
                    d_e.grid(row=3, column=3, padx=1, pady=10)
                    id_l = Label(rec_fr, text="ID")
                    id_l.grid(row=3, column=4, padx=1, pady=10)
                    id_e = Entry(rec_fr)
                    id_e.grid(row=3, column=5, padx=1, pady=10)
                    e_l = Label(rec_fr, text="Email")
                    e_l.grid(row=3, column=6, padx=1, pady=10)
                    e_e = Entry(rec_fr)
                    e_e.grid(row=3, column=7, padx=1, pady=10)
                    da_l = Label(rec_fr, text="Date")
                    da_l.grid(row=2, column=6, padx=1, pady=10)
                    da_e = Entry(rec_fr)
                    da_e.grid(row=2, column=7, padx=1, pady=10)
                    def sel_data(e):
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        id_e.delete(0, END)
                        sel = tree.focus()
                        val = tree.item(sel, 'val')
                        in_e.insert(0, val[0])
                        ic_e.insert(0, val[1])
                        p_e.insert(0, val[3])
                        d_e.insert(0, val[4])
                        e_e.insesrt(0,val[5])
                        da_e.insert(0, val[6])
                    def add_data():
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists shopping (
                                                     	item_name text,
                                                     	item_code text,
                                                     	quantity text,
                                                     	price text,
                                                     	discount text,
                                                     	email text,
                                                     	date text,
                                                     	id integer)
                                                     	""")

                        c.execute("INSERT INTO shopping VALUES (:first,:last,:quantity,:price,:discount,:email,:date,:id)",
                                  {
                                      'first': in_e.get(),
                                      'last': ic_e.get(),
                                      'quantity': qty_e.get(),
                                      'price': p_e.get(),
                                      'discount': d_e.get(),
                                      'email': e_e.get(),
                                      'date': da_e.get(),
                                      'id': id_e.get(),
                                  })
                        con.commit()
                        con.close()
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        id_e.delete(0, END)
                        tree.delete(*tree.get_children())
                        q_data()
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    add_b = Button(b_f, text="Purchase", command=add_data)
                    add_b.grid(row=0, column=1, padx=20, pady=10)
                    search_b= Button(b_f, text="Search", command=find_rcs)
                    search_b.grid(row=0, column=3, padx=20, pady=10)
                    search_b = Button(b_f, text="Reset", command=q_data)
                    search_b.grid(row=0, column=4, padx=20, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_data)
                    q_data()
                    wim.mainloop()
                def purchase():
                    wim = Tk()
                    wim.title('Self Purchase')
                    wim.geometry("1200x444")
                    messagebox.showinfo("!","Before Checkout\nPlease make a Payment\nfor a Recepit number")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM shopping")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[0],rec[7]), tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[0],rec[7]), tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists shopping (
                     	item_name text,
                     	item_code text,
                     	quantity text,
                     	price text,
                     	discount text,
                     	email text,
                     	date text,
                     	id integer)
                     	""")
                    con.commit()
                    con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "Discount","email","ID","date")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=200)
                    tree.column("Item Code", anchor=W, width=200)
                    tree.column("Quantity", anchor=CENTER, width=200)
                    tree.column("Price", anchor=CENTER, width=80)
                    tree.column("Discount", anchor=CENTER, width=80)
                    tree.column("date", anchor=CENTER, width=100)
                    tree.column("ID", anchor=CENTER, width=80)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("Discount", text="Discount", anchor=CENTER)
                    tree.heading("email", text="Email", anchor=CENTER)
                    tree.heading("date", text="Date", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    rec_fr = LabelFrame(wim, text="Entries")
                    rec_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                    in_l = Label(rec_fr, text="Item Name")
                    in_l.grid(row=2, column=0, padx=1, pady=10)
                    in_e = Entry(rec_fr)
                    in_e.grid(row=2, column=1, padx=1, pady=10)
                    ic_l = Label(rec_fr, text="Item Code")
                    ic_l.grid(row=2, column=2, padx=1, pady=10)
                    ic_e = Entry(rec_fr)
                    ic_e.grid(row=2, column=3, padx=1, pady=10)
                    qty_l = Label(rec_fr, text="Quantity")
                    qty_l.grid(row=2, column=4, padx=1, pady=10)
                    qty_e = Entry(rec_fr)
                    qty_e.grid(row=2, column=5, padx=1, pady=10)
                    p_l = Label(rec_fr, text="Price")
                    p_l.grid(row=3, column=0, padx=1, pady=10)
                    p_e = Entry(rec_fr)
                    p_e.grid(row=3, column=1, padx=1, pady=10)
                    d_l = Label(rec_fr, text="Discount")
                    d_l.grid(row=3, column=2, padx=1, pady=10)
                    d_e = Entry(rec_fr)
                    d_e.grid(row=3, column=3, padx=1, pady=10)
                    id_l = Label(rec_fr, text="ID")
                    id_l.grid(row=3, column=4, padx=1, pady=10)
                    id_e = Entry(rec_fr)
                    id_e.grid(row=3, column=5, padx=1, pady=10)
                    e_l = Label(rec_fr, text="Email")
                    e_l.grid(row=2, column=6, padx=1, pady=10)
                    e_e = Entry(rec_fr)
                    e_e.grid(row=2, column=7, padx=1, pady=10)
                    da_l = Label(rec_fr, text="Date")
                    da_l.grid(row=3, column=6, padx=1, pady=10)
                    da_e = Entry(rec_fr)
                    da_e.grid(row=3, column=7, padx=1, pady=10)
                    def sel_data(e):
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        e_e.delete(0,END)
                        id_e.delete(0, END)
                        da_e.delete(0, END)
                        sel = tree.focus()
                        val = tree.item(sel, 'val')
                        in_e.insert(0, val[0])
                        ic_e.insert(0, val[1])
                        qty_e.insert(0, val[2])
                        p_e.insert(0, val[3])
                        d_e.insert(0, val[4])
                        e_e.insert(0, val[5])
                        id_e.insert(0, val[6])
                        da_e.insert(0, val[7])
                    def checkout():
                        ws = Tk()
                        ws.title('Transaction Code check')
                        ws.geometry('390x100')
                        def staffsubmit():
                            con = sqlite3.connect("DATA.db")
                            c = con.cursor()
                            c.execute("SELECT * FROM tcheck where t=? and email=?", (tc.get(),e.get()))
                            row = c.fetchone()
                            if row:
                                tkinter.messagebox.showinfo("blah", "Thank you for shopping at Sierra\nPlease fill in to create Recepit")
                                ws.destroy()
                                con = sqlite3.connect('DATA.db')
                                c = con.cursor()
                                c.execute("""CREATE TABLE if not exists sold (
                                                                                item_name text,
                                                                                item_code text,
                                                                                quantity text,
                                                                                price text,
                                                                                email text,
                                                                                date text,
                                                                                t text,
                                                                                id integer)
                                                                                """)
                                con.commit()
                                con.close()
                                def clear_entries():
                                    q_spin.delete(0, tkinter.END)
                                    q_spin.insert(0, "1")
                                    d_en.delete(0, tkinter.END)
                                    p_spin.delete(0, tkinter.END)
                                    p_spin.insert(0, "0.0")
                                    ic_entry.delete(0, tkinter.END)
                                i_list = []
                                def add_item():
                                    con = sqlite3.connect('DATA.db')
                                    c = con.cursor()
                                    c.execute(
                                        "INSERT INTO sold VALUES (:first, :last, :quantity,:price,:email,:t ,:date,:id)",
                                        {
                                            'first': d_en.get(),
                                            'last': ic_entry.get(),
                                            'quantity': q_spin.get(),
                                            'price': p_spin.get(),
                                            'email': e_e.get(),
                                            't': da_e.get(),
                                            'date':ph_e.get() ,
                                            'id': id_e.get(),
                                        })
                                    c.execute("DELETE from shopping WHERE oid=" + id_e.get())
                                    con.commit()
                                    con.close()
                                    q = int(q_spin.get())
                                    d = d_en.get()
                                    p = float(p_spin.get())
                                    ic = ic_entry.get()
                                    da = da_e.get()
                                    total = q * p
                                    invoice_item = [q, d, p, total, ic, da]
                                    tree.insert('', 0, values=invoice_item)
                                    clear_entries()
                                    i_list.append(invoice_item)
                                def make_invoice():
                                    d = DocxTemplate("recepit_t.docx")
                                    email = e_e.get()
                                    date = da_e.get()
                                    tcode = ph_e.get()
                                    subtot = sum(item[3] for item in i_list)
                                    saletx = 0.1
                                    tot = subtot * (1 - saletx)
                                    d.render({"name": email,
                                              "tcode": tcode,
                                              "invoice_list": i_list,
                                              "subtotal": subtot,
                                              "salestax": str(saletx * 100) + "%",
                                              "total": tot,
                                              "date": date
                                              })
                                    d_name = "new_recepit" + email + datetime.datetime.now().strftime(
                                        "%Y-%m-%d-%H%M%S") + ".docx"
                                    d.save(d_name)
                                    d = "https://www.google.com"
                                    QRCfile = "qr.png"
                                    QRim = qrcode.QRCode(border=1, version=1, box_size=3)
                                    QRim.add_data(d)
                                    QRim.make(d)
                                    i = QRim.make_image(back_color="grey", fill_color='black')
                                    i.save(QRCfile)
                                    do = Document(d_name)
                                    qr_is = glob.glob("qr.png")
                                    for i in qr_is:
                                        image_n = os.path.basename(i)
                                        do.add_picture(i)
                                        do.save(f"{image_n}recepit_t.docx")
                                    messagebox.showinfo("Recepit Created", "Recepit Created")
                                    w.destroy()
                                    wim.destroy()
                                w = tkinter.Tk()
                                w.title("Recepit Generator Form")
                                fra = tkinter.Frame(w)
                                fra.pack(padx=1, pady=5)
                                e_label = tkinter.Label(fra, text="Email")
                                e_label.grid(row=1, column=0)
                                e_e = tkinter.Entry(fra)
                                e_e.grid(row=2, column=0)
                                ph_lab = tkinter.Label(fra, text="Recepit number")
                                ph_lab.grid(row=3, column=0)
                                ph_e = tkinter.Entry(fra)
                                ph_e.grid(row=4, column=0)
                                q_lab = tkinter.Label(fra, text="Qty")
                                q_lab.grid(row=1, column=1)
                                q_spin = tkinter.Spinbox(fra, from_=1, to=100)
                                q_spin.grid(row=2, column=1)
                                ic_lab = tkinter.Label(fra, text="Item Code")
                                ic_lab.grid(row=3, column=1)
                                ic_entry = tkinter.Entry(fra)
                                ic_entry.grid(row=4, column=1)
                                da_lab = tkinter.Label(fra, text="Date")
                                da_lab.grid(row=5, column=0)
                                da_e = tkinter.Entry(fra)
                                da_e.grid(row=6, column=0)
                                d_lab = tkinter.Label(fra, text="Item Name")
                                d_lab.grid(row=1, column=2)
                                d_en = tkinter.Entry(fra)
                                d_en.grid(row=2, column=2)
                                p_lab = tkinter.Label(fra, text="Unit Price")
                                p_lab.grid(row=3, column=2)
                                p_spin = tkinter.Entry(fra)
                                p_spin.grid(row=4, column=2)
                                add_it_b = tkinter.Button(fra, text="Add an Item", command=add_item)
                                add_it_b.grid(row=8, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                                columns = ('qty', 'name', 'code', 'total', 'icode', 'd')
                                tree = ttk.Treeview(fra, columns=columns, show="headings")
                                tree.heading('qty', text='Quantity')
                                tree.heading('name', text='Item Name')
                                tree.heading('code', text='Unit Price')
                                tree.heading('total', text="Total")
                                tree.heading('icode', text="Item Code")
                                tree.heading('d', text="Date")
                                tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
                                save_inv_b = tkinter.Button(fra, text="Create a Recepit", command=make_invoice)
                                save_inv_b.grid(row=9, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                                con.commit()
                                con.close()
                                tree.delete(*tree.get_children())
                                q_data()
                                w.mainloop()
                            else:
                                tkinter.messagebox.showinfo("blah", "Incorrect Transaction Code\nPlease proceed a payment and get Transaction Code")
                            con.commit()
                            con.close()
                            tc.delete(0, END)
                        tc = Entry(ws, width=30)
                        tc.grid(row=1, column=1, padx=20, pady=(5, 0))
                        e = Entry(ws, width=30)
                        e.grid(row=0, column=1)
                        tc_label = Label(ws, text="T\Code:")
                        tc_label.grid(row=1, column=0, pady=(5, 0))
                        email_label = Label(ws, text="Email")
                        email_label.grid(row=0, column=0)
                        tc_btn = Button(ws, text='Enter', command=staffsubmit)
                        tc_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=10, ipadx=10)
                        ws.mainloop()
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        id_e.delete(0, END)
                        tree.delete(*tree.get_children())
                        q_data()
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    add_b = Button(b_f, text="Checkout", command=checkout)
                    add_b.grid(row=0, column=1, padx=20, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_data)
                    q_data()
                    wim.mainloop()
                def R():
                    wim = Tk()
                    wim.title('Purchase History')
                    wim.geometry("1200x444")
                    def q_data():
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM sold")
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[7],rec[6], rec[8],rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(rec[1], rec[2], rec[3], rec[4], rec[5], rec[7],rec[6],rec[8], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def findr():
                        look_data = find_e.get()
                        look_data_name=find_e.get()
                        find.destroy()
                        for rec in tree.get_children():
                            tree.delete(rec)
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("SELECT rowid, * FROM sold WHERE t like ? or t like ?  ",(look_data, look_data_name))
                        recs = c.fetchall()
                        global count
                        cnt = 0
                        for rec in recs:
                            if cnt % 2 == 0:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                            rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('evenrow',))
                            else:
                                tree.insert(parent='', index='end', iid=cnt, text='',
                                            values=(
                                            rec[1], rec[2], rec[3], rec[4], rec[5], rec[7], rec[6], rec[8], rec[0]),
                                            tags=('oddrow',))
                            cnt += 1
                        con.commit()
                        con.close()
                    def find_rcs():
                        global find_e, find
                        find = Toplevel(wim)
                        find.title("Find Items")
                        find.geometry("400x200")
                        find_fr = LabelFrame(find, text="Search by Recepit No.")
                        find_fr.pack(padx=10, pady=10)
                        find_e = Entry(find_fr, font=("Helvetica", 18))
                        find_e.pack(pady=20, padx=20)
                        find_b = Button(find, text="Search List", command=findr)
                        find_b.pack(padx=20, pady=20)
                    con = sqlite3.connect('DATA.db')
                    c = con.cursor()
                    c.execute("""CREATE TABLE if not exists sold (
                                                                    item_name text,
                                                                    item_code text,
                                                                    quantity text,
                                                                    price text,
                                                                    email text,
                                                                    date text,
                                                                    t text,
                                                                    id integer)
                                                                    """)
                    con.commit()
                    con.close()
                    tree_f = Frame(wim)
                    tree_f.pack(pady=10)
                    tree_scr = Scrollbar(tree_f)
                    tree_scr.pack(side=RIGHT, fill=Y)
                    tree = ttk.Treeview(tree_f, yscrollcommand=tree_scr.set, selectmode="extended")
                    tree.pack()
                    tree_scr.config(command=tree.yview)
                    tree['columns'] = ("Item Name", "Item Code", "Quantity", "Price", "email","t","date", "ID")
                    tree.column("#0", width=0, stretch=NO)
                    tree.column("Item Name", anchor=W, width=160)
                    tree.column("Item Code", anchor=W, width=160)
                    tree.column("Quantity", anchor=CENTER, width=160)
                    tree.column("Price", anchor=CENTER, width=120)
                    tree.column("email", anchor=CENTER, width=160)
                    tree.column("ID", anchor=CENTER, width=120)
                    tree.column("date", anchor=CENTER, width=120)
                    tree.column("t", anchor=CENTER, width=160)
                    tree.heading("#0", text="", anchor=W)
                    tree.heading("Item Name", text="Item Name", anchor=W)
                    tree.heading("Item Code", text="Item Code", anchor=W)
                    tree.heading("Quantity", text="Quantity", anchor=CENTER)
                    tree.heading("Price", text="Price", anchor=CENTER)
                    tree.heading("email", text="Email", anchor=CENTER)
                    tree.heading("ID", text="ID", anchor=CENTER)
                    tree.heading("date", text="Date", anchor=CENTER)
                    tree.heading("t", text="Recepit", anchor=CENTER)
                    rec_fr = LabelFrame(wim, text="Entries")
                    rec_fr.pack(anchor=S, fill="x", expand="yes", padx=20)
                    in_l = Label(rec_fr, text="Item Name")
                    in_l.grid(row=2, column=0, padx=1, pady=10)
                    in_e = Entry(rec_fr)
                    in_e.grid(row=2, column=1, padx=1, pady=10)
                    ic_l = Label(rec_fr, text="Item Code")
                    ic_l.grid(row=2, column=2, padx=1, pady=10)
                    ic_e = Entry(rec_fr)
                    ic_e.grid(row=2, column=3, padx=1, pady=10)
                    qty_l = Label(rec_fr, text="Quantity")
                    qty_l.grid(row=2, column=4, padx=1, pady=10)
                    qty_e = Entry(rec_fr)
                    qty_e.grid(row=2, column=5, padx=1, pady=10)
                    p_l = Label(rec_fr, text="Price")
                    p_l.grid(row=3, column=0, padx=1, pady=10)
                    p_e = Entry(rec_fr)
                    p_e.grid(row=3, column=1, padx=1, pady=10)
                    d_l = Label(rec_fr, text="Email")
                    d_l.grid(row=3, column=2, padx=1, pady=10)
                    d_e = Entry(rec_fr)
                    d_e.grid(row=3, column=3, padx=1, pady=10)
                    id_l = Label(rec_fr, text="ID")
                    id_l.grid(row=3, column=4, padx=1, pady=10)
                    id_e = Entry(rec_fr)
                    id_e.grid(row=3, column=5, padx=1, pady=10)
                    e_l = Label(rec_fr, text="Recepit")
                    e_l.grid(row=3, column=6, padx=1, pady=10)
                    e_e = Entry(rec_fr)
                    e_e.grid(row=3, column=7, padx=1, pady=10)
                    da_l = Label(rec_fr, text="Date")
                    da_l.grid(row=2, column=6, padx=1, pady=10)
                    da_e = Entry(rec_fr)
                    da_e.grid(row=2, column=7, padx=1, pady=10)
                    def sel_data(e):
                        in_e.delete(0, END)
                        ic_e.delete(0, END)
                        qty_e.delete(0, END)
                        p_e.delete(0, END)
                        d_e.delete(0, END)
                        e_e.delete(0, END)
                        da_e.delete(0, END)
                        id_e.delete(0, END)
                        sel = tree.focus()
                        val = tree.item(sel, 'val')
                        in_e.insert(0, val[0])
                        ic_e.insert(0, val[1])
                        qty_e.insert(0, val[2])
                        p_e.insert(0, val[3])
                        d_e.insert(0, val[4])
                        e_e.insert(0, val[5])
                        da_e.insert(0, val[6])
                        id_e.insert(0, val[7])
                    def retu():
                        con = sqlite3.connect('DATA.db')
                        c = con.cursor()
                        c.execute("""CREATE TABLE if not exists return (
                                                                   	item_name text,
                                                                   	item_code text,
                                                                   	quantity text,
                                                                   	price text,
                                                                   	email text,
                                                                   	t text,
                                                                   	date text,
                                                                   	id integer)
                                                                   	""")
                        def clear_entries():
                            q_spin.delete(0, tkinter.END)
                            q_spin.insert(0, "1")
                            d_en.delete(0, tkinter.END)
                            p_spin.delete(0, tkinter.END)
                            p_spin.insert(0, "0.0")
                            ic_entry.delete(0, tkinter.END)
                        i_list = []
                        def add_item():
                            con = sqlite3.connect('DATA.db')
                            c = con.cursor()
                            c.execute(
                                "INSERT INTO return VALUES (:first, :last, :quantity,:price,:email,:t ,:date,:id)",
                                {
                                    'first': d_en.get(),
                                    'last': ic_entry.get(),
                                    'quantity': q_spin.get(),
                                    'price': p_spin.get(),
                                    'email': e_e.get(),
                                    't': da_e.get(),
                                    'date': ph_e.get(),
                                    'id': id_e.get(),
                                })
                            con.commit()
                            con.close()
                            q = int(q_spin.get())
                            d = d_en.get()
                            p = float(p_spin.get())
                            ic = ic_entry.get()
                            da = da_e.get()
                            total = q * p
                            invoice_item = [q, d, p, total, ic, da]
                            tree.insert('', 0, values=invoice_item)
                            clear_entries()
                            i_list.append(invoice_item)
                        def make_invoice():
                            d = DocxTemplate("return_t.docx")
                            email = e_e.get()
                            date = da_e.get()
                            tcode = ph_e.get()
                            subtot = sum(item[3] for item in i_list)
                            saletx = 0.1
                            tot = subtot * (1 - saletx)
                            d.render({"name": email,
                                      "tcode": tcode,
                                      "invoice_list": i_list,
                                      "subtotal": subtot,
                                      "salestax": str(saletx * 100) + "%",
                                      "total": tot,
                                      "date": date
                                      })
                            d_name = "new_return" + email + datetime.datetime.now().strftime(
                                "%Y-%m-%d-%H%M%S") + ".docx"
                            d.save(d_name)
                            messagebox.showinfo("Return Created", "Return Created")
                            w.destroy()
                            wim.destroy()
                        w = tkinter.Tk()
                        w.title("Return Generator Form")
                        fra = tkinter.Frame(w)
                        fra.pack(padx=1, pady=5)
                        e_label = tkinter.Label(fra, text="Email")
                        e_label.grid(row=1, column=0)
                        e_e = tkinter.Entry(fra)
                        e_e.grid(row=2, column=0)
                        ph_lab = tkinter.Label(fra, text="Recepit number")
                        ph_lab.grid(row=3, column=0)
                        ph_e = tkinter.Entry(fra)
                        ph_e.grid(row=4, column=0)
                        q_lab = tkinter.Label(fra, text="Qty")
                        q_lab.grid(row=1, column=1)
                        q_spin = tkinter.Spinbox(fra, from_=1, to=100)
                        q_spin.grid(row=2, column=1)
                        ic_lab = tkinter.Label(fra, text="Item Code")
                        ic_lab.grid(row=3, column=1)
                        ic_entry = tkinter.Entry(fra)
                        ic_entry.grid(row=4, column=1)
                        da_lab = tkinter.Label(fra, text="Date")
                        da_lab.grid(row=5, column=0)
                        da_e = tkinter.Entry(fra)
                        da_e.grid(row=6, column=0)
                        d_lab = tkinter.Label(fra, text="Item Name")
                        d_lab.grid(row=1, column=2)
                        d_en = tkinter.Entry(fra)
                        d_en.grid(row=2, column=2)
                        p_lab = tkinter.Label(fra, text="Unit Price")
                        p_lab.grid(row=3, column=2)
                        p_spin = tkinter.Entry(fra)
                        p_spin.grid(row=4, column=2)
                        add_it_b = tkinter.Button(fra, text="Add an Item", command=add_item)
                        add_it_b.grid(row=8, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                        columns = ('qty', 'name', 'code', 'total', 'icode', 'd')
                        tree = ttk.Treeview(fra, columns=columns, show="headings")
                        tree.heading('qty', text='Quantity')
                        tree.heading('name', text='Item Name')
                        tree.heading('code', text='Unit Price')
                        tree.heading('total', text="Total")
                        tree.heading('icode', text="Item Code")
                        tree.heading('d', text="Date")
                        tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
                        save_inv_b = tkinter.Button(fra, text="Create a Return", command=make_invoice)
                        save_inv_b.grid(row=9, column=0, columnspan=6, sticky="news", padx=20, pady=5)
                        con.commit()
                        con.close()
                        tree.delete(*tree.get_children())
                        q_data()
                        w.mainloop()
                    b_f = LabelFrame(wim, text="Commands")
                    b_f.pack(anchor=CENTER, fill="x", expand="yes", padx=20)
                    add_b = Button(b_f, text="Make Returns", command=retu)
                    add_b.grid(row=0, column=0, padx=20, pady=10)
                    search_b = Button(b_f, text="Reset", command=q_data)
                    search_b.grid(row=0, column=1, padx=20, pady=10)
                    search_b = Button(b_f, text="Search Old Transactions", command=find_rcs)
                    search_b.grid(row=0, column=2, padx=20, pady=10)
                    tree.bind("<ButtonRelease-1>", sel_data)
                    q_data()
                    wim.mainloop()
                activation = Button(wu1, text=" Search an Item       ", command=wim)
                activation.grid(row=0, column=0, columnspan=1, pady=0, padx=0, ipadx=70)
                activation = Button(wu1, text=" Proceed to Purchase  ", command=purchase)
                activation.grid(row=1, column=0, columnspan=1, pady=0, padx=0, ipadx=60)
                activation = Button(wu1, text=" Old Transactions    ", command=R)
                activation.grid(row=2, column=0, columnspan=1, pady=0, padx=0, ipadx=70)
                wu1.mainloop()
            else:
                tkinter.messagebox.showinfo("blah", "Email or Password is incorrect")
            email.delete(0, END)
            password.delete(0, END)
        email = Entry(wu, width=30)
        email.grid(row=0, column=1, padx=20, pady=(10, 0))
        password = Entry(wu, width=30, show="*")
        password.grid(row=1, column=1)
        email_label = Label(wu, text="Email")
        email_label.grid(row=0, column=0, pady=(10, 0))
        passport_label = Label(wu, text="Password")
        passport_label.grid(row=1, column=0)
        submit_btn = Button(wu, text='Login', command=usersubmit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=5, padx=10, ipadx=10)
        wu.mainloop()
    admin = Button(wa, text="   Admin ", command=admin)
    admin.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=25)
    staff = Button(wa, text="   Staff ", command=staff)
    staff.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=30)
    user = Button(wa, text="   User ", command=user)
    user.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=30)
    requestacc = Button(wa, text="Sing Up", command=RA)
    requestacc.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=30)
    con.commit()
    con.close()
    wa.mainloop()
activation=Label(w,image=pic)
activation.place(x=0,y=0,relwidth=1,relheight=1)
activation= Button(w, text="Please Click to Proceed", command=activate)
activation.grid(row=1, column=0, columnspan=1, pady=244, padx=30, ipadx=30)
con.commit()
con.close()
w.mainloop()
