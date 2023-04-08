t = int(input())
for i in range(t):
    score = list(map(int,input().split()))
    avg = sum(score[1:])/score[0]
    cnt = 0
    for j in score[1:]:
        if j > avg:
            cnt  += 1
    result = (cnt/score[0])*100
    print(f'{result:.3f}%')