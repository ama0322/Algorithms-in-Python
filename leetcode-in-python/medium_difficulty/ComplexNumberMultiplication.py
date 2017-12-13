class ComplexNumberMultiplication:
    def Solution(self, a, b):
        """
        Given two strings representing two complex numbers.

        You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

        Example 1:
        Input: "1+1i", "1+1i"
        Output: "0+2i"
        Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
        Example 2:
        Input: "1+-1i", "1+-1i"
        Output: "0+-2i"
        Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
        Note:

        The input strings will not have extra blank.
        The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of
        [-100, 100]. And the output should be also in this form.

        :param a: input first complex number
        :param b: input second complex number
        :return: output the multiplication of the two complex numbers
        """

        # figure out the real coefficients by starting from the 0 index and moving until the plus sign
        real_a = int(a[0: a.index("+", 0)])
        real_b = int(b[0: b.index("+", 0)])

        # figure out the imaginary components by starting from the plus sign and moving until "i"
        imag_a = int(a[a.index("+", 0, ) + 1: a.index("i", 0)])
        imag_b = int(b[b.index("+", 0, ) + 1: b.index("i", 0)])

        # construct the answer
        real_ans = real_a * real_b - imag_a * imag_b
        imag_ans = real_b * imag_a + real_a * imag_b

        return str(real_ans) + "+" + str(imag_ans) + "i"
