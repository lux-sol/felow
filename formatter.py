 #############
## Formatter ##
 #############

class Formatter(object):
    def _init_(self):
        self.text = ""
        self.sent_list = []

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    # def get_sentlist(self):
    #     return self.sent_list

    def set_sentlist(self, sent_list):
        self.sent_list = sent_list

    #Format sentence list as string
    def frmt_textstring(self):
        print("formatting text as string...")
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + " "
        
        self.text = temp_text
    
    #Format text as list
    def frmt_textlist(self):
        print("formatting text as list...")
        temp_text = ""
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + "\n"
        
        self.text = temp_text

    #Format text as block
    def frmt_textblock(self, par_len):
        print("formatting text as block...")
        temp_text = "\t"
        text_check = ""
        par_check = 0
        for sentc in self.sent_list:
            temp_text = temp_text + sentc
            temp_text = temp_text + "  "
           
            text_check = text_check + sentc
            text_check = text_check + "  "
            par_check = len(text_check.split())
            if par_check >= par_len:
                temp_text = temp_text + "\n"
                temp_text = temp_text + "\t"
                text_check = ""

        self.text = temp_text

    

