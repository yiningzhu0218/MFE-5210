import pandas as pd

#6日成交金额的移动平均值

def getfactor_TVMA6(amount_df, window=6):
    # 获取所有股票代码
    stocks = amount_df.columns.tolist()

    # 初始化一个空的DataFrame用于存储结果
    factor_TVMA6_df = pd.DataFrame(columns=stocks, index=amount_df.index)

    # 计算每只股票的"TVMA6"因子，并将结果存储在TVMA6_df中
    for ID in stocks:
        # 获取单只股票的收盘价数据
        amount = amount_df[ID]
        # 计算过去window天的成交金额的平均值
        past_6days_mean = amount.rolling(window=window).mean()
        # 计算"TVMA6"因子：6日成交金额的标准差
        factor_TVMA6 = past_6days_mean
        factor_TVMA6_df[ID] = factor_TVMA6
    return factor_TVMA6_df


# 读取数据
amount_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_amount.csv', index_col=0)
# 调用函数计算"TVMA6"因子
factor_TVMA6 = getfactor_TVMA6(amount_df, window=6)

# 输出所有股票的"TVMA6"因子
print(factor_TVMA6)
factor_TVMA6.to_csv("/Users/zhuyining/PycharmProjects/pythonProject/factor_TVMA6.csv", index=True)