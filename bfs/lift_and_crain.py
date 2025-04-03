"""
0. 지게차와 크레인 ()
https://school.programmers.co.kr/learn/courses/30/lessons/388353?language=python3

A 회사의 물류창고에는 알파벳 대문자로 종류를 구분하는 컨테이너가 세로로 n 줄, 가로로 m줄 총 n x m개 놓여 있습니다. 특정 종류 컨테이너의 출고 요청이 들어올 때마다 지게차로 창고에서 접근이 가능한 해당 종류의 컨테이너를 모두 꺼냅니다. 접근이 가능한 컨테이너란 4면 중 적어도 1면이 창고 외부와 연결된 컨테이너를 말합니다.

최근 이 물류 창고에서 창고 외부와 연결되지 않은 컨테이너도 꺼낼 수 있도록 크레인을 도입했습니다. 크레인을 사용하면 요청된 종류의 모든 컨테이너를 꺼냅니다.

물류창고-1-1.drawio.png

위 그림처럼 세로로 4줄, 가로로 5줄이 놓인 창고를 예로 들어보겠습니다. 이때 "A", "BB", "A" 순서대로 해당 종류의 컨테이너 출고 요청이 들어왔다고 가정하겠습니다. “A”처럼 알파벳 하나로만 출고 요청이 들어올 경우 지게차를 사용해 출고 요청이 들어온 순간 접근 가능한 컨테이너를 꺼냅니다. "BB"처럼 같은 알파벳이 두 번 반복된 경우는 크레인을 사용해 요청된 종류의 모든 컨테이너를 꺼냅니다.

물류창고-1-2.drawio.png

위 그림처럼 컨테이너가 꺼내져 3번의 출고 요청 이후 남은 컨테이너는 11개입니다. 두 번째 요청은 크레인을 활용해 모든 B 컨테이너를 꺼냈음을 유의해 주세요. 세 번째 요청이 들어왔을 때 2행 2열의 A 컨테이너만 접근이 가능하고 2행 3열의 A 컨테이너는 접근이 불가능했음을 유의해 주세요.

처음 물류창고에 놓인 컨테이너의 정보를 담은 1차원 문자열 배열 storage와 출고할 컨테이너의 종류와 출고방법을 요청 순서대로 담은 1차원 문자열 배열 requests가 매개변수로 주어집니다. 이때 모든 요청을 순서대로 완료한 후 남은 컨테이너의 수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
2 ≤ storage의 길이 = n ≤ 50
2 ≤ storage[i]의 길이 = m ≤ 50
storage[i][j]는 위에서 부터 i + 1번째 행 j + 1번째 열에 놓인 컨테이너의 종류를 의미합니다.
storage[i][j]는 알파벳 대문자입니다.
1 ≤ requests의 길이 ≤ 100
1 ≤ requests[i]의 길이 ≤ 2
requests[i]는 한 종류의 알파벳 대문자로 구성된 문자열입니다.
requests[i]의 길이가 1이면 지게차를 이용한 출고 요청을, 2이면 크레인을 이용한 출고 요청을 의미합니다.
테스트 케이스 구성 안내
아래는 테스트 케이스 구성을 나타냅니다. 각 그룹 내의 테스트 케이스를 모두 통과하면 해당 그룹에 할당된 점수를 획득할 수 있습니다.

그룹	총점	추가 제한 사항
#1	10%	requests에 크레인을 사용한 출고 요청만 존재합니다.
#2	15%	requests에 지게차를 사용한 출고 요청만 존재합니다.
#3	25%	requests에 컨테이너의 종류가 최대 한 번씩 등장합니다. 즉, 이전에 꺼낸 컨테이너 종류를 다시 꺼내지 않습니다.
#4	50%	제한사항 외 추가조건이 없습니다.
입출력 예
storage	requests	result
["AZWQY", "CAABX", "BBDDA", "ACACA"]	["A", "BB", "A"]	11
["HAH", "HBH", "HHH", "HAH", "HBH"]	["C", "B", "B", "B", "B", "H"]	4
입출력 예 설명
입출력 예 #1

문제 설명의 예시와 같습니다.

입출력 예 #2

물류창고-2.drawio.png

창고의 초기 상태와 모든 요청을 수행한 뒤의 상태입니다. 남은 컨테이너의 수인 4를 return 해야 합니다.
"""

def solution(storage, requests):
    def run_crain(matrix: list, container: str, boundary: list):
        for y in range(1, len(matrix) - 1):
            for x in range(1, len(matrix[0]) - 1):
                if matrix[y][x] == container:
                    matrix[y][x] = "-"
        return matrix
    
    def run_lift(matrix: list, container: str, boundary: list, direc: list):
        remove_cands = []
        for y in range(1, len(matrix) - 1):
            for x in range(1, len(matrix[0]) - 1):
                if matrix[y][x] == container:
                    for dx, dy in direc:
                        ax, ay = x + dx, y + dy
                        if is_inside(ax, ay) and boundary[ay][ax] == 1:
                            remove_cands.append((x, y))
                            break
        for x, y in remove_cands:
            matrix[y][x] = "-"
        return matrix
    
    def is_inside(x, y):
        if 0 <= x < max_x and 0 <= y < max_y:
            return True
        return False
        
    
    def bfs(matrix, direc, max_x, max_y):
        boundary = [[0] * max_x for _ in range(max_y)]
        boundary[0][0] = 1
        queue = [(0, 0)]
        while queue:
            x, y = queue.pop(0)
            for dx, dy in direc:
                ax, ay = x + dx, y + dy
                if is_inside(ax, ay) and matrix[ay][ax] == "-" and boundary[ay][ax] == 0:
                    boundary[ay][ax] = 1
                    queue.append((ax, ay))
        return boundary
        
        
     
    # padding matrix 생성
    max_y, max_x = len(storage) + 2, len(storage[0]) + 2
    matrix = [["-"] * max_x for _ in range(max_y)]
    for y in range(max_y - 2):
        for x in range(max_x - 2):
            matrix[y+1][x+1] = storage[y][x]
            
    # boundary matrix 생성
    direc = [(0,1), (1,0), (0, -1), (-1, 0)]
    boundary = bfs(matrix, direc, max_x, max_y)
    
        
    for req in requests:
        if len(req) == 1:
            matrix = run_lift(matrix, req[0], boundary, direc)
        else:
            matrix = run_crain(matrix, req[0], boundary)
        boundary = bfs(matrix, direc, max_x, max_y)
    
    answer = 0
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if matrix[y][x] != "-":
                answer += 1
    
    return answer
