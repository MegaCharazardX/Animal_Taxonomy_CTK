from customtkinter import *
from PIL import Image
import os 
from subprocess import call
import sqlite3
from Global_Config import *

root = CTk()

centreScreen(root, root,1000,550)
root.title("Animal Taxonomy")
root.maxsize(width = 1000, height = 550)
root.iconbitmap(r"icon/favicon6.ico")
set_appearance_mode("Dark")

con = sqlite3.connect("Animal_Taxonomy_Db.db", timeout = 3)

cur = con.cursor()

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=GLOBALS=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

global glb_top_position, \
    glb_crud_frame_width, glb_crud_frame_height, \
    glb_img_btn_height, glb_img_btn_width, \
    glb_menu_btn_ypos_space, glb_menu_btn_height, glb_menu_btn_width, glb_menu_btn_current_ypos, glb_menu_btn_font,\
    glb_home_btn_xpos, glb_img_btn_heights_space, \
    glb_fg_color_transparent,\
    border_line_size_2, glb_common_xpos, glb_current_working_directory,\
    is_add_btn_enabled, is_edit_btn_enabled, is_delete_btn_enabled, \
    glb_color_1, glb_color_2, glb_color_3, glb_after_time

# get the current working directory
glb_current_working_directory = os.path.dirname(os.path.realpath(__file__))
glb_top_position = 2
glb_crud_frame_height = 85
glb_crud_frame_width = 150
glb_img_btn_height, glb_img_btn_width = 10, 10
glb_menu_btn_ypos_space = 15
glb_menu_btn_xpos_space = 15
glb_menu_btn_height = 28
glb_menu_btn_width = 140
glb_menu_btn_current_ypos = 0
glb_menu_btn_font = ("Bradley Hand ITC" , 20, "italic", "bold" )
glb_fg_color_transparent = "transparent"
border_line_size_2 = 2
glb_common_xpos = 15
is_add_btn_enabled = "normal"
is_edit_btn_enabled = "normal" 
is_delete_btn_enabled = "normal"
glb_color_1 = "darkorchid2"# #FFC125 #FFCC70
glb_color_2 = "dodgerblue3"
glb_color_3 = "#308014"# darkorchid2, #308014 #c850c0
glb_after_time = 3000

def createFrame(_frame, _border_color, _border_width, _fg_color, _xpos = 0, _ypos = 0 , _width = 100, _height = 100, _is_content_frame = False):
    global glb_top_position
    if _is_content_frame :
        tmp_frame = CTkFrame(_frame, border_color = _border_color,  border_width= _border_width, fg_color = _fg_color, width = 820, height = 520)#
        tmp_frame.place(x = 15, y = 15)
        glb_top_position = glb_top_position + _height + 5
    else:
        tmp_frame = CTkFrame(_frame, border_color = _border_color,  border_width= _border_width, fg_color = _fg_color, width = _width, height = _height)#
        tmp_frame.place(x = _xpos, y = _ypos)
        glb_top_position = glb_top_position + _height + 5
    return tmp_frame

def createRadioButton (_frame ,_text , _value, _variable, _command,  _xpos, _ypos ):
    tmpRdBtn = CTkRadioButton(_frame, text = _text , value = _value, variable = _variable, command = lambda :(_command()) )
    tmpRdBtn.place(x =_xpos, y = _ypos)
    return tmpRdBtn

def createMenuButton (_frame, _text,  _command, _argument, _previous_control, _add_xpos = 0, _add_ypos = 0):
    global glb_menu_btn_font    
    tmp_btn = CTkButton(_frame,text = _text ,hover_color= glb_color_3, font = glb_menu_btn_font,
                         width=  glb_menu_btn_width, height= glb_menu_btn_height, command = lambda: (_command(_argument)))
    global glb_menu_btn_current_ypos 
    glb_menu_btn_current_ypos = glb_menu_btn_current_ypos + _previous_control._current_height + glb_menu_btn_ypos_space + _add_ypos
    tmp_btn.place(x = glb_menu_btn_xpos_space, y = glb_menu_btn_current_ypos)
    return tmp_btn

