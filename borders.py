from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.polygon import Polygon

def caution(color):
    border = []
    # top border
    border.append(Polygon([
        (0, 0), (1, 0),
        (0, 1), (2, 1),
        (1, 2), (3, 2),
        (2, 3), (4, 3)
    ], outline=color))

    border.append(Polygon([
        (5, 0), (7, 0),
        (6, 1), (8, 1),
        (7, 2), (9, 2),
        (8, 3), (10, 3)
    ], outline=color))

    border.append(Polygon([
        (11, 0), (13, 0),
        (12, 1), (14, 1),
        (13, 2), (15, 2),
        (14, 3), (16, 3)
    ], outline=color))

    border.append(Polygon([
        (17, 0), (19, 0),
        (18, 1), (20, 1),
        (19, 2), (21, 2),
        (20, 3), (22, 3)
    ], outline=color))

    border.append(Polygon([
        (23, 0), (25, 0),
        (24, 1), (26, 1),
        (25, 2), (27, 2),
        (26, 3), (28, 3)
    ], outline=color))

    border.append(Polygon([
        (29, 0), (31, 0),
        (30, 1), (32, 1),
        (31, 2), (33, 2),
        (32, 3), (34, 3)
    ], outline=color))

    border.append(Polygon([
        (35, 0), (37, 0),
        (36, 1), (38, 1),
        (37, 2), (39, 2),
        (38, 3), (40, 3)
    ], outline=color))

    border.append(Polygon([
        (41, 0), (43, 0),
        (42, 1), (44, 1),
        (43, 2), (45, 2),
        (44, 3), (46, 3)
    ], outline=color))

    border.append(Polygon([
        (47, 0), (49, 0),
        (48, 1), (50, 1),
        (49, 2), (51, 2),
        (50, 3), (52, 3)
    ], outline=color))

    border.append(Polygon([
        (53, 0), (55, 0),
        (54, 1), (56, 1),
        (55, 2), (57, 2),
        (56, 3), (58, 3)
    ], outline=color))

    border.append(Polygon([
        (59, 0), (61, 0),
        (60, 1), (62, 1),
        (61, 2), (63, 2),
        (62, 3), (64, 3)
    ], outline=color))

    # bottom border
    border.append(Polygon([
        (0, 28), (1, 28),
        (0, 29), (2, 29),
        (1, 30), (3, 30),
        (2, 31), (4, 31)
    ], outline=color))

    border.append(Polygon([
        (5, 28), (7, 28),
        (6, 29), (8, 29),
        (7, 30), (9, 30),
        (8, 31), (10, 31)
    ], outline=color))

    border.append(Polygon([
        (11, 28), (13, 28),
        (12, 29), (14, 29),
        (13, 30), (15, 30),
        (14, 31), (16, 31)
    ], outline=color))

    border.append(Polygon([
        (17, 28), (19, 28),
        (18, 29), (20, 29),
        (19, 30), (21, 30),
        (20, 31), (22, 31)
    ], outline=color))

    border.append(Polygon([
        (23, 28), (25, 28),
        (24, 29), (26, 29),
        (25, 30), (27, 30),
        (26, 31), (28, 31)
    ], outline=color))

    border.append(Polygon([
        (29, 28), (31, 28),
        (30, 29), (32, 29),
        (31, 30), (33, 30),
        (32, 31), (34, 31)
    ], outline=color))

    border.append(Polygon([
        (35, 28), (37, 28),
        (36, 29), (38, 29),
        (37, 30), (39, 30),
        (38, 31), (40, 31)
    ], outline=color))

    border.append(Polygon([
        (41, 28), (43, 28),
        (42, 29), (44, 29),
        (43, 30), (45, 30),
        (44, 31), (46, 31)
    ], outline=color))

    border.append(Polygon([
        (47, 28), (49, 28),
        (48, 29), (50, 29),
        (49, 30), (51, 30),
        (50, 31), (52, 31)
    ], outline=color))

    border.append(Polygon([
        (53, 28), (55, 28),
        (54, 29), (56, 29),
        (55, 30), (57, 30),
        (56, 31), (58, 31)
    ], outline=color))

    border.append(Polygon([
        (59, 28), (61, 28),
        (60, 29), (62, 29),
        (61, 30), (63, 30),
        (62, 31), (64, 31)
    ], outline=color))

    return border
