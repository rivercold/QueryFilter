def similar_judge(a, b):
	count = 0
	for i in range(len(a)):
		if a[i] in b:
			count += 1
	length_a = len(a)
	length_b = len(b)
	score = float(count)/float(length_a+length_b-count)
	if score > 0.3:
		return 1 
	# similar
	else:
		return 0


write_file= open("300_query.txt","w")
read_file = open("query.txt","r")
lines = read_file.readlines()
query_list = []
for line in lines:
    query = line.split("\t")[1]
    query = unicode (query, "utf-8")
    query_list.append(query)

count = 0
filter_list = {}
num = len(query_list)
for i in range(num):
	for j in range(i+1,num):
		if similar_judge(query_list[i],query_list[j]):
			filter_list[j] = 1
			#print query_list[i]+"\t" + query_list[j]
print len(filter_list)

for i in range(num):
 	if i not in filter_list.keys():
 		print query_list[i]
 		write_file.write(query_list[i].encode('utf-8')+"\n")
#print (query_list[0])
#a = query_list[1]
#b = query_list[12]
#similar_judge(a,b)


