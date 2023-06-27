class FileManager:
    def __init__(self,filename,mode,encode):
        self.filename = filename
        self.mode = mode
        self.encode = encode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('testowy.txt','w','utf-8') as f:
    f.write('to jest komunikat do pliku..')
print(f.closed)

with FileManager('testowy.txt','r','utf-8') as f:
    print(f.read())
    
