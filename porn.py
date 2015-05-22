import sys
import os

class PornJudge:
    def __init__(self, set_fn, weight_fn, limit, code):
        self.limit = limit
        self.code = code
        self.set = []
        self.weight = {}
        set_file = open(set_fn)
        linelist = set_file.readlines()
        self.porn_seed_num = len(linelist)
        for line in linelist:
            tl = line.strip().decode(self.code,"ignore")
            if len(tl) > 0:
                self.set.append(tl)
        set_file.close()
        weight_file = open(weight_fn)
        linelist = weight_file.readlines()
        for line in linelist:
            tl = line.strip().decode(self.code,"ignore")
            for i in range(0,len(tl)):
                self.add_weight(tl[i], 0.4)
        weight_file.close()
        #print self.weight
        
    def add_weight(self, word, weight):
        if self.weight.has_key(word):
            self.weight[word] = self.weight[word] + weight
        else:
            self.weight[word] = weight
    def get_weight(self, word):
        ret = 1.0
        if self.weight.has_key(word):
            ret = ret + self.weight[word]
        return ret
    def jaccard_similarity(self, word1, word2):
        m = len(word1)
        n = len(word2)
        #print "w1 : " + word1  + " , " + str(m)
        #print "w2 : " + word2  + " , " + str(n)
        A = [([0] * (n + 1) )for x in range(m + 1)]  
        G = [([-1] * (n + 1) )for x in range(m + 1)]
        #print str(len(A))
        #for i in range(0, len(A)):
        #    print "A " + str(i) + " : " + str(len(A[i]))
        for i in range(1, m + 1):
            for j in range (1, n + 1):
                t = 0
                if word1[i - 1] == word2[j - 1] :
                    t = self.get_weight(word1[i - 1])
                #print str(i) + "," + str(j)
                flag = 0
                A[i][j] = A[i - 1][j - 1] + t
                if A[i][j] < A[i - 1][j]:
                    A[i][j] = A[i - 1][j]
                    flag = 1
                if A[i][j] < A[i][j - 1]:
                    A[i][j] = A[i][j - 1]
                    flag = 2
                G[i][j] = flag
        score = 2.0 * A[m][n] / (m + n)
        #compute combo
        x = m
        y = n
        combo = 0
        while x > 0 and y > 0:
            if G[x][y] == 0:
                combo += 1
                x = x - 1
                y = y - 1
            else: 
                if combo > 0:
                    score += (1.0 * combo * combo / (n * n))
                combo = 0
                if G[x][y] == 1:
                    x = x - 1
                else:
                    y = y - 1
        return score
    def judge_porn(self, query):
        sum_sim = 0.0
        max_sim = 0.0
        for i in range(0, len(self.set)):
            word = self.set[i]
            sim = self.jaccard_similarity(query.decode(self.code,"ignore"), word)
            if sim > max_sim:
                max_sim = sim
            sum_sim += sim
            #print sim
        ret_sim = sum_sim / (0.05 * self.porn_seed_num)
        if max(ret_sim, max_sim) > self.limit:
            return 1
        return -1


print ("hahah")
porn_filter = PornJudge("porn_set_utf8.txt", "porn_weight_utf8.txt", 0.8, 'gbk')
if porn_filter.judge_porn("密爱电影")>0:
    print ("hehehhe")
   