import string
import hashlib

from merklelib import MerkleTree, beautify

data = ('A','B','C','D')

# build a Merkle tree for the data
tree = MerkleTree(data)

# generate an audit proof for the element 'C'
proof = tree.get_proof('C')

# now verify that C is in the tree
if tree.verify_leaf_inclusion('C', proof):
  print('C is in the tree')
else:
  print('C is not in the tree')

# generate an audit proof for the element 'E'
proof = tree.get_proof('E')

# now verify that E is not in the tree
if tree.verify_leaf_inclusion('E', proof):
  print('E is in the tree')
else:
  print('E is not in the tree')

# perform a consistency check by checking if the new tree 
# contains the same items and in the same order as the old one

new_data = ('E','F','G','H')
new_tree = MerkleTree(new_data)

if tree == new_tree:
  print('Versions are consistent')
else:
  print('Versions are different')


# display the tree in the terminal
print("display the tree:\n")
beautify(tree) 

