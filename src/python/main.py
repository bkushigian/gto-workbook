from sys import argv, exit, stderr
from workbook.gen.chapter import Chapter
from workbook.gen.section import Section
from workbook.gen.workbook import Workbook


def usage():
    print("usage: main.py ROOT OUT", file=stderr)
    exit(1)

if len(argv) != 3:
    usage()

root, out = argv[1:]

workbook = Workbook(root, out, 'md')
workbook.generate_workbook()
