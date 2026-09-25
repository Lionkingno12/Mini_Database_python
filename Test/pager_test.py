from Storage.page import page
from Storage.Pager import Pager
from Storage.constants import PAGE_SPACE
from hypothesis import given,strategies as st
#testing 
@given(st.lists(st.binary(min_size=20,max_size=50),min_size=50,max_size=60))
def test_pager_page(value):
    pager=Pager('arya.db')
    Page=page.empty()
    number=pager.allocate_page()
    pager.close()


    #insert
    for i in value:
        Page.insert(i)

    #get
    for slot,values in enumerate(value):
        assert Page.get(slot)==values

    #pager
    pager.write_page(number,Page.return_buf)  
    assert pager.read_page(number)==Page.return_buf
    pager.close()