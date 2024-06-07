from attrs import define
from itertools import batched as batch_itr
from typing import List, Iterable


@define
class DataSet:
    target: str | List[str] | None
    predictors: List[str]
    data: Iterable  # not really

    def get_X(self):
        # FIXME what if it's not subscriptable?
        return self.data[self.predictors]

    def get_y(self):
        # FIXME what if there's no target because it's unsupervised?
        return self.data[self.target]

    def batched(self, n_batches: int = 1):
        """Turns the data into an iterator of N batches.

        The iterator returns pairs of X, y objects.

        Example usage:

        >>> for X, y in ds.batched(100):
        >>>     my_nn_model.train_batch(X, y)
        """
        # assert n_batches > 0
        return batch_itr(zip(self.get_X(), self.get_y()), n_batches)
