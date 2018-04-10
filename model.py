#model.py
import csv

BB_FILE_NAME = 'umbball.csv'
FB_FILE_NAME = 'umfootball.csv'

b_seasons = []


def init_ball(csv_file_name):
    global b_seasons
    b_seasons = []  # reset, start clean

    with open(csv_file_name) as f:
        reader = csv.reader(f)
        if csv_file_name == BB_FILE_NAME:
            next(reader)  # throw away headers
            next(reader)  # throw away headers
            raw = list(reader)
        elif csv_file_name == FB_FILE_NAME:
            next(reader)  # throw away headers
            raw = list(reader)
        else:
            raw = []

    for r in raw:
        if csv_file_name == BB_FILE_NAME:
            b_seasons.append([r[1], int(r[3]), int(r[4]), float(r[5])])
        elif csv_file_name == FB_FILE_NAME:
            b_seasons.append([r[1], int(r[3]), int(r[4]), float(r[6])])


def get_ball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 0
    elif sortby == 'wins':
        sortcol = 1
    elif sortby == 'pct':
        sortcol = 3
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(b_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
