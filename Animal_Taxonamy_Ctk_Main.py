from customtkinter import *
from subprocess import call
from PIL import Image
import os
import sqlite3
from tkinter import messagebox
from Global_Config import *

root = CTk()

global glb_color_1, glb_color_2, glb_color_3

glb_color_1 = "darkorchid2"# #FFC125 #FFCC70
glb_color_2 = "dodgerblue3"
glb_color_3 = "#308014"# darkorchid2, #308014 #c850c0

centreScreen(root, root,600,600)
root.title("Animal Taxonomy")
root.maxsize(width = 600, height = 600)

root.iconbitmap(r"icon/favicon6.ico")
set_appearance_mode("Dark")

con = sqlite3.connect("Animal_Taxonomy_Db.db")
cur = con.cursor()

global  glb_current_working_directory
glb_current_working_directory = os.path.dirname(os.path.realpath(__file__))

def validation():
    username = username_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
            error_label = CTkLabel(login_frame, text = "Username or password is wrong", font = ("Bradley Hand ITC" , 15, "italic", "bold"), text_color = "red")
            error_label.place(x = 75, y = 170)
            def refresh():
                error_label.destroy()
            error_label.after(3000, refresh)

        # username_entry.configure(border_color = "red")
        # password_entry.configure(border_color = "red")
    else :
        tmp_qry = "SELECT Username, Password FROM User_details WHERE Username = '"+username+"' AND Password = '"+password+"' AND Active = 1"
        cur.execute(tmp_qry) 
        row  = cur.fetchone()
        if row :
            def admin_console():
                login.destroy()
                call(["python", glb_current_working_directory + "/Animal_Taxonomy_CTk_Admin_Console.py"])
            admin_console()
        else:
            error_label = CTkLabel(login_frame, text = "Username or password is wrong", font = ("Bradley Hand ITC" , 15, "italic", "bold"), text_color = "red")
            error_label.place(x = 75, y = 170)
            def refresh():
                error_label.destroy()
            error_label.after(3000, refresh)

welcome_text = "WELCOME"

def redirect_to_user(_isadmin = False):
    if _isadmin:
        login_text = "LOGIN"
        global login
        login = CTk()
        login.iconbitmap(r"icon/favicon6.ico")
        centreScreen(login, root,400,200)
        login.title("Admin Login")
        login.maxsize(width = 400, height = 200)

        global login_frame
        login_frame = CTkFrame(login, border_color = glb_color_1, border_width = 2, width = 400, height = 200)
        login_frame.pack()

        login_label = CTkLabel(login_frame, text = login_text, font = ("Bradley Hand ITC" , 40, "italic", "bold"), text_color = glb_color_3)
        login_label.place(x = 130, y = 5)

        username_label = CTkLabel(login_frame, text = "Username :-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = glb_color_2)
        username_label.place(x = 15, y = 70)

        global username_entry
        username_entry = CTkEntry(login_frame, text_color = glb_color_3, width = 200)
        username_entry.place(x = 170, y = 70)

        password_label = CTkLabel(login_frame, text = "Password:-", font = ("Bradley Hand ITC" , 20, "italic", "bold"), text_color = glb_color_2)
        password_label.place(x = 15, y = 110)

        global password_entry
        password_entry = CTkEntry(login_frame, show = "*", text_color = glb_color_3, width = 200)
        password_entry.place(x = 170, y = 110)

        submit_btn = CTkButton(login_frame, height = 15, text = "Submit", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                               command = lambda: validation())
        submit_btn.place(x = 45, y = 150)

        def back_to_main_console():
            login.destroy()
            call(["python", glb_current_working_directory + "/Animal_Taxonamy_Ctk_Main.py"])

        cancel_btn = CTkButton(login_frame, height = 15, text = "Back", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                               command = lambda: (back_to_main_console()))
        cancel_btn.place(x = 210, y = 150)
        
        root.destroy()
        login.mainloop()
        
    else:
        def guest_console():
            root.destroy()
            call(["python", glb_current_working_directory + "/Animal_Taxonomy_CTk_Guest_Console.py"])
        guest_console()

content_frame = CTkFrame(root, border_color = glb_color_1, border_width = 2, width = 600, height = 600)

welcome_message = CTkLabel(content_frame, text = welcome_text, font = ("Brush Script MT" , 50, "italic" ))
welcome_message.place(x = (600/2-len(welcome_text)//2)-100, y = 200)

welcome_message = CTkLabel(content_frame, text = "To the world of animals", font = ("Brush Script MT" , 18, "italic" ))
welcome_message.place(x = (600/2-len(welcome_text)//2)-50, y = 280)

guest_mode_btn = CTkButton(content_frame, text = "View As A Guest...", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                               width = 240, command = lambda :(redirect_to_user()))
guest_mode_btn.place(x = 45, y = 330)

admin_mode_btn = CTkButton(content_frame, text = "View As An Admin...", fg_color = glb_color_2,hover_color = glb_color_3,corner_radius = 35,
                                width = 240,command = lambda :(redirect_to_user(True)))
admin_mode_btn.place(x = 320, y = 330)

content_frame.place(x = 0, y = 0)

root.mainloop()
