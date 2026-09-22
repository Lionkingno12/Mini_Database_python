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