def createButton(_frame, _text, _corner_radius, _call_back_function, _xpos, _ypos):
    tmp_btn = CTkButton(_frame,text = _text,corner_radius = _corner_radius,hover_color = glb_color_3,
                         height= glb_img_btn_height, command = lambda: (_call_back_function()))
    tmp_btn.place(x = _xpos, y = _ypos)
    return tmp_btn

def createImageButton(_frame, _text, _image, _corner_radius, _call_back_function, _argument, _xpos, _ypos):
    img = Image.open(r"Images/" + _image)
    tmp_btn = CTkButton(_frame,text = _text, image = CTkImage(dark_image=img, light_image=img),corner_radius = _corner_radius,
                         width=  glb_img_btn_width, height= glb_img_btn_height,state = "normal",
                           command = lambda: (_call_back_function(_argument)))
    tmp_btn.place(x = _xpos, y = _ypos)
    return tmp_btn

def createSearchByLabel(_frame):
    tmp_label = CTkLabel(_frame, text = "Search by :-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = glb_color_3)
    tmp_label.place(x = glb_common_xpos, y = 70)
    return tmp_label

def createSearchResultLabel(_frame, _iskingdompage = False, _isafterclasspage = False):

    if _iskingdompage :
        tmp_label = CTkLabel(_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = glb_color_2)
        tmp_label.place(x = 15, y = 130)
        return tmp_label
    elif _isafterclasspage:
        tmp_label = CTkLabel(_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = glb_color_2)
        tmp_label.place(x = 15, y = 140)
        return tmp_label
    else :
        tmp_label = CTkLabel(_frame, text = "Search Result(s):-",font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = glb_color_2)
        tmp_label.place(x = 15, y = 160)
        return tmp_label

def createMainHeading(_frame, _text):
    tmp_heading = CTkLabel(_frame, text = _text,font = ("Bradley Hand ITC" , 50, "italic", "bold" ), fg_color = "transparent", text_color = glb_color_3)
    tmp_heading.place(x = 300, y = 5)
    return tmp_heading

def createSearchButton(_frame, _command, _ishomepage = False):
    if _ishomepage :
        tmp_Search_Btn = CTkButton(_frame, text = "SEARCH", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                                command = lambda :(_command()))
        tmp_Search_Btn.place(x = 660, y = 130)
        return tmp_Search_Btn
    else:
        tmp_Search_Btn = CTkButton(_frame, text = "SEARCH", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                                command = lambda :(_command()))
        tmp_Search_Btn.place(x = 660, y = 105)
        return tmp_Search_Btn

def createSearchEntry(_frame, _ishomepage = False):
    if _ishomepage :
        tmp_Entry = CTkEntry(_frame, width = 640, text_color = glb_color_3)
        tmp_Entry.place(x = 15, y = 130)
        return tmp_Entry
    else:
        tmp_Entry = CTkEntry(_frame, width = 640, text_color = glb_color_3)
        tmp_Entry.place(x = 15, y = 105)
        return tmp_Entry

def createScrollableFrame(_frame, _width, _height, _xpos, _ypos):
    tmp_ScrollableFrame = CTkScrollableFrame(_frame,width=_width, height=_height, border_color=glb_color_3, 
                                      border_width=2, fg_color="transparent", scrollbar_button_hover_color= glb_color_2)
    tmp_ScrollableFrame.place(x = _xpos, y = _ypos)
    return tmp_ScrollableFrame

def destroyAfterForLabel(_widget):
    _widget.configure("")

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=PAGES=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    
def home_page():
    home_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(home_frame, "HOME")

    label = createSearchByLabel(home_frame)

    global radio_value
    def radio_value():
        pass

    home_radio_val = StringVar(value = "other")

    search_name_btn = createRadioButton (home_frame , "NAME", "name", home_radio_val, radio_value, 10, 100 )

    search_kingdom_btn = createRadioButton (home_frame ,"KINGDOM", "kingdom" , home_radio_val, radio_value, 81, 100)

    search_phylum_btn = createRadioButton (home_frame ,"PHYLUM", "phylum" , home_radio_val, radio_value, 177, 100)

    search_class_btn = createRadioButton (home_frame ,"CLASS", "class" , home_radio_val, radio_value, 262, 100)

    search_order_btn = createRadioButton(home_frame ,"ORDER", "naturalorder" , home_radio_val, radio_value, 335, 100)

    search_family_btn = createRadioButton (home_frame ,"FAMILY", "family" , home_radio_val, radio_value, 415, 100)

    search_genus_btn = createRadioButton (home_frame ,"GENUS", "genus" , home_radio_val, radio_value, 495, 100)

    search_species_btn = createRadioButton (home_frame ,"SPECIES", "species" , home_radio_val, radio_value, 570, 100)

    result_frame = createScrollableFrame(home_frame, 762, 318, 15, 173)

    def on_home_search_btn_click():
        tosearch = ((search.get())).title()
        if home_radio_val.get() == "name":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  name LIKE '%"+tosearch+"%' AND active = 1"):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom") 
                

        elif home_radio_val.get() == "kingdom":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom LIKE '%"+tosearch+"%'AND active = 1"):
                label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        elif home_radio_val.get() == "phylum":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum LIKE '%"+tosearch+"%' AND active = 1"):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        elif home_radio_val.get() == "class":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class LIKE '%"+tosearch+"%' AND active = 1"):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        elif home_radio_val.get() == "naturalorder":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder LIKE '%"+tosearch+"%' AND active = 1"):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        elif home_radio_val.get() == "family":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family LIKE '%"+tosearch+"%' AND active = 1"):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        elif home_radio_val.get() == "genus":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  genus LIKE '%"+tosearch+"%'AND active = 1"):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        elif home_radio_val.get() == "species":
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  species LIKE '%"+tosearch+"%' AND active = 1"):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

    label = createSearchResultLabel(home_frame)

    search = createSearchEntry(home_frame, _ishomepage = True)

    search_btn = createSearchButton(home_frame, on_home_search_btn_click, _ishomepage = True)

