#!/usr/bin/env python
# coding: utf-8

# # Week 1 - Day 4
# ## Task 1: Terminal, VS Code and Jupyter
# 
# This notebook demonstrates Python list comprehension,
# for loops and execution time comparison.

# In[1]:


import timeit


# In[4]:


numbers=list(range(1,10001))
print(numbers[:10])


# In[5]:


list_comprehension = [x * 2 for x in numbers]
print(list_comprehension[:10])


# In[6]:


for_loop_result = []
for x in numbers:
    for_loop_result.append(x * 2)
print(for_loop_result[:10])


# In[7]:


get_ipython().run_line_magic('timeit', '[x * 2 for x in numbers]')


# In[8]:


get_ipython().run_line_magic('timeit', '[x * 2 for x in numbers if x % 2 == 0]')


# In[9]:


list_time = timeit.timeit(
    "[x * 2 for x in numbers]",
    globals=globals(),
    number=100
)


# In[10]:


loop_time = timeit.timeit(
    """
result = []
for x in numbers:
    result.append(x * 2)
    """,
    globals=globals(),
    number=100
)

print("List Comprehension Time:", list_time)
print("For Loop Time:", loop_time)


# ## Conclusion
# 
# 1. List comprehension provides a simple way to create lists.
# 2. For loops are useful for complex operations.
# 3. List comprehension is generally faster for simple operations.
# 4. %timeit helps compare Python execution time.

# 1. Jupyter Notebook is useful for data analysis and experimentation.
# 2. Notebook supports code, output, charts and explanations together.
# 3. Python (.py) files are useful for developing and running complete programs.
# 4. Python files are better for automation and reusable applications.
