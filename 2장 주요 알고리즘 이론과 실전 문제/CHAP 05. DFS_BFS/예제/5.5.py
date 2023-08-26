#재귀함수로 구현한 팩토리얼 예제
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))

    