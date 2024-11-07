import customtkinter as ctk
from modules import file_manipulation, langchain_pipe
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

class Frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Document Processor")
        self.geometry("800x600")

        #Main window/Frame layout
        self.grid_rowconfigure(1, weight=1) # Allows row 1 (frames) to expand
        self.grid_columnconfigure(0, weight=1) # Allows column 0 to expand
        self.grid_columnconfigure(1, weight=1) # Allows column 1 to expand
    
        #Header Button Frame:
        self.button_frame_1= Frame(self)
        self.button_frame_1.configure(fg_color="#404040")	 
        self.button_frame_1.grid(row=0, column=0, columnspan= 2, pady=0, sticky='new')
        self.button_frame_1.grid_columnconfigure(0, weight=1)

        #Inner Header Button Frame:
        self.inner_button_frame= Frame(self.button_frame_1)
        self.inner_button_frame.configure(fg_color="#404040")	
        self.inner_button_frame.grid(row=0, column=0, columnspan= 1, sticky='w')
        self.inner_button_frame.grid_columnconfigure(0, weight=1)

        # select files button:
        self.select_files_button = ctk.CTkButton(self.inner_button_frame, text="Add Documents", command=lambda: file_manipulation.select_files(self), fg_color='#33cccc', text_color="black")
        self.select_files_button.grid(row= 0, column = 0,columnspan=1,padx= 10, pady=5,sticky='w')
        self.open_chatbot_button = ctk.CTkButton(self.inner_button_frame, text="Chat?", fg_color="#d24dff", text_color="black", command= lambda: langchain_pipe.run_chatbot())
        self.open_chatbot_button.grid(row= 0, column = 1, padx =10, pady=10,sticky='e')

        #Column Frame 1 (left):
        self.frame_1 = Frame(self)
        self.frame_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.frame_1.grid_rowconfigure(0, weight=1) # Makes content inside frame expandable
        self.frame_1.grid_columnconfigure(0, weight=1)

        #Column Frame 2 (right):
        self.frame_2 = Frame(self)
        self.frame_2.configure(fg_color="black")  
        self.frame_2.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.frame_2.grid_rowconfigure(0, weight=1)
        self.frame_2.grid_rowconfigure(1,weight=1)
        self.frame_2.grid_columnconfigure(0, weight=1)

        #Column Frame 2 TextBox:
        self.doc_results_textbox = ctk.CTkTextbox(self.frame_2)
        self.doc_results_textbox.configure(fg_color="black") 
        self.doc_results_textbox.grid(row=0, column=0, sticky="nsew")

app = App()
app.mainloop()