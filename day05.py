# day05
import random

# def calculate_fee(*args):
def calculate_fee(args):    # * - age를 tuple type으로 추출
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: [전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료]
    """

    total = 0
    adults = 0
    kids = 0

    for age in args:
        if 19 <= age:
            total = total + 10000
            adults += 1

        else:
            total = total + 3000
            kids += 1

    return [len(args), adults, kids, total]

how_many = int(input("몇 분이서 오셨나요? (숫자로 입력) : "))
age_list = [random.randint(1, 60) for age in range(0, how_many)]
results = calculate_fee(age_list)
print(f'총 {results[0]}분 방문하셨으며, 어른은 {results[1]}명, 아이는 {results[2]}명이므로 지불할 총 요금은 {results[3]}원 입니다.')

# print(calculate_fee(20, 20, 25))
# print(calculate_fee(45, 43, 10))

# print(f'나이는 {age}총 요금은 {calculate_fee()}입니다.')