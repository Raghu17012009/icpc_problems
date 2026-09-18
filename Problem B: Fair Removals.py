t = int(input("Enter number of test cases"))
for i in range(t):
    n = int(input("Enter string length"))
    s = input("Enter the string").strip()
    ones = s.count('1')
    zeros = n - ones
    k = min(zeros, ones, n // 3)
    print(n - 3 * k)
