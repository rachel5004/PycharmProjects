# res = []
# for _ in range(int(input())):
#     a, d = map(int, input().split())  # a=배열길이 d = 값
#     lst = list(map(int, input().split()))
#     if sum(lst) <= a*d : res.append("YES")
#     else:
#         bCheck = False
#         for i in lst:
#             for j in lst:
#                 if (i+j < d) and ((i+j) in lst):
#                     bCheck = True
#                 else: continue
#         if bCheck: res.append("YES")
#         else: res.append("NO")
# for i in res: print(i)
