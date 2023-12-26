import os
import shutil
from . import qdir

copylevels = {"0":shutil.copyfile,"1":shutil.copy,"2":shutil.copy2}

class qfile:
    def __init__(self,file_dir):
        self.dir = file_dir

    def get(self):
        return self.dir

    def change(self,new_dir):
        self.dir = new_dir

    def read(self, n = None):
        with open(self.dir,"r") as file:
            return file.read(n)

    def write(self, text):
        with open(self.dir,"w") as file:
            file.write(text)

    def append(self, text):
        with open(self.dir,"a") as file:
            file.write(text)

    def writelines(self,lines):
        with open(self.dir,"w") as file:
            file.writelines(lines)

    def create(self):
        open(self.dir,"x").close()

    def rename(self,new_name):
        os.rename(self.dir, new_name)

    def remove(self):
        os.remove(self.dir)

    def move(self, new_path):
        shutil.move(self.dir,new_path)

    def copy(self,dst,lvl=0):
        """if lvl==0:
            shutil.copyfile(self.dir,dst)
        if lvl==1:
            shutil.copy(self.dir,dst)
        if lvl==2:
            shutil.copy2(self.dir,dst)"""
        copylevels[lvl](self,dst)