def kingdom_page():

    kingdom_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(kingdom_frame, "KINGDOM")

    label = createSearchByLabel(kingdom_frame)

    result_frame = createScrollableFrame(kingdom_frame, 760, 348, 15, 143)

    def on_search_animal_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Animalia"
        
        tmp_qry = "SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom LIKE '%"+tosearch+"%' AND active = 1"
        record_set = cur.execute(tmp_qry)
        for row in record_set:
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), fg_color = "transparent", text_color = glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")

    search_animal_btn = CTkButton(kingdom_frame, text = "ANIMALS", fg_color = glb_color_2,hover_color = glb_color_3, corner_radius = 40,
                                  command = lambda:(on_search_animal_btn_click()))
    search_animal_btn.place(x = 10, y = 98)


    def on_search_plant_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Plantae"
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom LIKE '%"+tosearch+"%'AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), fg_color = "transparent", text_color = glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")

    search_plant_btn = CTkButton(kingdom_frame, text = "PLANT", fg_color = glb_color_2,hover_color = glb_color_3,  corner_radius = 40,
                                 command = lambda:(on_search_plant_btn_click()))
    search_plant_btn.place(x = 158, y = 98)


    def on_search_fungi_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Fungi"
        
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom LIKE '%"+tosearch+"%'AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), fg_color = "transparent", text_color = glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")
            

    search_fungi_btn = CTkButton(kingdom_frame, text = "FUNGI", fg_color = glb_color_2,hover_color = glb_color_3, corner_radius = 40,
                                     command = lambda:(on_search_fungi_btn_click()))
    search_fungi_btn.place(x = 305, y = 98)


    def on_search_protista_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Protista"
        
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom LIKE '%"+tosearch+"%'AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), fg_color = "transparent", text_color = glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")
            
    
    search_protista_btn = CTkButton(kingdom_frame, text = "PROTISTA", fg_color = glb_color_2,hover_color = glb_color_3, corner_radius = 40,
                                     command = lambda:(on_search_protista_btn_click()))
    search_protista_btn.place(x = 453, y = 98)


    def on_search_monera_btn_click():
        for label in result_frame.winfo_children():
            label.destroy()
        tosearch = "Monera"
        
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  kingdom LIKE '%"+tosearch+"%'AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), fg_color = "transparent", text_color = glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")
            

    search_monera_btn = CTkButton(kingdom_frame, text = "MONERA", fg_color = glb_color_2,hover_color = glb_color_3,  corner_radius = 40,
                                     command = lambda:(on_search_monera_btn_click()))
    search_monera_btn.place(x = 600, y = 98)

    label =createSearchResultLabel(kingdom_frame, _iskingdompage = True)

