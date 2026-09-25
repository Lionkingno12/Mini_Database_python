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
    
    #return the page what your 
    def read_page(self,page_id):
        if page_id>=self.number_of_pages:
            raise Invalid(f'you intered  wronga id  ')
        file_pointer=self.start_location(page_id)
        self.file.seek(file_pointer)
        readed_file=self.file.read(PAGE_SPACE)
        return bytearray(readed_file)

    #put the updated page in the pager
    def write_page(self,page_id,buf):
        if len(buf)!=PAGE_SPACE:
            raise Invalid(f'you have entered the worng buf of wrong size')
        if page_id>=self.number_of_pages:
            raise Invalid(f'you intered  wronga id  ')
        file_pointer=self.start_location(page_id)
        self.file.seek(file_pointer)
        self.file.write(buf)
        
    #sync the file directly to the ssd 
    def sync(self):
        self.file.flush(self.file.fileno())    
        os.fsync()

    #close the paper which was open 
    def close(self):
        self.file.flush()
        os.fsync(self.file.fileno())
        self.file.close()



pager=Pager('arya.db')
page_created=pager.allocate_page()
print(page_created)
print(len(pager.read_page(3)))