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
#求列表最大数
def max(arg):
	if len(arg)==1:
		return arg[0]
	else:
		arg.pop(0) if arg[0]<arg[1] else arg.pop(1)
		return max(arg)
