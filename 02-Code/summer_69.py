def summer_69(arr):

    indexcount=0

    index6=0

    index9=0

    for num in arr:

        indexcount+=1

        if num==6:

            index6=indexcount-1

        if num==9:

            index9=indexcount-1

    print([index6,index9])

    if index6==0 or index9==0:

        return sum(arr)

    else:

        return sum(arr[0:index6])+sum(arr[index9+1:])
print(summer_69([1,2,3,4,6,4,5,7]))
