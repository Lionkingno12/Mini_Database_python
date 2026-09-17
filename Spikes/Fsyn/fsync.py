import os
import time
start=time.perf_counter()
#this was just the test to learn
with open('c:/Astitva/Program/Python/Projects/MiniDb/Spikes/Fsyn/test_fsyn.txt','w') as f:
    f.write('hello')
f.close()
end=time.perf_counter()-start
print(f"test time:{end}")
#i will use the fsync for each line 
start=time.perf_counter()
with open('c:/Astitva/Program/Python/Projects/MiniDb/Spikes/Fsyn/test_fsyn_each.txt','a') as f:
    for i in range(1000):
        f.write(f'hello no : {i}\n')
        f.flush()
        os.fsync(f.fileno())
end=time.perf_counter()-start
print(f'each row time: {end}')
#i will use the fsysn in the end
start=time.perf_counter()
with open('c:/Astitva/Program/Python/Projects/MiniDb/Spikes/Fsyn/test_fsyn_end.txt','a') as f:
    for i in range(1000):
        f.write(f'hello no : {i}\n')
    f.flush()
    os.fsync(f.fileno())
end=time.perf_counter()-start
print(f"at the end time: {end}")
