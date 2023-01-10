class UtilHelper:

    # a safe version of [].index that does not throw an error if the value does not exist in the array, but rather returns a -1
    @staticmethod
    def safeIndex(array, value):
        try:
            return array.index(value)
        except ValueError:
            return -1