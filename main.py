from collections import deque
class Node:
    def __init__(self, data): #every node in the tree is an object
        self.data = data
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    #search
    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    #insert
    def insert(self, data):
        new_node = Node(data)

        #first node is root w lazem teb2a black
        if self.root is None:
            new_node.color = "black"
            self.root = new_node
            return

        current = self.root #benebda2 mn el root

        #BST insertion 3ady
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                print("ERROR: Duplicate")
                return

        new_node.parent = current
        #fix
        self.fix_insert(new_node)

    #fix insert
    def fix_insert(self, node):
#after inserting 3shan nesala7 el tree law fe moshkela

        while node != self.root and node.parent and node.parent.color == "red":

            parent = node.parent
            grand = parent.parent

            if grand is None:
                break

            #parent on the left
            if parent == grand.left:
                uncle = grand.right

                #uncle red
                if uncle and uncle.color == "red":
                    parent.color = "black"
                    uncle.color = "black"
                    grand.color = "red"
                    node = grand

                else:
                    #uncle black

                    #LL
                    if node == parent.left:
                        parent.color = "black"
                        grand.color = "red"
                        self.right_rotate(grand)

                    #LR
                    else:
                        self.left_rotate(parent)
                        node = parent
                        parent = node.parent

                        parent.color = "black"
                        grand.color = "red"
                        self.right_rotate(grand)

            #parent on the right
            else:
                uncle = grand.left

                #uncle red
                if uncle and uncle.color == "red":
                    parent.color = "black"
                    uncle.color = "black"
                    grand.color = "red"
                    node = grand

                else:
                    #uncle black

                    #RR
                    if node == parent.right:
                        parent.color = "black"
                        grand.color = "red"
                        self.left_rotate(grand)

                    #RL
                    else:
                        self.right_rotate(parent)
                        node = parent
                        parent = node.parent

                        parent.color = "black"
                        grand.color = "red"
                        self.left_rotate(grand)

        self.root.color = "black"

    #rotations
    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    #size
    def get_size(self, node):
        if node is None:
            return 0
        return 1 + self.get_size(node.left) + self.get_size(node.right)

    #height
    def get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    #black height(edited)
    def get_black_height(self, node):
        if node is None:
            return 0

        left_bh = self.get_black_height(node.left)
        right_bh = self.get_black_height(node.right)

        if left_bh != right_bh:
            print("Tree violates black height property")

        if node.color == "black":
            return left_bh + 1
        else:
            return left_bh


#load dictionary
def load_dictionary(tree):
    try:
        with open ("dictionary.txt", "r") as f:
            for line in f:
                word = line.strip()
                if word:
                    tree.insert(word)
    except:
        print("ERROR: File not found")

#insert word
def insert_word (tree, word):
    if tree.search(tree.root, word):
        print("\033[91m Error: word already existed.\033[0m")
        return


    with open("dictionary.txt", "a") as f:
        tree.insert(word)
        f.write(word + "\n")

    print("word " + word + " is inserted successfully")
    print("Size: " , tree.get_size(tree.root))
    print("Height: " , tree.get_height(tree.root))
    print("Black Height: " , tree.get_black_height(tree.root))

#look up word
def lookup(tree, word):
    if tree.search(tree.root, word):
        print("\033[92m YES\033[0m")

    else:
        print("\033[91m NO\033[0m")

#Main UI
def main():
    tree = RedBlackTree()
    load_dictionary(tree)

    while True:
        print("\033[96m****Menu****\033[0m")
        print("1) insert word")
        print("2) search word")
        print("3) exit")

        try:
         choice = int(input("Enter your choice: "))
        except:
         print("\033[91m ERROR\033[0m")
         continue
        if choice == 1:
             word = input("Enter your word: ")
             insert_word(tree, word)
        elif choice == 2:
             word = input("Enter your word: ")
             lookup(tree, word)
        elif choice == 3:
          break

if __name__ == "__main__":
    main()
