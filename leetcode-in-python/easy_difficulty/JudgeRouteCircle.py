def Solution(moves):
    """
    Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a
    circle, which means it moves back to the original place.

    The move sequence is represented by a string. And each move is represent by a character. The valid robot moves
    are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot
    makes a circle.

    Example 1:
    Input: "UD"
    Output: true
    Example 2:
    Input: "LL"
    Output: false

    :param moves: string representing the moves
    :return: whether or not hte robot makes a circle
    """

    pos = [0, 0]

    # go through every character in moves and move the robot(apply it to the position list)
    for i in range(0, len(moves)):

        current_char = moves[i]

        if current_char == "U":
            pos[1] = pos[1] + 1

        elif current_char == "D":
            pos[1] = pos[1] - 1

        elif current_char == "R":
            pos[0] = pos[0] + 1

        else:
            pos[0] = pos[0] - 1

    return pos[0] == 0 and pos[1] == 0
