PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, name, is_long=False):
        self.name = name
        self.dur = is_long

    def __str__(self):
        if self.dur is True:
            if self.name == 'до':
                return self.name + '-о'
            elif self.name == 'ре':
                return self.name + '-э'
            elif self.name == 'ми':
                return self.name + '-и'
            elif self.name == 'фа':
                return self.name + '-а'
            elif self.name == 'соль':
                return 'со-оль'
            elif self.name == 'ля':
                return self.name + '-а'
            elif self.name == 'си':
                return self.name + '-и'
        else:
            return self.name


class LoudNote(Note):
    def __init__(self, name, is_long=False):
        self.name = name
        self.dur = is_long
        super().__init__(name, is_long)

    def __str__(self):
        if self.dur is True:
            if self.name == 'до':
                return (self.name + '-о').upper()
            elif self.name == 'ре':
                return (self.name + '-э').upper()
            elif self.name == 'ми':
                return (self.name + '-и').upper()
            elif self.name == 'фа':
                return (self.name + '-а').upper()
            elif self.name == 'соль':
                return 'со-оль'.upper()
            elif self.name == 'ля':
                return (self.name + '-а').upper()
            elif self.name == 'си':
                return (self.name + '-и').upper()
        else:
            return self.name.upper()


class DefaultNote(Note):
    def __init__(self, name='до', is_long=False):
        self.name = name
        self.dur = is_long
        super().__init__(name, is_long)


class NoteWithOctave(Note):
    def __init__(self, name, octave, is_long=False):
        self.name = name
        self.octave = octave
        self.dur = is_long
        super().__init__(name, is_long)

    def __str__(self):
        if self.dur is True:
            if self.name == 'до':
                return f'{self.name}-о ({self.octave})'
            elif self.name == 'ре':
                return f'{self.name}-э ({self.octave})'
            elif self.name == 'ми':
                return f'{self.name}-и ({self.octave})'
            elif self.name == 'фа':
                return f'{self.name}-а ({self.octave})'
            elif self.name == 'соль':
                return f'со-оль ({self.octave})'
            elif self.name == 'ля':
                return f'{self.name}-а ({self.octave})'
            elif self.name == 'си':
                return f'{self.name}-и ({self.octave})'
        else:
            return f'{self.name} ({self.octave})'
