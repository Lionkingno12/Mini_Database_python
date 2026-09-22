from Storage.page import page


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