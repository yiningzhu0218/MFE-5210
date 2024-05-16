import pandas as pd

# 读取因子数据
data = pd.read_csv("D:/code/python/MFE5250/factors/单日价量趋势.csv", index_col=0)


# MAD法进行去极值、中性化
def mad_scale(data, n=3):
    mad = (data - data.median()).abs().median()
    up_bound = data.median() + n * mad
    low_bound = data.median() - n * mad
    scaled = data.clip(lower=low_bound, upper=up_bound)
    return scaled


# zscore方法进行标准化
def standardize_norm(data):
    mu = data.mean()
    std = data.std()
    return data.subtract(mu).divide(std)


# 执行数据清洗操作,axis=1表明按照横截面进行清洗
data_cleaned = data.apply(mad_scale, axis=1).apply(standardize_norm, axis=1)

# 更新保存至原始CSV文件
data_cleaned.to_csv("D:/code/python/MFE5250/factors/单日价量趋势1.csv", index=True)
