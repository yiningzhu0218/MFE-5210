import pandas as pd

#CCI(n)=(TP－MA)÷MD÷0.015；TP=(high+low+close)÷3；MA=SUM(TP,n)÷n；MD=SUM(ABS(MA-TP))÷n; N:=20

def getfactor_CCL20(high_df, low_df, close_df, window=20):
    # 获取所有股票代码
    stocks = close_df.columns.tolist()

    # 初始化一个空的DataFrame用于存储结果
    factor_CCL20_df = pd.DataFrame(columns=stocks, index=close_df.index)

    # 计算每只股票的"CCL20"因子，并将结果存储在CCL20_df中
    for ID in stocks:
        # 获取单只股票的最高价，最低价，收盘价数据
        high = high_df[ID]
        low = low_df[ID]
        close = close_df[ID]
        # 计算TP
        TP = (high+low+close)/3
        # 计算过去window天的MA值
        MA = TP.rolling(window=window).mean()
        # 计算过去window天的MD值
        MD = (MA-TP).abs().rolling(window=window).mean()
        # 计算"CCL20"因子：(TP－MA)÷MD÷0.015
        factor_CCL20 = (TP-MA)/(MD*0.015)
        factor_CCL20_df[ID] = factor_CCL20
    return factor_CCL20_df


# 读取数据
high_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_high.csv', index_col=0)
low_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_low.csv', index_col=0)
close_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_close.csv', index_col=0)
# 调用函数计算"CCL20"因子
factor_CCL20 = getfactor_CCL20(high_df, low_df, close_df, window=20)

# 输出所有股票的"CCL20"因子
print(factor_CCL20)
factor_CCL20.to_csv("/Users/zhuyining/PycharmProjects/pythonProject/factor_CCL20.csv", index=True)