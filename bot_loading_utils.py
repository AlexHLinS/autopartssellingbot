import telebot

class aps_bot(telebot.TeleBot):
    """
    This class is implement Auto Parts Selling Telegram Bot, which is based on telebot object
    """

    template_text_start = ''
    template_text_help = ''
    template_text_contacts = ''
    template_text_dontunderstand = ''

    # this method returns function from self.bot_commands dictionary by there str key
    def parse_command(self, cmd):
        
        try:
            func = self.bot_commands.get(cmd,None)
        except:
            return self.get_dontunderstand()
        if func == None:
            return self.get_dontunderstand()
        return func(self)

    # this method returns "reaction" for text, non command message
    def parse_text(self, cmd):

        return self.get_dontunderstand()[0]
    

    '''
        Module to return texts from templates:
    '''

    def get_start_message(self):
        
        text = self.template_text_start

        return text
    
    
    def get_help_message(self):
        
        text = self.template_text_help

        return text
    
    
    def get_contacts_message(self):
        
        text = self.template_text_contacts

        return text
    
    def get_dontunderstand(self):
        
        text = self.template_text_dontunderstand

        return text

    '''
        End of module to return texts from templates:
    '''
            
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


    '''
        Module to load data from files:
    '''

    #loading text for /start command
    def load_template_text_start(self):
        
        self.template_text_start = self.get_lines_fromfile('message_templates/start_message')
        

    #loading text for /help command
    def load_template_text_help(self):
        
        self.template_text_help = self.get_lines_fromfile('message_templates/help_message')

    #loading text for /contact command
    def load_template_text_contacts(self):
        
        self.template_text_contacts = self.get_lines_fromfile('message_templates/contacts_message')
    
    #loading text for don't understand sentence 
    def load_template_text_dontunderstand(self):
       
        self.template_text_dontunderstand = self.get_lines_fromfile('message_templates/sorry_im_dnt_understand')
    
    # loading token method
    def load_api_key(self):
    
        result = False

        try:
            self.token = self.get_line_fromfile('data')
        except:
            return FileExistsError

        return result
  
    '''
        End of the module to load texts from templates:
    '''    

    # list of commands aliases
    bot_commands = {
        '/help': get_help_message,
        '/start': get_start_message,
        '/contacts': get_contacts_message
    }

    # just load all data from all templates
    def load_data_from_templates(self):
        self.load_template_text_contacts()
        self.load_template_text_help()
        self.load_template_text_start()
        self.load_template_text_dontunderstand()

    # main init class method
    def __init__(self):       
        if self.load_api_key():
           Exception
        self.load_data_from_templates()

    pass