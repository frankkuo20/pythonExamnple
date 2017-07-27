'''
docekr run -itd --name=python3 -v ${pwd}:/code python -w /code
docker exec python3 python /code/temp5.py
'''
def max(numList, n):
    if n == 1:
        return numList[1]
    x = max(numList, n-1)
    if numList[n]> x:
        return numList[n]
    return x
    
print(max([1, 3, 205, 200, 150, 10], 5))

    "editor.fontSize": 16, 
    "terminal.integrated.fontSize": 16