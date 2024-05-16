#import baostock as bs
import pandas as pd
#import datetime
#import copy
#import math
import numpy as np

# 读取数据
factor_df = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/factor_TVSTD6.csv', index_col=0)
pctChg = pd.read_csv('/Users/zhuyining/PycharmProjects/pythonProject/stock_data_pctChg.csv', index_col=0)

#### 由因子值计算仓位和 ####
# 计算仓位
Factor_rk_df = factor_df.rank(axis=1,pct=True)-0.5
Pos = Factor_rk_df.shift()
Pos[Pos>0] = Pos[Pos>0].div(Pos[Pos>0].sum(axis=1),axis=0)
Pos[Pos<0] = Pos[Pos<0].div(Pos[Pos<0].abs().sum(axis=1),axis=0)
next_day_ret_df = pctChg.shift(-1)

# 计算日收益
Daily_pnl = (Pos * next_day_ret_df).sum(axis=1) / 2
# 多头收益
Daily_long_pnl = (Pos[Pos > 0]*next_day_ret_df).sum(axis=1) - next_day_ret_df.mean(axis=1)

# 画图
Daily_pnl.cumsum().plot()
Daily_long_pnl.cumsum().plot()

# 计算夏普比率
Daily_pnl.mean()*242
Sharpe = Daily_pnl.mean()/Daily_pnl.std()*np.sqrt(242)
print("Sharpe ratio: ", Sharpe)

# 计算IC值和IR值
IC_series = factor_df.shift().corrwith(next_day_ret_df, axis=1)
IC = IC_series.mean()
IR = IC_series.mean()/IC_series.std()
print("IC: ", IC)
print("IR: ", IR)

# 计算RankIC值和RankIR值
RankIC_series = factor_df.shift().corrwith(next_day_ret_df, axis=1, method='spearman')
RankIC = RankIC_series.mean()
RankIR = RankIC_series.mean()/RankIC_series.std()
print("RankIC: ", RankIC)
print("RankIR: ", RankIR)