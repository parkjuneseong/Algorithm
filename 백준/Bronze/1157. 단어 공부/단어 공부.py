n = input().upper()
n_list = list(set(n))
cnt = []
for i in n_list:
    cnt.append(n.count(i))
if cnt.count(max(cnt)) > 1 :
    print('?')
else:
    print(n_list[cnt.index(max(cnt))])