from unstructured.partition.pdf import partition_pdf
from langchain.schema import Document
import logging

logger = logging.getLogger(__name__)


def unstructured_pdf_process(file):
    """
    Process the file with 'Unstructured.io' functionality. Attempt to use Unstrucutured and if unsucessful,
    (ie: the PDF is not machine-readable), then return None, so that the next flow will send the file to 
    the EasyOCR function for processing. If successful return a langchain Document.

    Args: 
        `file` (str) - the file to be processed, likely a PDF.

    Returns: 
        `Document` - a Langchain document instance containing content and metadata or None if processing fails.
    """
    try:
        elements = partition_pdf(filename=file)
        text = "\n\n".join([str(item) for item in elements])

        return Document(page_content=text, metadata={"source": file})
    except Exception as e:
        logger.error(f"Unstructured failed to process the {file} : {e}")
        return None
    