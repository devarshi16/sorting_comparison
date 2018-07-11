import os
import time
import matplotlib.pyplot as plt
import numpy as np
from progress.bar import Bar

def bubble_sort(a=[]):#Modified bubble sort
	b = a
	count = 0
	for i in range(len(b)):
		swap_done = False
		for j in range(0,len(b)-i-1):
			if b[j]>b[j+1]:
				b[j],b[j+1]=b[j+1],b[j]
				swap_done = True
				count+=1
		if swap_done == False:
			break
	#print b
	return count

def insertion_sort(a = []):
    b = a
    count = 0
    for i in range(1, len(b)): 
        key = b[i] 
        j = i-1
        while j >=0 and key < b[j] :
                b[j+1] = b[j]
                j -= 1
                count+=1
        b[j+1] = key
    #print b
    return count

def selection_sort(a = []):
	b = a
	i = len(b)
	
	count = 0
	for i in range(len(b)):
		j = len(b) - i
		pos = i
		for j in range(i+1,len(b)):
			if b[pos] > b[j]:
				pos = j
				count += 1
		b[i],b[pos] = b[pos],b[i]
	#print b
	return count


def quick_sort(a = []):
	b = a
	count = sorter(0,len(b)-1,b)
	#print b
	return count

def sorter(start_index, end_index,b = []):
	if start_index < end_index:
		partition_index,count3 = partition(start_index, end_index, b)
		count1 = sorter(start_index,partition_index-1,b)
		count2 = sorter(partition_index+1,end_index,b)
		return count1+count2+count3
	else:
		return 0

def partition(start_index, end_index,b = []) :
	x = b[end_index]
	i = start_index-1
	count = 0
	for j in range(start_index,end_index):
		count+=1
		if b[j] <= x:
			i = i + 1
			b[i],b[j] = b[j],b[i]
	b[i+1],b[end_index] = b[end_index],b[i+1]
	return [i+1,count]

def merge_sort(a = []):
	b = a
	count = mergeSort(b,0,len(b)-1)
	#print b
	return count

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0     
    j = 0     
    k = l
    count = 0
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            count += 1
        else:
            arr[k] = R[j]
            j += 1
            count += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        count += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        count += 1
    return count

def mergeSort(arr,l,r):
    if l < r:
        m = (l+(r-1))/2
        count_L = mergeSort(arr, l, m)
        count_R = mergeSort(arr, m+1, r)
        count_merge = merge(arr, l, m, r)
        return count_L+count_R+count_merge
    else:
    	return 0

def compare(sort_algo,function_name):	
	var_of_ops = []
	avg_ops = []
	avg_time = []
	bar = Bar(function_name,max = 10)
	#bar = Bar(function_name,max = 100/2)
	bar = Bar(function_name, max = 400/10)
	for i in range(1,400,10):
	#for i in range(1,100,2): #UNCOMMENT FOR CHANGING INPUT SIZE
	#for i in range(0,10):
		ops = []
		times = []
		with open("randoms.txt","r") as randoms_file:
			for j in range(0,1000):
				a = randoms_file.readline().strip(',\n').split(',')
				a = map(int,a)
				start_time = time.time()
				ops.append(sort_algo(a[:i]))
				times.append(time.time()-start_time)
			avg_time.append(np.average(times))
			avg_ops.append(np.average(ops))
		bar.next()
	bar.finish()
	return [avg_ops,avg_time]

avg_count_bub_sort,avg_time_bub_sort = compare(bubble_sort,'bubble sort')
avg_count_ins_sort,avg_time_ins_sort = compare(insertion_sort,'insertion sort')
avg_count_sel_sort,avg_time_sel_sort= compare(selection_sort,'selection sort')
avg_count_quick_sort,avg_time_quick_sort= compare(quick_sort,'quick sort')
avg_count_merge_sort,avg_time_merge_sort = compare(merge_sort,'merge sort')

'''
plt.plot(avg_count_bub_sort,label='bubble sort')
plt.plot(avg_count_ins_sort,label='insertion sort')
plt.plot(avg_count_sel_sort,label = 'selection sort')
plt.plot(avg_count_quick_sort,label = 'quick sort')
plt.plot(avg_count_merge_sort,label = 'merge sort')
plt.ylabel('average no. of ops')
plt.legend(loc='best')
plt.xlabel('number of elements in array')
plt.show()
'''

plt.plot(avg_time_bub_sort, label = 'bubble_sort')
plt.plot(avg_time_ins_sort, label = 'insertion_sort')
plt.plot(avg_time_sel_sort, label = 'selection_sort')
plt.plot(avg_time_quick_sort, label = 'quick_sort')
plt.plot(avg_time_merge_sort, label = 'merge_sort')
plt.ylabel('avg time of execution')
plt.xlabel('number of elements in array')
#plt.xticks(range(0,60,10),range(0,120,20))
plt.xticks(range(0,45,5),range(0,450,50))
plt.legend(loc='best')
plt.show()