import customtkinter as ctk
from services import easyOCR, unstructuredio
from tkinter import filedialog
from PIL import Image, ImageTk
from pdf2image import convert_from_path
import os
import magic
from modules import db
from tkinter import messagebox


def save_document_and_confirmation(document):
    global documents
    db.documents.append(document)
    print('document added')
    print(db.documents)
    messagebox.showinfo("Save Confirmation", "Document Saved!")




def check_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    return file_type

def select_files(app):
    """
    Opens a file dialog to select a file, processes the file, and updates the UI with its contents.

    Allows the user to select a file via a file dialog window. Then checks if the file exists, 
    clears the current UI content, performs OCR (using easyOCR) on the selected file, and displays the results 
    in the UI. The function also loads and displays the image using Pillow, updating various UI components 
    with the new content and providing an option to save the processed data.

    Args: None: This function does not take any direct arguments but interacts with the application's UI.

    Returns: None: The function does not return any value but updates the application's UI with the selected 
        file's information, including file existence, image display, and OCR results.
    """
    app.update() # Force UI to refresh and handle events

    # app.select_files_button.focus_set() #focus on the select_button
    file_path = filedialog.askopenfilename()

    if file_path:
        print(f"Selected file: {file_path}")
        # Example of using os module to perform an action with the file
        print(f"File exists: {os.path.exists(file_path)}")
        
        #clear old content from both frames
        for widget in app.frame_1.winfo_children():
            widget.destroy()
        app.doc_results_textbox.delete(1.0, "end")
        if hasattr(app, 'save_button') and app.save_button.winfo_exists():
            app.save_button.destroy()
    
        # Print file info and check if file exists
        doc_info = f"Selected file: {file_path}\n"
        doc_info += f"File exists: {os.path.exists(file_path)}\n"
        #check FILE TYPE:
        file_type = check_file_type(file_path)

        if file_type is not None and "pdf" in file_type:
            document = unstructuredio.unstructured_pdf_process(file_path)
            if document == None:
                document = easyOCR.easyOCR_pdf_process(file_path)

        elif file_type is not None and "image/png" in file_type or "image/jpeg" in file_type:
            document = easyOCR.easyOCR_image_process(file_path)  

        if document is None:
            print(f"Document processing failed or unsupported type: {file_type}")
            app.doc_results_textbox.insert("end", "Error: Document processing failed or unsupported file type.")
            raise ValueError(f"Unsupported file type: {file_type}. Please convert.") # Exit function to avoid displaying the Save button

        # display the results in a textbox:
        app.doc_results_textbox.insert("end", f"File Information:\n\n {doc_info}\n Scanned Text:\n\n {document}")

        # Load and display the image using Pillow
        try:
            image = Image.open(file_path)
            image = image.resize((400, 300))  # Resize image to fit the frame
            photo = ImageTk.PhotoImage(image)  # Convert to Tkinter-compatible image

            # Display the image in a label inside frame_1
            image_label = ctk.CTkLabel(app.frame_1, image=photo, text="")
            image_label.image = photo 
            image_label.grid(row=0, column=0, sticky="nsew")
        except Exception as e:
            print(f"error loading image: {e}")

        # Insert OCR results into the textbox
        app.save_button = ctk.CTkButton(app.frame_2, text="Save", fg_color="#ff9900", command= lambda: save_document_and_confirmation(document), text_color="black")
        app.save_button.grid(row= 1, column = 0, padx =10, pady=10,sticky='sw')
        
        return document