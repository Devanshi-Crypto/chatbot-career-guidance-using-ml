from tkinter import *
import customtkinter
from PIL import Image, ImageTk
FONT="Source Sans Pro"
FONT_BOLD = "Source Sans Pro bold"
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App:

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        self.window =Tk()
        self._setup_main_window()

    #basic run function
    def run(self):
        self.window.mainloop()
        
    #setting up the main window of GUI
    def _setup_main_window(self):
        self.window.title('Career Counselling CHATBOT')
        self.window.resizable(width=True, height=True)
        self.window.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.window.iconbitmap(r'C:\Users\USER\Downloads\bg.ico')        

        #configure grids and frames
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        #two frames
        self.frame_left = customtkinter.CTkFrame(master=self.window,width=180,corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        
        self.frame_right = customtkinter.CTkFrame(master=self.window)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
      
        #left frame
        
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        #head
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="WELCOME TO CAREER GUIDANCE CHATBOT",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        #appearance
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="APPEARANCE MODE:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["LIGHT", "DARK", "SYSTEM"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        self.optionmenu_1.set("DARK")
        
        #stream
        self.label_mode2 = customtkinter.CTkLabel(master=self.frame_left, text="SELECT YOUR CAREER STREAM:")
        self.label_mode2.grid(row=6, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["ENGINEERING SCIENCE","MEDICAL SCIENCE", "COMMERCE", "ARTS"],
                                                        command=self.select_stream)
        self.optionmenu_2.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.optionmenu_2.set("ENGINEERING SCIENCE")
        
        #right frame
        #text box
        self.text_widget=customtkinter.CTkTextbox(self.frame_right,width=20,height=2,padx=5,pady=5)
        self.text_widget.place(relheight=0.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor="arrow",state=DISABLED)
        
        #scrollbar
        scrollbar=Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        #bottomlabel
        bottom_label = Label(self.frame_right,height=80)  
        bottom_label.place(relwidth=1,rely=0.825) 
        
        #message entry  box
        self.entry = customtkinter.CTkEntry(bottom_label)
        self.entry.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
        self.entry.focus()
        self.entry.bind('<Return>',self._on_enter_pressed)
        
        #send button
        send_btn = customtkinter.CTkButton(bottom_label,text="SEND",width=20,
                          command=lambda:self._on_enter_pressed(NONE))
        send_btn.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
        
        #function for stream change
    
        
        #function for appearance
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

        #function for on press events
    def _on_enter_pressed(self,event):
        msg = self.entry.get()
        self._insert_msg(msg,"YOU")
        
        #function to insert message
    def _insert_msg(self,msg,sender):
        if not msg:
            return
        self.entry.delete(0,END)
        user = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,user)
        self.text_widget.configure(state=DISABLED)
        
        bot = f"BOT: GUI WORKING \n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,bot)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
        

        
#run application
if __name__ == '__main__':
    app = App()
    app.run()