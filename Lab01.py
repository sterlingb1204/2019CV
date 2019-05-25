
# coding: utf-8

# # Lab 01: Functions, RGB Colors

# In[6]:


from ipywidgets import interact
from IPython.core.display import display, HTML 


# ## Actvity 1: Functions

# ### Functions
# 
# Use the [modulo] (`%`) arithmetic operator and [less-than-or-equal-to] (`<=`) comparison operator to implement the following functions:
# 
# [modulo]: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
# [less-than-or-equal-to]: https://docs.python.org/3/reference/expressions.html#comparisons

# In[7]:


def is_odd(x):
    return(x%2 == 1)

''' Will return true if x is odd '''


# In[8]:


def is_even(x):
    return(x%2 == 0)

'''Will return true if x is even'''


# In[9]:


def is_multiple(x, y):
    return(x%y == 0)

''' Returns True if x is a multiple of y '''


# In[10]:


def is_between(x, y, z):
    return(y >= x and y <= z)

#Returns True if y is between x and z (inclusive)
    # Write boolean expression


# ### Interaction
# 
# Once you have implemented and tested the functions above, write a `test_numbers` function that uses the functions you wrote to display the results of passing inputs `x`, `y`, `z` to the respective functions:

# In[11]:


def test_numbers(x, y, z):
    print("is_odd({})          --> {}".format(x, is_odd(x)))
    print("is_even({})         --> {}".format(x, is_even(x)))
    print("is_multiple({},{})   --> {}".format(x, y, is_multiple(x,y)))
    print("is_between({},{},{})  --> {}".format(x, y, z, is_between(x,y,z)))

   # ''' Print the results of passing x, y, z to is_odd, is_even, is_multiple, is_between '''
    # Write print statement for each function


# In[12]:


test_numbers(2,3,4)


# The output of `test_numbers(5, 5, 5)` should look something like this:
# 
# ```
# is_odd(5)           -> True
# is_even(5)          -> False
# is_multiple(5, 5)   -> True
# is_between(5, 5, 5) -> True
# ```
# 
# Once you have a working `test_numbers` function, use the [interact] function to call the `test_numbers` function repeated based on interactive inputs:
# 
# [interact]: https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html

# In[13]:


interact(test_numbers, x=(0, 10), y=(0, 10), z=(0, 10))
test_numbers(4,5,6)


# ### Expressions
# 
# Use your functions above to write **boolean expressions** that evaluate the following:

# 1. Whether or not a number is both odd and a multiple of `7`?

# In[14]:


def boolexp0(x):
    return((x % 2 == 1) and (x % 7 == 0))
print(boolexp0(21))
print(boolexp0(11))


# 2. Whether or not a number is even but not a multiple of `6`?

# In[15]:


def boolexp1(x):
    return((x % 2 == 0) and (x % 6 != 0))
print(boolexp1(10))
print(boolexp1(12))


# 3. Whether or not a number is odd or a multiple of `8`?

# In[16]:


def boolexp2(x):
    return ((x % 2 == 1) or (x % 8 == 0))
print(boolexp2(64))
print(boolexp2(30))


# 4. Whether or not a number is between `0` and `100` and is even?

# In[17]:


def boolexp3(x):
    return(x > 0 and x < 100) and (x % 2 == 0)
print(boolexp3(10))
print(boolexp3(200))


# 5. Whether or not a number is odd but not between `20` and `50`, or a multiple of `3`?

# In[25]:


def boolexp4(x):
    return(((x < 20 or x > 50) and (x % 2 == 1)) or (x % 3 == 0))
print(boolexp4(21))
print(boolexp4(23))


# For each **boolean expression** provide an example of the expression evaluating to `True` and another where it evaluates to `False`.

# ## Activity 2: RGB Colors
# 
# Implement the function `display_color`, which given `r`, `g`, and `b` color components, it generates a table that shows the following:
# 
# <h5>Components of:</h5>
# <br>
# <div style="background: #7f7f7f;">&nbsp;</div>
# <table>
#     <thead>
#         <th>Component</th>
#         <th>Decimal</th>
#         <th>Hexadecimal</th>
#         <th>Binary</th>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Red</td>
#             <td>127</td>
#             <td>7f</td>
#             <td>01111111</td>
#         </tr>
#         <tr>
#             <td>Green</td>
#             <td>127</td>
#             <td>7f</td>
#             <td>01111111</td>
#         </tr>
#         <tr>
#             <td>Blue</td>
#             <td>127</td>
#             <td>7f</td>
#             <td>01111111</td>
#         </tr>
#     </tbody>
# </table>
# 
# That is, for each color component show its decimal, hexadecimal, and binary representation.  Likewise, display a color block that shows the color the three components combine to create.

# ### HTML Table
# 
# To display a [HTML] table in a Jupyter notebook, we can simply embed the [HTML] code into a string that we translate and convert using the `display` and `HTML` function.  For instance, to show some bolded text, we can do the following:
# 
# ```
# text = '<b>Hello, World</b>'
# display(HTML(text))
# ```
# 
# Note, the [HTML] text is simply a Python string and thus you can do all the things you can normally do on a string such as [format].
# 
# [HTML]: https://developer.mozilla.org/en-US/docs/Web/HTML
# [format]: https://docs.python.org/3/library/functions.html#format
# 
# Since we haven't covered [HTML] yet (we will later in the semester), we have provided with the necessary [HTML] template as a string below.  You simply need to format it with the appropriate values to make display the results.

# In[30]:


TABLE = '''
<h5>Components of:</h5>
<br>
<div style="background: #{};">&nbsp;</div>
<table>
    <thead>
        <th>Component</th>
        <th>Decimal</th>
        <th>Hexadecimal</th>
        <th>Binary</th>
    </thead>
    <tbody>
        <tr>
            <td>Red</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Green</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Blue</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
    </tbody>
</table>
'''


# ### Display Color Function
# 
# Write a `display_color` function that given the `r`, `g`, and `b` values of a color as integers, it outputs an [HTML] table as described above:
# 
# [HTML]: https://developer.mozilla.org/en-US/docs/Web/HTML

# In[28]:


def display_color(r, g, b):

    
    ''' Display a HTML table that shows the color of the r, g, b 
    components and their decimal, hexadecimal, and binary representations.
    '''
display(HTML(TABLE))
print(display_color(127,127,127))


# ### Color Interaction

# In[ ]:


interact(display_color, r=(0, 255), g=(0, 255), b=(0, 255))


# ### Exploration
# 
# Use your `display_color` widget to fill in the following table of colors:
# 
# | Color    | Red  | Green | Blue   | Hexadecimal |
# |----------|------|-------|--------|-------------|
# | Black    |      |       |        |             |
# | Red      |      |       |        |             |
# | Green    |      |       |        |             |
# | Yellow   |      |       |        |             |
# | Blue     |      |       |        |             |
# | Magenta  |      |       |        |             |
# | Cyan     |      |       |        |             |
# | Gray     |      |       |        |             |
# | White    |  255 |   255 |    255 |      ffffff |
# 
# Of course, there are many different shades of each color, so use your `display_color` widget to find your favorite shade and enter in the **RGB** values of each color as decimals, along with the hexadecimal representation of each color.
