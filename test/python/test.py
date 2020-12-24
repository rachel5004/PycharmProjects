# i learn python and you learn java.
# s = input('Enter one sentence:')
# list = s.split(' ')
# i=0
# sum = 0
# while list:
#     sum+=len(list[i])
#     i+=1
#     if i==len(list):
#         break
# print(sum)

# # Q16
# # 1등급=535원, 2등급=377원, 3등급=291원
# # 등급에 123외의 정수는 'No such grade'
# # 소수점 둘째까지
# # 전기사용료=사용량*등급별단가+세금(사용금액의 3%)
#
# usage=int(input('electricity usage:'))
# grade=int(input('grade:'))
# if grade==1:
#     gp=535
# if grade==2:
#     gp=377
# if grade==3:
#     gp=291
# else:
#     print('No such grade')
# price=(usage*gp)*1.03
# print('Your amount is {}'.format(price,".2f"))

# # Q1-2
# n=38724
# a=10000
# list = []
# while (a>=1): #i는 10000,1000,100,10
#     b=int(n//a)
#     n=n%a
#     a/=10
#     list.append(b)
# str=['만','천','백','십','일']
# m=0
# for i in str:
#     # for j in list:
#     print('{}의 자리 수:'.format(i),list[m])
#     m+=1
#
# a=1
# b=1
# i=0
# for i in range(10):
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     i+=1
#
# str='race car'
# print(''.join(reversed(str)))

# a='Happy'
# b='Pig'
# c='Python'
# # x=a[1].upper()+a[2:]+a[0].lower()+'ay'
# x=a[1:]+a[0].lower()+'ay'
# x=x.capitalize()
#
# y=b[1].upper()+b[2:]+b[0].lower()+'ay'
# z=c[1].upper()+c[2:]+c[0].lower()+'ay'
# string='{}->{}'
# print(string.format(a,x))
# print(string.format(b,y))
# print(string.format(c,z))
#
# preposition = {'of', 'with', 'at', 'from', 'into', 'during', 'including', 'until', 'against', 'among', 'throughout',
#                'despite', 'towards', 'upon', 'concerning', 'to', 'in', 'for', 'on',
#                'by', 'about', 'like', 'through', 'over', 'before', 'between', 'after', 'since', 'without', 'under',
#                'within', 'along', 'following', 'across', 'behind',
#                'beyond', 'plus', 'except', 'but', 'up', 'out', 'around', 'down', 'off', 'above', 'near'}
# word = input('단어를 입력하세요:')
#
# if word.lower() in preposition:
#     print('입력한 단어는 전치사입니다.')

# s=sentence.split(' ')
# ss=set(s)
# a=ss & preposition
# print(a,end=' ')

# s= sentence.split(' ')
# list=[]
# for i in s:
#     if i in preposition:
#         print(i, end=' ')
#
# s=sentence.split(' ')
# ss=set(s)
# a=ss & preposition
# print(a,end=' ')
#
# str = '12321'
# isPalindrome=True
# for i in range(len(str)):
#     if str[i]== str[len(str)-1-i]:
#         continue
#     else:
#         isPalindrome=False
#         break
#
# if isPalindrome:
#     print("palindrome")
# else:
#     print("noe palindrome")
#
# str='123456dfasadf54321'
#
# list = list(str)
# list.reverse()
# ss = ''
# for i in list:
#     ss= ss+i
#
# print(ss)
# if(ss==str):
#     print("palindrome")
# else:
#     print("not palindrome")
# list=['Life','is','too','short']
# sum=0
# for i in list:  #list의 원소에 대해
#     sum+=len(i)  #sum에 각 원소(life,is..)의 글자수(len)를 더함
# print(sum)
# name = '홍길동'
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# list=[]
# num=0
# list.append(num)
# for i in num:
#     num+=1
#     if len(list)==5:
#         break
# print(list)

# score=[]
# for i in range(5):
#     x=int(input('성적을 입력하세요:'))
#     score.append(x)
# print()
# print('최고성적:', max(score))
# def two_times(x):
#     return x * 2
# print(list(map(two_times, [1, 2, 3, 4])))
# chomsky = 'colorless green ideas sleep furiously'
# w = chomsky.split(' ')
# word = lambda a: a[:-1]
# list(map(word, w))
choice = input("CF or FC:")
if choice == 'CF':
    C = int(input("섭씨온도를 입력하세요:"))
    F = C*1.8+32
    print("섭씨온도",C,"는 화씨온도",F,"입니다.")
if choice == 'FC':
    F = int(input("화씨온도를 입력하세요:"))
    C = (F-32)/1.8
    print("화씨온도",F,"는 섭씨온도 {0:0.4f} 입니다.".format(C))