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

#update the  value
def page_update(update_value,target,page):
    number_of_slot=st.unpack('>H',page[0:2])[0]
    slot_number=0
    word=''
    found=False
    while slot_number<number_of_slot and found==False:
        start=10+(slot_number*6)
        slot=st.unpack('>Hi',page[start:start+6])
        length=slot[0]
        offset=slot[1]
        word=page[offset:offset+length].decode('utf-8')
        if word==target:
            found=True
        else:
            slot_number+=1
    if found:
        #three condition can happen
        start=10+(slot_number*6)
        slot=st.unpack('>Hi',page[start:start+6])
        length=slot[0]
        offset=slot[1]
        free_space_end=st.unpack('>i',page[6:10])[0]
        free_space_start=st.unpack('>i',page[2:6])[0]

        #if lenght of new is smaller of length is bigger or length is equal

        bytes_update_value=update_value.encode('utf-8')
        length_update_value=len(bytes_update_value)
        if length_update_value>length:
            if  ( free_space_end-free_space_start )<length_update_value:
                print(f"not enough space | space required: {length_update_value} | space remained: {free_space_end-free_space_start}")
                return
            offset=free_space_end-length_update_value
            length=length_update_value
            bytes_offset=st.pack('>i',offset)
            bytes_length=st.pack('>H',length)
            page[start:start+6]=bytes_length+bytes_offset
            page[offset:offset+length]=bytes_update_value
            bytes_space_end=st.pack('>i',offset)
            page[6:10]=bytes_space_end
            print('updated the data on new bytes')
            print(slot_number,length_update_value,offset)
        else:
                page[offset:offset+length_update_value]=bytes_update_value
                bytes_length=st.pack('>H',length_update_value)
                bytes_offset=st.pack('>i',offset)
                page[start:start+6]=bytes_length+bytes_offset
                print('update the data on old bytes')
                print(slot_number,length_update_value,offset)
    else:
        print('your update value is not found ')
page_insert('astitva',page_100)
page_insert('arya',page_100)
page_insert('abcdefghijklmnopqrstuvwxyz',page_100)
# page_insert('ashfdhaiufhidsuhfuas',page_100)
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
number_slot=st.unpack('>H',page_100[0:2])[0]
print(number_slot)
page_update('prashasti','astitva',page_100)
print(page_100[93:98])
print(st.unpack('>H', page_100[0:2] )[0])
print(st.unpack('>i',page_100[2:6])[0])
print(st.unpack('>i', page_100[6:10] )[0])