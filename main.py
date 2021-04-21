from tkinter import *
from tkinter import messagebox
import random
from tkinter import filedialog
import sqlite3
import matplotlib.pyplot as plt
from pandas import *
from numpy import *
import webbrowser



root = Tk()
root.title("Angaar's Simple Chemistry App v1.0")
df = read_csv("Periodic.csv")

# superscript and subscript code
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

#first part of app (information about elements)

# Making a drop down menu
element_list = df["Element"]
#dropdown boxes
options = element_list

# mass to mole frac and vice versa


def mass_or_mole_frac_window():
    top = Toplevel()
    top.title("Mass/Mole fraction conversion")
    Label(top, text = "Welcome. \n This app will let you convert between mass or molar fractions, for a mixture of up to 4 compounds that you define. \n Firstly, define your mass/molar basis using the dropdown menu on the right. If you do not have a mass/molar basis, please specify 100g or 100mol.\n NOTE: If you have less than 5 elements in a compound, choose any element in the remaining slot(s) and define the number of atoms as 0. You must specify at least two compounds. ").grid(column=0, row=0, columnspan =4,pady =25)

    def mass_or_mole_basis_unit(self):
        # This function determines what unit (grams or mol) is used for the mole/mass basis label at the top. Note .lower() method requires you to specify self as an argument.
        global mom_basis_unit, entry_basis
        if clicked1x.get() == "Mass Fraction":
            mom_basis_unit = "grams"
        else:
            mom_basis_unit = "mol"
        Label(top, text = "Please specify a " + clicked1x.get()[0:5].lower() + "basis in " + mom_basis_unit, pady =25).grid(column=7, row = 0)
        entry_basis = Entry(top)
        entry_basis.grid(column =8, row = 0) # generally good practice to apply grid on different line for an entry, otherwise you'll get a nonetype error when calling entry.get()

        # DELETE IF NOT NEEDED checkbox for setting mole or mass basis
        var_entry = IntVar()  # or int because its either a 0 or a 1 when you check a box
        #c_box_basis = Checkbutton(top, text="Selected all elements for Compound 1?", variable=var1, command=all_selected1)
       # c_box_basis.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
        #c_box_basis.grid(column=5, row=3)

    # Starting with mass or mole fractions?
    Label(top, text="Are you starting with mass or mole fractions?").grid(column=5, row=0)
    mass_or_mole_frac = ["Mole Fraction", "Mass Fraction", "Select"]
    clicked1x = StringVar()
    clicked1x.set(mass_or_mole_frac[2])
    drop = OptionMenu(top, clicked1x, *mass_or_mole_frac, command=mass_or_mole_basis_unit)
    drop.grid(column=6, row=0)

    # Compound 1, element 1

    Label(top, text= "Define First Element:").grid(column=0, row=2)
    options = element_list
    clicked11 = StringVar() # 11 indicates compound 1, element 1
    clicked11.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked11, *options)  # the star allows list to work
    drop.grid(column=0, row=3)

    # Compound 1, element 2
    Label(top, text="Define Second Element:").grid(column=1, row=2)
    options = element_list
    clicked12 = StringVar()
    clicked12.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked12, *options)  # the star allows list to work
    drop.grid(column=1, row=3)

    # Compound 1, element 3
    Label(top, text="Define Third Element:").grid(column=2, row=2)
    options = element_list
    clicked13 = StringVar()
    clicked13.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked13, *options)  # the star allows list to work
    drop.grid(column=2, row=3)

    # Compound 1, element 4
    Label(top, text="Define Fourth Element:").grid(column=3, row=2)
    options = element_list
    clicked14 = StringVar()
    clicked14.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked14, *options)  # the star allows list to work
    drop.grid(column=3, row=3)

    # Compound 1, element 5
    Label(top, text="Define Fifth Element:").grid(column=4, row=2)
    options = element_list
    clicked15 = StringVar()
    clicked15.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked15, *options)  # the star allows list to work
    drop.grid(column=4, row=3)


    def lock_in_compound1():
        global number_of_atoms_1, number_of_atoms_pre, data_atom_11, data_atom_12, data_atom_13, data_atom_14, data_atom_15, compound1_Label, compound1_name_str
        number_of_atoms_pre = [Entry11.get(), Entry12.get(), Entry13.get(), Entry14.get(), Entry15.get()]
        number_of_atoms_1 = [ ]
        for i in number_of_atoms_pre:
            number_of_atoms_1 += i.translate(SUB) # this turns all numbers of atoms into subscripts
        mom_frac_1 = Entrymom.get()
        data_atom_11 = df.loc[df.Element == clicked11.get()]
        data_atom_12 = df.loc[df.Element == clicked12.get()]
        data_atom_13 = df.loc[df.Element == clicked13.get()]
        data_atom_14 = df.loc[df.Element == clicked14.get()]
        data_atom_15 = df.loc[df.Element == clicked15.get()]
        symbol_atom_11 = data_atom_11.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_12 = data_atom_12.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_13 = data_atom_13.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_14 = data_atom_14.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_15 = data_atom_15.loc[:, "Symbol"].to_string(index=False)
        compound1_name_str = str(symbol_atom_11 + number_of_atoms_1[0] + symbol_atom_12 + number_of_atoms_1[1] + symbol_atom_13 + number_of_atoms_1[2] + symbol_atom_14 + number_of_atoms_1[3] + symbol_atom_15 + number_of_atoms_1[4])
        compound1_Label = Label(top, text = "Compound 1 confirmed as: " + symbol_atom_11 + number_of_atoms_1[0] + symbol_atom_12 + number_of_atoms_1[1] + symbol_atom_13 + number_of_atoms_1[2] + symbol_atom_14 + number_of_atoms_1[3] + symbol_atom_15 + number_of_atoms_1[4] + " with a " + clicked1x.get() + " of " + mom_frac_1).grid(column=6, row=8)

    def all_selected1():
        global compound_1
        compound_1 = [clicked11.get(), clicked12.get(), clicked13.get(), clicked14.get(), clicked15.get()]
        # Define number of atoms of each element and mass/mole frac for compound 1
        Label(top, text="How many atoms of " + compound_1[0] + "?").grid(column=6, row=1)
        Label(top, text="How many atoms of " + compound_1[1] + "?").grid(column=6, row=2)
        Label(top, text="How many atoms of " + compound_1[2] + "?").grid(column=6, row=3)
        Label(top, text="How many atoms of " + compound_1[3] + "?").grid(column=6, row=4)
        Label(top, text="How many atoms of " + compound_1[4] + "?").grid(column=6, row=5)
        Label(top, text= clicked1x.get() + " of compound? [0-1]").grid(column =6, row =6)
        global Entry11, Entry12, Entry13, Entry14, Entry15, Entrymom
        Entry11 = Entry(top)
        Entry11.grid(column =7, row =1)
        Entry12 = Entry(top)
        Entry12.grid(column=7, row=2)
        Entry13 = Entry(top)
        Entry13.grid(column=7, row=3)
        Entry14 = Entry(top)
        Entry14.grid(column=7, row=4)
        Entry15 = Entry(top)
        Entry15.grid(column=7, row=5)
        Entrymom = Entry(top)
        Entrymom.grid(column=7, row =6)
        Final_button1 = Button(top, text="Click when finished", command=lock_in_compound1).grid(column=7, row=7)

    # checkbox for updating number of atoms
    var1 = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box = Checkbutton(top, text="Selected all elements for Compound 1?", variable=var1, command = all_selected1)
    c_box.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
    c_box.grid(column=5, row=3)

    # REPEAT, BUT FOR COMPOUND 2

    # Compound 2, element 1

    Label(top, text="Define First Element:").grid(column=0, row=9)
    options = element_list
    clicked21 = StringVar()  # 11 indicates compound 1, element 1
    clicked21.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked21, *options)  # the star allows list to work
    drop.grid(column=0, row=10)

    # Compound 2, element 2
    Label(top, text="Define Second Element:").grid(column=1, row=9)
    options = element_list
    clicked22 = StringVar()
    clicked22.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked22, *options)  # the star allows list to work
    drop.grid(column=1, row=10)

    # Compound 2, element 3
    Label(top, text="Define Third Element:").grid(column=2, row=9)
    options = element_list
    clicked23 = StringVar()
    clicked23.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked23, *options)  # the star allows list to work
    drop.grid(column=2, row=10)

    # Compound 2, element 4
    Label(top, text="Define Fourth Element:").grid(column=3, row=9)
    options = element_list
    clicked24 = StringVar()
    clicked24.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked24, *options)  # the star allows list to work
    drop.grid(column=3, row=10)

    # Compound 2, element 5
    Label(top, text="Define Fifth Element:").grid(column=4, row=9)
    options = element_list
    clicked25 = StringVar()
    clicked25.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked25, *options)  # the star allows list to work
    drop.grid(column=4, row=10)

    def lock_in_compound2():
        global number_of_atoms_2, number_of_atoms_pre2, data_atom_21, data_atom_22, data_atom_23, data_atom_24, data_atom_25, compound2_Label, compound2_name_str
        number_of_atoms_pre2 = [Entry21.get(), Entry22.get(), Entry23.get(), Entry24.get(), Entry25.get()]
        number_of_atoms_2 = []
        for i in number_of_atoms_pre2:
            number_of_atoms_2 += i.translate(SUB)  # this turns all numbers of atoms into subscripts
        mom_frac_2 = Entrymom2.get()
        data_atom_21 = df.loc[df.Element == clicked21.get()]
        data_atom_22 = df.loc[df.Element == clicked22.get()]
        data_atom_23 = df.loc[df.Element == clicked23.get()]
        data_atom_24 = df.loc[df.Element == clicked24.get()]
        data_atom_25 = df.loc[df.Element == clicked25.get()]
        symbol_atom_21 = data_atom_21.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_22 = data_atom_22.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_23 = data_atom_23.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_24 = data_atom_24.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_25 = data_atom_25.loc[:, "Symbol"].to_string(index=False)
        compound2_name_str = str(symbol_atom_21 + number_of_atoms_2[0] + symbol_atom_22 + number_of_atoms_2[1] + symbol_atom_23 + number_of_atoms_2[2] + symbol_atom_24 + number_of_atoms_2[3] + symbol_atom_25 + number_of_atoms_2[4])
        compound2_Label = Label(top, text="Compound 2 confirmed as: " + symbol_atom_21 + number_of_atoms_2[
            0] + symbol_atom_22 + number_of_atoms_2[1] + symbol_atom_23 + number_of_atoms_2[2] + symbol_atom_24 +
                                          number_of_atoms_2[3] + symbol_atom_25 + number_of_atoms_2[
                                              4] + " with a " + clicked1x.get() + " of " + mom_frac_2).grid(column=6,
                                                                                                            row=16)

    def all_selected2():
        global compound_2
        compound_2 = [clicked21.get(), clicked22.get(), clicked23.get(), clicked24.get(), clicked25.get()]
        # Define number of atoms of each element and mass/mole frac for compound 1
        Label(top, text="How many atoms of " + compound_2[0] + "?").grid(column=6, row=9)
        Label(top, text="How many atoms of " + compound_2[1] + "?").grid(column=6, row=10)
        Label(top, text="How many atoms of " + compound_2[2] + "?").grid(column=6, row=11)
        Label(top, text="How many atoms of " + compound_2[3] + "?").grid(column=6, row=12)
        Label(top, text="How many atoms of " + compound_2[4] + "?").grid(column=6, row=13)
        Label(top, text=clicked1x.get() + " of compound? [0-1]").grid(column=6, row=14)
        global Entry21, Entry22, Entry23, Entry24, Entry25, Entrymom2
        Entry21 = Entry(top)
        Entry21.grid(column=7, row=9)
        Entry22 = Entry(top)
        Entry22.grid(column=7, row=10)
        Entry23 = Entry(top)
        Entry23.grid(column=7, row=11)
        Entry24 = Entry(top)
        Entry24.grid(column=7, row=12)
        Entry25 = Entry(top)
        Entry25.grid(column=7, row=13)
        Entrymom2 = Entry(top)
        Entrymom2.grid(column=7, row=14)
        Final_button2 = Button(top, text="Click when finished", command=lock_in_compound2).grid(column=7, row=15)

    # checkbox for updating number of atoms
    var2 = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box2 = Checkbutton(top, text="Selected all elements for Compound 2?", variable=var2, command=all_selected2)
    c_box2.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
    c_box2.grid(column=5, row=10)


    # REPEAT, BUT FOR COMPOUND 3

    # Compound 3, element 1

    Label(top, text="Define First Element:").grid(column=0, row=17)
    options = element_list
    clicked31 = StringVar()  # 11 indicates compound 1, element 1
    clicked31.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked31, *options)  # the star allows list to work
    drop.grid(column=0, row=18)

    # Compound 3, element 2
    Label(top, text="Define Second Element:").grid(column=1, row=17)
    options = element_list
    clicked32 = StringVar()
    clicked32.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked32, *options)  # the star allows list to work
    drop.grid(column=1, row=18)

    # Compound 3, element 3
    Label(top, text="Define Third Element:").grid(column=2, row=17)
    options = element_list
    clicked33 = StringVar()
    clicked33.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked33, *options)  # the star allows list to work
    drop.grid(column=2, row=18)

    # Compound 3, element 4
    Label(top, text="Define Fourth Element:").grid(column=3, row=17)
    options = element_list
    clicked34 = StringVar()
    clicked34.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked34, *options)  # the star allows list to work
    drop.grid(column=3, row=18)

    # Compound 3, element 5
    Label(top, text="Define Fifth Element:").grid(column=4, row=17)
    options = element_list
    clicked35 = StringVar()
    clicked35.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked35, *options)  # the star allows list to work
    drop.grid(column=4, row=18)

    def lock_in_compound3():
        global number_of_atoms_3, number_of_atoms_pre3, data_atom_31, data_atom_32, data_atom_33, data_atom_34, data_atom_35, compound3_Label, compound3_name_str
        number_of_atoms_pre3 = [Entry31.get(), Entry32.get(), Entry33.get(), Entry34.get(), Entry35.get()]
        number_of_atoms_3 = []
        for i in number_of_atoms_pre3:
            number_of_atoms_3 += i.translate(SUB)  # this turns all numbers of atoms into subscripts
        mom_frac_3 = Entrymom3.get()
        data_atom_31 = df.loc[df.Element == clicked21.get()]
        data_atom_32 = df.loc[df.Element == clicked22.get()]
        data_atom_33 = df.loc[df.Element == clicked23.get()]
        data_atom_34 = df.loc[df.Element == clicked24.get()]
        data_atom_35 = df.loc[df.Element == clicked25.get()]
        symbol_atom_31 = data_atom_31.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_32 = data_atom_32.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_33 = data_atom_33.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_34 = data_atom_34.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_35 = data_atom_35.loc[:, "Symbol"].to_string(index=False)
        compound3_name_str = str(symbol_atom_31 + number_of_atoms_3[0] + symbol_atom_32 + number_of_atoms_3[1] + symbol_atom_33 + number_of_atoms_3[2] + symbol_atom_34 + number_of_atoms_3[3] + symbol_atom_35 + number_of_atoms_3[4])
        compound3_Label = Label(top, text="Compound 3 confirmed as: " + symbol_atom_31 + number_of_atoms_3[
            0] + symbol_atom_32 + number_of_atoms_3[1] + symbol_atom_33 + number_of_atoms_3[2] + symbol_atom_34 +
                                          number_of_atoms_3[3] + symbol_atom_35 + number_of_atoms_3[
                                              4] + " with a " + clicked1x.get() + " of " + mom_frac_3).grid(column=6,
                                                                                                            row=24)

    def all_selected3():
        global compound_3
        compound_3 = [clicked31.get(), clicked32.get(), clicked33.get(), clicked34.get(), clicked35.get()]
        # Define number of atoms of each element and mass/mole frac for compound 1
        Label(top, text="How many atoms of " + compound_3[0] + "?").grid(column=6, row=17)
        Label(top, text="How many atoms of " + compound_3[1] + "?").grid(column=6, row=18)
        Label(top, text="How many atoms of " + compound_3[2] + "?").grid(column=6, row=19)
        Label(top, text="How many atoms of " + compound_3[3] + "?").grid(column=6, row=20)
        Label(top, text="How many atoms of " + compound_3[4] + "?").grid(column=6, row=21)
        Label(top, text=clicked1x.get() + " of compound? [0-1]").grid(column=6, row=22)
        global Entry31, Entry32, Entry33, Entry34, Entry35, Entrymom3
        Entry31 = Entry(top)
        Entry31.grid(column=7, row=17)
        Entry32 = Entry(top)
        Entry32.grid(column=7, row=18)
        Entry33 = Entry(top)
        Entry33.grid(column=7, row=19)
        Entry34 = Entry(top)
        Entry34.grid(column=7, row=20)
        Entry35 = Entry(top)
        Entry35.grid(column=7, row=21)
        Entrymom3 = Entry(top)
        Entrymom3.grid(column=7, row=22)
        Final_button3 = Button(top, text="Click when finished", command=lock_in_compound3).grid(column=7, row=23)

    # checkbox for updating number of atoms
    var3 = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box3 = Checkbutton(top, text="Selected all elements for Compound 3?", variable=var3, command=all_selected3)
    c_box3.deselect()  # if you don't do this, then the box will be checked by default, tkinter bug
    c_box3.grid(column=5, row=18)


    # checkbox for selecting no third compound
    varnc3 = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box_nc3 = Checkbutton(top, text="I don't want to specify Compound 3", variable=varnc3)
    c_box_nc3.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
    c_box_nc3.grid(column=5, row=19)

    # checkbox for selecting no fourth compound
    varnc4 = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box_nc4 = Checkbutton(top, text="I don't want to specify Compound 4", variable=varnc4)
    c_box_nc4.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
    c_box_nc4.grid(column=5, row=26)

    # REPEAT, BUT FOR COMPOUND 4

    # Compound 4, element 1

    Label(top, text="Define First Element:").grid(column=0, row=25)
    options = element_list
    clicked41 = StringVar()  # 11 indicates compound 1, element 1
    clicked41.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked41, *options)  # the star allows list to work
    drop.grid(column=0, row=26)

    # Compound 4, element 2
    Label(top, text="Define Second Element:").grid(column=1, row=25)
    options = element_list
    clicked42 = StringVar()
    clicked42.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked42, *options)  # the star allows list to work
    drop.grid(column=1, row=26)

    # Compound 4, element 3
    Label(top, text="Define Third Element:").grid(column=2, row=25)
    options = element_list
    clicked43 = StringVar()
    clicked43.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked43, *options)  # the star allows list to work
    drop.grid(column=2, row=26)

    # Compound 4, element 4
    Label(top, text="Define Fourth Element:").grid(column=3, row=25)
    options = element_list
    clicked44 = StringVar()
    clicked44.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked44, *options)  # the star allows list to work
    drop.grid(column=3, row=26)

    # Compound 4, element 5
    Label(top, text="Define Fifth Element:").grid(column=4, row=25)
    options = element_list
    clicked45 = StringVar()
    clicked45.set(options[0])  # selects default value
    drop = OptionMenu(top, clicked45, *options)  # the star allows list to work
    drop.grid(column=4, row=26)

    def lock_in_compound4():
        global number_of_atoms_4, number_of_atoms_pre4, data_atom_41, data_atom_42, data_atom_43, data_atom_44, data_atom_45, compound4_Label, compound4_name_str
        number_of_atoms_pre4 = [Entry41.get(), Entry42.get(), Entry43.get(), Entry44.get(), Entry45.get()]
        number_of_atoms_4 = []
        for i in number_of_atoms_pre4:
            number_of_atoms_4 += i.translate(SUB)  # this turns all numbers of atoms into subscripts
        mom_frac_4 = Entrymom4.get()
        data_atom_41 = df.loc[df.Element == clicked41.get()]
        data_atom_42 = df.loc[df.Element == clicked42.get()]
        data_atom_43 = df.loc[df.Element == clicked43.get()]
        data_atom_44 = df.loc[df.Element == clicked44.get()]
        data_atom_45 = df.loc[df.Element == clicked45.get()]
        symbol_atom_41 = data_atom_41.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_42 = data_atom_42.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_43 = data_atom_43.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_44 = data_atom_44.loc[:, "Symbol"].to_string(index=False)
        symbol_atom_45 = data_atom_45.loc[:, "Symbol"].to_string(index=False)
        compound4_name_str = str(symbol_atom_41 + number_of_atoms_4[0] + symbol_atom_42 + number_of_atoms_4[1] + symbol_atom_43 + number_of_atoms_4[2] + symbol_atom_44 + number_of_atoms_4[3] + symbol_atom_45 + number_of_atoms_4[4])
        compound4_Label = Label(top, text="Compound 4 confirmed as: " + symbol_atom_41 + number_of_atoms_4[
            0] + symbol_atom_42 + number_of_atoms_4[1] + symbol_atom_43 + number_of_atoms_4[2] + symbol_atom_44 +
                                          number_of_atoms_4[3] + symbol_atom_45 + number_of_atoms_4[
                                              4] + " with a " + clicked1x.get() + " of " + mom_frac_4).grid(column=6,
                                                                                                            row=32)
    def all_selected4():
        global compound_4
        compound_4 = [clicked41.get(), clicked42.get(), clicked43.get(), clicked44.get(), clicked45.get()]
        # Define number of atoms of each element and mass/mole frac for compound 1
        Label(top, text="How many atoms of " + compound_4[0] + "?").grid(column=6, row=25)
        Label(top, text="How many atoms of " + compound_4[1] + "?").grid(column=6, row=26)
        Label(top, text="How many atoms of " + compound_4[2] + "?").grid(column=6, row=27)
        Label(top, text="How many atoms of " + compound_4[3] + "?").grid(column=6, row=28)
        Label(top, text="How many atoms of " + compound_4[4] + "?").grid(column=6, row=29)
        Label(top, text=clicked1x.get() + " of compound? [0-1]").grid(column=6, row=30)
        global Entry41, Entry42, Entry43, Entry44, Entry45, Entrymom4
        Entry41 = Entry(top)
        Entry41.grid(column=7, row=25)
        Entry42 = Entry(top)
        Entry42.grid(column=7, row=26)
        Entry43 = Entry(top)
        Entry43.grid(column=7, row=27)
        Entry44 = Entry(top)
        Entry44.grid(column=7, row=28)
        Entry45 = Entry(top)
        Entry45.grid(column=7, row=29)
        Entrymom4 = Entry(top)
        Entrymom4.grid(column=7, row=30)
        Final_button4 = Button(top, text="Click when finished", command=lock_in_compound4).grid(column=7, row=31)

    # checkbox for updating number of atoms
    var4 = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box4 = Checkbutton(top, text="Selected all elements for Compound 4?", variable=var4, command=all_selected4)
    c_box4.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
    c_box4.grid(column=5, row=25)




    def mass_or_mole_want():
        # note this function chooses opposite of starting choice, as the user wants it converted.
        if clicked1x.get() == mass_or_mole_frac[1]:
            return mass_or_mole_frac[0]
        else:
            return mass_or_mole_frac[1]
    # Finally, lets actually do the mass/mole fraction conversions.
    # moles to mass first:

    def mass_mole_calc():
        last_label = Label(top, text= mass_or_mole_want() + "s of each compound are: ").grid(column=0, row=32)
        if clicked1x.get() == "Mass Fraction":
            if varnc4.get() and varnc3.get() == 1:
                atomic_mass_elements_compound_1 = [float(data_atom_11.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_12.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_13.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_14.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_15.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_1 = atomic_mass_elements_compound_1[0]*float(number_of_atoms_pre[0])+atomic_mass_elements_compound_1[1]*float(number_of_atoms_pre[1])+atomic_mass_elements_compound_1[2]*float(number_of_atoms_pre[2])+atomic_mass_elements_compound_1[3]*float(number_of_atoms_pre[3])+atomic_mass_elements_compound_1[4]*float(number_of_atoms_pre[4])
                atomic_mass_elements_compound_2 = [float(data_atom_21.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_22.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_23.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_24.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_25.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_2 = atomic_mass_elements_compound_2[0]*float(number_of_atoms_pre2[0])+atomic_mass_elements_compound_2[1]*float(number_of_atoms_pre2[1])+atomic_mass_elements_compound_2[2]*float(number_of_atoms_pre2[2])+atomic_mass_elements_compound_2[3]*float(number_of_atoms_pre2[3])+atomic_mass_elements_compound_2[4]*float(number_of_atoms_pre2[4])
                compound_1_mass_calc = float(Entrymom.get())*float(entry_basis.get())/atomic_mass_compound_1
                compound_2_mass_calc = float(Entrymom2.get())*float(entry_basis.get())/atomic_mass_compound_2
                total_mass = compound_1_mass_calc + compound_2_mass_calc
                compound_1_mass_frac_calc = compound_1_mass_calc/total_mass *100
                compound_2_mass_frac_calc = compound_2_mass_calc/total_mass *100
                massfrac1_label = Label(top, text = "Mass fraction of compound 1, " + compound1_name_str + " = " + str(compound_1_mass_frac_calc) + "%").grid(column = 0, row = 34)
                massfrac2_label = Label(top,text="Mass fraction of compound 2, " + compound2_name_str + " = " + str(compound_2_mass_frac_calc) + "%").grid(column = 0, row = 36)
                plt.pie([compound_1_mass_frac_calc, compound_2_mass_frac_calc], labels = [compound1_name_str, compound2_name_str], autopct = "%.2f %%")
                plt.title(mass_or_mole_want() + " distribution for the chosen chemical mixture")
                plt.show()
            elif varnc4.get() == 1:
                atomic_mass_elements_compound_1 = [float(data_atom_11.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_12.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_13.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_14.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_15.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_1 = atomic_mass_elements_compound_1[0] * float(number_of_atoms_pre[0]) + \
                                     atomic_mass_elements_compound_1[1] * float(number_of_atoms_pre[1]) + \
                                     atomic_mass_elements_compound_1[2] * float(number_of_atoms_pre[2]) + \
                                     atomic_mass_elements_compound_1[3] * float(number_of_atoms_pre[3]) + \
                                     atomic_mass_elements_compound_1[4] * float(number_of_atoms_pre[4])
                atomic_mass_elements_compound_2 = [float(data_atom_21.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_22.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_23.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_24.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_25.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_2 = atomic_mass_elements_compound_2[0] * float(number_of_atoms_pre2[0]) + \
                                     atomic_mass_elements_compound_2[1] * float(number_of_atoms_pre2[1]) + \
                                     atomic_mass_elements_compound_2[2] * float(number_of_atoms_pre2[2]) + \
                                     atomic_mass_elements_compound_2[3] * float(number_of_atoms_pre2[3]) + \
                                     atomic_mass_elements_compound_2[4] * float(number_of_atoms_pre2[4])
                atomic_mass_elements_compound_3 = [float(data_atom_31.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_32.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_33.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_34.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_35.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_3 = atomic_mass_elements_compound_3[0] * float(number_of_atoms_pre3[0]) + \
                                     atomic_mass_elements_compound_3[1] * float(number_of_atoms_pre3[1]) + \
                                     atomic_mass_elements_compound_3[2] * float(number_of_atoms_pre3[2]) + \
                                     atomic_mass_elements_compound_3[3] * float(number_of_atoms_pre3[3]) + \
                                     atomic_mass_elements_compound_3[4] * float(number_of_atoms_pre3[4])
                compound_1_mass_calc = float(Entrymom.get())*float(entry_basis.get())/atomic_mass_compound_1
                compound_2_mass_calc = float(Entrymom2.get())*float(entry_basis.get())/atomic_mass_compound_2
                compound_3_mass_calc = float(Entrymom3.get())*float(entry_basis.get())/atomic_mass_compound_3
                total_mass = compound_1_mass_calc + compound_2_mass_calc + compound_3_mass_calc
                compound_1_mass_frac_calc = compound_1_mass_calc/total_mass *100
                compound_2_mass_frac_calc = compound_2_mass_calc/total_mass *100
                compound_3_mass_frac_calc = compound_3_mass_calc/total_mass *100
                massfrac1_label = Label(top, text = "Mass fraction of compound 1, " + compound1_name_str + " = " + str(compound_1_mass_frac_calc) + "%").grid(column = 0, row = 34)
                massfrac2_label = Label(top,text="Mass fraction of compound 2, " + compound2_name_str + " = " + str(compound_2_mass_frac_calc) + "%").grid(column = 0, row = 36)
                massfrac3_label = Label(top,text="Mass fraction of compound 3, " + compound3_name_str + " = " + str(compound_3_mass_frac_calc) + "%").grid(column = 0, row = 38)
                plt.pie([compound_1_mass_frac_calc, compound_2_mass_frac_calc, compound_3_mass_frac_calc],
                        labels=[compound1_name_str, compound2_name_str, compound3_name_str], autopct="%.2f %%")
                plt.title(mass_or_mole_want() + " distribution for the chosen chemical mixture")
                plt.show()
            else:
                atomic_mass_elements_compound_1 = [float(data_atom_11.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_12.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_13.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_14.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_15.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_1 = atomic_mass_elements_compound_1[0]*float(number_of_atoms_pre[0])+atomic_mass_elements_compound_1[1]*float(number_of_atoms_pre[1])+atomic_mass_elements_compound_1[2]*float(number_of_atoms_pre[2])+atomic_mass_elements_compound_1[3]*float(number_of_atoms_pre[3])+atomic_mass_elements_compound_1[4]*float(number_of_atoms_pre[4])
                atomic_mass_elements_compound_2 = [float(data_atom_21.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_22.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_23.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_24.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_25.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_2 = atomic_mass_elements_compound_2[0]*float(number_of_atoms_pre2[0])+atomic_mass_elements_compound_2[1]*float(number_of_atoms_pre2[1])+atomic_mass_elements_compound_2[2]*float(number_of_atoms_pre2[2])+atomic_mass_elements_compound_2[3]*float(number_of_atoms_pre2[3])+atomic_mass_elements_compound_2[4]*float(number_of_atoms_pre2[4])
                atomic_mass_elements_compound_3 = [float(data_atom_31.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_32.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_33.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_34.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_35.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_3 = atomic_mass_elements_compound_3[0]*float(number_of_atoms_pre3[0])+atomic_mass_elements_compound_3[1]*float(number_of_atoms_pre3[1])+atomic_mass_elements_compound_3[2]*float(number_of_atoms_pre3[2])+atomic_mass_elements_compound_3[3]*float(number_of_atoms_pre3[3])+atomic_mass_elements_compound_3[4]*float(number_of_atoms_pre3[4])
                atomic_mass_elements_compound_4 = [float(data_atom_41.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_42.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_43.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_44.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_45.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_4 = atomic_mass_elements_compound_4[0]*float(number_of_atoms_pre4[0])+atomic_mass_elements_compound_4[1]*float(number_of_atoms_pre4[1])+atomic_mass_elements_compound_4[2]*float(number_of_atoms_pre4[2])+atomic_mass_elements_compound_4[3]*float(number_of_atoms_pre4[3])+atomic_mass_elements_compound_4[4]*float(number_of_atoms_pre4[4])
                compound_1_mass_calc = float(Entrymom.get())*float(entry_basis.get())/atomic_mass_compound_1
                compound_2_mass_calc = float(Entrymom2.get())*float(entry_basis.get())/atomic_mass_compound_2
                compound_3_mass_calc = float(Entrymom3.get())*float(entry_basis.get())/atomic_mass_compound_3
                compound_4_mass_calc = float(Entrymom4.get())*float(entry_basis.get())/atomic_mass_compound_4
                total_mass = compound_1_mass_calc + compound_2_mass_calc + compound_3_mass_calc + compound_4_mass_calc
                compound_1_mass_frac_calc = compound_1_mass_calc/total_mass *100
                compound_2_mass_frac_calc = compound_2_mass_calc/total_mass *100
                compound_3_mass_frac_calc = compound_3_mass_calc/total_mass *100
                compound_4_mass_frac_calc = compound_4_mass_calc/total_mass *100
                massfrac1_label = Label(top, text = "Mass fraction of compound 1, " + compound1_name_str + " = " + str(compound_1_mass_frac_calc) + "%").grid(column = 0, row = 34)
                massfrac2_label = Label(top,text="Mass fraction of compound 2, " + compound2_name_str + " = " + str(compound_2_mass_frac_calc) + "%").grid(column = 0, row = 36)
                massfrac3_label = Label(top,text="Mass fraction of compound 3, " + compound3_name_str + " = " + str(compound_3_mass_frac_calc) + "%").grid(column = 0, row = 38)
                massfrac4_label = Label(top,text="Mass fraction of compound 4, " + compound4_name_str + " = " + str(compound_4_mass_frac_calc) + "%").grid(column = 0, row = 40)
                plt.pie([compound_1_mass_frac_calc, compound_2_mass_frac_calc, compound_3_mass_frac_calc, compound_4_mass_frac_calc],
                        labels=[compound1_name_str, compound2_name_str, compound3_name_str, compound4_name_str], autopct="%.2f %%")
                plt.title(mass_or_mole_want() + " distribution for the chosen chemical mixture")
                plt.show()
        else: # now lets do mass fraction to mole fraction calcs
            if varnc4.get() and varnc3.get() == 1:
                atomic_mass_elements_compound_1 = [float(data_atom_11.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_12.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_13.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_14.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_15.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_1 = atomic_mass_elements_compound_1[0]*float(number_of_atoms_pre[0])+atomic_mass_elements_compound_1[1]*float(number_of_atoms_pre[1])+atomic_mass_elements_compound_1[2]*float(number_of_atoms_pre[2])+atomic_mass_elements_compound_1[3]*float(number_of_atoms_pre[3])+atomic_mass_elements_compound_1[4]*float(number_of_atoms_pre[4])
                atomic_mass_elements_compound_2 = [float(data_atom_21.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_22.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_23.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_24.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_25.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_2 = atomic_mass_elements_compound_2[0]*float(number_of_atoms_pre2[0])+atomic_mass_elements_compound_2[1]*float(number_of_atoms_pre2[1])+atomic_mass_elements_compound_2[2]*float(number_of_atoms_pre2[2])+atomic_mass_elements_compound_2[3]*float(number_of_atoms_pre2[3])+atomic_mass_elements_compound_2[4]*float(number_of_atoms_pre2[4])
                compound_1_moles_calc = float(Entrymom.get())*float(entry_basis.get())*atomic_mass_compound_1
                compound_2_moles_calc = float(Entrymom2.get())*float(entry_basis.get())*atomic_mass_compound_2
                total_moles = compound_1_moles_calc + compound_2_moles_calc
                compound_1_moles_frac_calc = compound_1_moles_calc/total_moles *100
                compound_2_moles_frac_calc = compound_2_moles_calc/total_moles *100
                molefrac1_label = Label(top, text = "Mole fraction of compound 1, " + compound1_name_str + " = " + str(compound_1_moles_frac_calc) + "%").grid(column = 0, row = 34)
                molefrac2_label = Label(top,text="Mole fraction of compound 2, " + compound2_name_str + " = " + str(compound_2_moles_frac_calc) + "%").grid(column = 0, row = 36)
                plt.pie([compound_1_moles_frac_calc, compound_2_moles_frac_calc],
                        labels=[compound1_name_str, compound2_name_str], autopct="%.2f %%")
                plt.title(mass_or_mole_want() + " distribution for the chosen chemical mixture")
                plt.show()
            elif varnc4.get() == 1:
                atomic_mass_elements_compound_1 = [float(data_atom_11.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_12.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_13.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_14.loc[:, "AtomicMass"].to_string(index=False)),
                                                       float(data_atom_15.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_1 = atomic_mass_elements_compound_1[0] * float(number_of_atoms_pre[0]) + \
                                     atomic_mass_elements_compound_1[1] * float(number_of_atoms_pre[1]) + \
                                     atomic_mass_elements_compound_1[2] * float(number_of_atoms_pre[2]) + \
                                     atomic_mass_elements_compound_1[3] * float(number_of_atoms_pre[3]) + \
                                     atomic_mass_elements_compound_1[4] * float(number_of_atoms_pre[4])
                atomic_mass_elements_compound_2 = [float(data_atom_21.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_22.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_23.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_24.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_25.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_2 = atomic_mass_elements_compound_2[0] * float(number_of_atoms_pre2[0]) + \
                                     atomic_mass_elements_compound_2[1] * float(number_of_atoms_pre2[1]) + \
                                     atomic_mass_elements_compound_2[2] * float(number_of_atoms_pre2[2]) + \
                                     atomic_mass_elements_compound_2[3] * float(number_of_atoms_pre2[3]) + \
                                     atomic_mass_elements_compound_2[4] * float(number_of_atoms_pre2[4])
                atomic_mass_elements_compound_3 = [float(data_atom_31.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_32.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_33.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_34.loc[:, "AtomicMass"].to_string(index=False)),
                                               float(data_atom_35.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_3 = atomic_mass_elements_compound_3[0] * float(number_of_atoms_pre3[0]) + \
                                     atomic_mass_elements_compound_3[1] * float(number_of_atoms_pre3[1]) + \
                                     atomic_mass_elements_compound_3[2] * float(number_of_atoms_pre3[2]) + \
                                     atomic_mass_elements_compound_3[3] * float(number_of_atoms_pre3[3]) + \
                                     atomic_mass_elements_compound_3[4] * float(number_of_atoms_pre3[4])
                compound_1_moles_calc = float(Entrymom.get())*float(entry_basis.get())*atomic_mass_compound_1
                compound_2_moles_calc = float(Entrymom2.get())*float(entry_basis.get())*atomic_mass_compound_2
                compound_3_moles_calc = float(Entrymom3.get())*float(entry_basis.get())*atomic_mass_compound_3
                total_moles = compound_1_moles_calc + compound_2_moles_calc + compound_3_moles_calc
                compound_1_moles_frac_calc = compound_1_moles_calc/total_moles *100
                compound_2_moles_frac_calc = compound_2_moles_calc/total_moles *100
                compound_3_moles_frac_calc = compound_3_moles_calc/total_moles *100
                molefrac1_label = Label(top,text = "Mole fraction of compound 1, " + compound1_name_str + " = " + str(compound_1_moles_frac_calc) + "%").grid(column = 0, row = 34)
                molefrac2_label = Label(top,text="Mole fraction of compound 2, " + compound2_name_str + " = " + str(compound_2_moles_frac_calc) + "%").grid(column = 0, row = 36)
                molefrac3_label = Label(top,text="Mole fraction of compound 3, " + compound3_name_str + " = " + str(compound_3_moles_frac_calc) + "%").grid(column = 0, row = 38)
                plt.pie([compound_1_moles_frac_calc, compound_2_moles_frac_calc, compound_3_moles_frac_calc],
                        labels=[compound1_name_str, compound2_name_str, compound3_name_str], autopct="%.2f %%")
                plt.title(mass_or_mole_want() + " distribution for the chosen chemical mixture")
                plt.show()
            else:
                atomic_mass_elements_compound_1 = [float(data_atom_11.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_12.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_13.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_14.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_15.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_1 = atomic_mass_elements_compound_1[0]*float(number_of_atoms_pre[0])+atomic_mass_elements_compound_1[1]*float(number_of_atoms_pre[1])+atomic_mass_elements_compound_1[2]*float(number_of_atoms_pre[2])+atomic_mass_elements_compound_1[3]*float(number_of_atoms_pre[3])+atomic_mass_elements_compound_1[4]*float(number_of_atoms_pre[4])
                atomic_mass_elements_compound_2 = [float(data_atom_21.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_22.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_23.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_24.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_25.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_2 = atomic_mass_elements_compound_2[0]*float(number_of_atoms_pre2[0])+atomic_mass_elements_compound_2[1]*float(number_of_atoms_pre2[1])+atomic_mass_elements_compound_2[2]*float(number_of_atoms_pre2[2])+atomic_mass_elements_compound_2[3]*float(number_of_atoms_pre2[3])+atomic_mass_elements_compound_2[4]*float(number_of_atoms_pre2[4])
                atomic_mass_elements_compound_3 = [float(data_atom_31.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_32.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_33.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_34.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_35.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_3 = atomic_mass_elements_compound_3[0]*float(number_of_atoms_pre3[0])+atomic_mass_elements_compound_3[1]*float(number_of_atoms_pre3[1])+atomic_mass_elements_compound_3[2]*float(number_of_atoms_pre3[2])+atomic_mass_elements_compound_3[3]*float(number_of_atoms_pre3[3])+atomic_mass_elements_compound_3[4]*float(number_of_atoms_pre3[4])
                atomic_mass_elements_compound_4 = [float(data_atom_41.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_42.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_43.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_44.loc[:, "AtomicMass"].to_string(index=False)), float(data_atom_45.loc[:, "AtomicMass"].to_string(index=False))]
                atomic_mass_compound_4 = atomic_mass_elements_compound_4[0]*float(number_of_atoms_pre4[0])+atomic_mass_elements_compound_4[1]*float(number_of_atoms_pre4[1])+atomic_mass_elements_compound_4[2]*float(number_of_atoms_pre4[2])+atomic_mass_elements_compound_4[3]*float(number_of_atoms_pre4[3])+atomic_mass_elements_compound_4[4]*float(number_of_atoms_pre4[4])
                compound_1_moles_calc = float(Entrymom.get())*entry_basis.get()*atomic_mass_compound_1
                compound_2_moles_calc = float(Entrymom2.get())*entry_basis.get()*atomic_mass_compound_2
                compound_3_moles_calc = float(Entrymom3.get())*entry_basis.get()*atomic_mass_compound_3
                compound_4_moles_calc = float(Entrymom4.get())*entry_basis.get()*atomic_mass_compound_4
                total_moles = compound_1_moles_calc + compound_2_moles_calc + compound_3_moles_calc + compound_4_moles_calc
                compound_1_moles_frac_calc = compound_1_moles_calc/total_moles *100
                compound_2_moles_frac_calc = compound_2_moles_calc/total_moles *100
                compound_3_moles_frac_calc = compound_3_moles_calc/total_moles *100
                compound_4_moles_frac_calc = compound_4_moles_calc/total_moles *100
                molefrac1_label = Label(top, text = "Mass fraction of compound 1, " + compound1_name_str + " = " + str(compound_1_moles_frac_calc) + "%").grid(column = 0, row = 34)
                molefrac2_label = Label(top,text="Mass fraction of compound 2, " + compound2_name_str + " = " + str(compound_2_moles_frac_calc) + "%").grid(column = 0, row = 36)
                molefrac3_label = Label(top,text="Mass fraction of compound 3, " + compound3_name_str + " = " + str(compound_3_moles_frac_calc) + "%").grid(column = 0, row = 38)
                molefrac4_label = Label(top,text="Mass fraction of compound 4, " + compound4_name_str + " = " + str(compound_4_moles_frac_calc) + "%").grid(column = 0, row = 40)
                plt.pie([compound_1_moles_frac_calc, compound_2_moles_frac_calc, compound_3_moles_frac_calc, compound_4_moles_frac_calc],
                        labels=[compound1_name_str, compound2_name_str, compound3_name_str, compound4_name_str], autopct="%.2f %%")
                plt.title(mass_or_mole_want() + " distribution for the chosen chemical mixture")
                plt.show()







    var = IntVar()  # or int because its either a 0 or a 1 when you check a box
    c_box5 = Checkbutton(top, text="When all compounds are defined, check this box to convert your fractions", variable=var, command=mass_mole_calc, pady = 30)
    c_box5.deselect()  # if you dont do this, then the box will be checked by default, tkinter bug
    c_box5.grid(column=0, row=33)

def visit_github():
    webbrowser.open("https://github.com/angaar96")

def open_link():
    webbrowser.open("https://gist.github.com/GoodmanSciences/c2dd862cd38f21b0ad36b8f96b4bf1ee")

label1 = Label(text = "Welcome.\n This app tells you information about the chemical elements. \n Please choose an element to get started:").grid(column=0, row =0)
label2 = Label(text = "DISCLAIMER: \n This app uses data from Goodman Sciences.").grid(column =1, row = 0)
button1 = Button(text = "Data source", command = open_link).grid(column =1, row = 1)
label3 = Label(text = "Click below to convert from mass to mole fraction and vice versa, \n for a mixture of compounds:").grid(column=2, row=0)
button2 = Button(root, text = "Mass/Mole Fraction Calculator", command = mass_or_mole_frac_window).grid(column=2, row=1)
label4 = Label(text = "Click below to visit the developers GitHub page:").grid(column=1, row = 2)
button3 = Button(text = "Github", command = visit_github).grid(column = 1, row =3)






def show_info():
    label1 = Label(text="You selected " + clicked.get() + ".").grid(column=0, row=3)
    get_data = df.loc[df.Element == clicked.get(), :]
    atomic_number = get_data.loc[:,"AtomicNumber"].to_string(index=False) # to_string gets rid of name:, datatype(e.g.float64) and the index when you output.
    chemical_symbol = get_data.loc[:, "Symbol"].to_string(index=False) # you can also use.values I think.
    atomic_mass = get_data.loc[:, "AtomicMass"].to_string(index=False)
    no_of_neutrons = get_data.loc[:, "NumberofNeutrons"].to_string(index=False)
    no_of_protons  = get_data.loc[:, "NumberofProtons"].to_string(index=False)
    no_of_electrons = get_data.loc[:, "NumberofElectrons"].to_string(index=False)
    period = get_data.loc[:, "Period"].to_string(index=False)
    group = get_data.loc[:, "Group"].to_string(index=False)
    phase = get_data.loc[:, "Phase"].to_string(index=False)
    is_it_radioactive = get_data.loc[:, "Radioactive"].to_string(index=False)
    is_it_natural = get_data.loc[:, "Natural"].to_string(index=False)
    is_it_a_metal = get_data.loc[:, "Metal"].to_string(index=False)
    is_it_a_nonmetal = get_data.loc[:, "Nonmetal"].to_string(index=False)
    is_it_a_metalloid = get_data.loc[:, "Metalloid"].to_string(index=False)
    type_of_element = get_data.loc[:, "Type"].to_string(index=False)
    atomic_radius = get_data.loc[:, "AtomicRadius"].to_string(index=False)
    electronegativity = get_data.loc[:, "Electronegativity"].to_string(index=False)
    first_ionisation_energy = get_data.loc[:, "FirstIonization"].to_string(index=False)
    density = get_data.loc[:, "Density"].to_string(index=False)
    melting_point = get_data.loc[:, "MeltingPoint"].to_string(index=False)
    boiling_point = get_data.loc[:, "BoilingPoint"].to_string(index=False)
    no_of_isotopes = get_data.loc[:, "NumberOfIsotopes"].to_string(index=False)
    discovered_by = get_data.loc[:, "Discoverer"].to_string(index=False)
    in_year = get_data.loc[:, "Year"].to_string(index=False)
    specific_heat = get_data.loc[:, "SpecificHeat"].to_string(index=False)
    no_of_shells = get_data.loc[:, "NumberofShells"].to_string(index=False)
    no_of_valence = get_data.loc[:, "NumberofValence"].to_string(index=False)
    # labels
    atomic_number_label = Label(root, text = "Atomic Number: " + atomic_number).grid(column =0, row =4)
    chemical_symbol_label = Label(root, text = "Chemical Symbol: " + chemical_symbol).grid(column =0, row =5)
    atomic_mass_label = Label(root, text = "Atomic Mass: " +  atomic_mass + " g/mol").grid(column =0, row =6)
    no_of_neutrons_label = Label(root, text = "Number of Neutrons: " + no_of_neutrons).grid(column =0, row =7)
    no_of_protons_label = Label(root, text = "Number of Protons: " + no_of_protons).grid(column =0, row =8)
    no_of_electrons_label = Label(root, text = "Number of Electrons: " + no_of_electrons).grid(column =0, row =9)
    period_label = Label(root, text = "Period: " + period).grid(column =0, row =10)
    group_label = Label(root, text = "Group: " + group).grid(column =0, row =11)
    phase_label = Label(root, text = "Phase: " + phase).grid(column =0, row =12)
    is_it_radioactive_label = Label(root, text = "Is it radioactive? : " + is_it_radioactive).grid(column =0, row =13)
    is_it_natural_label = Label(root, text = "Is it a natural element? : " + is_it_natural).grid(column =0, row =14)
    is_it_a_metal_label = Label(root, text = "Is it a metal? : " + is_it_a_metal).grid(column =0, row =15)
    is_it_a_nonmetal_label = Label(root, text = "Is it a non-metal? : " + is_it_a_nonmetal).grid(column =0, row =16)
    is_it_a_metalloid_label = Label(root, text = "Is it a metalloid? :" + is_it_a_metalloid).grid(column =0, row =17)
    type_of_element_label = Label(root, text = "Type of element: " + type_of_element).grid(column =0, row =18)
    atomic_radius_label = Label(root, text = "Atomic Radius: " + atomic_radius + " Å").grid(column =0, row =19)
    electronegativity_label = Label(root, text = "Electronegativity: " + electronegativity + " χr (Pauling Scale)").grid(column =0, row =20)
    first_ionisation_energy_label = Label(root, text = "First Ionisation Energy: " + first_ionisation_energy + " eV").grid(column =0, row =21)
    density_label = Label(root, text = "Density: " + density + " g/mL").grid(column =0, row =22)
    melting_point_label = Label(root, text = "Melting Point: " + melting_point + " K").grid(column =0, row =23)
    boiling_point_label = Label(root, text = "Boiling Point: " + boiling_point + " K").grid(column =0, row =24)
    no_of_isotopes_label = Label(root, text = "Number of Isotopes: " + no_of_isotopes).grid(column =0, row =25)
    no_of_valence_label = Label(root, text="Number of Valence: " + no_of_valence).grid(column=0, row=26)
    specific_heat_label = Label(root, text = "Specific Heat: " + specific_heat + " J/(g K)").grid(column =0, row =27)
    no_of_shells_label = Label(root, text = "Number of Shells: " + no_of_shells).grid(column =0, row =28)
    discovered_by_label = Label(root, text="This element was discovered by " + discovered_by + ", in the year " + in_year).grid(column=0, row=29)

clicked = StringVar()
clicked.set(options[0]) # selects default value
drop = OptionMenu(root, clicked, *options) # the star allows list to work
drop.grid(column = 0, row =1)
mybutton = Button(root, text = "Show element properties", command = show_info)
mybutton.grid(column = 0, row =2)

# syntax - df.loc[what rows, what column]
# df.ix[row, column]
root.mainloop()

