import pandas as pd
from sklearn.datasets import fetch_openml

X, y = fetch_openml('Wine', version=3, as_frame=True, return_X_y=True)
X.info()
