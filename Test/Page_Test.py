from Storage.page import page
from hypothesis import given,strategies as st


def test_empty_page():
    Page=page.empty(100)
    assert Page.header==(0,6,100)
    value='astitva'.encode('utf-8')
    Page.insert(value)
    assert Page.read_slot_value(0)==(93,7)
    assert Page.header==(1,10,93)
    assert Page.get(0)==b'astitva'
    Page.delete(0)

#Hypothesis test
def test_hypothesis():
    Page=page.empty(100)
    assert Page.header==(0,6,100)
    value='astitva'.encode('utf-8')
    Page.insert(value)
    assert Page.read_slot_value(0)==(93,7)
    assert Page.header==(1,10,93)
    assert Page.get(0)==b'astitva'
    value0='arya'.encode('utf-8')
    value1='prashasti'.encode('utf-8')
    value2='lionking12345'.encode('utf-8')
    value3='www.google.com/user/id=87498'.encode('utf-8')
    Page.insert(value0)
    Page.insert(value1)
    Page.insert(value2)
    Page.insert(value3)


@given(st.binary(min_size=10, max_size=50))
def test_limit_push(value):
    Page=page.empty(100)
    Page.insert(value)
    assert Page.get(0)==value

@given(st.lists(st.binary(min_size=1,max_size=5),min_size=1,max_size=10))
def test_all_function(value):
    Page=page.empty(100)
    #insert
    for i in value:
        Page.insert(i)

    #get
    for slot,values in enumerate(value):
        assert Page.get(slot)==values

    #delete
    for slot,values in enumerate(value):
        Page.delete(slot)