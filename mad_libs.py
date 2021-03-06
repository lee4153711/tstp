import re

txt = '''         기린은 아주 오래 전부터 __복수형_명사__의 호기심을 자극했다.
         기린은 현재 살아 있는 __복수형_명사__ 중에서 가장 키가 크지만,
         과학자들은  기린의 __신체의_일부분__이/가 어떻게 이렇게 길어졌는지
         알아내지 못했다. 기린은 키가 __숫자__ __길이단위__에 달할 정도로 큰데,
         그 키의 대부분은 다리와 __신체의_일부분__에서 나온다.'''

def mad_libs(mls):
    hints = re.findall('__.*?__', mls)
    if hints is not None:
        for word in hints:
            new = input('입력({}):'.format(word))
            mls = mls.replace(word, new, 1)
        print('\n')
        print(mls)
    else:
        print('invalid mls')

mad_libs(txt)
