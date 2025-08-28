from pprint import pprint

M = [[1, 2], [4, 5], [3, 6]]

MT = [list(row) for row in zip(*M)]

pprint(MT, indent=2)
