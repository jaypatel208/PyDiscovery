def stray(arr):
    if len(arr) >= 3:
       return min(arr,key=arr.count)
    return None