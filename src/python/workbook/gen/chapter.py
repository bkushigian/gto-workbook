import xml.etree.ElementTree as ET
import os.path as osp
from os import makedirs
from workbook.gen.section import Section
from workbook.gen.worksheet_generator import MarkdownWorksheetGenerator


class Chapter:
    def __init__(self, root_dir, out_dir, out_format='md'):
        self.root_dir = root_dir
        self.out_dir = out_dir
        self.out_format=out_format
        xml = osp.join(root_dir, "chapter.xml")
        root = ET.parse(xml).getroot()
        self.root = root

        self.title = root.find("title").text
        section_names = [c.attrib["name"] for c in root.findall("section")]
        self.sections = [Section(osp.join(root_dir, f"{name}.xml"), out_dir, self) for name in section_names]
    
    def generate_chapter(self):
        makedirs(self.out_dir)
        lines = []
        lines.append(f"# {self.title}")
        for i,section in enumerate(self.sections):
            makedirs(section.out_dir)
            makedirs(osp.join(section.out_dir, "img"))
            section_content = section.generate_section(MarkdownWorksheetGenerator())
            section_file = f"{section.out_dir}/section.md"
            rel_section_file = osp.relpath(section_file, self.out_dir)
            with open(section_file, "w+") as f:
                f.write(section_content)
            lines.append('')
            lines.append(f"## Section {i+1}: [{section.title}]({rel_section_file})")
        
        file_location = f"{self.out_dir}/chapter.md"
        with open(file_location, 'w+') as f:
            f.write('\n'.join(lines))
        return file_location
        

def main():
    from sys import argv, exit, stderr
    if len(argv) != 3:
        print("usage: chapter.py root_dir out_dir", file=stderr)
        exit(1)
    root_dir, out_dir = argv[1:]
    Chapter(root_dir, out_dir)

if __name__ == "__main__":
    main()