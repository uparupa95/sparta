''' 031점의 위치 구하기
사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.

x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다.
좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.
'''

# def solution(dot):
#     answer = 0
#     x = dot[0]
#     y = dot[1]
#     for i in dot:
#         if x > 0 and y > 0:
#             answer = 1
#         elif x < 0 and y > 0:
#             answer = 2
#         elif x < 0 and y < 0:
#             answer = 3
#         elif x > 0 and y < 0:
#             answer = 4
#     return answer

'''문자 반복 출력하기
문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록
solution 함수를 완성해보세요.
'''
# def solution(my_string, n):
#     answer = ''
#     for i in range(len(my_string)):
#         answer += my_string[i] * n
#     return answer
'''세균증식
어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
'''
# def solution(n, t):
#     answer = (2**t)*n
#
#     return answer
'''삼각형의 완성조건(1)
선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다.
세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.
'''
# def solution(sides):
#     answer = 0
#     sides.sort()
#     if sides[0] + sides[1] > sides[2]:
#         return answer = 1
#     else:
#         return answer = 2
'''중앙값 구하기
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때,
중앙값을 return 하도록 solution 함수를 완성해보세요.
'''
# def solution(array):
#     array.sort()
#     answer = array[(len(array)//2)]
#     return answer

'''짝수는 싫어요
정수 n이 매개변수로 주어질 때, 
n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
'''
# def solution(n):
#     answer = []
#     for i in range(n+1):
#         if i % 2 > 0:
#             answer.append(i)
#     return answer

'''순서쌍의 개수
순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다.
자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution
함수를 완성해주세요.
'''
# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             answer += 1
#     return answer
'''모음 제거
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
문자열 my_string이 매개변수로 주어질 때
모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
'''

# def solution(my_string):
#     answer = ("a,e,i,o,u")
#     for i in answer:
#         my_string = my_string.replace(i, '')
#     return my_string
'''문자 반복 출력하기
문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
'''
# def solution(my_string, n):
#     answer = ''
#     for i in range(len(my_string)):
#         answer += my_string[i] * n
#     return answer
'''옷가게 할인 받기
머쓱이네 옷가게는 10만 원 이상 사면 5%,
30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때,
지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
'''


# def solution(price):
#     answer = 0
#     if 100000 <= price < 300000:
#         answer = price * 0.95
#     elif 300000 <= price < 500000:
#         answer = price * 0.9
#     elif price >= 500000:
#         answer = price * 0.8
#     else:
#         answer = price
#
#     return int(answer)
'''제곱수 판별하기
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때,
n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
'''
# def solution(n):
#     num = n **(1/2)
#     if num % 1 == 0:
#         answer = 1
#     else:
#         answer = 2
#     return answer
'''숨어있는 숫자의 덧셈
문자열 my_string이 매개변수로 주어집니다.
my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
'''
def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer


