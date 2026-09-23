#libraries
import os
from Storage.constants import PAGE_SPACE,HEADER,SLOT

#class

class Invalid(Exception):
    pass

class Pager:
    # check if file exits or not and get the number of pages in it
    def __init__(self,Path):
        if not ( os.path.exists(Path) ):
            file=open(Path,'wb') 
            file.close()
        self.file=open(Path,'r+b')
        file_size=os.path.getsize(Path)
        check=file_size%PAGE_SPACE
        if check!=0:
            raise Invalid(f'your file if corrupted ')
        self.number_of_pages=file_size//PAGE_SPACE

    #where a page starts
    def   start_location(self,n):
        return n*PAGE_SPACE 

    #create space for new pages to come 
    def allocate_page(self):
        file_pointer=self.start_location(self.number_of_pages)
        self.file.seek(file_pointer)
        self.file.write(b'\x00'*PAGE_SPACE)
        self.number_of_pages+=1
        return self.number_of_pages-1