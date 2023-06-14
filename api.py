import subprocess
import time

class Player:

    proc = ""

    def start(self):
        process = subprocess.Popen(['python', 'server.py'],stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE,encoding='utf8')
        self.proc = process
        return process

    def toggleplay(self):
        self.proc.stdin.write("PlayPause\n")
        self.proc.stdin.flush()
    
    def next(self):
        self.proc.stdin.write("Next\n")
        self.proc.stdin.flush()    

    def back(self):
        self.proc.stdin.write("Prev\n")
        self.proc.stdin.flush()

    def shuffle(self):
        self.proc.stdin.write("Shuffle\n")
        self.proc.stdin.flush()   

    def repeat(self):
        self.proc.stdin.write("Repeat\n")
        self.proc.stdin.flush()
    
    def read(self):
        return self.proc.stdout.readline()

    def getdata(self):
        self.proc.stdin.write("getdata\n")
        self.proc.stdin.flush()
        return self.proc.stdout.readline()

if __name__ == "__main__":
    pl = Player()
    pl.start()
    while True:
        time.sleep(5)
        print(pl.getdata())