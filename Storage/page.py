#Libraries
import struct

#Structure
PAGE_SPACE=4096
HEADER=struct.Struct('>HHH') # 2bytes: number of slot , free_space_start, free_space_end
SLOT=struct.Struct('>HH') # 2bytes: offset,length

#class
class page:
    __slots__=('buf',)

    def __init__(self,buf):
        self.buf=buf

    @classmethod
    def empty(cls,size:int=PAGE_SPACE):
        buf=bytearray(size)
        HEADER.pack_into(buf,0,HEADER.size,size)
        return cls(buf)
    
    @property
    def header(self):
        head=struct.unpack_from(HEADER,self.buf,0)
        return head
    
    # @property
    def slot(self,id):
        start=(HEADER.size+(SLOT.size*id))
        slot=struct.unpack_from(SLOT,self.buf,start)
        return slot

    def read_slot_value(self,id):
        slot=self.slot(id) 
        slot_length=slot[1] 
        slot_offset=slot[0]
        return slot_offset,slot_length

Page=page(bytearray(100))
print(HEADER)
print( Page.header )
print(Page.slot(0))
print()