import os
import shutil

copylevels = {"0":shutil.copyfile,"1":shutil.copy,"2":shutil.copy2}

def getdir():
    return os.getcwd()

def changedir(new_dir):
    os.chdir(new_dir)

def getlist(set_dir=getdir()):
    return os.listdir(set_dir)

def createdir(new_dir):
    os.mkdir(new_dir)

def rename(path=getdir(),new_name="file"):
    os.rename(path,new_name)

def remove(path):
    shutil.rmtree(path)

def move(path,new_path):
    shutil.move(path, new_path)

def copy(path,dst,lvl=0):
    shutil.copytree(path,dst,copy_function=copylevels[lvl])