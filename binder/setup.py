#!/usr/local/bin/python3

import sys
import argparse
import xlrd
import re
import math
import logging
import os
import fnmatch

from shutil import copyfile

def parse_args(args):
    parser = argparse.ArgumentParser(description='Process index file and document directory.')
    parser.add_argument('--document-directory', '-d', dest='doc_dir', required=True, help='absolute path to document directory')
    parser.add_argument('--index-file', '-i', dest='index_file', required=True, help='absolute path to index file')
    parser.add_argument('--table-start', '-s', dest='table_start', required=True, help='top left cell of index table (including headers)')
    parser.add_argument('--output-directory', '-o', dest='out_dir', required=True, help='output directory')
    parser.add_argument('--force', '-f', dest='force', action='store_true', help='overwrite existing files with name conflicts in output directory')
    return parser.parse_args(args)

def base_26_characters_to_base_10(letters):
    acc = 0
    for i, char in enumerate(reversed(letters.upper())):
        acc += int(math.pow(26, i)) * (1 + ord(char) - ord('A'))
    return acc - 1

def parse_excel_cell_name(cell):
    rexp='([a-z]+)([0-9]+)'
    match = re.match(rexp, cell, re.I)
    if not match:
        raise ValueError

    groups = match.groups()
    if len(groups) != 2:
        raise ValueError

    return (base_26_characters_to_base_10(groups[0]), int(groups[1])-1)

def import_lookup_table(index_file, cellxy):
    wb = xlrd.open_workbook(index_file)
    sheet = wb.sheet_by_index(0)

    data = []

    try:
        i = 1 # skip header
        while True:
            row = {
                'tab' : int(sheet.cell_value(i + cellxy[1], cellxy[0])),
                'date' : sheet.cell_value(i + cellxy[1], cellxy[0] + 1),
                'bates_num' : sheet.cell_value(i + cellxy[1], cellxy[0] + 2).lower()
            }
            logging.debug(row)
            data.append(row)
            i += 1
    except IndexError:
        pass

    logging.debug(data)
    return data

def copy_and_name_files(doc_dir, out_dir, data):
    logging.debug('copy')
    logging.debug(data)

    for doc in data:
        for filename in os.listdir(doc_dir):
            if fnmatch.fnmatch(filename.lower(), '*{}*.pdf'.format(doc['bates_num'])):
                old_filename = os.path.join(doc_dir, filename)
                new_filename = os.path.join(out_dir, '{} - {}'.format(doc['tab'], filename))

                logging.debug('copying file {} to {}'.format(old_filename, new_filename))

                copyfile(old_filename, new_filename)


def setup_log():
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def main():
    args = parse_args(sys.argv[1:])
    setup_log()

    logging.debug(args)

    cellxy = parse_excel_cell_name(args.table_start)
    logging.debug(cellxy)

    data = import_lookup_table(args.index_file, cellxy)

    copy_and_name_files(args.doc_dir, args.out_dir, data)


if __name__ == '__main__':
    main()
