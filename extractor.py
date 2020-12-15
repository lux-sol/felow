 #############
## Extractor ##
 #############

from os.path import splitext
import os

from rake_nltk import Rake
import pdftotext

class Extractor(object):
    """ Creates an object for extracting text from files """
    def __init__(self):
        self.text = ""
        self.ext = ""

    def get_ext(self):
        return self.ext

    def set_ext(self, ext):
        self.ext = ext

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    #Split filepath for extension
    def split_ext(self, source):
        ext = splitext(source)[1]
        self.ext = ext

    #Extract text from source file
    def extract_text(self, source):
        temp_text = ""
        if self.ext == ".txt":
            print("extracting from .txt...")
            try:
                temp_doc = open(source, "r")
                temp_text = temp_doc.read()

            except:
                print("extraction failed")

        elif self.ext == ".docx":
            print("extracting from .docx...")
            try:
                from docx import Document
                temp_doc = Document(source)
                for prgrph in temp_doc.paragraphs:
                    for char in prgrph.text:
                        temp_text = temp_text + char
            
            except:
                print("extraction failed")

        elif self.ext == ".pdf":
            print("extracting from .pdf...")
            try:
                print("trying...")
                pdfobj = open(source, "rb")
                print("object set")
                pdf = pdftotext.PDF(pdfobj)
                print("pdf set")
                for pg in pdf:
                    temp_text = temp_text + pg

                pdf.close()


            # try:
            #     import PyPDF2
            #     pdf = open(source, "rb")
            #     reader = PyPDF2.PdfFileReader(pdf)
            #     print("reader set")
            #     pages = reader.numPages
            #     temp_text = ""
            #     for pg in range(pages):
            #         page = reader.getPage(pg)
            #         temp_text = temp_text + page.extractText()

            #     pdf.close()

            except:
                print("extraction failed")

        else:
            print("unsupported file type")

        self.text.strip()
        self.text = self.text + temp_text

    #Extract keywords from text
    def extract_kywrds(self):
        r = Rake(max_length=1)
        r.extract_keywords_from_text(self.text)
        keywords = r.get_ranked_phrases()
        return keywords

    #Strip string from collected text   
    def strip_string(self, string):
        print("stripping string...")
        temp_text = "" 
        temp_text += self.text
        if string in self.text:
            temp_text = temp_text.replace(string, "")
            self.text = temp_text
 
        else:
            print("string not found...")

    def strip_strings(self, string_list):
        for strng in string_list:
            while strng in self.text:
                self.strip_string(strng)

    #Strip slice from collected text
    def strip_slice(self, char1, char2):
        print("stripping slice...")
        temp_text = ""
        temp_text += self.text
        if char1 in temp_text:
            try:
                slice_start = temp_text.find(char1)
                slice_end = temp_text.find(char2, slice_start + 1)
                temp_text = temp_text.replace(temp_text[slice_start:slice_end + 1], "")
                
                self.text = temp_text
        
            except:
                print("slice end not found")

        else:
            print("slice start not found")

    def strip_slices(self, char1, char2):
        for char in self.text:
            if char == char1:
                self.strip_slice(char1, char2)

    #Discard collected text that appears after the given string
    def strip_page(self, string):
        print("stripping page...")
        temp_text = ""
        temp_text += self.text
        if string in temp_text:
            slice_start = temp_text.index(string)
            temp_text = temp_text[:slice_start]
            self.text = temp_text   
        
        else:
            print("page not found")

    def strip_pages(self, page_list):
        for pg in page_list:
            if pg in self.text:
                self.strip_page(pg) 
