'''
docekr run -itd --name=python3 -v ${pwd}:/code python
docker exec python3 python /code/temp5.py
'''
def triangle(count):
    if count==1:
        return '\n1'
    return '{}\n{}{}{}'.format(triangle(count-1), count, triangle(count-1).rsplit('\n', 1)[1], count)
    
print(triangle(5))