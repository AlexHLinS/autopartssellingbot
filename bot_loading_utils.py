import telebot

class aps_bot(telebot.TeleBot):
    """
    This class is implement Auto Parts Selling Telegram Bot, which is based on telebot object
    """

    template_text_start = ''
    template_text_help = ''
    template_text_contacts = ''
    


    def get_start_message(self,name):
        
        text = name + self.template_text_start

        return text
    
    def get_help_message(self,name):
        
        text = name + self.template_text_help

        return text
    
    def get_contacts_message(self,name):
        
        text = name + self.template_text_contacts

        return text
    


    def __init__(self):
        
        if self.load_api_key():
           Exception
        self.load_template_text_contacts()
        self.load_template_text_help()
        self.load_template_text_start()
        
    def get_line_fromfile(self, filename):
        result = ''
        try:
            data_file = open(filename, mode='r')
            result = data_file.readline()
        except:
            return FileExistsError
        return result

    def get_lines_fromfile(self, filename):
        result = ''
        try:
            data_file = open(filename, mode='r')
            result = data_file.readlines()
        except:
            return FileExistsError
        return result
        

    def load_api_key(self):
        
        result = False

        try:
            self.token = self.get_line_fromfile('data')
        except:
            return FileExistsError

        return result
    
    def load_template_text_start(self):
        self.template_text_start = self.get_lines_fromfile('message_templates\\start_message')
        

    def load_template_text_help(self):
        self.template_text_help = self.get_lines_fromfile('message_templates\\help_message')

    def load_template_text_contacts(self):
        self.template_text_contacts = self.get_lines_fromfile('message_templates\\contacts_message')

    pass