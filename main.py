import morse

if __name__ == '__main__':
    e = morse.encode('US')
    print(e)
    d = morse.decode('..- ...')

    assert morse.encode('us') == '..- ...', "Should be ..-"
    assert morse.decode('..- ...') == 'us', "Should be ..-"