def phylum_page():
    global search_result_ypos 
    search_result_ypos = 160

    phylum_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(phylum_frame, "PHYLUM")

    label = createSearchByLabel(phylum_frame)

    def combo_get_value(combo_value):
        tosearch = combo_value
    
        def on_pylum_search_btn_click():
            for label in result_frame.winfo_children():
                label.destroy()
            
            for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  phylum LIKE '%"+tosearch+"%' AND active = 1 "):
                label = CTkLabel(result_frame, text = row,font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
                label.pack(padx = 10, pady = 10, side = "bottom")
                

        search_btn = CTkButton(phylum_frame, text = "SEARCH", fg_color = glb_color_2, hover_color = glb_color_3, corner_radius = 40, 
                            command = on_pylum_search_btn_click)
        search_btn.place(x = 660, y = 130)

    def radio_value():
        val_of_phylum = home_radio_val.get()
        #pass
        if val_of_phylum == "":
            label = CTkLabel(phylum_frame, text = "! Please Choose An Option !",font = ("Brush Script MT" , 15, "italic" ),
                              fg_color = "darkgrey", fg = "red")
            label.place(x = 10, y = 470)
        else:
            global phylum_value
            phylum_value = val_of_phylum
        
            if phylum_value == "Animalia":
                combo_animal_val = [ 
                "Chordata", 
                "Arthropoda", 
                "Molusca", 
                "Echinoderm", 
                "Annalida"
                ] 
                combo = CTkComboBox(phylum_frame, width = 640, values = combo_animal_val, command = combo_get_value)
                combo.set("Animalia")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Plantae":
                combo_plant_val = [  
                "Bryophyta", 
                "Cycadophyta", 
                "Ginkgophyta", 
                "Chlorophyta", 
                "Lycophyta"
                ]
                combo = CTkComboBox(phylum_frame, width = 640, values = combo_plant_val, command = combo_get_value)
                combo.set("Plantae")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Fungi":
                combo_fungi_val = [ 
                "Ascomycota", 
                "Basidiomycota", 
                "Zygomycota",
                "Microsporidia",  
                "Bigyra",
                "Aphelida",
                "Mycetozoa"
                ]
                combo = CTkComboBox(phylum_frame, width = 640, values = combo_fungi_val, command = combo_get_value)
                combo.set("Fungi")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Protista":
                combo_protista_val = [ 
                "Dinoflagellates", 
                "Amoebozoa", 
                "Rhodophyta",
                "Ciliates"  
                ] 
                combo = CTkComboBox(phylum_frame, width = 640, values = combo_protista_val, command = combo_get_value)
                combo.set("Protista")
                #combo.current()
                combo.place(x = 10, y = 130)

            elif phylum_value == "Monera": 
                combo_monera_val = [ 
                "Archaebacteria", 
                "Schizopyta", 
                "Cyanophyta",
                "Prochlorophyta"  
                ] 
                combo = CTkComboBox(phylum_frame, width = 640, values = combo_monera_val, command = combo_get_value)
                combo.set("Monera")
                #combo.current()
                combo.place(x = 10, y = 130)

    global home_radio_val
    home_radio_val = StringVar(value = "other")

    search_phylum_animal_menu =createRadioButton (phylum_frame ,"Animal", "Animalia" , home_radio_val, radio_value, 10, 100)

    search_phylum_plant_menu =createRadioButton (phylum_frame ,"Plant", "Plantae" , home_radio_val, radio_value, 85, 100)

    search_phylum_fungi_menu =createRadioButton (phylum_frame ,"Fungi", "Fungi" , home_radio_val, radio_value, 150, 100)

    search_phylum_protista_menu =createRadioButton (phylum_frame ,"Protista", "Protista" , home_radio_val, radio_value, 215, 100)

    search_phylum_monera_menu =createRadioButton (phylum_frame ,"Monera", "Monera" , home_radio_val, radio_value, 295, 100)

    result_frame = createScrollableFrame(phylum_frame, 762, 318, 15, 173)

    label = createSearchResultLabel(phylum_frame)
    
    combo = CTkComboBox(phylum_frame, width = 640)
    combo.place(x = 10, y = 130)


    global search_btn
    search_btn = CTkButton(phylum_frame, text = "SEARCH", fg_color = glb_color_2, hover_color = glb_color_3, corner_radius = 40)
    search_btn.place(x = 660, y = 130)

def class_page():

    class_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(class_frame, "CLASS")
    label = createSearchByLabel(class_frame)

    result_frame = createScrollableFrame(class_frame, 762, 335, 15, 153)

    search = createSearchEntry(class_frame)

    def on_class_search_click():
        tosearch = ((search.get())).title()
        for label in result_frame.winfo_children():
            label.destroy()
        ypos = 10
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  class LIKE '%"+tosearch+"%' "):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ), text_color = glb_color_1 )
            label.pack(padx = 10, pady = 10, side = "bottom")
            
 
    search_btn = createSearchButton(class_frame, on_class_search_click)

    label = createSearchResultLabel(class_frame, _isafterclasspage = True)

def order_page():

    order_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(order_frame, "ORDER")

    label = createSearchByLabel(order_frame)

    result_frame = createScrollableFrame(order_frame, 762, 335, 15, 153)

    search = createSearchEntry(order_frame)

    def on_order_page_search_btn_click():
        ypos = 10
        tosearch = ((search.get())).title()
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  naturalorder LIKE '%"+tosearch+"%' AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ),text_color=glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")
            
 
    search_btn = createSearchButton(order_frame, on_order_page_search_btn_click)

    label = createSearchResultLabel(order_frame, _isafterclasspage = True)

