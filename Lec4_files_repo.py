#!/usr/bin/env python
# coding: utf-8

# # Version control - repositories
# 
# - Development of major pieces of code will involve updates and refinements that will result in different versions of code.
# - Python itself has major updates about once a year. Python 2.7, 3.0, 3.1, ..., 3.6, 3.7, 3.8
# - Often it is desirable to go back to a previous version of a program. Think of a major modification gone wrong.
# - Or worse: hours of work deleted or overwritten.

# ### Principles of version control
# 
# - We start with a *baseline* - a piece of code.
# - This is *committed* to a *repository*.
# - A repository contains the code *and* the record of changes.
# - The first commitment creates the *master branch*.
# - A simple linear structure is created.
# ![Repository structure](repository_structure.png)
# - A user can decide to create a *branch* - e.g. for testing or subdevlopment by another team member.
# - branches can be kept separate or later be *merged" 

# ### Git
# 
# - We will look at *Git* - one of a number of version control systems
# - It was created by Linus Torvald - the inventor of Linux.
# - Many developer are using *Git* in command line mode.
# - A GUI is available and will be explained here.
# 
# - *Git* is available for Linux, Windows and macOS. [Download page](https://git-scm.com/downloads). Note: When installing most defaults are alright, but select Notepad instead of Vim as default editor,
# - *Git* is installed on PC lab desktops.
# 
# Let's write and committ the classic `Hello World`program.

# In[58]:


print("Hello World")


# - Store it in a folder.
# - Start the Git GUI.
# - Select `Create New Repository"
# ![Create repo](start_repo.png)
# 
# 
# 
# - Select the folder and hit create.
# ![Browse for folder](create_repo.png)
# 
# 
# 
# - You will see this window
# ![Git_window](git_window.png)
# 
# 
# - Now you have first to stage it: `Commit --> Stage To Commit
# ![Staged](repo_staged.png)
# 
# 
# - Type in an initial comment and commit: `Commit --> Commit`
# 
# - The program file remains in the folder and a *hidden* folder `.git`is created.
# (Tick `Show hidden files` in folder view or `ls -a` on a Mac or Linux command line).
# - Modify the program, e.g.

# In[59]:


print()
print("Hello World!")
print()


# To commit the new version
# - `Rescan
# 
# ![Recommit program](repo_recommit.png)

# - Follow the same *stage* and *commit* steps as before.
# - Explain changes in new commit message.
# - Get the history of changes with `Repository --> Visualise Master's History'
# 
# ![Master history](repo_history.png)

# - Creating a new branch: `Branch --> Create`
# 
# ![Create branch](create_branch.png)

# - Make changes to the existing program.
# - Rescan and commit
# 
# ![German branch](commit_to_branch.png)
# 

# To continue work on the *Master* branch: `Branch --> check out
# 
# ![Check out](checkout.png)
# 
# 
# - Select *Master*, click on *Checkout* and the English version is back.
# - If used for code development the branch can be merged with the Master: `Merge --> Local Merge

# #### How to restore an old version?
# 
# The easiest way in the GUI (different from the command line version): 
# - `Repository --> View branch history`
# - Right click on the version to restore
# - Select `Create new branch`
# - `Branch --> Checkout`
# - The old version is now availabe for editing.

# ### Github
# 
# [Github](https://github.com) is an online platform hosting git repositories.
# 
# - You can register with username and password for free. 
# - Read the guide.
# - Create a repository (the `+` pulldown menu")
# - You can *create* a repository and upload your code versions
# 
# - It is recommended to add a README file with project description
# - You can create branches analogous to the local git.
# - We will use you git repository for checking your programming style and good use of version control.
# - Best make repos public (if happy with that) which minimises complications.
# 
# #### Create a new repo
# 
# - Login
# - Click on create repository. 
# - Give it a name
# - Add description
# - The first time the version for geeks will appear.
# - Go back and click again on Create new repository
# - Enter name, description and make your repo public.
# 
# ![Create repo](github_creation.png)
# 
# #### Use your repo
# 
# - upload files
# - to recover files open your repo
# - click on commits
# - select the version you intend to recover
# 
# ![Select version](github_commits.png)
# 
# ![Version info](github_show.png)
# 
# - Select view
# 
# ![Python code](github_file.png)
# 
# - Click on Raw
# - Download

# In[ ]:





# ## Writing and reading files
# 
# #### Build in functionality
# 
# Let's assume we have gathered weather data for one year stored in `numpy` arrays and we want to produce a table to be read by humans. The standard Python way to do that:
# 

# In[60]:


