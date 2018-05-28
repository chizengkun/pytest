import matplotlib.pyplot as plt
import numpy as np

noUsed = (40, 68, 229,593,738)
Used = (4,113,518,358,193)
ind1 = np.arange(5)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, (ax1, ax2) = plt.subplots(2,1) # rows, columns
ax1.set_ylim(0,1000)
ax1.set_xticks(ind1)
ax1.set_xticklabels(['辽源','雄安','仙桃','四平','白山'])
ax1.set_title('公卫业务机构周活跃')
ax1.set_ylabel("机构数")
ax1.bar(ind1, noUsed, width,label='未活跃机构')
ax1.bar(ind1, Used, width, bottom=noUsed, label='活跃机构')
ax1.legend(loc='upper left')

#,'
noUsed2=(1092,1516)
Used2  =(495, 284)
ind2= np.arange(2)
ax2.set_ylim(0,2000)
ax2.set_xticks(ind2)
ax2.set_xticklabels(['松原', '吉林'])
ax2.bar(ind2, noUsed2, width,label='未活跃机构')
ax2.bar(ind2, Used2, width, bottom=noUsed2, label='活跃机构')
ax2.legend(loc='upper center')

plt.show()


