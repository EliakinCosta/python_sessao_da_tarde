def decorate(func):
    def inner():
        print('running inner')
    return inner


@decorate
def target():
    print('running target')

#ou

def target():
    print('running target')

target = decorate(target)

if __name__=='__main__':
    target()
