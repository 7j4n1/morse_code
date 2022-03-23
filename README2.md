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
Morse Code: ..- ... -..
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

### Decoder
- The decoder function which decodes the given morse code to equivalent string.
> For example
```python
import morse

decoded_text = morse.decode("..- ... -.. -")
print("String: " + decoded_text)
```
The Output of the code is
```shell
String: usdt
```
> Example 2
Decoding of extra symbols
```python
import morse

new_text = morse.decode("-.--. ..--. . -..- - .-. .- ---..- -.---.")
print(new_text)
```
The Output is
```shell
(?extra:)
```
### Print Morse Binary Tree Stack
call the function after importing
```python
morse.printTree()
```
It would print the stack directly

### or to print a  stack with any node
call the function and give the node to print the tree
```python
import morse

node = morse.Node(1)
node = morse.insert_node(node, 2);
node = morse.insert_node(node, 3);

morse.getTree(node)
```
The following output would be
```shell
r - 1
   l - 2
   r - 3
```