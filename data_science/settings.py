import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import warnings

def setting_styles_basic():
    rcParams['font.family'] = 'Malgun Gothic' # windows
    # rcParams['font.family'] = 'AppleGothic' # mac
    rcParams['axes.unicode_minus'] = False

setting_styles_basic()

# 경고창 무시
warnings.filterwarnings('ignore')