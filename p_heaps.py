class Heap:
    def __init__(self):
        self.maxsize = 10
        self.data = [-1] * self.maxsize
        self.csize = 0

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def insert(self, e):
        if self.csize == self.maxsize:
            print('No Space in Heap')
            return
        self.csize = self.csize + 1
        hi = self.csize
        while hi > 1 and e > self.data[hi // 2]:
            self.data[hi] = self.data[hi // 2]
            hi = hi // 2
        self.data[hi] = e

    def max(self):
        if self.csize == 0:
            print('Heap is Empty')
            return
        return self.data[1]

    def delete(self):
        if self.csize==0:
            print("Heap is empty")
            return 
        e=(self.data[1])
        self.data[1]=self.data[self.csize]
        self.data[self.csize]=-1
        self.csize-=1
        i=1
        j=i*2
        while j<=self.csize:
            if self.data[j]<self.data[j+1]:
                j+=1
            if self.data[i]<self.data[j]:
                temp=self.data[i]
                self.data[i]=self.data[j]
                self.data[j]=temp
                i=j
                j=j*2
            else:
                break
        return e



S = Heap()
S.insert(25)
S.insert(14)
S.insert(6)
S.insert(20)
S.insert(23)
print(S.data)
S.insert(40)
print(S.data)
print(S.delete())
print(S.data)

