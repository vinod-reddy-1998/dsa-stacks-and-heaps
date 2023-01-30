# it works min priority call ..


import heapq as heap
l1=[]
heap.heappush(l1,23)
heap.heappush(l1,2)
heap.heappush(l1,43)
heap.heappush(l1,28)
heap.heappush(l1,43)
heap.heappush(l1,78)
print(l1)
e=heap.heappushpop(l1,89)
k=heap.heappop(l1)
print(k,e)
print(l1)


# we can directly heapify the function.
# by heap.heapify(list)
# samllest by heap.nsmallest(3,l1)