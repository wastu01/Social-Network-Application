# practice code
# import matplotlib

import matplotlib
print(matplotlib.__file__)


import matplotlib.font_manager
 
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
 
for i in a:
    print(i)