import numpy as np

month = np.arange(1,13)
t_high = np.array([5.0, -1.1, 7.3, 8.3, 17.5, 33.5, 38.5, 39.5, 25.2, 30.5, 17.5, 4.0])
t_low = np.array([-2.8, -21.1, -4.1, -0.2, 3.3, 20.5, 25.9, 25.5, 11.5, 9.5, 5.7, -3.3])
rain = np.array([27.7, 0.5, 11.8, 33.9, 22.1, 5.3, 276.5, 58.3, 68.2, 121.7, 42.1, 57.0])


outfile = open("weather_2020.txt", "w")
print(outfile)

outfile.write("month,t(high),t(low),rain\n")
outfile.write(",C,C,mm\n")
for i in range (12):
    string = str(month[i])+","+str(t_high[i])+","+str(t_low[i])                    +","+str(rain[i])+"\n"
    outfile.write(string)

# very important
outfile.close()

print("Done")


# ##### What's going on?
# 
# The `open` statement opens a file.
# 
# * The string `"weather_2020.txt"` will be the name of the file
# * The second argument specifies whether the file is opened for
# * __`w`__ writing
# * __`r`__ for reading an existing file.
# * __`a`__ appending. The file is opened for writing, but appended at the end of an already existing file.
# * The object outfile is assigned information about the location of the file (not for humans)
#     
# The method `.write()`
# * writes a string into the file
# * The _escape character_ `\n` is needed to start the next line.
# * `.write()` accepts only _one string_ as argument
# * Thus the conversion in the loop
# 
# The file needs to be closed.
# - use method `.close()` to do that
# - data can be lost, if a file is not closed!

# ##### Using list comprehension for multiple arrays
# 
# * Above simple list comprehension could not be used. 
# * The `zip()` function allows us to do that.
# * Execution stops when the first array runs out of values.

# In[61]:


import numpy as np

month = np.arange(1,13)
t_high = np.array([5.0 , -1.1, 7.3, 8.3, 17.5, 33.5, 38.5,39.5, 25.2, 30.5, 17.5, 4.0])
t_low = np.array([-2.8, -21.1, -4.1, -0.2, 3.3, 20.5, 25.9, 25.5, 11.5, 9.5, 5.7, -3.3])
rain = np.array([27.7, 0.5, 11.8, 33.9, 22.1, 5.3, 276.5, 58.3, 68.2, 121.7, 42.1, 57.0])

outfile = open ("weather_2020zip.txt", "w")
outfile.write("month t(high) t(low) rain\n")
outfile.write("         C       C    mm\n")

for m, th, tl, r in zip(month, t_high, t_low, rain):
    string = str(m)+"  "+str(th)+"    "+str(tl)+"   "+str(r) + "\n"
    outfile.write(string)

outfile.close()


# ##### Reading data from files

# Every line of data is read in as a single string.
# 
# Use `.split()` to divide. And `.pop()` to extract the header strings.
# 
# - The default separator for split is space(s).
# - That can be changed, e.g. .split(",")
# - Note that .split(" ") makes every single blank a separator

# In[62]:


import numpy as np

outfile = open ("weather_2020.txt", "r")

lines = []
for line in outfile:
    # use the split method to divide the string
    lines.append(line.split())
    
print (lines)
print ()
header1 = lines.pop(0)
header2 = lines.pop(0)
# alternative lines = lines[2:]

print (lines)
print ()
print (header1)
print (header2)
print ()
for data in lines:
    print (data)


# In[63]:


import pandas as pd

def remove(string):
    """ This function returns word with non-letters removed and 
    converts letters to lower case"""
    
    # remove non-ascii signs like the quotes in this text
    string = string.encode('ascii', 'ignore').decode()
    # convert to lower case
    string = string.lower()
    
    # now remove list of punctuation marks
    string = string.replace('.', '')
    string = string.replace(',', '')
    string = string.replace(':', '')
    string = string.replace(';', '')
    string = string.replace('!', '')
    string = string.replace('?', '')

    return string


text = open("pride_and_prejudice.txt", "r")

all_words = []
counter = 0
for line in text:
    words = line.split()
    counter = counter + 1
    # if counter == 20:
    #     break
    for word in words:
        word = remove(word)
        all_words.append(word)
        
# convert into dataframe and use value_counts method
df_words = pd.DataFrame(data=all_words, columns=("words",))
df_counts = df_words["words"].value_counts()

print(df_counts.iloc[100:120])
df_counts.to_csv("wordcount.csv")


# In[64]:


print(df_words)


# In[ ]:




