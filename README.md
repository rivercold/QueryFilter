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