# Document Processor

Document Processor is a desktop application built with `customtkinter` to facilitate document management and interaction with an integrated AI chatbot powered by LangChain. The application allows users to select documents, process them for text extraction using OCR, and query the content interactively through a chatbot interface.


## Features

- **Document Selection and Processing**: Easily select PDF or image files, perform OCR to extract text, and view the results in the app.
- **AI Chatbot**: Interact with an AI chatbot that uses LangChain and OpenAI's GPT-3.5-turbo model to answer questions based on the content of loaded documents.
- **Save Functionality**: Save processed document text to a local database for future reference.


## Project Structure

- `main.py`: Sets up the main application layout, buttons, and user interface.
- `modules/`: Contains key modules:
  - `file_manipulation.py`: Handles file selection, OCR processing, and displays document data in the application.
  - `langchain_pipe.py`: Manages the LangChain-based chatbot interactions, handling document retrieval and querying.
- `services/`: Expected to contain OCR and document processing utilities such as `easyOCR` and `unstructuredio` for text extraction.

## Prerequisites

- Python 3.8 or higher
- Required libraries:
  - `customtkinter`: for the GUI
  - `langchain_openai`: for integrating with LangChain and OpenAI models
  - `Pillow`: for handling image display
  - `python-magic`: for checking file types
  - `dotenv`: for managing environment variables (e.g., OpenAI API keys)
