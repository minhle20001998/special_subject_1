month = ['Janruary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
arr = list(map( int, input().split('/') ))
res = "{0} {1}, {2}".format(month[arr[0] - 1], arr[1], arr[2])
print(res)