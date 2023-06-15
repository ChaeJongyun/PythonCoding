class JSS:
    def __init__(self):
        self.name = input("이름 :")
        self.age= input("나이: ")
        
        print("JSS 클래스 선언!")
    def show(self):
        print("나의 이름은 {},나이는{}세 입니다.".format(self.name,self.age))
        
a = JSS()
a.name
a.age
a.show()
# 여기서 a는 클래스를 지칭하는 self에 해당함
# __init__클래스 안에서 쓸때는 a.name이 아닌 self.name이라 씀
# input으로 입력하면 self.name 즉 a.name에 저장됨