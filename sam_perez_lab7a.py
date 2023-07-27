#temp table
f = [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

c = []
for temp in f:
    c.append(float((temp - 32) * 5/9))

f_c = [f, c]

for x in range(2):
    for y in range(12):
        print(f_c[x][y], end=' ')
    print()

#weight table
p = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

k = []
for weight in p:
    k.append(float(weight / 2.2))

p_k = [p, k]

for x in range(2):
    for y in range(11):
        print(p_k[x][y], end=' ')
    print()

#distance table
m = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

km = []
for distance in m:
    km.append(float(distance * 1.609))

m_km = [m, km]

for x in range(2):
    for y in range(11):
        print(m_km[x][y], end=' ')
    print()

#measurement table
i = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

cm = []
for measurement in i:
    cm.append(float(measurement * 2.54))

i_cm = [i, cm]

for x in range(2):
    for y in range(11):
        print(i_cm[x][y], end=' ')
    print()

#volume table
g = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

l = []
for volume in g:
    l.append(float(volume * 3.785))

g_l = [g, l]

for x in range(2):
    for y in range(11):
        print(g_l[x][y], end=' ')
    print()
