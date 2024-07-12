from customtkinter import *
from Global_Config import *
import Password_Hasher as PH



global  glb_current_working_directory
glb_current_working_directory = os.path.dirname(os.path.realpath(__file__))

root = CTk()

global glb_color_1, glb_color_2, glb_color_3

glb_color_1 = "darkorchid2"# #FFC125 #FFCC70
glb_color_2 = "dodgerblue3"
glb_color_3 = "#308014"# darkorchid2, #308014 #c850c0

app_width = 600
app_height = 300

centreScreen(root, root,app_width,app_height)
root.title("Animal Taxonomy")
root.maxsize(width = app_width, height = app_height)

#root.iconbitmap(r"icon/favicon6.ico")
set_appearance_mode("Dark")

#=-=-=-=-=-=-=-=-==-=-=

def createRadioButton (_frame ,_text , _value, _variable, _command,  _xpos, _ypos ):
    tmpRdBtn = CTkRadioButton(_frame, text = _text , value = _value, variable = _variable, command = lambda :(_command()) )
    tmpRdBtn.place(x =_xpos, y = _ypos)
    return tmpRdBtn



def createSearchButton(_frame, _command, _ishomepage = False):
    if _ishomepage :
        tmp_Search_Btn = CTkButton(_frame, text = "SEARCH", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                                command = lambda :(_command()))
        tmp_Search_Btn.place(x = 60, y = 130)
        return tmp_Search_Btn
    else:
        tmp_Search_Btn = CTkButton(_frame, text = "SEARCH", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                                command = lambda :(_command()))
        tmp_Search_Btn.place(x = 240, y = 185)
        return tmp_Search_Btn

#=-=-=-=-=-=-=-=-==-=-=

content_frame = CTkFrame(root, border_color = glb_color_1, border_width = 2, width = app_width, height = app_height)
content_frame.place(x = 0, y = 0)

welcome_message = CTkLabel(content_frame, text = "En & De Crypt", font = ("Brush Script MT" , 50, "italic" ))
welcome_message.place(x = (600/2-len("En & De Crypt")//2)-120, y = 10)


def radio_value():
    pass

home_radio_val = StringVar(value = "other")

search_name_btn = createRadioButton (content_frame , "Encrypt", "en", home_radio_val, radio_value, 10, 100 )

search_kingdom_btn = createRadioButton (content_frame ,"Decrypt", "de" , home_radio_val, radio_value, 86, 100)



label = CTkLabel(content_frame, text = "What to En (or) De Crypt :-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = glb_color_2)
label.place(x = 5, y = 130)

entry = CTkEntry(content_frame, text_color = glb_color_3, width = 300)
entry.place(x = 270, y = 130)


result_frame = CTkFrame(root, border_color = glb_color_1, border_width = 2, width = 200, height =40)
result_frame.place(x = 220, y = 230)


label = CTkLabel(result_frame, text ="Result : ", font = ("Arial" , 14, "italic" ), text_color = "Red")
label.place(x = 250, y = 230)

def on_btn_click():
    tosearch = ((entry.get()))
    if home_radio_val.get() == "en":
        enc = PH.Encrypter(tosearch).encrypt()
        
        for reslabel in result_frame.winfo_children():
            reslabel.destroy()
            
        reslabel = CTkLabel(result_frame, text = enc, font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
        reslabel.place(x = 300, y = 230)
        
    if home_radio_val.get() == "de":
        enc = PH.Encrypter(tosearch).decrypt()
        
        for reslabel in result_frame.winfo_children():
            reslabel.destroy()
            
        reslabel = CTkLabel(result_frame, text = enc, font = ("Arial" , 14, "italic" ), text_color = glb_color_1)
        reslabel.place(x = 300, y = 230)
        


search_btn = createSearchButton(content_frame, on_btn_click)

root.mainloop()