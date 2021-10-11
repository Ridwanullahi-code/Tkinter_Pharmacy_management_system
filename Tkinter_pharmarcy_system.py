from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image


def Main_program():
	Display_root()
	project_title()
	Display_frame1()
	Display_label1()
	Display_entry1()
	Display_label2()
	Display_entry2()
	Display_image_frame()
	Display_other()
	Display_sm_treview()
	Display_button1()
	Display_button2()
	Display_Big_treeview()

def Display_root():
	global root,my_image,my_image2,my_image3,my_image4
	root = Tk()
	root.geometry("1150x530+100+120")
	root.title("Pharmacy management system")
	root.config(bg="white")

	my_image = ImageTk.PhotoImage(Image.open("image/phar_logo3.jpg"))
	my_image2 = ImageTk.PhotoImage(Image.open("image/logo2.jpg"))
	my_image3 = ImageTk.PhotoImage(Image.open("image/logo3.jpg"))
	my_image4 = ImageTk.PhotoImage(Image.open("image/logo4.jpg"))

def project_title():
	title_frame = Frame(root,bg='white',bd=5,relief=GROOVE)
	title_frame.place(x=0,y=0,width=1149,height=53)
	pro_logo = Label(title_frame,image= my_image,bg="white")
	pro_logo.place(x=225,y=0,width=100,height=40)
	title = Label(title_frame,text="PHARMACY MANAGEMENT SYSTEM",fg="#006406",bg="white",font=("times new roman",25,"bold"))
	title.place(x=300,y=0)
	
def Display_frame1():
	global sub_frame1,sub_frame2	
	frame1 = Frame(root,bg='#F0F0F0',bd=5,relief=RIDGE)
	frame1.place(x=0,y=57,width=1149,height=295)

	sub_frame1 = Frame(frame1,bg='#F0F0F0',bd=6,relief= RIDGE)
	sub_frame1.place(x=0,y=10,width=735,height=270)

	sub_frame2 = Frame(frame1,bg='#F0F0F0',bd=6,relief= RIDGE)
	sub_frame2.place(x=745,y=10,width=395,height=270)

	
def Display_label1():

		medicine_info = Label(root,text="Medicine Information",fg="#006406",bg="#F0F0F0",font=("Verdana",8,"bold"))
		medicine_info.place(x=5,y=61)

		texts = ["Reference No","Company Name","Type Of Medicine","Medicine Name","Lot No:","Issue Date","Exp Date:","Uses:","Side Effect:"]
		for n in range(len(texts)):
			label = Label(sub_frame1,text=texts[n],bg="#F0F0F0",font=("Verdana",8,"bold"))
			label.grid(column=0,row=3+n,sticky=W,pady=4)

def Display_entry1():
		refence_list = (1122,2234,5334,5545,6777,4443,7789,1235,7789)
		combo1 = ttk.Combobox(sub_frame1,values=refence_list,font=("Verdana",10,"bold"))
		combo1.set("1122")
		combo1.place(x=130,y=5,width=215)
		e1 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
		e1.place(x=130,y=31)
		med_type = ("alendronate tablet","acyclovir capsule","albuterol sulfate","alitretinoin","alprazolam")
		combo2 = ttk.Combobox(sub_frame1,values=med_type,font=("Verdana",10,"bold"))
		combo2.set("1122")
		combo2.place(x=130,y=57,width=215)
		combo3 = ttk.Combobox(sub_frame1,values=med_type,font=("Verdana",10,"bold"))
		combo3.set("1122")
		combo3.place(x=130,y=83,width=215)
		e2 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
		e2.place(x=130,y=109)
		e3 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
		e3.place(x=130,y=135)
		e4 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
		e4.place(x=130,y=161)
		e5 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
		e5.place(x=130,y=187)
		e6 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
		e6.place(x=130,y=213)

