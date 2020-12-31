from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

# 생선분류 문제
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# 도미의 길이,무게
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
# 빙어의 길이,무게
#
# plt.scatter(bream_length,bream_weight)
# plt.scatter(smelt_length,smelt_weight)
# plt.xlabel('lenght')         # X축은 길이
# plt.ylabel('weight')         # Y축은 무게
# plt.show()

# 머신러닝 프로그램
lenght = bream_length + smelt_length
weight = bream_weight + smelt_weight
# fish_data = [[l, w] for l, w in zip(lenght, weight)]
# fish_target = [1] * 35 + [0] * 14
#
kn = KNeighborsClassifier()
# kn.fit(fish_data, fish_target)     # fit() = training method
# kn.score(fish_data, fish_target)     # score() = 평가 method(0~1)
# kn.predict([[30,600]])       # 길이 30, 무게 600인 생선은 도미일까 광어일까?
#
# kn49 = KNeighborsClassifier(n_neighbors=49)    # 참고 데이터를 49개로 한 모델
# kn49.fit(fish_data, fish_target)
# kn49.score(fish_data, fish_target)
# # Question - 기본값 5~49 중 정확도가 1.0 이하인 이웃의 수는?
# for n in range(5,50):
#   kn.n_neighbors = n
#   score = kn.score(fish_data, fish_target)
#   if score < 1:
#     print(n, score)
#     break
#Chapter2
fish_lenght = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0,
               6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]
fish_data = [[l, w] for l, w in zip(fish_lenght,fish_weight)]
fish_target = [1]*35 + [0]*14

train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]

kn = kn.fit(train_input,train_target)
kn.score(test_input,test_target)

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)
# print(input_arr.shape)  # 샘플 수, 특성 수 출력
np.random.seed(42)      # random 함수는 실행할 때마다 다른 값을 생성하므로 seed 로 값 지정
index = np.arange(49)      # 0부터 N-1 까지 1씩 증가하는 배열 생성
np.random.shuffle(index)
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]
# 훈련 세트와 테스트 세트에 도미와 방어가 잘 섞여있나 확인
# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(test_input[:,0], test_input[:,1])
# plt.xlabel(lenght)
# plt.ylabel(weight)
# plt.show()

kn = kn.fit(train_input, train_target)
print(kn.score(test_input, test_target))
print(kn.predict(test_input))