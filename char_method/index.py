text = "Hello, World!"
try:
    position = text.index("World")
    print(position)
except ValueError:
    print("찾는 문자열이 없습니다.")
