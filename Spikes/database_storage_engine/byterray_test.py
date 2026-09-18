#suppose i take a block of size 4096 bytes
import struct as st
box=bytearray(4096)
print(len(box))
print(box[1])
box[1]=65
# print(st.unpack('>i',box[1]))
print(hex(box[1]))
print(bytes([box[1]]))
box[10:14] = st.pack(">i", 31488484)
#create a page of 100 bytes 
#4 thing header , slot ,free space ,cell
#i will keep header 9 bytes,slot : 6 bytes , cell dynamic bytes 
page_100=bytearray(100)
#header
number_of_slot=0
page_100[0:2]=st.pack('>H',number_of_slot)
free_space_start=10
free_space_end=100
bytes_spcae_start=st.pack('>i',free_space_start)
bytes_spcae_end=st.pack('>i',free_space_end)
page_100[2:6]=bytes_spcae_start
page_100[6:10]=bytes_spcae_end
def page_insert(value,page):
    #cell
    bytes_value=value.encode('utf-8')
    length=len(bytes_value)

    #header (number_of_slot,free_space_start,free_space_end)
    number_of_slot=st.unpack('>H',page[0:2])[0]
    free_space_start=st.unpack('>i',page[2:6])[0]
    free_space_end=st.unpack('>i',page[6:10])[0]
    new_start=st.pack('>i', free_space_start+6 )
    new_end=st.pack('>i', free_space_end-length )
    New_count=number_of_slot+1
    bytes_slot=st.pack('>H',New_count)

    #check 
    total_space=free_space_end-free_space_start
    if total_space<(length+6):
        print('not enough space remained ')
        print(f'you need : {length+6} bytes and remaning is : {total_space} bytes')
        return 

    #slot (length,offset)
    bytes_length=st.pack('>H',length)
    offset=free_space_end-length
    bytes_offset=st.pack('>i',offset)

    #Now adding the data in the page

    #header
    page[0:2]=bytes_slot
    page[2:6]=new_start
    page[6:10]=new_end
    
    #slot(length,offset)
    header_end=10
    slot_length=6
    start=(header_end+(number_of_slot*slot_length))
    page[start:start+slot_length]=bytes_length+bytes_offset

    #cell
    page[free_space_end-length:free_space_end]=bytes_value

page_insert('astitva',page_100)
page_insert('arya',page_100)
page_insert('abcdefghijklmnopqrstuvwxyz',page_100)
page_insert('ashfdhaiufhidsuhfuas',page_100)
page_insert('ary',page_100)
start=st.unpack('>i' ,page_100[2:6] )[0]
end=st.unpack('>i', page_100[6:10] )[0]
total_now=end-start
print(total_now)
print(start)
print(end)
print(page_100[start-6:start])
slot=st.unpack('>Hi',page_100[start-6:start])
print(slot)
number_slot=st.unpack('>H',page_100[0:2])
print(number_slot)