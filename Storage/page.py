#Libraries
import struct

#Structure
PAGE_SPACE=4096
HEADER=struct.Struct('>HHH') # 2bytes: number of slot , free_space_start, free_space_end
SLOT=struct.Struct('>HH') # 2bytes: offset,length

#class
 
class Error(Exception):
    pass

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
    
    @property

    #reture the remaning space
    def remaning_space(self):
        head=self.header
        free_space_start=head[1]
        free_space_end=head[2]
        total_remaning=free_space_end-free_space_start
        return total_remaning
    
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
        head=self.header
        number_of_slot=head[0]
        if not ( 0<=id<number_of_slot ):
            raise Error(f'you have entered wrong id ')
        if number_of_slot==0:
            raise Error(f'you have not intered anything ')
        if length==0 :
            raise Error(f'you have already deleted it  ')
        cell= self.buf[offset:offset+length]
        return cell

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
    def insert(self,bytes_value):
        head=self.header
        free_space_start=head[1]
        free_space_end=head[2]
        total_remaning=free_space_end-free_space_start
        length=len(bytes_value)
        required_space=length+SLOT.size
        if total_remaning>=required_space:
            self.cell_insert_new_slot(bytes_value)
            print('you value is inserted ....')
        else:
            raise Error(f'sorry you dont have enough space | remained: {total_remaning} | needed: {required_space}')

    #delete function we delete the value after taking the slot number 
    def delete(self,id):
        head=self.header
        number_of_slot=head[0]
        if  not ( 0<=id<(number_of_slot) ): 
            raise Error('you have input a worng id which does not exits ')
        offset,length=self.read_slot_value(id)
        if length==0:
            raise Error('your value is already deleted')
        offset=9999
        length=0
        self.slot(id,offset,length)
        print('your value is deleted .....')