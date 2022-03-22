import encoding as mtalk
import argparse

class MorseBinaryTree(object):
    def __init__(self, d=None, tree=None, char='char'):
        self._tree = {}

        self._char = char

        if d is None and tree is None:
            self._create_from_morse_dict(mtalk.morsetab)
        elif tree is not None:
            self._create_from_tree(tree)
        else:
            raise NotImplementedError("Can't create MorseBinaryTree")

    def _create_from_tree(self, tree):
        self._tree = tree

    def _create_from_morse_dict(self, d_morse):
        for value, code in d_morse.items():
            if value != ' ':
                self._add(self._tree, value, code)
    
    def _add(self, node, value, code):
        if code:
            self._add(node.setdefault(code[0], {}), value, code[1:])
        else:
            node[self._char] = value
    def __str__(self):
        return self._pretty_pprint()
        # return self._pretty_custom(self._tree)

    def _pretty_pprint(self):
        import pprint
        return pprint.pformat(self._tree)

    def _pretty_custom(self, d, indent_nb=0, indent_char='  '):
        s = ''
        for key, value in d.items():
            if key != self._char:
                s += (indent_char * indent_nb + str(key)) + '\n'
            if isinstance(value, dict):
                s += self._pretty_custom(value, indent_nb + 1)
            else:
                # s += ((indent_char * (indent_nb + 1) + str(value))) + '\n'
                s += "%20s\n" % value
            # s += '\n'
        return s
    @property
    def char(self):
        char = self._tree[self._char]
        return char

    @property
    def dit(self):
        return self['.']

    @property
    def dah(self):
        return self['-']
    
    def __getitem__(self, morse_code):
        if len(morse_code) == 0:
            return self
        if len(morse_code) == 1:
            tree = self._tree[morse_code]
            mt = MorseBinaryTree(tree=tree)
            return mt
        else:
            tree = self._tree[morse_code[0]]
            mt = MorseBinaryTree(tree=tree)[morse_code[1:]]
            return mt

def main():
    parser = argparse.ArgumentParser(description='Display morse binary tree')
    parser.add_argument('-c', '--c', help='Morse code character', default='')
    args = parser.parse_args()
    c = args.c.strip()

    mt = MorseBinaryTree()
    print(mt)

if __name__ == '__main__':
    main()