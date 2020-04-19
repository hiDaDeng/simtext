from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_similarity_score
from difflib import Differ, SequenceMatcher
import jieba
from math import *
import warnings
warnings.filterwarnings('ignore')

def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False



class similarity(object):
    def __init__(self):
        pass

    def transform(self, text1, text2):
        """
        把文本text1，text2转化为英文样式的text1，text2和向量vec1，vec2
        :param text1:
        :param text2:
        :return:
        """

        if check_contain_chinese(text1):
            text1 = ' '.join(jieba.lcut(text1))
            text2 = ' '.join(jieba.lcut(text2))
        else:
            pass

        corpus = [text1, text2]
        cv = CountVectorizer()
        cv.fit(corpus)
        vec1 = cv.transform([text1]).toarray()
        vec2 = cv.transform([text2]).toarray()
        return text1, text2, vec1, vec2



    def compute(self, text1, text2):
        """
        对输入的text1和text2进行相似性计算，返回相似性信息
        :param text1:  文本字符串
        :param text2: 文本字符串
        :return:  字典， 形如{
                'Sim_Cosine':0.8,
                'Sim_Jaccard': 0.3,
                'Sim_MinEdit': 0.5,
                'Sim_Simple': 0.8
                }
        """
        text1, text2, vec1, vec2 = self.transform(text1, text2)
        data = {
                'Sim_Cosine': self.cosine_similarity(vec1, vec2),
                'Sim_Jaccard': self.jaccard_similarity(vec1, vec2),
                'Sim_MinEdit': self.minedit_similarity(text1, text2),
                'Sim_Simple': self.simple_similarity(text1, text2)
                }
        return data

    def cosine_similarity(self, vec1, vec2):
        cos_sim = cosine_similarity(vec1, vec2)
        return cos_sim[0][0]


    def jaccard_similarity(self, vec1, vec2):
        """ returns the jaccard similarity between two lists """
        try:
            return jaccard_similarity_score(vec1[0], vec2[0])
        except:
            warnings.warn('scikit-learn版本问题，可以在命令行执行"pip install scikit-learn==0.22"')


    def minedit_similarity(self, text1, text2):
            words1 = jieba.lcut(text1.lower())
            words2 = jieba.lcut(text2.lower())
            leven_cost = 0
            s = SequenceMatcher(None, words1, words2)
            for tag, i1, i2, j1, j2 in s.get_opcodes():
                if tag == 'replace':
                    leven_cost += max(i2 - i1, j2 - j1)
                elif tag == 'insert':
                    leven_cost += (j2 - j1)
                elif tag == 'delete':
                    leven_cost += (i2 - i1)
            return leven_cost

    def simple_similarity(self, text1, text2):
        words1 = jieba.lcut(text1.lower())
        words2 = jieba.lcut(text2.lower())
        diff = Differ()
        diff_manipulate = list(diff.compare(words1, words2))
        c = len(diff_manipulate) / (len(words1) + len(words2))
        cmax = max([len(words1), len(words2)])
        return (cmax - c) / cmax



