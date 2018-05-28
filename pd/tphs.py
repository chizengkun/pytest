import matplotlib.pyplot as plt
import numpy as np


N = 7
noUsed =    (40,    68,     229,    738,    593,    1092,   1516)
Used =      (4,     113,    518,    193,    495,    358,    284)
xticklabels=('辽源','雄安', '仙桃', '松原' , '四平',  '白山',  '吉林')
ind1 = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence
#, yerr=noUsedStd , yerr=UsedStd
p1 = plt.bar(ind1, noUsed, width, label='未使用')
p2 = plt.bar(ind1, Used, width,bottom=noUsed, label='本周活跃')

plt.ylabel('机构数')
plt.title('公卫业务机构周活跃')
plt.xticks(ind1, xticklabels)
plt.yticks(np.arange(0, 2000, 100))
plt.legend(loc='upper left')


plt.show()


