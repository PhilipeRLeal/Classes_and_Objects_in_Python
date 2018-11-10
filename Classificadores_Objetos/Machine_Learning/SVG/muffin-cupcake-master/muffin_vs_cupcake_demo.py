
# coding: utf-8

# **Classifying Muffins and Cupcakes with SVM**

# __Step 1:__ Import Packages

# In[2]:


# Packages for analysis
import pandas as pd
import numpy as np
from sklearn import svm
import matplotlib.ticker as plticker

# Packages for visuals
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Allows charts to appear in the notebook
get_ipython().magic(u'matplotlib inline')

# Pickle package
import pickle


# In[5]:




# __Step 2:__ Import Data

# In[4]:

# Read in muffin and cupcake ingredient data
recipes = pd.read_csv(r'C:\Users\Philipe Leal\Dropbox\Profissao\Python\Objetos\Classificadores_Objetos\Machine_Learning\SVG\muffin-cupcake-master\recipes_muffins_cupcakes.csv')
recipes.head(15)


# In[6]:

# Plot two ingredients
sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type',
           palette='Set1', fit_reg=False, scatter_kws={"s": 70})

  
# Plot three ingredients
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np


# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

#===============
#  First subplot
#===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')






# plot a 3D surface like in the example mplot3d/surface3d_demo



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m in [('r', 'o'), ('b', 'x')]:
    xs = recipes.Sugar
    ys = recipes.Butter
    zs = recipes.Flour
    ax.scatter(xs, ys, zs)

ax.set_xlabel('Sugar %')
ax.set_ylabel('Butter %')
ax.set_zlabel('Flour %')
ax.legend(s=10)
plt.show()


# __Step 3:__ Prepare the Data

# In[111]:

# Specify inputs for the model
# ingredients = recipes[['Flour', 'Milk', 'Sugar', 'Butter', 'Egg', 'Baking Powder', 'Vanilla', 'Salt']].as_matrix()
ingredients = recipes[['Flour','Sugar']].as_matrix()
type_label = np.where(recipes['Type']=='Muffin', 0, 1)

print (ingredients)

print('')
print('')

print(type_label)


# Feature names
recipe_features = recipes.columns.values[1:].tolist()

print("Recipe features é: ", type(recipe_features))

print('')

print(recipe_features)


# __Step 4:__ Fit the Model

# In[130]:

# Fit the SVM model
model = svm.SVC(kernel='linear')
model.fit(ingredients, type_label)


# __Step 5:__ Visualize Results

# In[133]:

# Get the separating hyperplane
w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(30, 60)
yy = a * xx - (model.intercept_[0]) / w[1]

print(xx)
print(yy)
# Plot the parallels to the separating hyperplane that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])


# In[18]:

# Plot the hyperplane
sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color='black');


# In[19]:

# Look at the margins and support vectors
sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color='black')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
            s=80, facecolors='none');


# __Step 6:__ Predict New Case

# In[20]:

# Create a function to guess when a recipe is a muffin or a cupcake
def muffin_or_cupcake(flour, sugar):
    if(model.predict([[flour, sugar]]))==0:
        print('You\'re looking at a muffin recipe!')
    else:
        print('You\'re looking at a cupcake recipe!')


# In[21]:

# Predict if 50 parts flour and 20 parts sugar
muffin_or_cupcake(50, 20)


# In[23]:

# Plot the point to visually see where the point lies
sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color='black')
plt.plot(50, 20, 'yo', markersize='9');


# In[24]:

# Predict if 40 parts flour and 20 parts sugar
muffin_or_cupcake(40,20)


# In[137]:

muffin_cupcake_dict = {'muffin_cupcake_model': model, 'muffin_cupcake_features': ['Flour','Sugar'], 'all_features': recipe_features}


# In[138]:

muffin_cupcake_dict


# In[139]:

# Pickle
pickle.dump(muffin_cupcake_dict, open("muffin_cupcake_dict.p", "wb"))


# In[140]:

# S = String
pickle.dumps(muffin_cupcake_dict)




         