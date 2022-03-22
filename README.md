# morse_code
Morse Code Encoder and Decoder Using Binary Tree

The morse code binary tree in the program is explicitly build inside the morse module.

To make use of the available functions, morse module has to be import into the main environment.

```python
import morse
```
the morse tree nodes can be called using the following method.
```
morse.tree
```
It points to the morse binary tree

### Instantiate
This program provides three functions:

### Encoder
- The encoder function which encode the given string to morse code.
> For example
```python
import morse

encoded_text = morse.encode('usd')
print("Morse Code: " + encoded_text)
```
The Output of the code is
```shell
Morse Code: ..- ... -.. -.---.
```
> Example 2
Encoding of extra symbols
```python
import morse

new_text = morse.encode('(?extra:)')
print(new_text)
```
The Output is
```shell
-.--. ..--. . -..- - .-. .- ---..- -.---.
```

