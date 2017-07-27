def countup(max, count=2, temp='1'):
    print(temp)
    if max >= count:
        countup(max, count + 1, '{}{}{}'.format(count, temp, count)) 
countup(5)