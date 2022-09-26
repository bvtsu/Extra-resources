#!/usr/bin/env python3

"""Script summary

Explanation of script function"""

# from
import argparse
import logging

# Create logger
logger=logging.getLogger(__name__)

# Set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
file_handler=logging.FileHandler('test_logging.log')
formatter=logging.Formatter('[%(asctime)s:%(levelname)s:%(lineno)d %(message)s', datefmt='%H:%M:%S') #time:levelname:message:line#
file_handler.setFormatter(formatter)

# set up a stream handler in the same format
stream_handler=logging.StreamHandler()
stream_handler.setFormatter(formatter)

# add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def parse_args():
    parser = argparse.ArgumentParser(prog = 'template.py', conflict_handler = 'resolve')
    parser.add_argument('-i', type = str, required = True, help = '=> info on arg')
    return(parser.parse_args())

def function1(arg: argtype) -> returntype:
    """Function summary

    explanation of important function parts"""
    # code here

def main():
    args = parse_args()
    logger.debug(args.i)
    function1(args.i)

if __name__ == '__main__':
    main()