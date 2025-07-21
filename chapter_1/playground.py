# # ABS
#
# some_integer : int = -545
#
# print(abs(some_integer))
#
# # ALL
#
# some_bools = [True, True, False]
#
# print(all(some_bools))
# print(any(some_bools))


class ListSum:

    def __init__(self, some_digits : list[int]):
        if (not isinstance(some_digits, list)):
            raise Exception("Input must be List")

        if not all( [isinstance(i,int) for i in some_digits] ):
            raise Exception("All of the elements of list must be integers")


        self.some_digits = some_digits


    def __add__(self, other : list):

        # result = []
        # for index, element in enumerate(self.some_digits):
        #     result.append(self.some_digits[i] + other.some_digits[i])
        # return result

        return [element + other.some_digits[i] for i, element in enumerate(self.some_digits)]

    def __len__(self):
        return len(self.some_digits)

    def __getitem__(self, index):
        return self.some_digits[index]

    def __call__(self, *args, **kwargs):
        print("Some one called me")


print()
