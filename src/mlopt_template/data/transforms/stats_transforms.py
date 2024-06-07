"""Statistics-based transformations."""


# Use partial(means, stdevs)(normalize) to create a function
# that uses precomputed (on e.g. training data) values to
# normalize the data.
def normalize_data(data, means, stdevs):
    # FIXME we assume the data is broadcastable, which is
    # the case for pandas, polars and numpy, but not in general
    return (data - means) / stdevs


def mean(data):
    return sum(data) / len(data)


def stddev(data):
    return (sum(map(lambda x: x**2, (data - mean(data)))) / len(data)) ** (1 / 2)
