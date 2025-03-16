import random

directions = {
    'start': [330, 315, 300, 60, 135, 120, 150, 30, 45, 60],
    'right_top': [15, 25, 35, 45],
    'right_bottom': [315, 325, 335, 340],
    'left_top': [135, 145, 155, 165, 175],
    'left_bottom': [190, 200, 210, 220]
}

headings = {
    'left_heading': [(random.randint(-500, -100), 370), (random.randint(-500, -100), -370)],
    'right_heading': [(random.randint(100, 500), 370), (random.randint(100, 500), -370)],
}