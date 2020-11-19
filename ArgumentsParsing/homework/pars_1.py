import os
import argparse


def file_names(start_year, end_year, path_to_source_files):
    all_files = os.listdir(path_to_source_files)
    filtered_files = list(filter(lambda year: start_year <= year <= end_year, all_files))
    return filtered_files


def merge_files(source_files, path_to_source, destination_filename, path_to_destination):
    with open(os.path.join(path_to_destination, f'{destination_filename}.csv'), 'a') as f:
        for csv_file in reversed(source_files):
            with open(os.path.join(path_to_source, csv_file), 'r') as file:
                for line in file:
                    f.write(line)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('-sy', '--start_year', required=False, default=1998, dest='start_year')
    parser.add_argument('-ey', '--end_year', required=False, default=2008, dest='end_year')
    parser.add_argument('-pf', '--path_to_source_files', required=True, dest='path_to_source_files')
    parser.add_argument('-dp', '--destination_path', required=False, default='.', dest='destination_path')
    parser.add_argument('-df', '--destination_filename', required=False, default=' ', dest='destination_filename')
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_arguments()
    files = file_names(arguments.start_year, arguments.end_year, arguments.path_to_source_files)
    merge_files(files, arguments.path_to_source_files, arguments.destination_filename, arguments.destination_path)
