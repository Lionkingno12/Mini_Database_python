import struct as st
import os
arya={
    'name':'arya',
    'id':75
}
def  serialize(object):
    name=object['name']
    id=object['id']
    utf_code=name.encode('utf-8')
    length=len(utf_code)
    bytes_id=st.pack('>i',id)
    bytes_length=st.pack('>i',length)
    return bytes_id+bytes_length+utf_code
bytes_object=serialize(arya)
def deserialize(bytes):
    id=bytes[0:4]
    bytes=bytes[4::]
    lenght=bytes[0:4]
    bytes=bytes[4::]
    debytes_id=st.unpack('>i',id)[0]
    debytes_length=st.unpack('>i',lenght)[0]
    name=bytes[0:debytes_length].decode('utf-8')
    bytes=bytes[debytes_length::]
    return [ [ debytes_id,name,debytes_length ] ,bytes]
objects=[{'name':'arya','id':76},{'name':'astitva','id':81},{'name':'udit','id':70},{'name':'om','id':68},{'name':'falak','id':48}]
for student in objects:
    if bytes_object==None:
        bytes_object=serialize(student)
    else:
        bytes_object=bytes_object+serialize(student)
print(bytes_object)
while bytes_object:
    object_bytes=deserialize(bytes_object)
    bytes_object=object_bytes[1]
    print(object_bytes[0])