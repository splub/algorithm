#求列表元素总和
def sum(srg):
	if len(arg)==1:
		return arg[0]
	else:
		return arg.pop() + sum(arg)
#求列表总个数
def compare(arg):
	if arg == []:
		return 0
	else:
		arg.pop()
		return 1+compare(arg)
