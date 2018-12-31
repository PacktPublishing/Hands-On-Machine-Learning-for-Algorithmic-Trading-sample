from pathlib import Path
import pandas as pd
import numpy as np
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, datetime

n = 1000000
review = pd.read_parquet('combined_tb.parquet', engine='fastparquet')[['stars']].iloc[:5000000]
print(review.info())
review = review.assign(text=[l for i, l in enumerate(Path('clean_reviews.txt').open()) if i < len(review)])
print(review.info())
review.sample(n=n).to_csv('yelp_sample.csv', index=False)
