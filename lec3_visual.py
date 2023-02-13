#!/usr/bin/env python
# coding: utf-8

# # More visualisation with pyplot
# 

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# This is a magic line to inform Jupyter Notebook how to 
# display graphics
# graphics
# Do not include in Spyder programs
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Line plots - selecting line style and colour

# In[ ]:


x = np.linspace(0.0, 2.0*np.pi, 1000)
ys = np.sin(x)
yc = np.cos(x)

plt.figure()
plt.plot(x, ys, label="sin(x)")
plt.plot(x, yc, "k--", label="cos(x)")

plt.xlabel("phase")
plt.ylabel("f(x)")
plt.legend()

plt.xlim(0.0, 2.0*np.pi)

plt.show()


# * supported colours (b)lue, (g)reen, (r)ed, (c)yan, (m)agenta, (y)ellow, blac(k), (w)hite
# * supported line styles
#     * `'-'` solid line style
#     * `'--'` dashed line style
#     * `'-.'` dash-dot line style
#     * `':'` dotted line style

# #### Insert symbols (e.g. lab measurements)

# In[ ]:


df_measure = pd.read_excel("measurements.xlsx")

plt.figure()
plt.plot(x, ys, label="sin(x)")
plt.plot(df_measure["phase"], df_measure["value"], "mo", label="measurement")

plt.xlabel("phase")
plt.ylabel("f(x)")
plt.legend()

plt.xlim(0.0, 2.0*np.pi)

plt.show()


# Selection of symbols
# * `o` filled circle
# * `.` dot
# * `^`, `v`, `<`, `>` triangle up, down, left, right
# * `s` square
# * `+` cross
# * `x` tilted cross
# * `D` diamond
# 
# See [List of markers](https://matplotlib.org/stable/api/markers_api.html) for full list

# In[ ]:


df_measure = pd.read_excel("measurements.xlsx")

colour = np.random.randint(0, 6, len(df_measure["phase"]))

plt.figure()

plt.scatter(df_measure["phase"], df_measure["value"], 10, colour, label="measurement")

plt.xlabel("phase")
plt.ylabel("f(x)")
plt.legend()

plt.xlim(0.0, 2.0*np.pi)

plt.show()


# ### Random numbers
# 
# - np.random contains a number of functions to produce random number of different distributions. 
# - The work horse random number generator in Python and other languages produces uniform random numbers in [0, 1).
# - These are then converted to random numbers of the chooses distribution, e.g. the normal distribution.

# In[ ]:


help(np.random)


# #### Histograms

# In[ ]:



rnd_numbers = np.random.normal(0.0, 1.0, 10000)

# and now compute and plot the the distributon as histogram
plt.figure(1)
plt.hist(rnd_numbers)
plt.show()


# In[ ]:



rnd_numbers = np.random.normal(0.0, 1.0, 10000)

# and now compute and plot the the distributon as histogram
plt.figure(1)
plt.hist(rnd_numbers, range=(-3.0, 3.0), bins=40)

plt.xlabel("x")
plt.ylabel("N(x)")
plt.title("normal distribution", size=18)

plt.show()


# input of `plt.hist`:
# * an array with values, which will be sorted into the bins and counted
# * `range` lowest and highest value used. Default min and max values of distribution.
# * `bins` number of bins (can be a bit delicate when dealing with distributions not forming a continuum of floats). Default: 10.
# * Values outside `range` are ignored. (Can be changed. Check documentation for keyword arguments).

# In[ ]:


ran_int = np.random.randint(1, 11, 100)
print(ran_int[0:40])

plt.figure()
plt.hist(ran_int)
plt.show()


# Let's do it for two normal distributions.

# In[ ]:



rnd_numbers = np.random.normal(0.0, 1.0, 10000)
rnd_numbers2 = np.random.normal(0.5, 1.5, 5000)

# and now compute and plot the the distributon as histogram
plt.figure(1)
# IMPORTANT range and bins setting need to be identical
plt.hist(rnd_numbers, range=(-3.0, 4.0), bins=40, label="Sample 1")
plt.hist(rnd_numbers2, range=(-3.0, 4.0), bins=40, label="Sample 2")
plt.legend()
plt.show()


# The distributions have different sizes, which makes comparison difficult.
# 
# Keyword argument `density=True` can be used to normalise both distributions. 
# 
# 
# For each distribution the bin's raw count divided by the total number of counts will be displayed. Summing up values times bin width will give one.
# 
# Keyword argument `alpha` is used to make the histograms somewhat transparent. Value 1 = intransparent

# In[ ]:



