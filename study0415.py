class Node():
    def __init__ (self):
        self.data = None
        self.link = None
        self.num = 0

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.num, end = ' ')
    print(current.data, end = ' ')

    cnt=0
    
    while (current.link != None) & (cnt<len(memory)):
        current = current.link
        print(current.num, end=' ')
        print(current.data, end=' ')
        cnt+=1
        
    print()

memory = []
head, current, pre = None,None,None
dataArray=['다현','정연','쯔위','사나','지효']

node=Node()
node.data = dataArray[0]
node.link=node
node.num=1
head=node
memory.append(node)


if __name__ == "__main__":
    
    for data in dataArray[1:]:
        pre=node
        node=Node()
        node.data=data
        node.num=len(memory)+1
        pre.link=node
        node.link=memory[0]
        memory.append(node)

    printNodes(head)


def findNode(findData):
    global memory, head, current, pre

    current=head

    if current.data==findData:
        return current

    while current.link!=head:
        current=current.link
        if current.data==findData:
            return current

    return Node()


while True:
    name=input("찾을 사람의 이름을 입력하세요(없으면 0입력) : ")
    if name!="0":
        fNode=findNode(name)
        print(fNode.num, end=' ')
        print(fNode.data)
    else:
        break


