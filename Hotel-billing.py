import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import date
import mysql.connector as mysql



window = tk.Tk()
window.geometry("2000x1000")
window.title("Billing")

#=================================================Global Variable=======================================================#
#================================For-Date-Variable=================#
global today
global day
global nu_month
global st_month
global year
#===============================For-Main-Data-VAriable============#
global manager_index_database
global manager_username_database
global manager_password_database
global waiter_index_database
global waiter_username_database
global waiter_password_database
global CGST_index_database
global CGST_value_database
global SGST_index_database
global SGST_value_database
global TGST_index_database
global TGST_value_database

#==================================================StringVar===========================================================#          
#=================Login-Window-StringVar================#
usernameVar = tk.StringVar()
passwordVar = tk.StringVar()

#=================Waiter-Window-StringVar================#
tableNumberVar = tk.StringVar()
itemNameVar = tk.StringVar()
itemQuantityVar = tk.StringVar()
SubTotalVar = tk.IntVar()
GstTotalVar = tk.IntVar()
TotalVar = tk.IntVar()

#================Menu-Window-StringVar=================#
indexofitemVar = tk.StringVar()
nameofitemVar = tk.StringVar()
costofitemVar = tk.StringVar()

#================GST-Window-StringVar=================#
cgstVar = tk.StringVar()
sgstVar = tk.StringVar()
tgstVar = tk.StringVar()

#================Setting-Window-StringVar==============#
managerusernameVar = tk.StringVar()
managerpasswordVar = tk.StringVar()
waiterusernameVar = tk.StringVar()
waiterpasswordVar = tk.StringVar()

#===============Summary-Window-StringVar===============#
FromDateVar = tk.StringVar()
FromMonthVar = tk.StringVar()
FromYearVar = tk.StringVar()
ToDateVar = tk.StringVar()
ToMonthVar = tk.StringVar()
ToYearVar = tk.StringVar()
From_Month = tk.StringVar()
To_Month = tk.StringVar()
CGSTinSummaryVar = tk.DoubleVar()
SGSTinSummaryVar = tk.DoubleVar()
TGSTinSummaryVar = tk.DoubleVar()
SubTotalinSummaryVar = tk.DoubleVar()
TotalinSummaryVar = tk.DoubleVar()
#================================================TreeView==============================================================#
#=============================Waiter-bills-Tv===================#
billsTV = ttk.Treeview(height=13, columns=('Item Name','Rate','Quantity','Cost'))
#=============================Manager-Item-TV==================#
itemsTV = ttk.Treeview(height=12,columns=('Item Name','Cost'))
#============================Summary-TV==================#
summaryTV = ttk.Treeview(height=15,columns=('Date','Table Number','Sub Total','CGST','SGST','TGST','Total Amount'))
#=================================================Function=============================================================#
#=================For-Main-Data-(WithoutFunction)==============================#
conn = mysql.connect(host="localhost", user="root",passwd="",db="elm")
cursor = conn.cursor()
query="SELECT * from setting"
cursor.execute(query)
main_info = cursor.fetchall()
for idx, n in enumerate(main_info):
    if(idx == 0):
        manager_index_database = n[0]
        manager_username_database = n[1]
        manager_password_database = n[3]
    elif(idx == 1):
        waiter_index_database = n[0]
        waiter_username_database = n[1]
        waiter_password_database = n[3]
    elif(idx == 2):
        CGST_index_database = n[0]
        CGST_value_database = n[2]
    elif(idx == 3):
        SGST_index_database = n[0]
        SGST_value_database = n[2]
    elif(idx == 4):
        TGST_index_database = n[0]
        TGST_value_database = n[2]
#=================To-remove-widgets===========================#
def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.grid_remove()

#================================For-Date-Function=================#
today = date.today()
Month=["0"," January "," February"," March "," April "," May "," June "," July "," August "," September "," October "," November "," December "]
year = date.today().year
nu_month = date.today().month
day = date.today().day
st_month = Month[nu_month]

#=================================================Button-Event==========================================================#
#====================Reset-Button==================#
def reset():
    usernameVar.set("")
    passwordVar.set("")

#====================Login-Button==================#
def login():
    name = usernameVar.get()
    password = passwordVar.get()
    if name == waiter_username_database and int(password) == int(waiter_password_database):
        reset()
        remove_all_widgets()
        waiterWindow()
        
    elif name == manager_username_database and int(password) == int(manager_password_database):
        reset()
        remove_all_widgets()
        managerWindow()
    else :
        reset()
        messagebox.showerror("Invalid user", "Credentials enters are invalid")

#==================Logout-Button-ManagerWindow======#
def logout():
    
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        remove_all_widgets()
        loginWindow()

#=================Logout-Button-WaiterWindow========#
def logoutW():
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("truncate billing")
    cursor.execute("commit")
    logout()
#====Go-To-MenuWindow-From-ManagerWindow-Button=======#
def go_to_menuWindow():
    remove_all_widgets()
    menuWindow()

#==============Go-To-ManagerWindow-Button==============#
def go_to_managerWindow():
    remove_all_widgets()
    managerWindow()

#==========Add-Item-to-List-Button-(MenuWindow)========#
def addToList():
    index=indexofitemVar.get()
    name=nameofitemVar.get()
    cost=costofitemVar.get()
    try:
        index=int(index)
        name=str(name)
        cost=int(cost)
        if(nameofitemVar.get() != "" and costofitemVar.get() != "" and indexofitemVar.get() != ""):
            conn = mysql.connect(host="localhost", user="root",passwd="",db="elm")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `menu`(`Index`, `Name`, `Cost`) VALUES ('" + indexofitemVar.get() + "','" + nameofitemVar.get() +"','" + costofitemVar.get() +"')")
            cursor.execute("commit")
            messagebox.showinfo("Insert Status","Item Inserted to List Successfully")
            conn.close()
            indexofitemVar.set("")
            nameofitemVar.set("")
            costofitemVar.set("")
        elif(nameofitemVar.get() == "" or costofitemVar.get() == "" or indexofitemVar.get() == "" ):
            messagebox.showinfo("Insert Status","Enter the Information of Item")
        go_to_menuWindow()
    except ValueError:
        messagebox.showerror("Insert Status","Enter Valid Info")
#================Delete-Item-From-List-Button-(MenuWindow)===#
def deleteFromList():
    if(indexofitemVar.get() == ""):
        messagebox.showinfo("Delete Status","Enter Valid Index")
    else:
        conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
        cursor = conn.cursor()
        cursor.execute("Delete From `menu` where `Index`='" + indexofitemVar.get() + "'")
        cursor.execute("commit")
        indexofitemVar.set("")
        nameofitemVar.set("")
        costofitemVar.set("")
        messagebox.showinfo("Delete Status","Delete Item From List Successfully")
        conn.close()
        go_to_menuWindow()

#=================Update-Item-to-List-Button-(MenuWindow)====#
def updateToList():
    index=indexofitemVar.get()
    name=nameofitemVar.get()
    cost=costofitemVar.get()
    try:
        index=int(index)
        name=str(name)
        cost=int(cost)
        if(indexofitemVar.get() == "" and nameofitemVar.get() == "" and costofitemVar.get() == ""):
            messagebox.showinfo("Update Status","Enter Valid Info")
        else:
            conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
            cursor = conn.cursor()
            cursor.execute("Update `menu` set `Name`='" + nameofitemVar.get() + "',`Cost` = '" + costofitemVar.get() + "' where  `Index`='" + indexofitemVar.get() + "'")
            cursor.execute("commit")
            indexofitemVar.set("")
            nameofitemVar.set("")
            costofitemVar.set("")
            messagebox.showinfo("Update Status","Update Item From List Successfully")
            conn.close()
            go_to_menuWindow()
    except ValueError:
        messagebox.showerror("Update Status","Enter Valid Info")

#==================Go-To-GST-Window-Button=================#
def go_to_gstWindow():
    remove_all_widgets()
    gstWindow()

#==================Refresh-Button-inGSTWindow===============#
def to_refresh_gstWindow():
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("SELECT * from setting")
    database_fetch = cursor.fetchall()
    for idx, n in enumerate(database_fetch):
        if(idx == 2):
            CGST_value_database = n[2]
        elif(idx == 3):
            SGST_value_database = n[2]
        elif(idx == 4):
            TGST_value_database = n[2]
    conn.close()
    cgstVar.set(CGST_value_database)
    sgstVar.set(SGST_value_database)
    tgstVar.set(TGST_value_database)
#================UpGrade-Button-inGSTWinodw================#
def to_upgrade_gstWindow():
    cgst = cgstVar.get()
    sgst = sgstVar.get()
    try:
        cgst = float(cgst)
        sgst = float(sgst)
        tgst = cgst + sgst
        conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
        cursor = conn.cursor()
        tgstVar.set(tgst)
        cursor.execute("Update `setting` set `Value` = '" + cgstVar.get() + "' where `index`='"+ str(CGST_index_database) + "'")
        cursor.execute("Update `setting` set `Value` = '" + sgstVar.get() + "' where `index`='"+ str(SGST_index_database) + "'")
        cursor.execute("Update `setting` set `Value` = '" + tgstVar.get() + "' where `index`='"+ str(TGST_index_database) + "'")
        cursor.execute("commit")
        messagebox.showinfo("Update Status","Update GST Successfully")
        cursor.execute("SELECT * from setting")
        database_fetch = cursor.fetchall()
        for idx, n in enumerate(database_fetch):
            if(idx == 2):
                CGST_value_database = n[2]
            elif(idx == 3):
                SGST_value_database = n[2]
            elif(idx == 4):
                TGST_value_database = n[2]
        conn.close()
    except ValueError as error:
        messagebox.showerror("Invalid Input","Please Enter Valid Interger")
        
#================Go-To-Setting-Window-Button=================#
def go_to_settingWindow():
    remove_all_widgets()
    settingWindow()

#===============Refresh-Button-inSettingWindow===============#
def to_refresh_settingWindow():
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("SELECT * from setting")
    database_fetch = cursor.fetchall()
    for idx, n in enumerate(database_fetch):
        if(idx == 0):
            manager_username_database = n[1]
            manager_password_database = n[3]
        elif(idx == 1):
            waiter_username_database = n[1]
            waiter_password_database = n[3]
    conn.close()
    managerusernameVar.set(manager_username_database)
    managerpasswordVar.set(manager_password_database)
    waiterusernameVar.set(waiter_username_database)
    waiterpasswordVar.set(waiter_password_database)
#============Upgrade-ManagerInfo-Button-(SettingWinodw)======#
def upgrade_manager_info():
    username = managerusernameVar.get()
    password = managerpasswordVar.get()
    if( str(username) == str(waiter_username_database)):
        messagebox.showerror("Invalid Input","Please enter another username")
    else:
        try:
            username = str(username)
            password = int(password)
            conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
            cursor = conn.cursor()
            cursor.execute("Update `setting` set `Info` = '" + managerusernameVar.get() +"',`Password` = '"+managerpasswordVar.get()+"' where `index` ='"+str(manager_index_database)+"'")
            cursor.execute("commit")
            messagebox.showinfo("Update Status","Update Manager Info Successfully")
            cursor.execute("SELECT * from setting")
            database_fetch = cursor.fetchall()
            conn.close()
        except ValueError:
            messagebox.showerror("Invalid Input","Please Enter Valid Info,(Username should be in string,Password should be in integer)")
#=============Summary-Button-(MangerWindow)====================#
def go_to_summaryWindow():
    remove_all_widgets()
    summaryWindow()

#============Upgrade-WaiterInfo-Button-(SettingWinodw)======#
def upgrade_waiter_info():
    username = waiterusernameVar.get()
    password = waiterpasswordVar.get()
    if( str(username) == str(manager_username_database)):
        messagebox.showerror("Invalid Input","Please enter another username")
    else:
        try:
            username = str(username)
            password = int(password)
            conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
            cursor = conn.cursor()
            cursor.execute("Update `setting` set `Info` = '" + waiterusernameVar.get() +"',`Password` = '"+waiterpasswordVar.get()+"' where `index` ='"+str(waiter_index_database)+"'")
            cursor.execute("commit")
            messagebox.showinfo("Update Status","Update Manager Info Successfully")
            cursor.execute("SELECT * from setting")
            database_fetch = cursor.fetchall()
            conn.close()
        except ValueError:
            messagebox.showerror("Invalid Input","Please Enter Valid Info,(Username should be in string,Password should be in integer)")