rnd_numbers = np.random.normal(0.0, 1.0, 10000)
rnd_numbers2 = np.random.normal(0.5, 1.5, 5000)

# and now compute and plot the the distributon as histogram
plt.figure(1)
# IMPORTANT range and bins setting need to be identical
plt.hist(rnd_numbers, range=(-3.0, 4.0), bins=40, label="Sample 1", density=True, alpha=0.7)
plt.hist(rnd_numbers2, range=(-3.0, 4.0), bins=40, label="Sample2", density=True, alpha=0.7)
plt.legend()
plt.xlabel("daily returns (%)")
plt.ylabel("N")
plt.show()


# Cumulative histogram

# In[ ]:



rnd_numbers = np.random.normal(0.0, 1.0, 10000)
rnd_numbers2 = np.random.normal(0.5, 1.5, 20000)

# and now compute and plot the the distributon as histogram
plt.figure(1)
# IMPORTANT range and bins setting need to be identical
plt.hist(rnd_numbers, range=(-3.0, 4.0), bins=1000, cumulative=True, alpha=0.7, density=True)
plt.hist(rnd_numbers2, range=(-3.0, 4.0), bins=1000, cumulative=True, alpha=0.7, density=True)
plt.show()


# ### Pie charts
# 
# Pie charts of the GDP of the 5 largest economies in the EU.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

gdp = np.array([3132.670e9, 2225.260e9, 1672.438e9, 1113.851e9])
countries = ["Germany", "France", "Italy", "Spain"]

plt.figure()
plt.pie(gdp, labels=countries)
plt.title("GDP largest EU economies")
plt.show()


# As easy as pie.
# 
# If numbers are scaled as fractions, summing up $<1$. 

# In[ ]:


gdp = np.array([3132.670e9, 2225.260e9, 1672.438e9, 1113.851e9])
countries = ["Germany", "France", "Italy", "Spain"]

gdp_EU = 12451.987e9
gdp = gdp/gdp_EU

plt.figure()
plt.pie(gdp, labels=countries, normalize=False)
plt.title("GDP largest EU economies")
plt.show()


# Again a number of keyword arguments to influence the behaviour.

# ### Sub-plots
# 
# - Often it is useful to compare several plots side by side in one figure.
# - This can be done using subplots
# 
# Example $2\times 2$ grid showing trigonometric and hyperbolic functions.

# In[ ]:


x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 1000)
sample1 = np.random.normal(-1.0, 1.0, 10000)
sample2 = np.random.normal(1.0, 0.5, 10000)
sample3 = np.random.normal(0.0, 1.5, 10000)
sample4 = np.random.normal(-0.2, 2.0, 10000)

# join in an iterable list
data = [sample1, sample2, sample3, sample4]

plt.figure()
# adjust space between plots
plt.subplots_adjust(hspace=0.4, wspace=0.4)

plt.subplot(2, 2, 1)  # subplot count starts at 1
plt.xlim(-4.0, 4.0)
plt.ylim(0.0, 750.0)
plt.hist(sample1, bins=50)
plt.xlabel("Sample 1")
plt.ylabel("N")

plt.subplot(2, 2, 4)  # subplot count starts at 1
plt.xlim(-4.0, 4.0)
plt.ylim(0.0, 750.0)
plt.hist(sample4, bins=50)
plt.xlabel("Sample 4")
plt.ylabel("N")
 
# # # loop over list of samples
# for i in range(4):
#     plt.subplot(2, 2, i+1)  # subplot count starts at 1
#     plt.xlim(-4.0, 4.0)
#     plt.ylim(0.0, 750.0)
#     plt.hist(data[i], bins=50)
#     plt.xlabel("Sample "+str(i+1))
#     plt.ylabel("N")
    
plt.show()


# `plt.subplot(m, n, i)` specifices a $m\times n$ subplot. The $i$th subplot is used for the plot. Count starts at 1.
# 
# `plt.subplot_adjust()` allows to fine tune the layout.
# 
# One can mix different values for $m$ and $n$, e.g., to plot plots inside a plot. Follow this [link](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.subplot.html) to find out more. Scroll to the bottom for plenty of examples.
# 

# ### Boxes and whiskers
# 
# Box plots can illustrate the quartile range
# 
# ![Quartiles](quantiles.png)
# 
# Quartiles are more *robust* estimates than *average* and *standard deviation*. *Robust* means they are less sensitive to outliers and deviations from the normal distribution. Example.
# 
# - Average income per head USA: \$54,960.
# - Median income per head USA: \$31,333.
# 
# 
# - Robust estimates can be converted for distributions reasonable close to a normal distribution, e.g. to exclude the effect of a few outliers.
# - median $\longrightarrow$ average
# - 16% - 84% percentile $\longrightarrow$ $\pm 1 \sigma$
# 
# Box plots indicate the quartile regions.

