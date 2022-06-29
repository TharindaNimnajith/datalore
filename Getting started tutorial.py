# -*- coding: utf-8 -*-

# -- Code editor --

print("Hello, world!")

# # Getting started tutorial
# 
# Datalore is an online data analysis notebook that enables you to edit, execute, and share your data more productively.
# 
# In this tutorial, we will learn to work with several **worksheets**:
# - Code editor (general Datalore overview)
# - Data analysis flow (example of dataset analysis)
# - Team collaboration (teamwork in Datalore)
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Sheets.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# **Important!**
# We are always adding new features to Datalore. You can find the most up-to-date tutorial with the newest features [here](https://view.datalore.jetbrains.com/notebook/LvUIisWBfqWLaoMKh7joJ8).
# 
# **Take a look at our features:**
#   * [Watch our Getting Started video](#Watch-our-Getting-Started-video)
#   * [Сode editor](#Code-editor)
#     * [Task 1:](#Task-1:)
#       * [Create a new worksheet](#Create-a-new-worksheet)
#       * [Create cells](#Create-cells)
#     * [Task 2:](#Task-2:)
#       * [Run some code](#Run-some-code)
#   * [Coding assistance](#Coding-assistance)
#     * [Task 3:](#Task-3:)
#       * [Code completion](#Code-completion)
#       * [Open documentation](#Open-documentation)
#       * [Inspections and quick-fixes](#Inspections-and-quick-fixes)
#       * [Auto imports](#Auto-imports)
#     * [Task 4:](#Task-4:)
#       * [Adjust notebook look](#Adjust-notebook-look)
#     * [Task 5:](#Task-5:)
#       * [Install libraries and packages](#Install-libraries-and-packages)
#     * [Task 6:](#Task-6:)
#       * [Choose a kernel](#Choose-a-kernel)
#       * [Create a notebook](#Create-a-notebook)
#   * [Data analysis flow](#Data-analysis-flow)
#     * [Collecting data](#Collecting-data)
#       * [Upload a dataset](#Upload-a-dataset)
#     * [Exploring data](#Exploring-data)
#     * [Visualizing results](#Visualizing-results)
#     * [Sharing insights](#Sharing-insights)
#   * [Team collaboration](#Team-collaboration)
#     * [Share notebooks](#Share-notebooks)
#     * [Share workspaces](#Share-workspaces)
#     * [History checkpoints](#History-checkpoints)
#   * [Tutorials](#Tutorials)
#   * [Follow us](#Follow-us)


# ## Watch our Getting Started video


from IPython.display import HTML

HTML('<div align="center"><iframe align = "middle" width="560" height="315" src="https://www.youtube.com/embed/MjvFQxqNSe0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')

# ## Code editor
# 
# Learn how to use the editor by completing the following small tasks.
# 
# ### Task 1:
# #### Create a new worksheet
# 
# Click `+` button at the bottom left corner of the editor to create a new worksheet.
# All sheets in a notebook share the same files, and sheets on the right
# inherit the environment from the sheets on the left.
# 
# #### Create cells
# 
# 1. Add a new **code cell** by pressing `Ctrl+Alt+Enter / Cmd+Option+Enter` or by clicking on the "+" button in the top
#    right of the cell. You can toggle the cell type between code and Markdown with `Ctrl+M` / `Cmd+M`.
# 
# 2. Add a **Markdown cell** by hovering over the middle of the bottom of the cell and clicking "Add markdown cell".
#    - Markdown cells support Markdown text editing and LaTeX transformations;
#    - Double newline clears formatting and starts a new paragraph;
#    - All input is HTML-escaped.
#   
#   <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/HTMLescaped.png" width = 300 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
# 
# 3. **Move cells up and down** by pressing "Move cell up" or "Move cell down" in the cell toolbar.


# ### Task 2:
# #### Run some code
# 
# 1. Execute the code in the following cell by pressing the **Run/Stop buttons** at the top-right corner of the cell **or** just press 'Shift+Enter'.
# 
# 2. If you encounter any problems, try the **Kernel → Restart** or **Kernel → Interrupt** commands in the main menu.


# Try it now
import datetime

now_moment = datetime.datetime.now()
print('– What is the right time to start?')
print('– Now!\n')

