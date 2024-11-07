import cv2
import easyocr
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
from langchain.schema import Document
import os
import numpy as np
from typing import Optional
import logging

logger = logging.getLogger(__name__)

reader = easyocr.Reader(['en', 'fr', 'de', 'it'])

# Process PDF with easyOCR, convert pdf to image and process:
def easyOCR_pdf_process(pdf_file: str) -> Optional[Document]:
        try:
                #convert each page to image 
                pdf_pages = convert_from_path(pdf_file)
                text = ""

                for page in pdf_pages:
                        #convert PIL image to numpy array
                        page_np = np.array(page)
                        result = reader.readtext(page_np, detail=0)
                        page_text = " ".join(result)
                        text += page_text + "\n\n"       
                return Document(page_content=text, metadata={"source": pdf_file})
        except Exception as e:
                logger.error(f"EasyOCR Failed to process {pdf_file} : {e}")
                return None


# process jpg/png with easyOCR
def easyOCR_image_process(file):

    """
    Extracts text from a jpg image file using the EasyOCR library.

    This function accepts an image file (in jpg, jpeg, or png format), uses EasyOCR to read the text within the image, 
    and returns the extracted text as a string. If the file format is not supported, it returns a warning message.

    Args:
            `file` (str): The path to the image file you want to process. Must be in jpg, jpeg, or png format.

    Returns:
            str: A string containing the extracted text from the image, or a warning message if the file type is invalid.

    Raises:
            FileNotFoundError: If the specified file does not exist.
            ValueError: If the file is not in a supported format (jpg, jpeg, or png).
    """
    try:
        img = cv2.imread(file)
        results = reader.readtext(img,detail=0)
        ocr_results = " ".join(results)
        return Document(page_content=ocr_results, metadata={"source": file})

    except Exception as e:
        logger.error(f"EasyOCR failed to process {file}: {e}")
        return None





      #Check image is jpg/png if not, return error msg: 
#     _, file_extension = os.path.splitext(file)
  
#     if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
#         img = cv2.imread(file)
        # run OCR:
# results = reader.readtext(img,detail=0)
# ocr_results = " ".join(results)
# print(ocr_results)
# return ocr_results
#     else:
#         return "WARNING: File type not valid. \n\n Please convert file to jpg, jpeg, or png."