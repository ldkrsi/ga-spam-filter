my_dict = {}

for line in open("spam_list.txt",'r'):
	second, top = line.strip().split('.')
	try:
		my_dict[top].add(second)
	except:
		my_dict[top] = set([second])

my_list = []
for key, value in my_dict.items():
	tmp = list(value)
	my_list.append("(%s)\\.%s" % ("|".join([i.replace("-","\\-") for i in tmp]), key))
	

with open("result.re",'w') as f:
	f.write("(^|\\.|\\/)(%s)($|\\/)" % ("|".join(my_list)))
	
