import argparse
import csv
from statistics import mode
from time import gmtime, strftime


def found_grade(source_file_path):
    max_grade = 0
    current_number = 0
    max_number_of_row = 0
    with open(arguments.source_file_path, 'r') as csv_data:
        beer_dict = csv.DictReader(csv_data)
        for row in beer_dict:
            current_number += 1
            current_grade = (float(row.get('review_overall')) +
                             float(row.get('review_aroma')) +
                             float(row.get('review_taste')))
            if max_grade < current_grade:
                max_grade = current_grade
                max_number_of_row = current_number
    return max_number_of_row


def get_type_beer(source_file_path, row_number):
    current_number = 0
    with open(arguments.source_file_path, 'r') as csv_data:
        beer_dict = csv.DictReader(csv_data)
        for row in beer_dict:
            current_number += 1
            if current_number == row_number:
                print('The best type of beer:', row.get('beer_style'), '\n')
                return


def popular_name(source_file_path):
    beer_list = []
    with open(arguments.source_file_path, 'r') as csv_data:
        beer_dict = csv.DictReader(csv_data)
        for row in beer_dict:
            beer_list.append(row['beer_name'])
    print(f'The most popular name is: {mode(beer_list)}\n')


def best_day(source_file_path):
    days = {}
    with open(arguments.source_file_path, 'r') as csv_data:
        beer_dict = csv.DictReader(csv_data)
        for row in beer_dict:
            day = strftime(f'"%a, %d %b %Y +0000"', gmtime(float(row['review_time'])))
            if day in days:
                days[day] += 1
            else:
                days[day] = 0
        print(f'The most viwed day is {max(days, key=lambda key: days[key])}\n')


def count_review(source_file_path):
    reviews = {}
    with open(arguments.source_file_path, 'r') as csv_data:
        beer_dict = csv.DictReader(csv_data)
        for row in beer_dict:
            reviewer = row.get('review_profilename')
            if reviewer in reviews:
                reviews[reviewer] += 1
            else:
                reviews[reviewer] = 0
            max_key = max(reviews, key=lambda key: reviews[reviewer])
        print(f'The number {reviews.get(max_key)} of reviews of reviwer: {max_key}')


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-sp', '--source_file_path',
                        required=True,
                        dest='source_file_path')
    parser.add_argument('-bt', '--beer_type',
                        required=False,
                        dest='beer_type',
                        action='store_true',
                        help='find most favorite beer type')
    parser.add_argument('-bn', '--beer_name',
                        required=False,
                        dest='beer_name',
                        action='store_true',
                        help='find most favorite beer name')
    parser.add_argument('-dr', '--day_of_review',
                        required=False,
                        action='store_true',
                        dest='day_of_review',
                        help='find day with they most number of review')
    parser.add_argument('-rs', '--reviewer_stats',
                        required=False,
                        dest='reviewer_stats',
                        action='store_true',
                        help='Show number of reviews for reviewer')
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    if arguments.beer_type:
        max_row = found_grade(arguments.source_file_path)
        get_type_beer(arguments.source_file_path, max_row)
    if arguments.beer_name:
        popular_name(arguments.source_file_path)
    if arguments.day_of_review:
        best_day(arguments.source_file_path)
    if arguments.reviewer_stats:
        count_review(arguments.source_file_path)