# ## Coding assistance
# 
# We hope you enjoy Datalore's smart coding assistance and that it helps you work more productively.
# 
# ### Task 3:
# #### Code completion
# 
# Add a new code cell and print the `now_moment` variable from the previous code cell.
# Whenever you type a function, method, class, or variable name,
# Datalore suggests possible completions.
# 
# #### Open documentation
# 
# Try opening the documentation for the pyplot.hist() function in the following cell.
# 
# Use:
# * `Ctrl/Command + hover` for brief documentation.
# * `set the caret + F1` for full documentation.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Documentation.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# Try opening Documentation for pyplot.hist() function

from matplotlib import pyplot as plt
import numpy as np

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

# #### Inspections and quick-fixes
# 
# Click the string “Probability” in the previous cell and apply the suggested quick-fix. Just press `Alt/Option+Enter` on the error and
# choose a fix from the popup menu.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Quickfix.png" width = 300 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
# 
# Inspections detect errors in your code.
# In most cases, errors can be fixed automatically with quick-fixes – automatic fixes
# that can be applied to the code with a simple shortcut.
# 
# #### Auto imports
# 
# Try importing LinearRegression in the following cell using Import suggestions by Datalore.
# If you forget to import the library for a method, class, or function,
# Datalore will suggest auto-import expressions.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Auto-imports.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# Try importing LinearRegression using Import suggestions by Datalore and applying the quickfix for the first line

lr = LinearRegression()

# ### Task 4:
# #### Adjust notebook look
# 
# Go to the **View** section in the Datalore menu to:
# 
# * Switch to Split output view. Change back to Sequential view by unchecking the "Split view" option;
# * Toggle line numbers;
# * Enable documentation on hover;
# * Switch on "Distraction-free mode".
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/View.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ### Task 5:
# #### Install libraries and packages 
# 
# In Datalore, the most popular data science libraries are already **preinstalled.** Hover over the plot in the following cell and see how the interactive visualization works in the preinstalled **Lets-plot** library.
# 
# Use **Matplotlib, pandas, NumPy, Scikit-learn, TensorFlow**, and other popular packages by
# typing the `import` clause for the package you need. Datalore will take care of all the dependencies.
# 
# If you need to install more libraries:
# * Go to **Tools → Library manager** in the main menu
# * Or write a `!pip install` clause in a code cell
# 
# Try installing `pymorphy2` or any other library that you might need.


from lets_plot import *
import numpy

LetsPlot.setup_html()
numpy.random.seed(100)
data = dict(
    cond=numpy.repeat(['A','B'], 200),
    rating=numpy.concatenate((numpy.random.normal(0, 1, 200), numpy.random.normal(1, 1.5, 200)))
)

ggplot(data, aes(x='rating', fill='cond')) + ggsize(500, 250) \
+ geom_density(color='dark_green', alpha=.7) + scale_fill_brewer(type='seq') \
+ theme(axis_line_y='blank')

# ### Task 6:
# #### Choose a kernel
# 
# Datalore lets you use one of three kernels:
# * The classic **IPython kernel**.
#   Datalore supports Jupyter Notebooks in `.ipynb` format.
# 
#   Upload an existing notebook from the homepage by pressing the downward arrow next to the "New notebook" button.
# 
#   <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Import_notebook.png" width = 200 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
# 
# * **Datalore kernel**
#   Our experimental Datalore Python kernel helps your notebook stay consistent.
#   It features **incremental recalculations**. When you change some code,
#   the dependent proceeding cells will be automatically recalculated.
# 
#   The Datalore kernel also supports **Reactive mode** - you can switch it on in the bottom-left corner.
# 
# * **Zeppelin kernel**
#   The Zeppelin kernel is an adapter for notebooks running on an external Apache Zeppelin instance.
#   The instance itself is not provided, you have to specify the access credentials using secrets.
#   Create a secret in **Tools → Attached secrets**.
# 
#   <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Secrets.png" width = 300 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
# 
# #### Create a notebook
# 
# Create a notebook and choose the kernel you need from the dialog.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Kernels.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>




# -- Data analysis flow --

# ## Data analysis flow
# ### Collecting data
# #### Upload a dataset
# 
# To start working with your own dataset:
# - Upload it via **Tools → Attached files** menu;
# - Import it directly from your code. **See how to import files from an s3-storage in the example below!**
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Attached_files.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>
# 
# The files will be **attached to your notebook**,
# and you will have access to them even after you restart the kernel or
# close and reopen Datalore.


