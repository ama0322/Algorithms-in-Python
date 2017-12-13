import math

class ReverseInteger(object):

    @staticmethod
    def solution(self, n):
        """
        Given a 32-bit signed integer, reverse digits of an integer.

        Example 1:

        Input: 123
        Output:  321
        Example 2:

        Input: -123
        Output: -321
        Example 3:

        Input: 120
        Output: 21
        Note:
        Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
        For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

        :param n: - the inputted number
        :return: - the outputted reversed number
        """

        if n == 0:
            return 0

        BASE_TEN = 10
        reversed = 0
        digits = int(math.log10(abs(n))) + 1

        is_negative = n < 0
        n = abs(n)

        while n > 0:

            # put the last digit of n into reversed
            last_dig = n % BASE_TEN
            reversed += last_dig * pow(BASE_TEN, digits - 1)

            # if reversed overflows, return 0
            if not -2147483647 <= n <= 2147483647:
                return 0

            # update n and counter for next iteration
            n /= BASE_TEN

            digits -= 1

        if is_negative:
            reversed *= -1

        if reversed > 2147483647 or reversed < -2147483647:
            return 0

        return reversed
