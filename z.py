a = {"a": 1 , "b":2,"c":3}
b = {"d":4  , "a":[6,5], "f":6} 
import pandas as pd
d = pd.DataFrame(b)
# print(d)
print(a.keys())
# with open("a.txt","w") as f:
#     f.write(str(a))