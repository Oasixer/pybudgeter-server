
class Logger:
    def __init__(self):
        import os
        self.directory = 'logs'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.filename = os.path.join(self.directory, datetime.now().strftime("%Y%m%d-%H%M%S"))

    def log(self, string):
        if type(string) is not str:
            string = str(string)
        with open(self.filename, 'a+') as f:
            f.writeline(string+" \n")
