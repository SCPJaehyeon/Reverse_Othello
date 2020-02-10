import time, os

def get_current_time():
    return time.strftime('%c', time.localtime(time.time())).replace(':', '.')

class Log:
    def __init__(self, console=True, filename=None, ext='.log'):
        if not os.path.exists('log/'):
            os.makedirs('log')

        if filename is None:
            self.log_file_name = 'log/' + get_current_time() + ext
        else:
            self.log_file_name = 'log/' + filename + ext
        
        self.log_file = open(self.log_file_name, 'w')
        self.console = console

    def write(self, data:str):
        self.log_file.write('['+get_current_time()+']:' + data + '\n')
        if self.console:
            print('['+get_current_time()+']:' + data)
