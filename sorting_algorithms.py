# l = [4,7,3,1,8,5,2,6]
#
# def bubble_sort(sample_list):
#     changed = True
#     while changed:
#         changed = False
#         for i in range(len(sample_list) - 1 ):
#             if sample_list[i+1] < sample_list[i]:
#                 temp = sample_list[i+1]
#                 sample_list[i+1] = sample_list[i]
#                 sample_list[i] = temp
#                 changed = True
#         #print(sample_list)
#
# bubble_sort(l)

# l = [4,7,3,1,8,5,2,6]
#
# def insertion_sort(sample_list):
#     for i in range(len(sample_list) - 1):
#         if sample_list[i+1] < sample_list[i]:
#             temp = sample_list[i+1]
#             j = i
#             while j >= 0:
#                 if temp < sample_list[j]:
#                     sample_list[j+1] = sample_list[j]
#                     if j > 0:
#                         j -= 1
#                     else:
#                         sample_list[j] = temp
#                         break
#                 else:
#                     sample_list[j+1] = temp
#                     break
#
# insertion_sort(l)
#
# print(l)

#l = [4,7,3,1,8,5,2,6]

# def selection_sort(sample_list):
#     for i in range(len(sample_list)):
#         min_value = sample_list[i]
#         min_index = i
#
#         for j in range(i,len(sample_list)):
#             if sample_list[j] < min_value:
#                 min_value = sample_list[j]
#                 min_index = j
#         if min_index != i:
#             temp = sample_list[i]
#             sample_list[i] = min_value
#             sample_list[min_index] = temp
#     #print("i : " + str(i) + " min_index : " + str(min_index) + " min_value : " + str(min_value) + " sample_list : " + str(sample_list))
#
# selection_sort(l)
#
# print(l)

## recursive implementation of selection sort
# def selection_sort(sample_list,start):
#     min_value = sample_list[start]
#     min_index = start
#     for j in range(start,len(sample_list)):
#         if sample_list[j] < min_value:
#             min_value = sample_list[j]
#             min_index = j
#     if min_index != start:
#         temp = sample_list[start]
#         sample_list[start] = min_value
#         sample_list[min_index] = temp
#     if start == len(sample_list) - 1:
#         return
#     else:
#         selection_sort(sample_list,start+1)
#
# selection_sort(l,0)
#
# print(l)

def merge_sort(sample_list):
    if len(sample_list) < 2:
        return sample_list[:]
    else:
        middle = int(len(sample_list)/2)
        left = merge_sort(sample_list[:middle])
        right = merge_sort(sample_list[middle:])
        #print("left : " + str(left) + " right " + str(right))
        return merge(left,right)

def merge(left,right):
    i,j = 0,0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    #print("result : " + str(result))
    return result

l = [4,7,3,1,8,5,2,6]

sorted_l =  merge_sort(l)
print(sorted_l)
