class HammingDistance:
    def Solution(self, x, y):
        """
        The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

        Given two integers x and y, calculate the Hamming distance.

        Note:
        0 ≤ x, y < 231.

        Example:

        Input: x = 1, y = 4

        Output: 2

        Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
               ↑   ↑

        The above arrows point to positions where the corresponding bits are different.

        :param x: first number
        :param y: second number
        :return: hamming distance
        """

        hamming_dist = 0

        first = str(bin(x))[2:]
        second = str(bin(y))[2:]

        max_len = max(len(first), len(second))

        if len(first) > len(second):
            second = "0" * (max_len - len(second)) + second
        else:
            first = "0" * (max_len - len(first)) + first

        for x in range(len(first)):
            if not first[x] == second[x]:
                hamming_dist = hamming_dist + 1

        return hamming_dist