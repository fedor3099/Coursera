from abc import ABC, abstractmethod
import math
"""
Задание второй недели из ООП про абстрактный базовый класс

В этом задании вам даны 3 класса A, B, C, имеющие сходный (но не одинаковый) интерфейс. Вам необходимо создать абстрактный базовый класс Base и построить корректную схему наследования.

При выполнении следует избегать дублирования кода, и стараться следовать SOLID принципам ООП.

Кроме того, рекомендуется самостоятельно тестировать код перед отправкой, а также при написании следовать стандарту PEP 8.

"""
class Base(ABC):

    @abstractmethod
    def get_answer(self):
        pass

    @abstractmethod
    def get_score(self):
        pass

    @abstractmethod
    def get_loss(self):
        pass


class A(Base):

    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) \
               / len(ans)

    def get_loss(self):
        return sum([(x - y) * (x - y) for (x, y) in zip(self.data,
                                                        self.result)])


class B(Base):

    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_loss(self):
        return -sum([y * math.log(x) + (1 - y) * math.log(1 - x)
                     for (x, y) in zip(self.data, self.result)])

    def get_pre(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans,
                                                        self.result)]
        return sum(res) / sum(ans)

    def get_rec(self):
        ans = self.get_answer()
        res = [int(x == 1 and y == 1) for (x, y) in zip(ans,
                                                        self.result)]
        return sum(res) / sum(self.result)

    def get_score(self):
        pre = self.get_pre()
        rec = self.get_rec()
        return 2 * pre * rec / (pre + rec)


class C(Base):

    def __init__(self, data, result):
        self.data = data
        self.result = result

    def get_answer(self):
        return [int(x >= 0.5) for x in self.data]

    def get_score(self):
        ans = self.get_answer()
        return sum([int(x == y) for (x, y) in zip(ans, self.result)]) \
               / len(ans)

    def get_loss(self):
        return sum([abs(x - y) for (x, y) in zip(self.data,
                                                 self.result)])
