# Pre Lab 3





## Set up to displat the imgage
from myst_nb import glue
from PIL import Image

# Antinode at end image
antinode = Image.open('../../images/lab3/end_antinode_lab3.jpg')
# Node at end image
node = Image.open('../../images/lab3/end_node_lab3.jpg')
basewidth = 300
wpercent = (basewidth/float(node.size[0]))
hsize = int((float(node.size[1])*float(wpercent)))
node = node.resize((basewidth,hsize), Image.ANTIALIAS)
node.save('../../images/lab3/end_node_lab3.jpg')

glue('antinode', antinode, display=False)
glue('node', node, display=False)

## Part 1

- Now, I want you to answer this questions: <mark>Are the ends of a vibrating rod considered nodes or antinodes?</mark>
- If you do not know, I suggest go back to your lecture note on ***Sound Wave***.

```{tip}
Are there fixed boundaries?
```

## Part 2

- Two longest wavelength that can fit in this rod is equivalent to <font color='red'><b>two minimum number of nodes that can be formed within this rod's length</b><font>.

- Your sketch will depends on **your answer for part 1**. This illustration might give you a sense of what your base case looks like.


|Antinodes at 2 ends|Nodes at two ends|
|:---:|:---:|
|{glue:}`antinode`|{glue:}`node`|


```{caution}
These are two different cases corresponding your answer in Part 1. One of them is wrong!
```

- Now, you are asked where to hold the rod to produce 2 wave patterns you just draw. It is pretty easy if you know what **holding** is for.

```{tip}
Holding is to force a node at that point!
```