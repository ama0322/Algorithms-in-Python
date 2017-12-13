class ZigZagConversion:
    @staticmethod
    def solution(self, s, numRows):
        """
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
        display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
        And then read line by line: "PAHNAPLSIIGYIR"
        Write the code that will take a string and make this conversion given a number of rows:

        string convert(string text, int nRows);
        convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

        :param s: - the inputted string
        :param numRows:
        :return:
        """

        # Edge Case
        if numRows == 1:
            return s

        # Edge Case
        if numRows == 2:

            first_half = ""
            second_half = ""

            for i in range(0, len(s)):
                if i % 2 == 0:
                    first_half = first_half + s[i]
                else:
                    second_half = second_half + s[i]
            return first_half + second_half

        # Edge Case
        if len(s) <= numRows:
            return s



        converted = ""
        row = 0

        # boolean to determine whether this current character is in a column of the zig zag or a diagonal
        straight_col = True

        # Create a 2 dimensional list of lists to store the zigzag pattern
        zig_zag = [[] for i in range(0, numRows)]

        # put the characters from s into zig_zag in proper format
        for i in range(0, len(s)):

            current_char = s[i]

            # if in straight_column, put the current character into the proper list
            if straight_col:
                zig_zag[row].append(current_char)

                # if no longer in straight column, update straight_col and move the row back for the diagonal
                if row + 1 == numRows:
                    straight_col = False
                    row = row - 1

                # otherwise, move on to the next row
                else:
                    row = row + 1


            # when not in straight_col, AKA in the diagonal. Put the current_char in to the proper list
            else:
                zig_zag[row].append(current_char)

                # if no longer in the diagonal, update straight_col and move the row back for the straight col
                if row - 1 == 0:
                    straight_col = True
                    row = row - 1  # should be zero

                # otherwise, move onto the next row
                else:
                    row = row - 1
            # END OF LOOP

        # figure out the converted strings based on the zigzag list
        for i in range(0, len(zig_zag)):
            for x in range(0, len(zig_zag[i])):
                converted = converted + zig_zag[i][x]

        return converted
