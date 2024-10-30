result = '9001'
count = 0
for indx in range(len(result)):
    if indx < len(result) - 2:
        if result[indx] != '0':
            count += int(result[indx] + '0' * (len(result) - indx - 1))
    else:
        if int(result[indx: indx + 2]) in range(10, 20):
            count += int(result[indx: indx + 2])
            break
        else:
            count += int(result[indx] + '0' * (len(result) - indx - 1))
print(count)
            
    
