def push_data(stack, data):
    global top, count
    
    if len(stack) < count:
        top+=1
        stack.insert(top,data)
    else:
        print('스택 개수 한도를 초과하였습니다.')
        return

def pop_data(stack):
    global top
    if isStackEmpty(stack) == False:
        print(f'top -> {stack[top]}')
        del stack[top]
        top-=1
    else:
        print('데이터가 없습니다.')
    
def isStackFull(stack):
    global count
    if len(stack) == count:
        return True
    else:
        return False

def isStackEmpty(stack):
    global top
    if top == -1:
        return True
    else:
        return False
    

data_list=['a','b','c','d','e']

stack = []
top = -1
count = int(input('스택 개수 한도를 입력하세요 : '))

for i in data_list:
    push_data(stack, i)

push_data(stack,'f')

print(stack)

print(f'isStackFull? -> {isStackFull(stack)}')

for i in range(len(stack)):
   pop_data(stack)

pop_data(stack)