def family_page():

    family_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(family_frame, "FAMILY")

    label = createSearchByLabel(family_frame)

    search = createSearchEntry(family_frame)

    def on_family_page_search_btn_click():
        tosearch = ((search.get())).title()
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  family LIKE '%"+tosearch+"%' AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ),text_color=glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")

    result_frame = createScrollableFrame(family_frame, 762, 335, 15, 153)
    
    search_btn =createSearchButton(family_frame, on_family_page_search_btn_click)
    label = createSearchResultLabel(family_frame, _isafterclasspage = True)

def genus_page():

    genus_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(genus_frame, "GENUS")

    label = createSearchByLabel(genus_frame)

    def on_genus_search_click():
        tosearch = ((search.get())).title()
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  genus LIKE '%"+tosearch+"%' AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ),text_color=glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")
            

    search = createSearchEntry(genus_frame)
    contents = StringVar()
    contents.set("Search For Genus.")
    search["textvariable"] = contents
    
    result_frame = createScrollableFrame(genus_frame, 762, 335, 15, 153)

    search_btn = createSearchButton(genus_frame, on_genus_search_click)

    label = createSearchResultLabel(genus_frame, _isafterclasspage = True)

def species_page():
    species_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(species_frame, "SPEICES")

    label = createSearchByLabel(species_frame)

    def on_species_search_click():
        ypos = 10
        tosearch = ((search.get())).title()
        for row in cur.execute("SELECT name, kingdom, phylum, class, naturalorder, family, genus, species FROM animal_details WHERE  species LIKE '%"+tosearch+"%' AND active = 1"):
            label = CTkLabel(result_frame, text = row, font = ("Arial" , 14, "italic" ),text_color=glb_color_1)
            label.pack(padx = 10, pady = 10, side = "bottom")
            

    search = createSearchEntry(species_frame)
    contents = StringVar()
    contents.set("Search For Species.")
    search["textvariable"] = contents
    
    result_frame = createScrollableFrame(species_frame, 762, 335, 15, 153)

    search_btn =createSearchButton(species_frame, on_species_search_click)
    label = createSearchResultLabel(species_frame, _isafterclasspage = True)

