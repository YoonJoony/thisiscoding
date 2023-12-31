**..대충 코딩테스트 하는 사람 는다는 내용**

1장, 2장은 그냥 깃허브에서 올리고 3장부터 해설로 velog에 작성해야겠다. <br>
<br>

### 온라인 개발 환경
**리플릿**<br>
협력기능이 있는 파이썬 개발 환경이다.<br><br>
**파이참**<br>
세계적으로 많이 쓰는 파이썬 개발 환경. <br>
<br>

## 복잡도 ![image](https://github.com/YoonJoony/thisiscoding/assets/110625854/387fc30c-5a6e-401f-8352-089509084322)
**복잡도** 는 알고리즘의 성능을 나타내는 척도. <br>
**시간 복잡도**와 **공간 복잡도**로 나눌 수 있다. <br>
<br>
**시간 복잡도** : 특정 크기의 입력에 대해 알고리즘이 얼마나 오래 걸리는지. <br>
**공간 복잡도** : 특정 크기의 입력에 대해 알고리즘이 얼마나 많은 메모리를 차지하는지. <br>
<br>
동일한 기능일 경우 -> 복잡도가 낮을수록 좋은 알고리즘 <br>
<br>
이 책에서는 직관적인? 이해를 위해 복잡도의 정의를 설명한다고 한다.<br><br>
**복잡도 측정 시 나오는 계산**<br>
**시간 복잡도** : 알고리즘을 위해 필요한 연산 횟수 <br>
**공간 복잡도** : 알고리즘을 위해 필요한 메모리 양 <br>
<br>

이 복잡도 둘 관계는 비례 반비례 관계다. <br>
**엄.. 메모리를 더 쓰고싶은데** ➡️ **반복되는 연산 생략 후 정보관리** <br>
이때 메모리 소모 대신 얻을 수 있는 시간적 이점이 많다고 한다.
<br><br>

## 시간 복잡도
보통 알고리즘 문제 풀 때 단순히 복잡도 하면 시간 복잡도를 의미한다. <br>
..시간 안에 동작하는 프로그램을 효율적으로 만들면 좋다는 뜻 <br><br>
**시간 복잡도 표현 방법** : 빅오 표기법 사용. <br>
간단히 말해 가장 빠르게 증가하는 항만 고려하는 표기법. <br><br>

🎨 N개의 데이터가 있을 때, 모든 데이터 값을 더한 결과 출력 <br>
~~~py
array = [1, 3, 5, 6, 7]
sum = 0

for x in array
  sum += x

print(sum)
~~~

다음 예제는 5개 데이터를 받아 5번 더해준다 (N=5).<br>
연산 횟수는 N에 비례한다.<br>
이 소스코드의 영향력이 가장 큰 부분은 N에 비례하는 연산을 수행하는 반복문<br>
시간복잡도 **O(N)** 으로 표기 
<br>
<br>
연산이 반복문 뿐 아니라 일반출력, 2중 for문 등이 존재한다. <br>
**따라서 빅오 표기법도 많아진다.** -> 정처기때 공부했쥬? <br><br>
![image](https://github.com/YoonJoony/thisiscoding/assets/110625854/5a0d432e-b2d8-4fd0-ae7d-138f8d4ff609)
<br><br><br>
하지만 빅오 표기법이 **절대적인 것은 아님** <br>
연산 횟수 : 3N^3 + 5N^2 + 1,000,000인 알고리즘이 있을 경우<br>
빅오 표기법은 **차수가 가장 큰 항만 남김** ➡️ **O(N^3)** <br><br>
❗ N = 10 일때 결과는 1,003,500이 나옴. <br>
따라서 상수의 영향이 매우 큰 경우도 있음 <br>
➡️ *빅오 표 기법이 항상 절대적인 경우는 없다.** <br>
<br><br>
**시간 복잡도 분석은 문제 풀이의 핵심.**<br>
고인물들은 알고리즘을 해석 전에 조건을 먼저 봄.<br>
➡️ 조건 확인하면 문제를 풀기 위해 얼마나 효율적인 알고리즘을 작성해야 하는지 눈치 챌 수 있음.<br>  
N이 1000만개가 넘고 제한시간이 1초면, 대략 최악의 경우 O(N)의 시간 복잡도로 동작하는 알고리즘을 작성해야 할 것이라고 예상. <br>
데이터의 탐색 범위가 100억, 1000억이 넘을 경우 이잔탐색과 같이 O(logN)의 시간 복잡도를 갖는 알고리즘을 작성. <br>
>실제로 고인물들은 **문제 조건 확인 후 사용할 알고리즘을 좁혀 나가기도 한다.**

<br>다음은 문제를 출 때 예시. 모두 시간 제한이 1초인 문제.<br>
- N의 범위가 500인 경우 : O(N^3)
- N의 범위가 2,000인 경우 : O(N^2)
- N의 범위가 100,000인 경우 : O(NlogN)
- N의 범위가 10,000,000인 경우 : O(N)
<br>

> .. 뭔지 이해안됨 <br>

## 공간 복잡도 
이 친구도 빅오 사용.<br>
시간 복잡도에서 1초라는 절대적인 제한이 있는 것처럼, <br>
**공간 복잡도도 MB기준으로 메모리 사용량이 제한됨.** <br>
ex) 메모리 128MB 기준 <br>
<br>
코딩 테스트 문제는 대부분 리스트(배열)을 사용해서 푼다. <br>
리스트의 크기가 1,000 만 단위 이상이면 알고리즘을 잘못 설계한 것. <br>
<br>

## 시간과 메모리 측정
설계한 알고리즘의 성능 확인을 위해, 시간 측정 라이브러리를 사용하는 습관을 기르자.<br><br>
🎨 선택 정렬과 기본 정렬 라이브러리 수행 시간<br>
~~~py
# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
..대충 선택 정렬 소스코드

end_time - time.time() # 측정 종료

# 기본 정렬 프로그램 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리
array.sort()

end_time = time.time() # 측정 종료
...
~~~

