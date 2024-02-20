from customtkinter import *
from Global_Config import *
from subprocess import call
from PIL import Image

root = CTk()

global glb_color_1, glb_color_2, glb_color_3

glb_color_1 = "darkorchid2" # #FFC125 #FFCC70
glb_color_2 = "dodgerblue3"
glb_color_3 = "#308014" # darkorchid2, #308014 #c850c0
glb_img_btn_height, glb_img_btn_width = 10, 10

centreScreen(root, root,200,250)
root.title("Animal Taxonomy")
root.maxsize(width = 200, height = 250)

root.iconbitmap(r"icon/favicon6.ico")
set_appearance_mode("Dark")
global  glb_current_working_directory
glb_current_working_directory = os.path.dirname(os.path.realpath(__file__))

def back_to_main_console():
    root.destroy()
    call(["python", glb_current_working_directory + "/Animal_Taxonomy_CTk_Admin_Console.py"])


def Heli():
    root.destroy()
    call(["python", glb_current_working_directory + "/Helicopter.py"])

content_frame = CTkFrame(root, border_color = glb_color_1, border_width = 2, width = 200, height = 250)

img = Image.open(r"Images/" + "previous.png")
back_btn =  CTkButton(content_frame, text = "", image = CTkImage(dark_image=img, light_image=img),corner_radius = 100,
                         width=  glb_img_btn_width, height= glb_img_btn_height,state = "normal",
                           command = lambda: (back_to_main_console()))
back_btn.place(x = 5, y = 5)


Heli_btn = CTkButton(content_frame, text = "Helicopter", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                               command = lambda :(Heli()))# width = 240
Heli_btn.place(x = 30, y = 35)

content_frame.place(x = 0, y = 0)

root.mainloop()