#=======================Show-Bill-Button(From-Waiter-Winodow)=======================#
def show_bill():
    flag = 0
    data_in_bill = 0
    total = 0
    Gst = 0
    SubTotal = 0

    previous_menu = billsTV.get_children()
        
    for element in previous_menu:
        billsTV.delete(element)
    tablenumber = tableNumberVar.get()
    try:
        tablenumber = int(tablenumber)
        conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
        cursor = conn.cursor()
        cursor.execute("select * from billing")
        bills = cursor.fetchall()
        if(len(bills) == 0):
            messagebox.showerror("Bill","No Data")
        else:
            data_in_bill = 1
    except ValueError as er:
        messagebox.showerror("Table Number","PLease Enter integer table number.")
    if(data_in_bill == 1):
        index=1
        for indx,n in enumerate(bills):
            idx,tableno,item,rate,quantity,totalcost = n
            if(int(tablenumber) == int(tableno)):
                billsTV.insert("",index,text=index,values=(item,rate,quantity,totalcost))
                index=index+1
                SubTotal = SubTotal + totalcost 
            elif(int(tablenumber) != int(tableno)):
                flag = 1
    conn.close()
    conn = mysql.connect(host="localhost", user="root",passwd="",db="elm")
    cursor = conn.cursor()
    query="SELECT * from setting"
    cursor.execute(query)
    main_info = cursor.fetchall()
    for idx, n in enumerate(main_info):
        if(idx == 4):
            TGST_value = n[2]
    Gst = ((SubTotal * TGST_value)/100)
    total = SubTotal + Gst
    SubTotalVar.set(SubTotal)
    GstTotalVar.set(Gst)
    TotalVar.set(total)
        
    
#==============================Add-To-List-Button(From-Waiter-Winodow)========================#
def add_to_list():
    to_check_item_inlist = 0
    flag = 0
    tableno = tableNumberVar.get()
    itemname = itemNameVar.get()
    itemquantity = itemQuantityVar.get()
    try:
        tableno = int(tableno)
        itemname = str(itemname)
        itemquantity = int(itemquantity)
        conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
        cursor = conn.cursor()
        cursor.execute("select * from billing")
        bills = cursor.fetchall()
        if(len(bills) == 0):
            flag = 1
        else:
            flag = 2
    except ValueError as er:
        messagebox.showerror("Add To List","Please Enter Valid Info")
    if(flag == 1):
        cursor.execute("select * from menu")
        menu = cursor.fetchall()
        for n in menu:
            idx,itemname_menu,itemcost_menu = n
            if(str(itemname_menu) == str(itemname)):      
                cursor.execute("INSERT INTO `billing`(`Index`, `Billno`, `Item`, `Rate`, `Quantity`, `TotalCost`) VALUES ('','" + tableNumberVar.get() + "','" + itemNameVar.get() + "','"+ str(itemcost_menu) +"','" + itemQuantityVar.get() + "','" + str(itemcost_menu * itemquantity) + "')")
                cursor.execute("commit")
                break
    elif(flag == 2):
        cursor.execute("select * from menu")
        menu2 = cursor.fetchall()
        for n in menu2:
            itemindex_menu2,itemname_menu2,itemcost_menu2 = n
            if(str(itemname_menu2) == str(itemname)):
                to_check_item_inlist = 1
                break
        cursor.execute("select * from billing")
        billing = cursor.fetchall()
        cursor.execute("select count(*) from billing")
        number = cursor.fetchall()
        for n  in number:
            number_len=n[0]
        if(to_check_item_inlist == 1):
            for index1, bill in enumerate(billing):
                idx,tablenumber,item_name,rate,quantity,totalcost = bill
                if(int(tableno) == int(tablenumber)):
                    if(str(item_name)== str(itemname)):
                        new_quantity = quantity + itemquantity
                        cursor.execute("Update `billing` set `Billno` = '" + tableNumberVar.get() +"',`Item` = '" + itemNameVar.get()+"',`Rate` = '" + str(itemcost_menu2) +"',`Quantity` = '" + str(new_quantity) + "',`TotalCost` = '" + str(itemcost_menu2 * new_quantity)+"'where `index` ='"+str(idx)+"'")
                        cursor.execute("commit")
                        break
                    elif((int(index1)+1) == int(number_len)):
                        cursor.execute("INSERT INTO `billing`(`Index`, `Billno`, `Item`, `Rate`, `Quantity`, `TotalCost`) VALUES ('','" + tableNumberVar.get() + "','" + itemNameVar.get() + "','"+ str(itemcost_menu2) +"','" + itemQuantityVar.get() + "','" + str(itemcost_menu2 * itemquantity) + "')")
                        cursor.execute("commit")
                        break
                elif((int(index1)+1) == int(number_len)):
                        cursor.execute("INSERT INTO `billing`(`Index`, `Billno`, `Item`, `Rate`, `Quantity`, `TotalCost`) VALUES ('','" + tableNumberVar.get() + "','" + itemNameVar.get() + "','"+ str(itemcost_menu2) +"','" + itemQuantityVar.get() + "','" + str(itemcost_menu2 * itemquantity) + "')")
                        cursor.execute("commit")
                        break
        else:
            messagebox.showerror("Menu Status","Please Enter Valid Input")
    conn.close()
    itemNameVar.set("")
    itemQuantityVar.set("")
    show_bill()
#==============================Delete-From-List-Button(From-Waiter-Winodow)========================#
def delete_from_list():
    flag = 0
    tableno = tableNumberVar.get()
    itemname = itemNameVar.get()
    itemquantity = itemQuantityVar.get()
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("select * from billing")
    billing = cursor.fetchall()
    cursor.execute("select count(*) from billing")
    number = cursor.fetchall()
    for n1  in number:
        number_len=n1[0]
    if(tableno != '' and itemname == '' and itemquantity == ''):
        for index1,n in enumerate(billing):
            idx,tablenumber,item_name,rate,quantity,totalcost = n
            if(int(tablenumber) == int(tableno)):
                cursor.execute("Delete From `billing` where `Index`='" + str(idx) + "'")
                cursor.execute("commit")
            elif((int(index1)+1) == int(number_len)):
                messagebox.showerror("Table Status","Please Enter Valid Input")
    elif(tableno != '' and itemname != '' and itemquantity == ''):
        for index1,m in enumerate(billing):
            idx_m,tablenumber_m,item_name_m,rate_m,quantity_m,totalcost_m = m
            if(int(tablenumber_m) == int(tableno)and str(itemname) == str(item_name_m)):
                cursor.execute("Delete From `billing` where `Index`='" + str(idx_m) + "'")
                cursor.execute("commit")
            elif((int(index1)+1) == int(number_len)):
                messagebox.showerror("Table Status","Please Enter Valid Input")
    elif(tableno != '' and itemname != '' and itemquantity != ''):
        for index1,n1 in enumerate(billing):
            idx1,tablenumber1,item_name1,rate1,quantity1,totalcost1 = n1
            if(int(tableno) == int(tablenumber1) and str(itemname) == str(item_name1)):
                new_quantity = int(quantity1) - int(itemquantity)
                if(0 < new_quantity):
                    cursor.execute("Update `billing` set `Billno` = '" + tableNumberVar.get() +"',`Item` = '" + itemNameVar.get()+"',`Rate` = '" + str(rate1) +"',`Quantity` = '" + str(new_quantity) + "',`TotalCost` = '" + str(rate1 * new_quantity)+"'where `index` ='"+str(idx1)+"'")
                    cursor.execute("commit")
                else:
                    cursor.execute("Delete From `billing` where `Index`='" + str(idx1) + "'")
                    cursor.execute("commit")
            elif((int(index1)+1) == int(number_len)):
                messagebox.showerror("Table Status","Please Enter Valid Input")
    conn.close()
    itemNameVar.set("")
    itemQuantityVar.set("")
    show_bill()

