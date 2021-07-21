
def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)


hello_world("HelloWorld")


def decorator(func):
    def decorated(b,h):
        if b>0 and h>0 :
            return func(find_area)
        else :
            print(error)

@decorator
def find_area(b,h):
    triangle = 1/2 * b * h
    square = b * h
    print(triangle, square)

find_area(3,4)


class User :
    def __init__(self, auth):
        self.is_authenticated = auth
    user = User(auth=False)

    r_area = rect_area(user, 1010)