'''
문제 잘못 이해 빵-야채-고기-빵 순서인데 빵-야채-고기만 있으면 된다고 생각... => 정확성 33.3
'''
def solution(ingredient):
    answer = 0
    stack = [0]
    
    for i in ingredient:
        if i == 1:
            stack.append(i)
        elif i == 2:
            if stack[-1] == 1:
                stack.append(i)
            else:
                stack = [0]
        elif i == 3:
            if stack[-1] == 2: 
                stack.append(i)
                answer += 1
                stack = [0]
            else:
                stack = [0]
            
    return answer