def about_page():
    about_frame = createFrame(main_frame,  glb_color_2,  2, "transparent", _is_content_frame = True)

    label = createMainHeading(about_frame, "ABOUT")

    frame = createFrame(about_frame,  glb_color_3,  2, "transparent", 15, 70, 790, 436)

    label = CTkLabel(frame, text = "\
We are a group of students studying in XI std,\n\
<--CREDITS-->\n\
Ideaology       --> Hari Dhejus V.S.\n\
Cheif Devoloper --> Hari Dhejus V.S.\n\
Co-Devoloper    --> Anandha Krishnan\n\
Co-Devoloper    --> Dhana Lekshmi\n\
Chief Biologist --> Pranav Krishna Prathap\n\
Co-Biologist-1  --> Adharsh S.M.\n\
Co-Biologist2   --> Akshay Ram R.F\n\
\n\
Contact us --> +91 948 668 3398\n\
\n\
        Thank you for using this program © AnimalTaxonaomy HAPAA™", 
                        font = ("Brush Script MT" , 20, "italic" ), fg_color = "transparent", text_color = glb_color_1)
    label.place(x = 120, y = 80)


#=-=-=-=-=-=-=-EXTRA-=-=-=-=-=-=-=#

def indicate(page):
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def back_to_main_console():
    root.destroy()
    call(["python", glb_current_working_directory + "/Animal_Taxonamy_Ctk_Main.py"])

menu_frame = CTkFrame(root, fg_color = "transparent")

crud_frame = createFrame(menu_frame, "",  border_line_size_2, glb_fg_color_transparent , 5, 5, 150, glb_crud_frame_height)


img = Image.open(r"Images/" + "previous.png")
back_btn =  CTkButton(crud_frame, text = "", image = CTkImage(dark_image=img, light_image=img),corner_radius = 100,
                         width=  glb_img_btn_width, height= glb_img_btn_height,state = "normal",
                           command = lambda: (back_to_main_console()))
back_btn.place(x = 5, y = 5)

home_btn = createMenuButton(menu_frame, "Home", indicate, home_page, crud_frame)

kingdom_btn = createMenuButton(menu_frame, "Kingdom", indicate, kingdom_page, home_btn)

phylum_btn =  createMenuButton(menu_frame, "Phylum-\n-Division", indicate, phylum_page, kingdom_btn)

class_btn =  createMenuButton(menu_frame, "Class", indicate, class_page, phylum_btn, _add_ypos = 25)

order_btn =  createMenuButton(menu_frame, "Order", indicate, order_page, class_btn)

family_btn = createMenuButton(menu_frame, "Family", indicate, family_page, order_btn)

genus_btn = createMenuButton(menu_frame, "Genus", indicate, genus_page, family_btn)

species_btn = createMenuButton(menu_frame, "Species", indicate, species_page, genus_btn)

about_btn = createMenuButton(menu_frame, "About", indicate, about_page, species_btn)

menu_frame.pack(side = "left")
menu_frame.pack_propagate(False)
menu_frame.configure(width = 150, height = 550)

main_frame = createFrame(root,  glb_color_1,  3, "transparent", 0 , 0, 950, 550)
main_frame.pack(side = "left")
main_frame.pack_propagate(False)



root.mainloop()
con.close()