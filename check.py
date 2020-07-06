import pandas as pd
df = pd.read_csv('IMDb-movies.csv', nrows=2)
for dtype in df.dtypes.iteritems():
    print(dtype)

