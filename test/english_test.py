from simtext import similarity

A = 'We expect demand to increase.'
B = 'We expect worldwide demand to increase.'
C = 'We expect weakness in sales'

sim = similarity()
AB = sim.compute(A, B)
AC = sim.compute(A, C)
