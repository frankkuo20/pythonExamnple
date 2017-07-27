def triangle2(count):
    if count==1:
        print('1')
        return '1'
    print('{}{}{}'.format(count, triangle2(count-1), count))
    return '{}{}{}'.format(count, triangle2(count-1), count)
    
triangle2(5)
    