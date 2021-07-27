Your task is to encode the alphabet as a binary tree using the frequencies of letters in the given text. You need to perform 
the following steps

* for each character in the text calculate its number of occurences / frequency, e.g. for string `aba` it would be `a -> 2`, `b -> 1`
* for each character and its frequency create a one-node tree
* take two trees `T1` and `T2` with lowest frequencies and merge them into a larger tree `T1-2` (`T1` should become the left sub-tree and `T2` the right subtree)
* repeat the previous step until there is only 1 tree left

That last tree represents the created encoding.
For example, given text `abaca` you should get:

```
      a+b+c(5) 
       /  \
      /    \
     /      \
    /        \
  b+c(2)     a(3)
  /   \
 /     \   
b(1)   c(1)    
```

Implement the method `create_code` in `code.py`. All the auxiliary classes for building the tree are provided.