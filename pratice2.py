import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

import warnings; warnings.simplefilter('ignore')

md = pd.read_csv('C:/Users/JinnyeongHeo/Desktop/2022-1_리뷰/추천시스템/movies_metadata.csv')

md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x,list) else [])

# 주어진 데이터의 genres 열이 list 타입으로 저장되어 있으므로, 
# literal_eval 함수를 이용해 데이터 타입을 dict으로 변환해줘야 한다.
# 그리고 gernes의 수가 둘 이상인 경우가 있기 때문에 반복문을 이용하여 해당되는 모든 장르를 추출한다.

print(md['genres'].head())

print(md['release_date'].head())
md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
print(md['year'].head())

# 출시된 날의 연, 월, 일을 모두 사용하는 것보다 연도만 사용하는 것이 구분하기 편리하므로 release_date에서 year만 추출

# Content based recommender