def Display_label2():
	texts2 = ["Price&Warning:","Dosage:","Tablets Price:","Product QT:"]
	l1 = Label(sub_frame1,text=texts2[0],bg="#F0F0F0",font=("Verdana",8,"bold"))
	l1.place(x=360,y=5)
	l2 = Label(sub_frame1,text=texts2[1],bg="#F0F0F0",font=("Verdana",8,"bold"))
	l2.place(x=360,y=31)
	l3 = Label(sub_frame1,text=texts2[2],bg="#F0F0F0",font=("Verdana",8,"bold"))
	l3.place(x=360,y=57)
	l4 = Label(sub_frame1,text=texts2[3],bg="#F0F0F0",font=("Verdana",8,"bold"))
	l4.place(x=360,y=83)

def Display_entry2():
	e7 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
	e7.place(x=480,y=5)
	e8 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
	e8.place(x=480,y=31)
	e9 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
	e9.place(x=480,y=57)
	e10 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=19)
	e10.place(x=480,y=83)

def Display_other():
	dept_med =Label(root,text="New Medicine Add Department",fg="#006406",bg="#F0F0F0",font=("Verdana",8,"bold"))
	dept_med.place(x=745,y=63)

	ref_no = Label(sub_frame2,text="Reference No",bg="white",font=("times new roman",12,"bold"))
	ref_no.place(x=5,y=60)
	med_name = Label(sub_frame2,text="Medicine Name",bg="white",font=("times new roman",12,"bold"))
	med_name.place(x=5,y=90)

	e11 = Entry(sub_frame2,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=10)
	e11.place(x=120,y=60)
	e12 = Entry(sub_frame2,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=10)
	e12.place(x=120,y=90)

	logo3 = Label(sub_frame2,image = my_image3,width=233,height=50)
	logo3.place(x=0,y=0)
	logo4 = Label(sub_frame2,image=my_image4,width=140,height=80)
	logo4.place(x=237,y=0)


def Display_image_frame():
	image_frame = Frame(sub_frame1,bg='white')
	image_frame.place(x=350,y=115,width=370,height=120)
	warnig_lb = Label(image_frame,text= "Stay Home Stay Safe",fg="#D30000",bg="white",font=("Verdana",12,"bold"))
	warnig_lb.place(x=90,y=2)

	logo2 = Label(image_frame,image=my_image2,width=370,height=100)
	logo2.place(x=0,y=28)
	
def Display_sm_treview():
	data = ["Reference No","Company Name","Type Of Medicine","Medicine Name","Lot No",
				"Issue Date","Exp Date","Uses","Side Effect","Price&Warning","Dosage"
				,"Tablets Price","Product QT"]
	column_no = list(range(len(data)))

	small_frame =  Frame(sub_frame2,bg='white',bd=2,relief=GROOVE)
	small_frame.place(x=5,y=120,width=235,height=119)

	x_scrollbar = Scrollbar(small_frame,orient=HORIZONTAL)
	y_scrollbar = Scrollbar(small_frame,orient=VERTICAL)
	x_scrollbar.pack(side=BOTTOM,fill="x")
	y_scrollbar.pack(side=RIGHT,fill="y")

	style = ttk.Style()
	style.configure("Treeview.Heading",font=("Verdana",10,"bold"))
	sm_treeview = ttk.Treeview(small_frame, columns=column_no,
			 xscrollcommand = x_scrollbar.set, yscrollcommand= y_scrollbar.set,show="headings")
	x_scrollbar.configure(command= sm_treeview.xview)
	y_scrollbar.configure(command= sm_treeview.yview)

	for col in range(len(column_no)):
		sm_treeview.column(column_no[col],width=125,anchor=CENTER)
		sm_treeview.heading(column_no[col], text = data[col])

	sm_treeview.pack(fill=BOTH)

