from enum import Enum


class Color(Enum):
    # def __init__(self, player_name1, player_name2):
    #     self.white_piece_player_name = player_name1
    #     self.black_piece_player_name = player_name2

    WHITE = 1
    BLACK = 2


def toOppositeColor(color: Color):
    return Color.BLACK if color == Color.WHITE else Color.WHITE
