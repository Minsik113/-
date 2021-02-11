'''
# 1/23
# 문제 난이도: Silver 4
# 문제 유형: DP, LIS
# 추천 풀이 시간: 50분
'''
'''
가장 긴 증가하는 부분(LIS) 문제의 심화 변형문제
벽돌의 수가 N개일 때 O(N^2)으로 해결 가능

가장 먼저 벽돌을 무게or밑변 기준으로 정렬 (동빈은 '무게')
D[i] = 인덱스가 i인 벽돌을 가장 아래에 두었을 떄의 최대 높이
각 벽돌에 대해서 확인하며 D[i]를 갱신하자

1. 무게 기준으로 정렬된 벽돌을 보자.
if area[i] > area[j]:
    D[i] = max(D[i], D[j]+height[i])

'''
