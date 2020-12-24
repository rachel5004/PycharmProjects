# from random import random, randint, randrange
#
# cnt=0
# for i in range(1,51):
#     time = randrange(5, 51)
#     if 5<=time<=15:
#         drive="o"
#         cnt+=1
#     else:
#         drive=" "
#     print("[{}]{}번째 손님 (소요시간 : {}분)".format(drive,i,time))
# print("총 탑승 승객 : {}분".format(cnt))
#
# def std_weight(height,gender):
#     if gender=="남자":
#         cnt_height=height/100
#         weight=round(cnt_height*cnt_height*22,2)
#         print("키 {}cm 남자의 표준 체중은 {}kg 입니다.".format(height,weight))
#     if gender=="여자":
#         cnt_height=height/100
#         weight=round(cnt_height*cnt_height*21,2)
#         print("키 {}cm 여자의 표준 체중은 {}kg 입니다.".format(height,weight))
# std_weight(173,"여자")

# for i in range(1,51):
#     with open("{}주차.txt".format(i),"w",encoding="utf8") as report:
#         report.write("-{}주차 주간보고-".format(i))
#         report.write("부서:")
#         report.write("이름:")
#         report.write("업무 요약:")
# #
# class Unit:
#     def __init__(self,name,hp):
#         self.name=name
#         self.hp=hp
#
# class AttackUnit(Unit):
#     def __init__(self,name,hp,damage):
#         Unit.__init__(self,name,hp)
#         self.damage=damage
#     def attack(self,location):
#         print("{}:{} 방향으로 적군을 공격합니다. 공격력 {}".\
#               format(self.name,location,self.damage))
#
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flying_speed=flying_speed
#
#     def fly(self,location):
#         print("{}:{} 방향으로 이동합니다. 속력:{}"\
#               .format(self.name,location,self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self,name,hp,damage,flying_speed):
#         AttackUnit.__init__(self,name,hp,damage)
#         Flyable.__init__(self,flying_speed)
# valkyrie=FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly("3시")
#
# tank=AttackUnit("탱크",50,4)
# tank.attack("1시")
#
# class building:
#     def __init__(self,location,house_type,deal_type,price,year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.year=year
#     def show_detail(self):
#         print(self.location,self.house_type,self.deal_type,\
#               self.price,self.year)
# house=[]
# house1=building("강남","아파트","매매","10억","2010년")
# house2=building("마포","오피스텔","전세","7억","1930년")
# house3=building("송파","아파트","매매","10억","2010년")
# house.append(house1)
# house.append(house2)
# house.append(house3)
# print("총 {}대의 매물이 있습니다".format(len(house)))
# for i in house:
#     i.show_detail()

# chicken=10
# waiting=1
#
# class SoldOutError(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
#
#
# while(True):
#     try:
#         print("[남은 치킨 : {}]".format(chicken))
#         order=int(input("치킨 몇마리 주문하겠습니까?"))
#         if order>chicken:
#             print("재료가 부족합니다")
#         elif order<=0:
#             raise ValueError
#         else:
#             print("[대기번호 {}] {}마리 주문이 완료되었습니다".format(waiting,order))
#             waiting+=1
#             chicken-=order
#         if chicken <= 0:
#             raise SoldOutError("재고가 소진되어..")
#     except ValueError:
#          print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as Err:
#         print(Err)
#         break
# import theater as mv
# mv.price(3)
# cnt = 10
# while cnt > -1:
#     print(cnt)
#     cnt-=1
#     if cnt < 0:
#         print("발사")

# for i in range(0,11):
#     cnt = 10
#     cnt -= i
#     print(cnt)
#     if cnt <= 0:
#         print("launch")