# In[ ]:


sample1 = np.random.normal(1.0, 1.0, 10000)

sample2 = np.random.normal(3.0, 2.0, 10000)
plt.figure()
plt.boxplot([sample1, sample2], labels=["Sample 1", "Sample 2"])
plt.ylabel("Ranges")
plt.show()


# What do we see?
# - The box represents the 25% to 75% quantile
# - The horizontal line the median (= 50% quantile)
# - The "whiskers" represents the minimum and maximum.
# - Outliers are removed and plotted extra.

# ### Bar plots

# In[ ]:


# data from 2010
countries = [["Lithuania", 3.4e6, 38.3e9, 66.8],
            ["Australia", 20.6e6, 821e9, 88.6],
            ["United Kingdom", 60.0e6, 2772e9, 89.9],
            ["United States", 303.9e6, 13751e9, 81.4],
            ["China", 1331.4e6, 3206e9, 42.2]]

# convert to dataframe
df_countries = pd.DataFrame(data=countries,
                 columns=("Country", "Population", 
                         "GDP", "Urban population"))

df_countries["GDP/head"] = df_countries["GDP"] / df_countries["Population"]
# have a look at this
print(df_countries)


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

# population data for inner, outer and greater (=inner+outer) London
# data made numpy arrays for more convenient calculations
years = np.array([1801, 1851, 1901, 1951, 2001]) 
inner_pop = np.array([879491, 1995846, 4670177, 3680821, 2765975])
outer_pop = np.array([131666, 290763, 1556317, 4483595, 4406061])
greater_pop = np.array([1011157, 2286609, 6226494, 8164416, 7172036])

plt.figure()
# the 2nd argument is the height of the bars
# width in units of the x-axis
# tick_label expects a list with values (usually strings)
plt.bar(df_countries["Country"], df_countries["Population"], width=0.8)
                     #, tick_label = df_countries["Country"])

# general matters
plt.title("Population of countries")
plt.xlabel("Country")
plt.ylabel("population")  
plt.show()


# ### Area fill
# 
# `plt.fill_between(x, y1, y2)` fills the area between arrays (x,y1) and (x,y2).
# 
# `plt.text(x, y, label)` puts the string label at the position (x,y)

# In[ ]:


# attainable portfolios in X1-X2 space
plt.figure(figsize=(6,6))
plt.xlabel("$X_1$")
plt.ylabel("$X_2")
# draw filled areas of attainable and unattainable regions
x = (0.0, 1.0)
y1 = (0.0, 0.0)
y2 = (1.0, 0.0)
plt.fill_between(x, y1, y2)

x = (0.0, 1.0, 1.3)
y1 = (1.0, 0.0, 0.0)
y2 = (1.3, 1.3, 1.3)
plt.fill_between(x, y1, y2)

x = (0.0, 1.3)
y1 = (0.0, 0.0)
y2 = (-1.3, -1.3)
plt.fill_between(x, y1, y2)

x = (0.0, -1.3)
y1 = (0.0, 0.0)
y2 = (-1.3, -1.3)
plt.fill_between(x, y1, y2)

x = (0.0, -1.3)
y1 = (0.0, 0.0)
y2 = (1.3, 1.3)
plt.fill_between(x, y1, y2, color="cyan")

# label the regions
plt.text(0.25, 0.2, "E", size=20)
plt.text(1.0, 0.5, "D", size=20)
plt.text(0.75, -0.75, "C", size=20)
plt.text(-0.75, 0.5, "A", size=20)
plt.text(-0.75, -0.75, "B", size=20)

plt.savefig("attainable.png")
plt.show()


# This can be used, e.g, to plot $1 \sigma$ ranges.

# In[ ]:


df_measure = pd.read_excel("measurements.xlsx")
yplus = ys + 0.05
yminus = ys - 0.05
x = np.linspace(0.0, 2.0*np.pi, 1000)

plt.figure()
plt.plot(x, ys, label="sin(x)")
plt.plot(df_measure["phase"], df_measure["value"], "ko", label="measurement")

plt.fill_between(x, yminus, yplus, alpha=0.3)

plt.xlabel("phase")
plt.ylabel("f(x)")
plt.legend()

plt.xlim(0.0, 2.0*np.pi)

plt.show()


# In[ ]:




