import pandas as pd
import os
import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import seaborn as sns
from scipy.stats import poisson
import statsmodels.api as sm
import statsmodels.formula.api as smf
import itertools
from IPython.display import display, HTML

df = pd.read_csv(r'C:\Users\Vas\OneDrive\Business\Pyhton Practice\Training\Data\football_results.csv')
df.head(2)
