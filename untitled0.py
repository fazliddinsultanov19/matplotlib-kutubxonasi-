# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X3bS6xLLxEdU7OVlNpyU96mpcM7HJLEm
"""

"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zfkE0MCRTPjbM0Qhxb4QVAqqgm7R1CyH
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,'o:r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=20)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=20,mec='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x1=np.array([1,2,6,8])
y1=np.array([3,8,1,10])
x2=np.array([7,8,10,1])
y2=np.array([3,6,9,11])
plt.plot(x1,y1,x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=20,mfc='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,7,10,5,8,11])
y=np.array([0,3,2,1,13,14])
plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,6,7,3,9])
y=np.array([0,25,11,12,19,21])
plt.scatter(x,y,color='red')
x=np.array([21,10,8,12,14,20])
y=np.array([22,24,16,28,30,32])
plt.scatter(x,y,color='blue')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,6,7,3,9])
y=np.array([0,25,11,14,16,19])
mycolor=['red','green','blue','purple','lime','aqua']
plt.scatter(x,y,color=mycolor)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,6,7,3,9])
y=np.array([0,25,11,14,16,19])
mycolor=['red','green','blue','purple','lime','aqua']
size=[10,27,11,29,34,7]
plt.scatter(x,y,color=mycolor,s=size)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['510-23','613-23','614-23'])
y=np.array([18,22,25])
plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([25,11,18])
plt.pie(y)
plt.show

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25])
mylabels=["Apples","Bananas","Cherries"]
plt.pie(y,labels=mylabels)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25])
mylabels=["Apples","Bananas","Cherries"]
myexplode=[0.7,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25])
mylabels=["Apples","Bananas","Cherries"]
explode=[0.7,0,0]
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,25])
mylabels=["Apples","Bananas","Cherries"]
mycolors=["black","red","b"]
explode=[0.7,0,0]
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True,colors=mycolors)
plt.show()