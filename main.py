from morse import morse

print("Encoding:")
encoded_msg = morse().encode('USE')
print(encoded_msg)
print("Decoding")
decoded_msg = morse().decode(encoded_msg)
print(decoded_msg)

morse().printTree()