#===============================Check-out-Button(From-Waiter-Winodow)========================#
def total():
    CGST_value = 0
    SGST_value = 0
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    subtotal = SubTotalVar.get()
    cursor.execute("SELECT * from setting")
    main_info = cursor.fetchall()
    for idx, n in enumerate(main_info):
        if(idx == 2):
            CGST_value= n[2]
        elif(idx == 3):
            SGST_value = n[2]
    cgst = ((subtotal * CGST_value)/100)
    sgst = ((subtotal * SGST_value)/100)
    tgst = cgst + sgst
    total = tgst + subtotal
    cursor.execute("INSERT INTO `summary`(`Index`, `Date`, `Day`, `Month`, `Year`, `Tableno`, `TotalAmount`, `CGST`, `SGST`, `TGST`, `SubTotal`) VALUES ('','" + str(today) + "','" + str(day) + "','" + str(nu_month) + "','" + str(year) + "','" + tableNumberVar.get()+ "','" + str(total) + "','" + str(cgst)+ "','" + str(sgst)+ "','" + str(tgst)+ "','" + str(SubTotalVar.get())+ "')")
    cursor.execute("commit")
    MsgBox = tk.messagebox.askquestion ('Check Out','Are you sure you want to check out',icon = 'warning')
    if MsgBox == 'yes':
        cursor.execute("select * from billing")
        bills = cursor.fetchall()
        for n in bills:
            idx,tablenumber,item_name,rate,quantity,totalcost = n
            if(int(tablenumber) == int(tableNumberVar.get())):
                cursor.execute("Delete From `billing` where `Index`='" + str(idx) + "'")
                cursor.execute("commit")
    show_bill()

#=======================refresh-button-(Summary-Window)=================# 
def to_refresh_summaryWindow():
    previous_menu = summaryTV.get_children()

    for element in previous_menu:
        summaryTV.delete(element)
        
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("select * from summary")
    menu = cursor.fetchall()
    idx = 1
    for n in menu:
        index,date,day,month,year,tableno,totalamount,cgst,sgst,tgst,subtotal = n    
        summaryTV.insert("",idx,text=idx,values=(date,tableno,subtotal,cgst,sgst,tgst,totalamount))
        idx = idx +1
    conn.close()

#=======================Get_Summary-Button-(Summary-Window)=========#
def get_summary():
    month_list = ['All','January','February','March','April','May','June','July','August','September','October','November','December']
    for index,i in enumerate(month_list):
        if(From_Month.get() == i):
            FromMonthVar.set(index)
        if(To_Month.get() == i):
            ToMonthVar.set(index)

    fDate = FromDateVar.get()
    fMonth = FromMonthVar.get()
    fYear = FromYearVar.get()
    tDate = ToDateVar.get()
    tMonth = ToMonthVar.get()
    tYear = ToYearVar.get()
    try:
        fDate = int(fDate)
        fYear = int(fYear)
        tDate = int(tDate)
        tYear = int(tYear)
    except ValueError as er:
        messagebox.showerror("Summary Info","Please Enter Valid Info")

    if(fMonth == '0' or tMonth == '0'):
        messagebox.showerror("Summary Info","Please Enter Valid Info")

#=======================Reset-App-Button-(Setting-Window)====================#
def reset_app():
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("Update `setting` set `Value` = 0 where `index`='"+ str(CGST_index_database) + "'")
    cursor.execute("Update `setting` set `Value` = 0 where `index`='"+ str(SGST_index_database) + "'")
    cursor.execute("Update `setting` set `Value` = 0 where `index`='"+ str(TGST_index_database) + "'")
    cursor.execute("commit")
    delete_all_menu()
    delete_all_summary()
    remove_all_widgets()
    loginWindow()

#=======================Delete-All-Menu-Button-(Setting-Window)====================#
def delete_all_menu():
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("truncate table menu")
    cursor.execute("commit")
    conn.close()
    
#=======================Delete-All-Summary-Button-(Setting-Window)====================#
def delete_all_summary():
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("truncate table summary")
    cursor.execute("commit")
    conn.close()   
    

#===============================================Windows===============================================================#
#==================Login-Window==================#
def loginWindow():
    title_main = ttk.Label(window,text="Hotel Billing Managment",font="Arial 40")
    title_main.grid(row=0,column=0,columnspan=3,padx=(450,0),pady=(50,0))

    title_login = ttk.Label(window,text="Login",font="Arial 30")
    title_login.grid(row=2,column=0,columnspan=2,padx=(650,0),pady=(100,0))

    usernameLabel = ttk.Label(window,text="Username",font="Arial 15")
    usernameLabel.grid(row=4,column=1,padx=(20,0),pady=(50,0))

    passwordLabel = ttk.Label(window,text="Password",font="Arial 15")
    passwordLabel.grid(row=5,column=1,padx=(20,0),pady=(50,0))

    usernameEntry = ttk.Entry(window,textvariable=usernameVar)
    usernameEntry.grid(row=4,column=2,padx=(0,0),pady=(50,0))

    passwordEntry = ttk.Entry(window,textvariable=passwordVar,show="*")
    passwordEntry.grid(row=5,column=2,padx=(0,0),pady=(50,0))

    loginButton = ttk.Button(window, text="Login",width=20,command=lambda:login())
    loginButton.grid(row=6, column=1, columnspan=2,padx=(50,0),pady=(25,0))

    resetButton = ttk.Button(window, text="Reset",width=20,command=lambda:reset())
    resetButton.grid(row=7, column=1, columnspan=2,padx=(50,0),pady=(25,0))

