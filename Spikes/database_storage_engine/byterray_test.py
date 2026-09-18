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
#i will keep header 9 bytes,slot : 4 bytes , cell dynamic bytes 
page_100=bytearray(100)
#header
number_of_slot=page_100[0]
free_space_start=9
free_space_end=100
bytes_spcae_start=st.pack('>i',free_space_start)
bytes_spcae_end=st.pack('>i',free_space_end)
page_100[1:5]=bytes_spcae_start
page_100[5:9]=bytes_spcae_end
print(page_100[0:10])
start=st.unpack('>i',page_100[1:5])
end=st.unpack('>i',page_100[5:9])
print(start[0])
print(end[0])
name='arya'
name2='asttiva'
name1='sourabh'
def page_insert(value,page):
    #header (number_of_slot,free_space_start,free_space_end)
    number_of_slot=page[0]+1
    free_space_start=st.unpack('>i',page_100[1:5])[0]+4
    free_space_end=st.unpack('>i',page_100[5:9])[0]
    #check 

    #cell
    bytes_value=value.encode('utf-8')
    #slot (length,offset)
    lenght=len(bytes_value)
    # bytes_length=st.pack('>H',length)
    # offset=
