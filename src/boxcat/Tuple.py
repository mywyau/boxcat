from typing import Callable, TypeVar, Tuple

from boxcat.Option import Option
from boxcat.Seq import Seq

T = TypeVar('T')
U = TypeVar('U')


class ProductO:

    values: tuple['Option[T]', ...]

    def __init__(self, *options: 'Option[T]'):
        self.values = options

    def mapN(self, func: Callable[..., U]) -> 'Option[U]':
        mapped_values = [opt.value for opt in self.values if opt is not None]
        if len(mapped_values) == len(self.values):
            return Option(func(*mapped_values))
        else:
            return Option()

    def get(self):
        return self.values


class ProductSeq:

    values: tuple['Seq[T]', ...]

    def __init__(self, *sequences: 'Seq[T]'):
        self.values = sequences

    def mapN(self, func) -> 'Seq[U]':
        return Seq([func(Seq(items.list)) for items in self.values])

    def get(self):
        return self.values


if __name__ == "__main__":
    opt1 = Option(1)
    opt2 = Option(2)
    opt3 = Option(3)

    productO = (
        ProductO(
            opt1,
            opt2,
            opt3
        )
        .mapN(lambda x, y, z: x + y + z)
        .unsafe_get()
    )

    print(productO)

    seq1 = Seq([1, 2, 3, 4])
    seq2 = Seq([4, 5, 6, 4])
    seq3 = Seq([7, 8, 9, 4])

    productSeq = (
        ProductSeq(
            seq1,
            seq2,
            seq3,
        )
        .mapN(lambda x: x.fold_left(0)(lambda i, j: i + j))
        .to_list()
    )

    print(productSeq)
