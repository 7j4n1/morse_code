import morse2 as morse

if __name__ == "__main__":
    print(morse.find(")"))
    e = morse.encode('morse_code')
    print('%s' % e)
    d = morse.decode(e)
    assert morse.encode('us') == '..- ...', "Should be ..-"
    assert morse.decode('..- ...') == 'us', "Should be ..-"