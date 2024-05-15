import pandas as pd

#6日成交金额的标准差

def getfactor_TVSTD20(amount_df, window=20):
    # 获取所有股票代码
    stocks = amount_df.columns.tolist()

    # 初始化一个空的DataFrame用于存储结果
    factor_TVSTD20_df = pd.DataFrame(columns=stocks, index=amount_df.index)

    # 计算每只股票的"TVSTD20"因子，并将结果存储在TVSTD20_df中
    for ID in stocks:
        # 获取单只股票的收盘价数据
        amount = amount_df[ID]
        # 计算过去window天的成交金额的标准差
        past_20days_std = amount.rolling(window=window).std()
        # 计算"TVSTD20"因子：20日成交金额的标准差
        factor_TVSTD20 = past_20days_std
        factor_TVSTD20_df[ID] = factor_TVSTD20
    return factor_TVSTD20_df


# 读取数据
amount_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_amount.csv', index_col=0)
# 调用函数计算"TVSTD20"因子
factor_TVSTD20 = getfactor_TVSTD20(amount_df, window=20)

# 输出所有股票的"TVSTD20"因子
print(factor_TVSTD20)
factor_TVSTD20.to_csv("/Users/zhuyining/PycharmProjects/pythonProject/factor_TVSTD20.csv", index=True)