## QueryFilter
### 目的是找出适合 UP标注的查询
处理从搜索日志中抽取下来的Query，进行色情查询过滤和去除掉类似的Query
色情查询过滤代码来自Chao Wang:
************
使用的话就
porn_filter = PornJudge("./porn_set.txt", "./porn_weight.txt", 0.8, 'gbk')

if porn_filter.judge_porn(query) > 0: 
表示是色情查询

其中porn_set.txt是色情词表,因为很多色情查询具有时效性,如果有的过滤不了可以手动添加一些进去
*************


similar.py 是用来判断是否当前query类似的已经在list 里面了，但是这个代码我加入到了 QueryFilter.py里面


**** 

QueryFilter.py的我们的主要函数
__init___ 中的 query_list 表示已经做过标注实验的query_list

add2list 是检验目前query是否是porn or similar , 如果不是加入self.query_list

similar_judge 判断 similar与否

parseFile 自动化处理之前从 log里面抽取的频率文件
格式是 ： query+”\t” + frequency

save2File 把没做过标注实验的query写到一个文件里面去，参数exist_query——list是做过实验的query list