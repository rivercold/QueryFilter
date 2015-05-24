from porn import PornJudge
import copy

class QueryFilter:
	query_list = []
	def __init__(self,query_list):
		self.query_list = copy.deepcopy(query_list)

	def add2list(self,query,porn_filter):
		if porn_filter.judge_porn(query) > 0:
			print query + "\t This is a porn!"
		else:
			if self.query_list == []:
				self.query_list.append(query)
			else:
				exist_flag = 0
				for item in self.query_list:
					if self.similar_judge(query,item):
						#print query + "\t This query has been saved! " + item
						exist_flag = 1
						break
				if exist_flag == 0:
					self.query_list.append(query)
					#print (query+" is saved")

	def similar_judge(self, a, b):
		a = unicode(a,"utf8")
		b = unicode(b,"utf8")
		count = 0
		for i in range(len(a)):
			if a[i] in b:
				count += 1
		length_a = len(a)
		length_b = len(b)
		score = float(count)/float(length_a+length_b-count)
		if score > 0.2:
			#print str(count) + "\t" + str(length_a) + "\t" + str(length_b)
			return 1 
		# similar
		else:
			return 0

	def parseFile(self,path):
		porn_filter = PornJudge("porn_set_utf8.txt", "porn_weight_utf8.txt", 0.8, 'utf8')
		print "porn_filter has been created"
		query_file = open(path,"r")
		lines = query_file.readlines()
		for line in lines:
			[query,hits] = line.strip().split("\t")
			self.add2list(query,porn_filter)
			if len(self.query_list)%20 == 0:
				print str(len(self.query_list)/20)+ "%"
				if len(self.query_list)>=2000:
					break

	def save2file(self,exist_query_list):
		additional_file = open("additional_query_file.txt","w")
		for item in self.query_list:
			if item not in exist_query_list:
				additional_file.write(item+"\n")
				print "new item " + item
			#else:
			#	print str(len(exist_query_list)) + "\t" + str(len(self.query_list))


if __name__=='__main__':
	query_list = []
	query_lines = open("./files/query_id.txt","r").readlines()
	for line in query_lines:
		query = line.split("\t")[0].replace(".html","")
		query_list.append(query)
		print "Already exits "+ query
	exist_query_list = query_list
	QF = QueryFilter(query_list)
	QF.parseFile("./files/filter_query_file.txt")
	print len(exist_query_list)
	print len(QF.query_list)
	QF.save2file(query_list)
