     ##############
    ##  STRIPPER  ##
     ##############

class Stripper(object):
    """ Creates an object for stripping unwanted characters from text """
    def __init__(self):
        self.text= ""

    #Return collected text
    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    #Strip string from collected text   
    def strip_string(self, string):
        print("stripping string...")
        temp_text = self.text
        if string in temp_text:
            temp_text = temp_text.replace(string, "")
            self.text = temp_text
 
        else:
            print("string not found")
        
       
    #Strip slice from collected text
    def strip_slice(self, char1, char2):
        print("stripping slice...")
        temp_text = self.text
        try:
            slice_start = temp_text.find(char1)
            slice_end = temp_text.find(char2, slice_start + 1)
            temp_text = temp_text.replace(temp_text[slice_start:slice_end + 1], "")
            self.text = temp_text
        
        except:
            print("slice not found")

    #Discard collected text that appears after the given string
    def strip_page(self, string):
        print("stripping page...")
        temp_text = self.text
        if string in temp_text:
            slice_start = temp_text.index(string)
            temp_text = temp_text[:slice_start]
            self.text = temp_text   
        
        else:
            print("string not found")
        
     
