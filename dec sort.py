import operator
d={1:90,2:100,3:20,4:120}
print ('original dictionary=',d)
sorted_d=dict(sorted(d.iteams(),key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value:',sorted_d)