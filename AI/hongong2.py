from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

fish_lenght = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0,
               6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
kn = KNeighborsClassifier()
# fish_data = [[l, w] for l, w in zip(fish_lenght,fish_weight)]
# fish_target = [1]*35 + [0]*14
#
# train_input = fish_data[:35]
# train_target = fish_target[:35]
# test_input = fish_data[35:]
# test_target = fish_target[35:]
#
# kn = kn.fit(train_input,train_target)
# kn.score(test_input,test_target) # 정확도 0.0 출력
# # 샘플링 편향: 훈련세트와 테스트세트에 샘플이 골고루 섞이지 않으면 샘플링이 한쪽으로 치우침.
# # 훈련세트에는 도미만, 테스트세트에는 빙어만 들어있는 상태
# input_arr = np.array(fish_data)
# target_arr = np.array(fish_target)
# # print(input_arr.shape)  # 샘플 수, 특성 수 출력
# np.random.seed(42)      # random 함수는 실행할 때마다 다른 값을 생성하므로 seed 로 값 지정
# index = np.arange(49)      # 0부터 N-1 까지 1씩 증가하는 배열 생성
# np.random.shuffle(index)
# train_input = input_arr[index[:35]]
# train_target = target_arr[index[:35]]
# test_input = input_arr[index[35:]]
# test_target = target_arr[index[35:]]
# # 훈련 세트와 테스트 세트에 도미와 방어가 잘 섞여있나 확인
# # plt.scatter(train_input[:,0], train_input[:,1])
# # plt.scatter(test_input[:,0], test_input[:,1])
# # plt.xlabel(lenght)
# # plt.ylabel(weight)
# # plt.show()
#
# kn = kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))
# print(kn.predict(test_input))

# Chapter 2-2

fish_data = np.column_stack((fish_lenght, fish_weight))
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
# train_input, test_input, train_target, test_target = train_test_split(fish_data,fish_target,random_state=42)
# print(train_input.shape, test_input.shape)    # shape() - 데이터의 크기
# print(train_target.shape, test_target.shape)

# print(test_target)  # [1. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# 13개 중 도미 10,빙어 3 -> 샘플링편향
train_input, test_input, train_target, test_target = train_test_split(fish_data,fish_target,stratify=fish_target,random_state=42)
# print(test_target)  #[0. 0. 1. 0. 1. 0. 1. 1. 1. 1. 1. 1. 1.]

kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))
#
# print(kn.predict([[25,150]]))  #[0.] = 빙어

# plt.scatter(train_input[:,0],train_input[:,1])
# plt.scatter(25,150,marker='^')    # marker - 매개변수의 모양 지정
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

distance, indexes = kn.kneighbors([[25,150]])

# plt.scatter(train_input[:,0],train_input[:,1])
# plt.scatter(25,150,marker='^')    # marker - 매개변수의 모양 지정
# plt.scatter(train_input[indexes,0],train_input[indexes,1],marker='D')  # 지정샘플에 가장 가까운 5개의 샘플
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# print(train_input[indexes])  # 5개 샘플의 데이터 확인
# print(train_target[indexes])

# print(distance)  #[[92.00 130.48 130.73 138.32 138.39]]
plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(25,150,marker='^')    # marker - 매개변수의 모양 지정
plt.scatter(train_input[indexes,0],train_input[indexes,1],marker='D')  # 지정샘플에 가장 가까운 5개의 샘플
plt.xlim(0,1000)    # xlim - x축의 범위 지정
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
#page 98