def Display_button1():
	button_frame = Frame(sub_frame2,bg="#026302",bd=4,relief= RIDGE)
	button_frame.place(x=250,y=112,width=120,height=143)

	add_button = Button(button_frame,text="ADD",fg="white",bg="#00FF01",font=("Verdana",12,"bold"))
	add_button.place(x=2,y=2,width=112,height=30)
	update_button = Button(button_frame,text ="UPDATE",fg="white",bg="#7F0081",font=("Verdana",12,"bold"))
	update_button.place(x=2,y=35,width=112,height=30)
	del_button = Button(button_frame,text="DELETE",fg="white",bg="#D30000",font=("Verdana",12,"bold"))
	del_button.place(x=2,y=69,width=112,height=30)
	clr_button = Button(button_frame,text="CLEAR",fg="white",bg="#FDA602",font=("Verdana",12,"bold"))
	clr_button.place(x=2,y=103,width=112,height=30)

def Display_button2():
	button_frame2 = Frame(root,bg="#F0F0F0",bd=4,relief=GROOVE)
	button_frame2.place(x=0,y=353,width=1149,height=40)

	add_m_button = Button(button_frame2,text="ADD MEDICINE",fg="white",bg="#026302",font=("Roboto",11,"bold"))
	add_m_button.place(x=0,y=0,width=120,height=30)
	update_button2 = Button(button_frame2,text ="UPDATE",fg="white",bg="#026302",font=("Roboto",11,"bold"))
	update_button2.place(x=120,y=0,width=114,height=30)
	del_button2 = Button(button_frame2,text="DELETE",fg="white",bg="#D30000",font=("Roboto",11,"bold"))
	del_button2.place(x=234,y=0,width=114,height=30)
	reset_button = Button(button_frame2,text="RESET",fg="white",bg="#026302",font=("Roboto",11,"bold"))
	reset_button.place(x=348,y=0,width=114,height=30)
	exit_button = Button(button_frame2,text="EXIT",fg="white",bg="#026302",font=("Roboto",11,"bold"))
	exit_button.place(x=462,y=0,width=114,height=30)
	search_by_button = Button(button_frame2,text="Search By",fg="white",bg="#D30000",font=("Roboto",11,"bold"))
	search_by_button.place(x=576,y=0,width=112,height=30)

	combo3 = ttk.Combobox(button_frame2,values=("Ref","No"),font=("times new roman",15,"bold"))
	combo3.set("Ref")
	combo3.place(x=690,y=0,width=112,height=30)

	e12 = Entry(button_frame2,bd=3,bg='white',font= ("Roboto",11,"bold"),relief=GROOVE,width=13)
	e12.place(x=804,y=0,height=31)

	search_button = Button(button_frame2,text="SEARCH",fg="white",bg="#026302",font=("Roboto",11,"bold"))
	search_button.place(x=915,y=0,width=112,height=30)
	search_all_button = Button(button_frame2,text="SEARCH ALL",fg="white",bg="#026302",font=("Roboto",11,"bold"))
	search_all_button.place(x=1027,y=0,width=112,height=30)

def Display_Big_treeview():
	data2 = ["Reference No","Company Name","Type Of Medicine","Medicine Name","Lot No",
				"Issue Date","Exp Date","Uses","Side Effect","Price&Warning","Dosage"
				,"Tablets Price","Product QT"]
	sub_frame3 = Frame(root,bg='#F0F0F0',bd=6,relief=GROOVE)
	sub_frame3.place(x=0,y=395,width=1149,height=133)

	x_scrollbar2 = Scrollbar(sub_frame3,orient=HORIZONTAL)
	y_scrollbar2 = Scrollbar(sub_frame3,orient=VERTICAL)

	x_scrollbar2.pack(side=BOTTOM,fill="x")
	y_scrollbar2.pack(side=RIGHT,fill="y")

	big_treeview = ttk.Treeview(sub_frame3,columns=data2,show="headings",
		xscrollcommand = x_scrollbar2.set,yscrollcommand = y_scrollbar2.set)

	x_scrollbar2.configure(command=big_treeview.xview)
	y_scrollbar2.configure(command=big_treeview.yview)

	for col in range(len(data2)):
		big_treeview.column(data2[col], width=133,anchor=CENTER)
		big_treeview.heading(data2[col],text=data2[col])

	big_treeview.pack(fill=BOTH)

print(Main_program())
root.mainloop()
