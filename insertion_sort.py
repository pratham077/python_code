sample_list = [4,7,3,1,8,5,2,6]
#sample_list = [1,4,5,3,2]

for i in range(len(sample_list) - 1):
    print("i : " + str(i) + " sample_list : " + str(sample_list) +  " comparing " + str(sample_list[i]) +  " and " + str(sample_list[i+1]))
    if sample_list[i+1] < sample_list[i]:
        print("inserting " + str(sample_list[i+1]) + " in the right place")
        temp = sample_list[i+1]
        j = i
        while j >= 0:
            if temp < sample_list[j]:
                sample_list[j+1] = sample_list[j]
                print("i : " + str(i) + " j : " + str(j) + " temp : " + str(temp) + " sample_list : " + str(sample_list))
                if j > 0:
                    j -= 1
                else:
                    sample_list[j] = temp
                    print("i : " + str(i) + " j : " + str(j) + " temp : " + str(temp) + " sample_list : " + str(sample_list))
                    break
            else:
                sample_list[j+1] = temp
                print("i : " + str(i) + " j : " + str(j) + " temp : " + str(temp) + " sample_list : " + str(sample_list))
                break

print(sample_list)
