try:
    a = 1 / 0
except Exception as e:
    print(e)

try:
    with open('test1.txt') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up")

