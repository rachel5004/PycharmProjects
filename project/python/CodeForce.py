res = []
for _ in range(int(input())):
    a, d = map(int, input().split())  # a=배열길이 d = 값
    lst = list(map(int, input().split()))
    if sum(lst) <= a*d : res.append("YES")
    else:
        bCheck = False
        for i in lst:
            for j in lst:
                if (i+j < d) and ((i+j) in lst):
                    bCheck = True
                else: continue
        if bCheck: res.append("YES")
        else: res.append("NO")
for i in res: print(i)
# res=[]
# def al(s,t):
#     if len(s)>len(t):
#         a,b = s,t
#     else: a,b = t,s
#     if a==b*(len(a)/len(b)):
#         return a
#     else:
# for _ in range(int(input())):
#     s = input(); t = input()
#     if len(s)<len(t):
#         s*=len(t)
#     i = 0
#     j = len(t)
#     for _ in range(len(s)//len(t)):
#         if s[i:j] == t:
#             i+=len(t)
#             j*=2
#             if j==len(s)-1:
#                 res.append(s)
#         else: res.append("-1")
# print(res)
#
