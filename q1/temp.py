'''
  1
 212
32123
'''


'''
class Triangle():
    def __init__(self, max):
        self._max = max
        self._temp = ''

        self.run(1)

    def run(self, count):
        if self._max >= count:
            if self._temp=='': # count == 1
                result = '1'
            else:
                result = '{}{}{}'.format(count, self._temp, count)

            print(result)
            self._temp = result
            count += 1
            return self.run(count)

        return
Triangle(5)
'''


def triangle(max, count, temp):
    
    if max >= count:
        if temp=='': # count == 1
            result = '1'
        else:
            result = '{}{}{}'.format(count, temp, count)

        print(result)
        temp = result
        count += 1
        return triangle(max, count, temp)

    return
  
    
triangle(9, 1, '')
  
  
  