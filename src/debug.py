from sys import argv, exit, stderr
from gen.chapter import Chapter
from gen.section import Section
from gen.workbook import Workbook


def usage():
    print("usage: debug.py TYPE ROOT OUT", file=stderr)
    print("valid types:\n  (w)orkbook\n  (c)hapter\n  (s)ection", file=stderr)
    exit(1)

if len(argv) != 4:
    usage()

tp, root, out = argv[1:]

if "workbook".startswith(tp.lower()):
    workbook = Workbook(root, out, 'md')
    workbook.generate_workbook()

elif "chapter".startswith(tp.lower()):
    chapter = Chapter(root, out, 'md')

elif "section".startswith(tp.lower()):
    section = Section(root, out)
