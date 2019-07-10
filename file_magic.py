import tempfile


class File:
    def __init__(self, path):
        self._path = path
        self._itero = None

    def __str__(self):
        return self._path

    def __add__(self, obj):
        new_file = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)
        try:
            with open(new_file.name, 'a') as nf:
                with open(self._path, 'r') as f:
                    tmp = f.read()

                nf.write(tmp)
                with open(obj.path, 'r') as f:
                    tmp = f.read()

                nf.write('' + tmp)

            return File(new_file.name)
        except IOError as err:
            print(f'Ошибка! {err.filename}\n{err.errno} {err.strerror}')
            return None

    def __iter__(self):
        try:
            self._itero = open(self._path, 'r')
        except IOError as err:
            print(f'Ошибка! {err.filename}\n{err.errno} {err.strerror}')
        return self

    def __next__(self):
        if self._itero is None:
            raise StopIteration

        result = self._itero.readline()
        if not result:
            self._itero.close()
            raise StopIteration

        return result

    @property
    def path(self):
        return self._path

    def write(self, line):
        try:
            with open(self._path, 'a') as f:
                f.write(line)
        except IOError as err:
            print(f'Ошибка! {err.filename}\n{err.errno} {err.strerror}')
