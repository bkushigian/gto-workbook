import random
from gen.document import QuestionGenerationDocument
import os.path as osp
from os import makedirs
import sys
sys.path.append(osp.join(osp.dirname(__file__), "lib"))

SEED = 12345

FILE_FORMAT_EXTENSIONS = {"md" : "md", "markdown": "md", "txt": "txt", "text": "txt"}

def main():
    from sys import argv, exit
    if len(argv) < 3 or len(argv) > 4:
        print("usage: transform.py file.xml format [output]")
        exit(1)
    file = argv[1]
    format = argv[2]

    if format not in FILE_FORMAT_EXTENSIONS:
        raise RuntimeError("Unrecognized output format: " + format)

    if len(argv) == 4:
        output_file = argv[3]
    else:
        output_file = osp.splitext(file)[0] + "." + FILE_FORMAT_EXTENSIONS[format]

    output_dir = osp.dirname(output_file)
    try:
        makedirs(osp.join(output_dir, "img"))
    except OSError as e:
        pass

    random.seed(SEED)
    t = QuestionGenerationDocument(file, output_dir=output_dir)

    print("writing to", output_file)

    if format == 'text' or format == 'txt':
        t.to_text_file(output_file)
    elif format == 'md' or format == 'markdown':
        t.to_markdown_file(output_file)
    else:
        print("Unknown format: " + format)
        exit(1)

if __name__ == '__main__':
    main()