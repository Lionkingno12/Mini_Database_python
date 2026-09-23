import struct
PAGE_SPACE=4096
HEADER=struct.Struct('>HHH') # 2bytes: number of slot , free_space_start, free_space_end
SLOT=struct.Struct('>HH') # 2bytes: offset,length