#==================Waiter-Window================#
def waiterWindow():
    
    previous_menu = billsTV.get_children()
        
    for element in previous_menu:
        billsTV.delete(element)
        
        
    dateLabel = ttk.Label(window,text="Date :- ",font="Arial 15")
    dateLabel.grid(row=0,column=0,padx=(30,0))

    date = ttk.Label(window,text = today,font="Arial 15")
    date.grid(row=0,column=1,padx=(10,0))

    logout_button_waiterwindow = ttk.Button(window, text="Logout",width=20,command=lambda:logoutW())
    logout_button_waiterwindow.grid(row=0, column=7, columnspan=2,padx=(50,0),pady=(25,0))
    
    title_waiterwindow = ttk.Label(window,text="Waiter Billing Managment",font="Arial 23")
    title_waiterwindow.grid(row=1,column=3,columnspan=3,padx=(30,),pady=(5,15))

    table_no = ttk.Label(window,text="Table No.:-",font="Arial 15")
    table_no.grid(row=3,column=2,pady=(10,0))
    
    table_no_entry = ttk.Entry(window,textvariable=tableNumberVar,width=10)
    table_no_entry.grid(row=3,column=4,pady=(10,0))

    show_bill_button = ttk.Button(window,text="Show Bill",command=lambda:show_bill())
    show_bill_button.grid(row=3,column=5)

    item_label = ttk.Label(window,text="Enter the item :- ",font="Arial 15")
    item_label.grid(row=4,column=2,pady=(10,0))

    conn = mysql.connect(host="localhost", user="root", passwd="", db="elm")
    cursor = conn.cursor()
    query="SELECT `Name` FROM `menu`"
    cursor.execute(query)
    itemName = cursor.fetchall()
    conn.close()
    

    item_name_entry = ttk.Combobox(window,text=itemNameVar,width=100)
    item_name_entry.grid(row=4,column=4,pady=(10,0))
    item_name_entry['values']=itemName
    
    quantity_label = ttk.Label(window,text="Enter Quantity of item :- ",font="Arial 15")
    quantity_label.grid(row=5,column=2,pady=(10,10))

    item_quantity_entry = ttk.Entry(window,text=itemQuantityVar,width=10)
    item_quantity_entry.grid(row=5,column=4,pady=(10,10))

    add_item_button = ttk.Button(window,text="Add to List",width=100,command=lambda:add_to_list())
    add_item_button.grid(row=6,column=2,columnspan=4,pady=(10,))

    delete_item_button = ttk.Button(window,text="Delete From List",width=100,command=lambda:delete_from_list())
    delete_item_button.grid(row=7,column=2,columnspan=4,pady=(5,))
    
    billsTV.grid(row=8, column=2,columnspan=4,pady=(5,0))

    scrollBar = ttk.Scrollbar(window, orient="vertical",command=billsTV.yview)
    scrollBar.grid(row=8, column=5, sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV["columns"]=("one","two","three","four")
    billsTV.column("#0",width=100)
    billsTV.column("one",width=500)
    billsTV.column("two",width=100)
    billsTV.column("three",width=100)
    billsTV.column("four",width=100)
    

    billsTV.heading('#0',text="Index")
    billsTV.heading('one',text="Item Name")
    billsTV.heading('two',text="Rate")
    billsTV.heading('three',text="Quantity")
    billsTV.heading('four',text="Cost")
    
    
    total_button = ttk.Button(window,text="Check Out",width=100,command=lambda:total())
    total_button.grid(row=9,column=2,columnspan=4,pady=(20,10))
    
    subtotal_label = ttk.Label(window,text="Sub Total :- ",font="Arial 15")
    subtotal_label.grid(row=10,column=6,pady=(10,0))
    
    subtotal_value_label = ttk.Label(window,textvariable=SubTotalVar,font="Arial 15")
    subtotal_value_label.grid(row=10,column=7,pady=(10,0))
    
    gst_label = ttk.Label(window,text="GST :- ",font="Arial 15")
    gst_label.grid(row=11,column=6)

    gst_value_label = ttk.Label(window,textvariable=GstTotalVar,font="Arial 15")
    gst_value_label.grid(row=11,column=7)
    
    total_label = ttk.Label(window,text="Total :- ",font="Arial 15")
    total_label.grid(row=12,column=6)

    total_value_label = ttk.Label(window,textvariable=TotalVar,font="Arial 15")
    total_value_label.grid(row=12,column=7)

    SubTotalVar.set("")
    GstTotalVar.set("")
    TotalVar.set("")
        
    

#==================Manager-Window================#
def managerWindow():
    dateLabel = ttk.Label(window,text="Date :- ",font="Arial 15")
    dateLabel.grid(row=0,column=0,padx=(30,0))

    date = ttk.Label(window,text = today,font="Arial 15")
    date.grid(row=0,column=1,padx=(10,0))

    logout_button_managerwindow = ttk.Button(window, text="Logout",width=30,command=lambda:logout())
    logout_button_managerwindow.grid(row=0, column=7, columnspan=2,padx=(300,0),pady=(25,0))
    

    menu_button = ttk.Button(window,text="Menu",width=30,command=lambda:go_to_menuWindow())
    menu_button.grid(row=2,column=1,columnspan=2,padx=(10,40),pady=(100,50))

    summary_button = ttk.Button(window,text="Summary",width=30,command=lambda:go_to_summaryWindow())
    summary_button.grid(row=2,column=3,columnspan=2,padx=(10,40),pady=(100,50))

    gst_button = ttk.Button(window,text="GST INFO",width=30,command=lambda:go_to_gstWindow())
    gst_button.grid(row=2,column=5,columnspan=2,padx=(10,80),pady=(100,50))

    setting_button = ttk.Button(window,text="Setting",width=30,command=lambda:go_to_settingWindow())
    setting_button.grid(row=2,column=6,columnspan=2,padx=(50,40),pady=(100,50))

    title_managerwindow = ttk.Label(window,text="Manager Billing Managment",font="Arial 23")
    title_managerwindow.grid(row=4,column=3,columnspan=4,pady=(100,40))

#=================Menu-Window===================#
def menuWindow():
    dateLabel = ttk.Label(window,text="Date :- ",font="Arial 15")
    dateLabel.grid(row=0,column=0)

    date = ttk.Label(window,text = today,font="Arial 15")
    date.grid(row=0,column=1)

    back_button_menuWindow = ttk.Button(window,text="Back to Menu",width=30,command=lambda:go_to_managerWindow())
    back_button_menuWindow.grid(row=0,column=7,columnspan=2,padx=(100,0),pady=(25,0))

    menu_management_label = ttk.Label(window,text="Hotel Menu Management",font="Arial 25")
    menu_management_label.grid(row=1,column=1,columnspan=6,pady=(0,0))

    enter_index_no_item = ttk.Label(window,text="Enter the Index Number Of Item :- ",font="Arial 15")
    enter_index_no_item.grid(row=2,column=0,columnspan=4,pady=(40,0),padx=(170,0))

    index_of_item = ttk.Entry(window,textvariable=indexofitemVar,width=20)
    index_of_item.grid(row=2,column=2,columnspan=3,pady=(40,0),padx=(240,0))

    enter_name_item = ttk.Label(window,text="Enter the Name of Item :- ",font="Arial 15")
    enter_name_item.grid(row=3,column=0,columnspan=4,pady=(40,0),padx=(100,0))

    name_of_item = ttk.Entry(window,textvariable=nameofitemVar,width=50)
    name_of_item.grid(row=3,column=2,columnspan=3,pady=(40,0),padx=(240,0))

    enter_cost_item = ttk.Label(window,text="Enter the cost of Item :- ",font="Arial 15")
    enter_cost_item.grid(row=4,column=0,columnspan=4,pady=(40,0),padx=(100,0))

    cost_of_item = ttk.Entry(window,textvariable=costofitemVar,width=20)
    cost_of_item.grid(row=4,column=2,columnspan=3,pady=(40,0),padx=(240,0))

    add_to_list_button = ttk.Button(window,text="Add to List",width=35,command=lambda:addToList())
    add_to_list_button.grid(row=5,column=1,columnspan=2,padx=(150,0),pady=(50,50))

    delete_from_list_button = ttk.Button(window,text="Delete From List",width=35,command=lambda:deleteFromList())
    delete_from_list_button.grid(row=5,column=3,columnspan=2,padx=(50,0),pady=(50,50))

    update_to_list_button = ttk.Button(window,text="Upadte to List",width=35,command=lambda:updateToList())
    update_to_list_button.grid(row=5,column=5,padx=(50,0),pady=(50,50))


    itemsTV.grid(row=7, column=1,columnspan=6,pady=(5,0),padx=(140,0))

    scrollBar = ttk.Scrollbar(window, orient="vertical",command=itemsTV.yview)
    scrollBar.grid(row=7, column=6, sticky="NSE")

    itemsTV.configure(yscrollcommand=scrollBar.set)

    itemsTV["columns"] = ("one","two")
    itemsTV.column('#0',width=200)
    itemsTV.column('one',width=500)
    itemsTV.column('two',width=200)


    itemsTV.heading('#0',text="Item Index")
    itemsTV.heading('one',text="Item Name")
    itemsTV.heading('two',text="Cost")

    previous_menu = itemsTV.get_children()

    for element in previous_menu:
        itemsTV.delete(element)
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("select * from menu")
    menu = cursor.fetchall()
    for ind,n in enumerate(menu):
        index,name,cost=n
        itemsTV.insert("",index,text=index,values=(name,cost))
        
    conn.close()

#=================GST-Window======================#
def gstWindow():
    dateLabel = ttk.Label(window,text="Date :- ",font="Arial 15")
    dateLabel.grid(row=0,column=0)

    date = ttk.Label(window,text = today,font="Arial 15")
    date.grid(row=0,column=1)

    back_button_gstWindow = ttk.Button(window,text="Back to Menu",width=30,command=lambda:go_to_managerWindow())
    back_button_gstWindow.grid(row=0,column=7,columnspan=2,padx=(500,0),pady=(25,0))

    refresh_button_gstWindow = ttk.Button(window,text="Refresh",width=20,command=lambda:to_refresh_gstWindow())
    refresh_button_gstWindow.grid(row=2,column=7,padx=(430,0))
    
    cgst_label = ttk.Label(window,text="CGST In Value (%) :- ",font="Arial 18")
    cgst_label.grid(row=2,column=2,columnspan=4,padx=(150,0),pady=(190,0))

    cgst_entry = ttk.Entry(window,textvariable=cgstVar,width=50,font="Arial 15")
    cgst_entry.grid(row=2,column=4,columnspan=4,padx=(200,0),pady=(190,0))

    cgstVar.set(CGST_value_database)
    sgst_label = ttk.Label(window,text="SGST In Value (%) :- ",font="Arial 18")
    sgst_label.grid(row=4,column=2,columnspan=4,padx=(150,0),pady=(50,0))

    sgstVar.set(SGST_value_database)
    sgst_entry = ttk.Entry(window,textvariable=sgstVar,width=50,font="Arial 15")
    sgst_entry.grid(row=4,column=4,columnspan=4,padx=(200,0),pady=(50,0))

    tgst_label = ttk.Label(window,text="Total GST In Value (%) :- ",font="Arial 18")
    tgst_label.grid(row=6,column=2,columnspan=4,padx=(120,0),pady=(50,0))

    tgstVar.set(TGST_value_database)
    tgst_entry = ttk.Entry(window,textvariable=tgstVar,width=50,font="Arial 15",state="readonly")
    tgst_entry.grid(row=6,column=4,columnspan=4,padx=(200,0),pady=(50,0))

    upgrade_button_gstWindow = ttk.Button(window,text="UPGRADE The GST Info",width=130,command=lambda:to_upgrade_gstWindow())
    upgrade_button_gstWindow.grid(row=7,column=2,columnspan=6,pady=(60,0),padx=(50,0))

    
#================Setting-Window===================#
def settingWindow():
    dateLabel = ttk.Label(window,text="Date :- ",font="Arial 15")
    dateLabel.grid(row=0,column=0)

    date = ttk.Label(window,text = today,font="Arial 15")
    date.grid(row=0,column=1)

    back_button_gstWindow = ttk.Button(window,text="Back to Menu",width=30,command=lambda:go_to_managerWindow())
    back_button_gstWindow.grid(row=0,column=7,columnspan=2,padx=(0,0),pady=(25,0))

    refresh_button_gstWindow = ttk.Button(window,text="Refresh",width=20,command=lambda:to_refresh_settingWindow())
    refresh_button_gstWindow.grid(row=2,column=7,padx=(0,0))

    logininfo_label_settingWindow = ttk.Label(window,text="Login Info :- ",font="Arial 20")
    logininfo_label_settingWindow.grid(row=2,column=1,padx=(10,0),pady=(70,0))

    managerinfo_label_settingWindow = ttk.Label(window,text="Manager Info :- ",font="Arial 17")
    managerinfo_label_settingWindow.grid(row=3,column=1,padx=(10,0),pady=(10,0))

    manager_username_label_settingWindow = ttk.Label(window,text="Username :- ",font="Arial 15")
    manager_username_label_settingWindow.grid(row=4,column=1,padx=(10,0),pady=(10,0))

    managerusernameVar.set(manager_username_database)
    manager_username_entry_settingWindow = ttk.Entry(window,textvariable=managerusernameVar,width=30,font="Arial 15")
    manager_username_entry_settingWindow.grid(row=4,column=2,padx=(0,0),pady=(20,0))

    manager_password_label_settingWindow = ttk.Label(window,text="Password :- ",font="Arial 15")
    manager_password_label_settingWindow.grid(row=5,column=1,padx=(10,0),pady=(10,0))

    managerifo_update_button = ttk.Button(window,text="Update Manager Info",width=80,command=lambda:upgrade_manager_info())
    managerifo_update_button.grid(row=6,column=1,columnspan=2,padx=(30,0),pady=(30,0))

    managerpasswordVar.set(manager_password_database)
    manager_password_entry_settingWindow = ttk.Entry(window,textvariable=managerpasswordVar,width=30,font="Arial 15")
    manager_password_entry_settingWindow.grid(row=5,column=2,padx=(0,0),pady=(20,0))

    waiterinfo_label_settingWindow = ttk.Label(window,text="Waiter Info :- ",font="Arial 17")
    waiterinfo_label_settingWindow.grid(row=3,column=4,padx=(90,0),pady=(10,0))

    waiter_username_label_settingWindow = ttk.Label(window,text="Username :- ",font="Arial 15")
    waiter_username_label_settingWindow.grid(row=4,column=4,padx=(100,0),pady=(10,0))

    waiterusernameVar.set(waiter_username_database)
    waiter_username_entry_settingWindow = ttk.Entry(window,textvariable=waiterusernameVar,width=30,font="Arial 15")
    waiter_username_entry_settingWindow.grid(row=4,column=6,padx=(0,0),pady=(20,0))

    waiter_password_label_settingWindow = ttk.Label(window,text="Password :- ",font="Arial 15")
    waiter_password_label_settingWindow.grid(row=5,column=4,padx=(100,0),pady=(10,0))

    waiterpasswordVar.set(waiter_password_database)
    waiter_password_entry_settingWindow = ttk.Entry(window,textvariable=waiterpasswordVar,width=30,font="Arial 15")
    waiter_password_entry_settingWindow.grid(row=5,column=6,padx=(0,0),pady=(20,0))

    waiterifo_update_button = ttk.Button(window,text="Update Waiter Info",width=80,command=lambda:upgrade_waiter_info())
    waiterifo_update_button.grid(row=6,column=4,columnspan=3,padx=(100,0),pady=(30,0))

    app_setting_label = ttk.Label(window,text="App Settings :- ",font="Arial 18")
    app_setting_label.grid(row=7,column=1,pady=(50,0))

    reset_app_label = ttk.Label(window,text="1] To Reset App :- ",font="Arial 15")
    reset_app_label.grid(row=8,column=1,columnspan=3,padx=(0,140),pady=(20,0))

    reset_app_button = ttk.Button(window,text="Reset App",width=30,command=lambda:reset_app())
    reset_app_button.grid(row=8,column=3,padx=(00,0),pady=(20,0))

    delete_all_menu_label = ttk.Label(window,text="2] To Delete All Menu From App :- ",font="Arial 15")
    delete_all_menu_label.grid(row=9,column=1,columnspan=3,padx=(0,0),pady=(20,0))

    delete_all_menu_button = ttk.Button(window,text="Delete Menu",width=30,command=lambda:delete_all_menu())
    delete_all_menu_button.grid(row=9,column=3,padx=(00,0),pady=(20,0))

    delete_all_summary_label = ttk.Label(window,text="3] To Delete All Summary :- ",font="Arial 15")
    delete_all_summary_label.grid(row=10,column=1,columnspan=3,padx=(0,60),pady=(20,0))

    delete_all_summary_button = ttk.Button(window,text="Delete Summary",width=30,command=lambda:delete_all_summary())
    delete_all_summary_button.grid(row=10,column=3,padx=(0,0),pady=(20,0))

#=======================Summary-Window====================#
def summaryWindow():
    dateLabel = ttk.Label(window,text="Date :- ",font="Arial 15")
    dateLabel.grid(row=0,column=0)

    date = ttk.Label(window,text = today,font="Arial 15")
    date.grid(row=0,column=1)

    back_button_gstWindow = ttk.Button(window,text="Back to Menu",width=30,command=lambda:go_to_managerWindow())
    back_button_gstWindow.grid(row=0,column=9,padx=(20,0),pady=(25,0))

    summary_label = ttk.Label(window,text="Summary Info",font="Arial 25")
    summary_label.grid(row=1,column=1,columnspan=6,pady=(25,25))

    refresh_button_gstWindow = ttk.Button(window,text="Refresh",width=20,command=lambda:go_to_summaryWindow())
    refresh_button_gstWindow.grid(row=2,column=8,padx=(25,0))

    From_label = ttk.Label(window,text="From :- ",font="Arial 20")
    From_label.grid(row=2,column=0,padx=(50,0),pady=(0,10))

    From_year_label = ttk.Label(window,text="Year :- ",font="Arial 18")
    From_year_label.grid(row=3,column=0,padx=(50,0),pady=(5,5))

    FromYearVar.set("")
    From_year_entry = ttk.Entry(window,textvariable=FromYearVar,font="Arial 13")
    From_year_entry.grid(row=3,column=1,pady=(5,5))

    From_month_label = ttk.Label(window,text="Month :-  ",font="Arial 18")
    From_month_label.grid(row=4,column=0,padx=(50,0),pady=(5,5))

    month_list = ['All','January','February','March','April','May','June','July','August','September','October','November','December']
    From_Month.set(month_list[0])
    From_month_entry = ttk.OptionMenu(window,From_Month,*month_list)
    From_month_entry.grid(row=4,column=1,pady=(5,5))

    From_date_label = ttk.Label(window,text="Date :- ",font="Arial 18")
    From_date_label.grid(row=5,column=0,padx=(50,0),pady=(5,5))

    FromDateVar.set("")
    From_date_entry = ttk.Entry(window,textvariable=FromDateVar,font="Arial 13")
    From_date_entry.grid(row=5,column=1,pady=(5,5))

    To_label = ttk.Label(window,text="To :- ",font="Arial 20")
    To_label.grid(row=2,column=2,padx=(10,0),pady=(0,10))

    To_year_label = ttk.Label(window,text="Year :- ",font="Arial 18")
    To_year_label.grid(row=3,column=2,padx=(10,0),pady=(5,5))

    ToYearVar.set("")
    To_year_entry = ttk.Entry(window,textvariable=ToYearVar,font="Arial 13")
    To_year_entry.grid(row=3,column=3,pady=(5,5))

    To_month_label = ttk.Label(window,text="Month :-  ",font="Arial 18")
    To_month_label.grid(row=4,column=2,padx=(10,0),pady=(5,5))

    To_Month.set(month_list[0])
    To_month_entry = ttk.OptionMenu(window,To_Month,*month_list)
    To_month_entry.grid(row=4,column=3,pady=(5,5))

    To_date_label = ttk.Label(window,text="Date :- ",font="Arial 18")
    To_date_label.grid(row=5,column=2,padx=(10,0),pady=(5,5))

    FromDateVar.set("")
    To_date_entry = ttk.Entry(window,textvariable=ToDateVar,font="Arial 13")
    To_date_entry.grid(row=5,column=3,pady=(5,5))

    get_summary_button = ttk.Button(window,text="Get Summary",width=130,command=lambda:get_summary())
    get_summary_button.grid(row=7,column=0,columnspan=7,pady=(30,20),padx=(50,0))

    summaryTV.grid(row=8, column=0,columnspan=7,rowspan=8,pady=(0,0),padx=(50,0))

    scrollBar = ttk.Scrollbar(window, orient="vertical",command=summaryTV.yview)
    scrollBar.grid(row=8, column=6, sticky="NSE",rowspan=9)

    summaryTV.configure(yscrollcommand=scrollBar.set)

    summaryTV["columns"] = ("Date","Table Number","Sub Total","CGST","SGST","TGST","Total Amount")
    summaryTV.column('#0',width=75)
    summaryTV.column('Date',width=120)
    summaryTV.column('Table Number',width=110)
    summaryTV.column('Sub Total',width=110)
    summaryTV.column('CGST',width=90)
    summaryTV.column('SGST',width=90)
    summaryTV.column('TGST',width=90)
    summaryTV.column('Total Amount',width=140)

    summaryTV.heading('#0',text="Index")
    summaryTV.heading('Date',text="Date")
    summaryTV.heading('Table Number',text="Table Number")
    summaryTV.heading('Sub Total',text="Sub Total")
    summaryTV.heading('CGST',text="Central-GST")
    summaryTV.heading('SGST',text="State-GST")
    summaryTV.heading('TGST',text="Total GST")
    summaryTV.heading('Total Amount',text="Total Amount")

    cgst_label = ttk.Label(window,text="Central-GST Amount :- ",font="Arial 16")
    cgst_label.grid(row=8,column=8,pady=(10,10),padx=(30,0))

    cgst_label_val = ttk.Label(window,textvariable=CGSTinSummaryVar,font="Arial 15")
    cgst_label_val.grid(row=8,column=9,pady=(10,10))

    sgst_label = ttk.Label(window,text="State-GST Amount :- ",font="Arial 16")
    sgst_label.grid(row=9,column=8,pady=(10,10),padx=(30,0))

    sgst_label_val = ttk.Label(window,textvariable=SGSTinSummaryVar,font="Arial 15")
    sgst_label_val.grid(row=9,column=9,pady=(10,10))

    tgst_label = ttk.Label(window,text="Total-GST Amount :- ",font="Arial 16")
    tgst_label.grid(row=10,column=8,pady=(10,10),padx=(30,0))

    tgst_label_val = ttk.Label(window,textvariable=TGSTinSummaryVar,font="Arial 15")
    tgst_label_val.grid(row=10,column=9,pady=(10,10))

    subtotal_label = ttk.Label(window,text="Total Summary(Without GST) :- ",font="Arial 16")
    subtotal_label.grid(row=11,column=8,pady=(10,10),padx=(30,0))

    subtotal_label_val = ttk.Label(window,textvariable=SubTotalinSummaryVar,font="Arial 15")
    subtotal_label_val.grid(row=11,column=9,pady=(10,10))

    total_label = ttk.Label(window,text="Total Summary(With GST) :- ",font="Arial 16")
    total_label.grid(row=12,column=8,pady=(10,10),padx=(30,0))

    total_label_val = ttk.Label(window,textvariable=TotalinSummaryVar,font="Arial 15")
    total_label_val.grid(row=12,column=9,pady=(10,10))
    
    sgst_summary = 0
    cgst_summary = 0
    tgst_summary = 0
    subtotal_summary = 0
    total_summary = 0
    previous_menu = summaryTV.get_children()

    for element in previous_menu:
        summaryTV.delete(element)
        
    conn = mysql.connect(host="localhost",user="root",passwd="",db="elm")
    cursor = conn.cursor()
    cursor.execute("select * from summary")
    menu = cursor.fetchall()
    idx = 1
    for n in menu:
        index,date,day,month,year,tableno,totalamount,cgst,sgst,tgst,subtotal = n    
        summaryTV.insert("",idx,text=idx,values=(date,tableno,subtotal,cgst,sgst,tgst,totalamount))
        idx = idx +1
        sgst_summary = sgst_summary + sgst
        cgst_summary = cgst_summary + cgst
        tgst_summary = tgst_summary + tgst
        subtotal_summary = subtotal_summary + subtotal
        total_summary = total_summary + totalamount
    conn.close()

    CGSTinSummaryVar.set(round(cgst_summary,2))
    SGSTinSummaryVar.set(round(sgst_summary,2))
    TGSTinSummaryVar.set(round(tgst_summary,2))
    SubTotalinSummaryVar.set(round(subtotal_summary,2))
    TotalinSummaryVar.set(round(total_summary,2))
                  
  
loginWindow()
#go_to_summaryWindow()
#go_to_settingWindow()
window.mainloop()
