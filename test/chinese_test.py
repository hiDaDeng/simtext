from simtext import similarity

text1 = '在宏观经济背景下，为继续优化贷款结构，重点发展可以抵抗经济周期不良的贷款'
text2 = '在宏观经济背景下，为继续优化贷款结构，重点发展可三年专业化、集约化、综合金融+物联网金融四大金融特色的基础上'

sim = similarity()
res = sim.compute(text1, text2)
print(res)