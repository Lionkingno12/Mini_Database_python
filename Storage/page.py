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
        print(HEADER,HEADER.size,size)
        HEADER.pack_into(buf,0,0,HEADER.size,size)
        return cls(buf)
    
    @property

    #return the value of head 
    def header(self):
        head=HEADER.unpack_from(self.buf,0)
        return head
    
    # @property
    
    #create a slot and also change the start free space in haeder 
    def slot(self,id,offset,length):
        start=(HEADER.size+(SLOT.size*id))
        SLOT.pack_into(self.buf,start,offset,length)
        # head=self.header
        # number_of_slot=head[0]
        # free_space_start=head[1]
        # free_space_end=head[2]
        # free_space_start=free_space_start+SLOT.size
        # HEADER.pack_into(self.buf,0,number_of_slot,free_space_start,free_space_end)

    #return the value of length offset of a slot 
    def read_slot_value(self,id):
        start=(HEADER.size+(id*SLOT.size))
        slot=SLOT.unpack_from(self.buf,start)
        slot_length=slot[1] 
        slot_offset=slot[0]
        return slot_offset,slot_length

    #for geting the value of of slot 
    def get(self,id):
        offset,length=self.read_slot_value(id)
        cell= self.buf[offset:offset+length]

        return cell.decode('utf-8')

    #put the value of cell in the buf with creating new slot
    def cell_insert_new_slot(self,bytes_value):
        length=len(bytes_value)
        head=self.header
        number_of_slot=head[0]
        free_space_end=head[2]
        free_space_start=head[1]
        offset=free_space_end-length
        free_space_end=offset
        self.slot(number_of_slot,offset,length)
        free_space_start+=SLOT.size
        number_of_slot+=1
        HEADER.pack_into(self.buf,0,number_of_slot,free_space_start,free_space_end)
        self.buf[offset:offset+length]=bytes_value

        #inset the cell with the reuse of old slot
    def cell_insert_old_slot(self,bytes_value,id):
        length=len(bytes_value)
        head=self.header
        number_of_slot=head[0]
        free_space_end=head[2]
        free_space_start=head[1]
        offset=free_space_end-length
        free_space_end=offset
        self.slot(id,offset,length)
        HEADER.pack_into(self.but,0,number_of_slot,free_space_start,free_space_end)
        self.buf[offset:offset+length]=bytes_value

    #for now if i want i can expand it and reuse the slot too 
    def insert(self,value):
        head=self.header
        free_space_start=head[1]
        free_space_end=head[2]
        total_remaning=free_space_end-free_space_start
        bytes_value=value.encode('utf-8')
        length=len(bytes_value)
        required_space=length+SLOT.size
        if total_remaning>=required_space:
            self.cell_insert_new_slot(bytes_value)
        else:
            return print(f'sorry you dont have enough space | remained: {total_remaning} | needed: {required_space}')


Page=page.empty(100)
print(HEADER.size)
head=Page.header
print(head[0],head[1],head[2])
Page.slot(0,100,7)
print(Page.read_slot_value(0))
Page.insert('astitva')
print(Page.read_slot_value(0))
print(Page.header)
print( Page.get(0) )