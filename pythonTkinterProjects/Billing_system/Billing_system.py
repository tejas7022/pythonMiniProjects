from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#00FFCE"
        title = Label(self.root, text="Billing Software ", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#00FFCE", fg="Black", relief=GROOVE)
        title.pack(fill=X)
    # ================variables=======================
        self.Gems = IntVar()
        self.Galaxy = IntVar()
        self.Kisses = IntVar()
        self.Kitkat = IntVar()
        self.Snickers = IntVar()
        self.Mars = IntVar()
    # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDtinks=============================
        self.sprite = IntVar()
        self.Limca = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_duo = IntVar()
    # ==============Total product price================
        self.choclate_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.choclate_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#00FFCE")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#00FFCE", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#00FFCE", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

    # ===================choclate====================================
        F2 = LabelFrame(self.root, text="CHOCLATES", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#00FFCE")
        F2.place(x=5, y=180, width=325, height=380)

        Gems_lbl = Label(F2, text="Gems", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        Gems_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        Gems_txt = Entry(F2, width=10, textvariable=self.Gems, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Gems_txt.grid(row=0, column=1, padx=10, pady=10)

        Galaxy_lbl = Label(F2, text="Galaxy", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        Galaxy_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Galaxy_txt = Entry(F2, width=10, textvariable=self.Galaxy, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Galaxy_txt.grid(row=1, column=1, padx=10, pady=10)

        Kisses_lbl = Label(F2, text="Kisses", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        Kisses_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        Kisses_txt = Entry(F2, width=10, textvariable=self.Kisses, font=('times new roman', 16, 'bold'), bd=5, relief =GROOVE)
        Kisses_txt.grid(row=2, column=1, padx=10, pady=10)

        Kitkat_lbl = Label(F2, text="Kitkat", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        Kitkat_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        Kitkat_txt = Entry(F2, width=10, textvariable=self.Kitkat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Kitkat_txt.grid(row=3, column=1, padx=10, pady=10)

        Snickers_lbl = Label(F2, text="Snickers", font =('times new roman', 16, 'bold'), bg = "#00FFCE", fg = "black")
        Snickers_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        Snickers_txt = Entry(F2, width=10, textvariable=self.Snickers, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Snickers_txt.grid(row=4, column=1, padx=10, pady=10)

        Mars_lbl = Label(F2, text="Mars", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        Mars_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        Mars_txt = Entry(F2, width=10, textvariable=self.Mars, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Mars_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="GROCERIES", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#00FFCE")
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="COOL DRINKS", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#00FFCE")
        F4.place(x=670, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        Limca_lbl = Label(F4, text="Limca", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        Limca_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        Limca_txt = Entry(F4, width=10, textvariable=self.Limca, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        Limca_txt.grid(row=1, column=1, padx=10, pady=10)

        mazza_lbl = Label(F4, text="Mazza", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        mazza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F4, width=10, textvariable=self.mazza, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_duo_lbl = Label(F4, text="Mountain Duo", font=('times new roman', 16, 'bold'), bg="#00FFCE", fg="black")
        mountain_duo_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_duo, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#00FFCE")
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total choclate Price", font=('times new roman', 14, 'bold'), bg="#00FFCE", fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.choclate_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#00FFCE", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#00FFCE", fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="choclate Tax", font=('times new roman', 14, 'bold'), bg="#00FFCE", fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.choclate_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#00FFCE", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#00FFCE", fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================
    def total(self):
        self.m_h_g_p = self.Kisses.get()*12
        self.m_s_p = self.Gems.get()*2
        self.m_m_p = self.Galaxy.get()*15
        self.m_d_p = self.Kitkat.get()*30
        self.m_n_p = self.Snickers.get()*25
        self.m_t_g_p = self.Mars.get()*35
        self.total_choclate_price = float(self.m_m_p+self.m_h_g_p+self.m_d_p+self.m_n_p+self.m_t_g_p+self.m_s_p)

        self.choclate_price.set("Rs. "+str(self.total_choclate_price))
        self.c_tax = round((self.total_choclate_price*0.05), 2)
        self.choclate_tax.set("Rs. "+str(self.c_tax))

        self.g_r_p = self.rice.get()*10
        self.g_f_o_p = self.food_oil.get()*10
        self.g_w_p = self.wheat.get()*10
        self.g_d_p = self.daal.get()*6
        self.g_f_p = self.flour.get()*8
        self.g_m_p = self.maggi.get()*5
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_l_p = self.Limca.get()*10
        self.c_d_m_p = self.mazza.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_f_p = self.fanta.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_choclate_price+self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome To Retail Shop")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.choclate_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
    # ============choclate===========================
        if self.Gems.get() != 0:
            self.txtarea.insert(END, f"\n Gems\t\t{self.Gems.get()}\t\t{self.m_s_p}")
        if self.Galaxy.get() != 0:
            self.txtarea.insert(END, f"\n Gems\t\t{self.Galaxy.get()}\t\t{self.m_m_p}")
        if self.Kisses.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.Kisses.get()}\t\t{self.m_h_g_p}")
        if self.Kitkat.get() != 0:
            self.txtarea.insert(END, f"\n Kitkat\t\t{self.Kitkat.get()}\t\t{self.m_d_p}")
        if self.Snickers.get() != 0:
            self.txtarea.insert(END, f"\n Snickers\t\t{self.Snickers.get()}\t\t{self.m_n_p}")
        if self.Mars.get() != 0:
            self.txtarea.insert(END , f"\n Thermal Gun\t\t{self.Gems.get()}\t\t{self.m_t_g_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.Limca.get() != 0:
            self.txtarea.insert(END, f"\n Gems\t\t{self.Limca.get()}\t\t{self.c_d_l_p}")
        if self.mazza.get() != 0:
            self.txtarea.insert(END, f"\n Mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Kitkat\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\n Fanta\t\t{self.Snickers.get()}\t\t{self.c_d_f_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.Gems.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
        if self.choclate_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n choclate Tax\t\t\t{self.choclate_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("C:/Users/Tejaswar/Desktop/bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("C:/Users/Tejaswar/Desktop/bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"C:/Users/Tejaswar/Desktop/bills/{i}", "r")
                messagebox.showinfo("Valid"," VALID BILL No")
                self.txtarea.delete("1.0", END)
                self.txtarea.insert(INSERT, f1.read())
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.Gems.set(0)
            self.Galaxy.set(0)
            self.Kisses.set(0)
            self.Kitkat.set(0)
            self.Snickers.set(0)
            self.Mars.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.Limca.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.choclate_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.choclate_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()