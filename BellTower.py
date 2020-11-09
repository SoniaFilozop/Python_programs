class Bell:
    def __init__(self, *args, **kwargs):
        self.args = []
        for arg in args:
            self.args.append(arg)
        self.kwargs = {kwarg: kwargs[kwarg] for kwarg in sorted(kwargs)}

    def print_info(self):
        k = 0
        if not self.args and not self.kwargs:
            print('-')
        else:
            for key, val in self.kwargs.items():
                print(key, end=': ')
                k += 1
                if k != len(self.kwargs):
                    print(val, end=', ')
                else:
                    if self.args:
                        print(val, end='; ')
                    else:
                        print(val, end='')
            print(', '.join(self.args))


class LittleBell(Bell):
    def sound(self):
        print('ding')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        self.d = 0
        self.args = []
        for arg in args:
            self.args.append(arg)
        self.kwargs = {kwarg: kwargs[kwarg] for kwarg in sorted(kwargs)}
        super().__init__(*args, **kwargs)

    def sound(self):
        self.d += 1
        if self.d % 2 != 0:
            print('ding')
        else:
            print('dong')


class BellTower(LittleBell, BigBell):
    def __init__(self, *args):
        self.bell = []
        for arg in args:
            self.bell.append(arg)
        super().__init__()

    def append(self, bell):
        self.bell.append(bell)

    def sound(self):
        for bell in self.bell:
            bell.sound()
        print('...')
