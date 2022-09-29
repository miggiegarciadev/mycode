#!/usr/bin/env python3
import shutil  #used to move files 
import os # Where shutil allows for higher-level file manipulation, os is more targeted at the operating system.

def main():
os.chdir('/home/student/mycode/') # goes to new part (dir)
shutil.move('raynor.obj', 'ceph_storage/')

#take a breath here aka pausing and xname is taking input from user cause of the question
xname = input('What is the new name for kerrigan.obj? ')

shutil.move('ceph_storage/kerrigan.obj ')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#this is needed in every code now , not sure what it does though
if __name__ == "__main__":
    main()
