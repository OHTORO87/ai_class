
class Date(object):
    def  __init__(self, year, month):
        self.year = year
        self.month = month
#self.month = month
#좌측은 멤버변수 우측은 내가 넘겨받은 값        

    def disp_Date(self):
        print('{}년 {}월'.format(self.year, self.month))

# __del__ 없어도 상관없다.


class Man(object):
    # class 이름은 Man
    # object를 상속받겠다는 의미

    #현재 객체 생성개수를 알고 싶을때
    ##class변수
    ##class내부에서만 접근가능    
    cnt = 0 
    
    #@붙은거 '장식자' 라고함(데코레이터)
    #고정되어있는 method라는 말. 
    @staticmethod
    def get_cnt1():
        return Man.cnt

    #class 전체에 소속되어있는 method
    @classmethod
    def get_cnt2(cls): # cls라는 인수는 전달 받겠다는 의미
        return Man.cnt

    #객체 생성시 자동호출되는 함수
    #(생성자 : constructor)
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Man.cnt += 1
        print(' Man __init__')
    
    #객체 소멸시 자동호출되는 함수
    #(소멸자 : distructor)
    def __del__(self):
        print(' Man __del__')

    #객체 출력시 자동으로 호출되는 함수, 기본값은 객체의 id값
    #이게 없으면 주소값(id)만 호출된다
    def __str__(self): 
        return ' {}님은 {}살'.format(self.name, self.age)


    #같은 내용의 또다른 손흥민 m3와 m1이 같게 만들어주는과정?
    #method 재정의_동일한 함수 재정의?(override : 덮어쓰는거)
    #(__eq__의 용도를 다른 용도로 만들어줌)
    def __eq__(self, ohter):
        if self.name == ohter.name and self.age == ohter.age:
            return True
        else:
            return False

    def __add__(self, num):
        self.age = self.age + num

    def __sub__(self, num):
        self.age -= num
        
    def disp_Man(self):
        print( '{}님은 {}살'.format(self.name, self.age))

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

print('현재 객체생성수는 : {}'.format(Man.cnt))
# 위아래 똑같음(표현방식의 차이 알고있기)
print('현재 객체생성수는 : {}'.format(Man.get_cnt1()))

m1 = Man( '손흥민', 30)
m2 = Man(' 이강인', 21)
m3 = Man(' 손흥민', 30)

print('현재 객체생성수는 : {}'.format(Man.cnt))
# 위아래 똑같음
print('현재 객체생성수는 : {}'.format(Man.get_cnt2()))
####### cnt2뒤에 ()생략해서 오류났었다 ########

print(m1) #str 함수를 호출한다.
print(m2) 
#print(m1.__str__()) print(m1)과 같은 표현이다. 
#print(m2.__str__()) 

print(m1 == m3)

m1 + 2 #이거 가능하게 하기 위해 위에서 def __add__만든거임
m2 - 4 #안만들었으면 이거 안됨.
m1.disp_Man()
m2.disp_Man()
#()에 숫자를 넣으면 숫자만큼 출력된다
#default값은 1인듯?

d1 = Date(2020 , 10)
d2 = Date(2121 , 5)