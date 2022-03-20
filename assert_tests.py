import morse

def test_encode_us():
    assert morse.encode('us') == '..- ...', "Should be ..- ..."