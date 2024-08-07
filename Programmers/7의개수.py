
"""
문제 풀이의 핵심: 문자로 인식 or 숫자로 인식
"""
def solution(array):
    answer = 0
    
    for i in range(len(array)):
        a = list(str(array[i]))
        for j in a:
            if j == '7':
                answer+=1
        
    return answer