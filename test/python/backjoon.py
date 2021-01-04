import sys
import math


# a, b = map(int, input().split())
# fst = a*(b%10)
# snd = a*((b//10)%10)
# lst = a*(b//100)
# fst + snd*10 + lst*100
# print(fst,snd,lst,a*b,sep="\n")
# A, B, C =map(int, input().split())
# print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep="\n")

# case = int(input())
# for i in range(case):
#     a, b = map(int, input().split())
#     print(a+b)

# n = int(input())
# lst = []
# for i in range(n+1):
#     lst.append(i)
# print(sum(lst))

# cnt = int(input())
# for i in range(cnt):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)
# for i in reversed(range(1, int(sys.stdin.readline())+1)):
#     print(i)
# for i in range(1, int(sys.stdin.readline())+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print("Case #{}: {} + {} = {}".format(i,a,b,a+b))

# cnt = int(sys.stdin.readline())
# for i in range(1,cnt+1):
#     print(("*"*i).rjust(cnt))

# n, x = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
# for i in range(n):
#     if a[i] < x:
#         print(a[i],end=' ')

# while True:
#    try:
#        a, b = map(int, input().split())
#        print(a+b)
#    except:
#        break
# i = 0
# check = n = int(input())
# new_n = 0  #26
# c = 0   #8
# while True :
#     c = n//10 + n%10
#     new_n = (n%10)*10 + c%10
#     i+=1
#     n = new_n
#     if new_n == check:
#         break
# print(i)
# lst = []
# for i in range(9):
#     a = int(input())
#     lst.append(a)
# print(max(lst), (lst.index(max(lst))+1))

# a = int(input())
# b = int(input())
# c = int(input())
# total = a*b*c
# total_str = str(total)
# for i in range(10):
#     cnt = total_str.count(str(i))
#     print(cnt)
# lst = []
# cnt = 0
# for i in range(10):
#     a = int(input())
#     res = a % 42
#     lst.append(res)
# for a in range(42):
#     if a in lst:
#         cnt += 1
# print(cnt)

# score_lst = []
# n = int(input())
# a = list(map(int, input().split()))
# m = max(a)
# for i in a:
#     score = i/m*100
#     score_lst.append(score)
# print(sum(score_lst)/n)

# n = int(input())
# for i in range(n):
#     case = str(input())
#     score = 0
#     cnt = 1
#     for a in case:
#         if a == "O":
#             score += cnt
#             cnt +=1
#         else:
#             cnt = 1
#     print(score)
# def self_number(a):
#     if 10<=a<100:
#         d = a + a//10 + a%10
#     elif 100<=a<1000:
#         d = a+a//100+(a//10)%10+a%10
#     else:
#         d = a+a//1000+(a//100)%10+(a//10)%10+a%10
#     return d
# lst = []
# lst_res = []
# for i in range(1,10001):
#     lst.append(i)
#     lst_res.append(i)
# for a in lst:
#     if self_number(a) in lst:
#         try: lst_res.remove(self_number(a))
#         except: pass
#     if a in lst_res:
#         print(a)
# n = int(input())
# cnt = 0
# for i in range(1, n+1):
#     if i < 100:
#         cnt += 1
#     else:
#         num = list(map(int, str(i)))
#         if num[0] - num[1] == num[1] - num[2]:
#             cnt += 1
# print(cnt)

# n = int(input())
# for i in range(n):
#     word = input()
#     for j in range(1, len(word)):
#         if word.find(word[j-1]) > word.find(word[j]):
#             n -= 1
#             break
# print(n)

# n = int(input())
# lst = int(input())
# sum = 0
# for i in str(lst):
#     sum += int(i)
# print(sum)
# from string import ascii_lowercase
# alphabet = list(ascii_lowercase)
# s = input()
# lst =[]
# for i in alphabet:
#     if i in s:
#         lst.append(s.find(i))
#     else: lst.append("-1")
# for j in lst:
#     print(j, end=' ')
# print(*map(input().find, map(chr, range(97,123))),sep="")

# t = int(input())
# for i in range(t):
#         r, s = map(str, input().split())
#         for i in s:
#             print(i*int(r), end='')
#         print()

# w = input().upper()
# lst = []
# for i in list(map(chr, range(65, 91))):
#     lst.append(w.count(i))
# if lst.count(max(lst)) == 1:
#     print(list(map(chr, range(65, 91)))[lst.index(max(lst))])
# else: print("?")
# from string import ascii_uppercase
# alphabet = list(ascii_uppercase)
# w = str(input()).upper()
# lst = []
# for i in alphabet:
#     lst.append(w.count(i))
# if lst.count(max(lst)) == 1:
#     print(alphabet[lst.index(max(lst))])
# else: print("?")
# print(*map(input().lower().count(),map(chr, range(97, 123))))
# s = input().split()
# print(len(s))
# def reverse(n):
#     return ''.join(n[::-1])
#
#
# a, b = map(str, input().split())
# if int(reverse(a)) > int(reverse(b)):
#     print(reverse(a))
# else:
#     print(reverse(b))
# if int(a[::-1]) > int(b[::-1]):
#     print(a[::-1])
# else: print(b[::-1])
# a, b, c = map(int, input().split())
# if b >= c:
#     print("-1")
# else: print(a//(c-b)+1)
# n = int(input())
# answer = -1
# if n % 5 == 0:
#     answer = n // 5
# for i in [3,6,9,12]:
#     if n > i and (n-i)%5 == 0:
#         answer = (n-i)//5+i//3
# print(answer)

# n = int(input())
# box = 0
# while n >= 0:
#     if n % 5 == 0:
#         box += n//5
#         print(box)
#         break
#     n -= 3
#     box += 1
# else: print("-1")
# n = int(input())
# c = 1
# new_c = 0
# cnt = 1
# while True:
#     if n == 1:
#         print(cnt)
#         break
#     new_c = c + 6*cnt
#     cnt += 1
#     if n in range(c, new_c+1):
#         print(cnt)
#         break
#     else:
#         c = new_c
#         continue

# x = int(input())
# n = 1
# i = 1
# while True:
#     if x in range(n, n+i):
#         if i%2 != 0:
#             print("{}/{}".format(i+n-x,1+x-n))
#             break
#         else: print("{}/{}".format(1+x-n,i+n-x))
#         break
#     else:
#         n = n+i
#         i += 1
# import math
# a,b,v = map(int,input().split())
# print(math.ceil((v-a)/(a-b)+1)
# t = int(input())
# for i in range(t):
#     h,w,n = map(int, input().split())
#     if n%h ==0:
#         print(h, "%02d" % (n // h), sep='')
#     else: print((n%h),"%02d"%(n//h+1),sep='')
# for _ in range(int(input())):
#     k = int(input());n = int(input())
#     floor1 = [i for i in range(1, n + 1)]
#     for _ in range(k):
#         for p in range(1, n):
#             floor1[p] += floor1[p - 1]
#     print(floor1[-1])
# for _ in range(int(input())):
# n = int(input())
# lst = [*map(int, input().split())]
#
def prime(num):
    if num == 1: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True


# cnt = 0
# for i in lst:
#     if prime(i):
#         cnt += 1
# print(cnt)
# lst = list(range(2,246912))
# prime_lst = []
# for i in lst:
#     if prime(i):
#         prime_lst.append(i)
# while True:
#     cnt = 0
#     n = int(input())
#     if n==0: break
#     for i in prime_lst:
#         if n < i <= 2*n:
#             cnt += 1
#     print(cnt)
# def gold(num, lst):
#     idx = max([i for i in range(len(lst)) if lst[i] <= num / 2])
#     for i in range(idx, -1, -1):
#         for j in range(i, len(lst)):
#             if num == lst[i] + lst[j]:
#                 return print(lst[i], lst[j])
# prime_lst = []
# for i in range(2, 10002):
#     if prime(i):
#         prime_lst.append(i)
# for _ in range(int(input())):
#     n = int(input())
#     gold(n)
# def ractangle(lst):
#     lst.sort()
#     if lst[2]**2 == lst[0]**2+lst[1]**2:
#         return print("right")
#     else: return print("wrong")
# while True:
#     lst = list(map(int, input().split()))
#     if lst[0] == 0:
#         break
#     ractangle(lst)

# def blackJack(list, num):
#     res = 0
#     for i in list:
#         for j in range(list.index(i)+1, len(list)):
#             for k in range(1,len(list)-j):
#                 a = i+list[j]+list[j+k]
#                 if a <= num and a>res:
#                     res = a
#     return print(res)
#
# n, m = map(int,input().split())
# num = list(map(int,input().split()))
# blackJack(num, m)
# str = str(input())
# lst = ["c=","c-","dz=","d-","lj","nj","s=","z="]
# cnt = 0
# for i in lst:
#     str = str.replace(i,"a")
# print(len(str))
str = str(input())
while True:
    i = 0
    cnt = 1
    for j in range(1,len(str)-i):
        if str[i] == str[i+j]:
            cnt+=1
        else: i+=j
    if i == len(str)-1: break
print(cnt)