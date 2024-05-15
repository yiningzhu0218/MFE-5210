import pandas as pd

#计算 12 日收盘价格，与日期序号（1-12）的线性回归系数，(close / mean(close)) = beta * t + alpha

def getfactor_PLRC12(close_df, window=12):
    # 获取所有股票代码
    stocks = close_df.columns.tolist()

    # 初始化一个空的DataFrame用于存储结果
    factor_PLRC12_df = pd.DataFrame(columns=stocks, index=close_df.index)

    # 计算每只股票的"PLRC12"因子，并将结果存储在PLRC12_df中
    for ID in stocks:
        # 获取单只股票的收盘价数据
        close = close_df[ID]
        # 计算过去window天的收盘价均值
        past_12days_mean = close.rolling(window=window).mean()
        # 计算"PLRC12"因子：计算 12 日收盘价格，与日期序号（1-12）的线性回归系数，(close / mean(close)) = beta * t + alpha
        # 回归系数的计算公式：β₁=（Σ（xᵢ - x̄）（yᵢ - ȳ））÷Σ（（xᵢ - x̄）²）
        factor_PLRC12 =
        factor_PLRC12_df[ID] = factor_PLRC12
    return factor_PLRC12_df


# 读取数据
close_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_close.csv', index_col=0)
# 调用函数计算"PLRC12"因子
factor_PLRC12 = getfactor_PLRC12(close_df, window=12)

# 输出所有股票的"PLRC12"因子
print(factor_PLRC12)
factor_PLRC12.to_csv("/Users/zhuyining/PycharmProjects/pythonProject/factor_PLRC12.csv", index=True)