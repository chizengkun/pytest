from pyecharts import Bar,Line

attr = ['辽源','雄安', '仙桃', '松原' , '四平',  '白山',  '吉林']
v1 = [41,    72,     167,    1039,    562,    693,   1518]
v2 = [3,     109,    580,    411,    526,    237,    282]
bar = Bar("公卫机构周活跃情况")
bar.add("未使用", attr, v1,label_color=['blue'], is_label_show=True,
		is_stack=True,label_pos='inside',mark_line=["average"]
		)
bar.add("活跃机构", attr, v2, is_label_show=True, is_stack=True,
	label_pos='inside',mark_line=["average"])
line = Line()
line.add("",attr, v1)
line.add("",attr, v2)
bar.render()
line.render()