# **Arxiv dataset**
# 
# Let's work with a part of **Arxiv dataset** - a selection of scientific papers from 1991 to 2020.
# The topics of the articles in this dataset include:
# - Physics
# - Mathematics
# - Computer science
# - Economics
# - Biology
# - Statistics


# Let's download the Dataset from the S3 cloud storage

import urllib
urllib.request.urlretrieve('https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/arxiv-papers-unique.json',
                           'arxiv-papers-unique.json')

# To open "Attached files" go to "Tools → Attached files"
# In this cell the files in the root directory are displayed

import os
os.listdir('.')

import json
with open('arxiv-papers-unique.json', 'r') as fp:
    arxiv_papers = json.load(fp)

# ### Exploring data
# 
# The way Datalore displays tables can help you explore the data more easily.
# 
# See the code result below and click on the table. Try scrolling it in the output!


import pandas as pd

papers_df = pd.DataFrame(arxiv_papers).fillna(0).sort_index()
papers_df.index = papers_df.index.astype(int)
papers_df.index.name = 'Year'
papers_df

# ### Visualizing results
# 
# Datalore supports all popular visualization libraries
# such as **Matplotlib, Plotly, seaborn, ggplot (as Lets-Plot),** etc.
# 
# Let's now show how the number of scientific papers has changed through the years.


import seaborn as sns

sns.set()
fig = papers_df.plot.line(figsize=(19,10), grid=True, title='Arxiv papers by category and year')

papers_2019 = papers_df[:-1]

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(19, 10))
sns.regplot(x=papers_2019.index, y='Physics', data=papers_2019, order=4, ax=axes[0])
sns.regplot(x=papers_2019.index, y='Computer Science', data=papers_2019, order=4, ax=axes[1])
plt.show()

# ### Sharing insights
# 
# To share the results you can:
# - Publish the whole notebook by clicking **File → Publish** and then share it with colleagues via a link.
#   In the published notebook you can discuss the results with others via comments.
#   The notebook will be published at Datalore View.
#   Update your published notebook again by clicking **File → Publish** in the editor.
# 
#   <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Publish.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# - You can copy any output image by pressing `Shift+right-click` and then "Copy".
# - Use the bundled Datalore plugin to publish [PyCharm notebooks](https://www.jetbrains.com/help/pycharm/sharing-notebooks-in-datalore.html) to the web.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Save_image.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# -- Team collaboration --

# ## Team collaboration
# 
# In Datalore, you can collaborate with your team and work together on the same notebook
# in real-time. When you start working on a notebook together, you'll see the
# cursors and names of each of your team members.
# 
# ### Share notebooks
# 
# To share a notebook,  press the share button in the top-right corner of the window.
# Add your team members’ email addresses, edit role permissions, and send them invitations.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Collaborate.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ### Share workspaces
# 
# Workspaces are a way of organizing collaborative work.
# Each user has a personal workspace that is accessible only to themselves.
# 
# You can create other workspaces that can be shared with your team on the Datalore homepage.
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/Workspace.png" width = 300 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ### History checkpoints
# 
# * **Tools → History** opens our internal version control dialog that saves all the changes made to the notebook.
# * **Tools → Add history checkpoint** creates a new checkpoint for the internal version control dialog. When you revert to the checkpoint, a “Revert” checkpoint is created
# that represents the notebook’s state before the revert.
# 
# **Try reverting a notebook to a previous history checkpoint!**
# 
# <div align="center"><img src="https://datalore-samples.s3-eu-west-1.amazonaws.com/getting-started/History.png" width = 560 border="1" style="border-color: #d3d3d3; margin-top: 1%;"/></div>


# ## Tutorials
# 
# Check out our other tutorials:
# 
# - [Getting Started](https://www.youtube.com/watch?v=MjvFQxqNSe0)
# - [Visualization with Pyplot](https://www.youtube.com/watch?v=qSY3DMMM850)


# ## Follow us
# 
# Follow our [blog](https://blog.jetbrains.com/datalore/) to get to know about new features and updates.
# 
# Found an annoying bug, have an idea for a feature, or got a question? Post it directly
# to our [forum](https://datalore-forum.jetbrains.com/) or use the Feedback button in the top-right corner of the window.
# 
# Follow us on Twitter at [@JBDatalore](https://twitter.com/JBDatalore)
# to learn [#HowToDatalore](https://twitter.com/hashtag/howtodatalore).


