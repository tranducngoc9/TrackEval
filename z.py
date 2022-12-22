a = {"a": 1 , "b":2,"c":3}
b = {"d":4  , "a":[6,5], "f":6} 
import pandas as pd
d = pd.DataFrame(b)
# print(d)
import numpy as np
c = ["1"]*10
print(np.asarray(c, dtype=np.float))
# with open("a.txt","w") as f:
#     f.write(str(a))