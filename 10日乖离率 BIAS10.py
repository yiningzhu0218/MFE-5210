import pandas as pd

#（收盘价-收盘价的N日简单平均）/ 收盘价的N日简单平均*100，在此N取10

def getfactor_BIAS10(close_df, window=10):
    # 获取所有股票代码
    stocks = close_df.columns.tolist()

    # 初始化一个空的DataFrame用于存储结果
    factor_BIAS10_df = pd.DataFrame(columns=stocks, index=close_df.index)

    # 计算每只股票的"BIAS10"因子，并将结果存储在BIAS10_df中
    for ID in stocks:
        # 获取单只股票的收盘价数据
        close = close_df[ID]
        # 计算过去window天的收盘价均值
        past_10days_mean = close.rolling(window=window).mean()
        # 计算"BIAS10"因子：（收盘价-收盘价的10日简单平均）/ 收盘价的10日简单平均*100
        factor_BIAS10 = ((close-past_10days_mean)/past_10days_mean) *100
        factor_BIAS10_df[ID] = factor_BIAS10
    return factor_BIAS10_df


# 读取数据
close_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_close.csv', index_col=0)
# 调用函数计算"BIAS10"因子
factor_BIAS10 = getfactor_BIAS10(close_df, window=10)

# 输出所有股票的"BIAS10"因子
print(factor_BIAS10)
factor_BIAS10.to_csv("/Users/zhuyining/PycharmProjects/pythonProject/factor_BIAS10.csv", index=True)