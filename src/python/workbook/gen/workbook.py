"""
Takes a directory as an input and a location as an output. Traverse
the workbook xml structure, rooted at the input, and output the workbook
rooted at output.
"""
import xml.etree.ElementTree as ET
import random
import os.path as osp
from os import makedirs
from sys import argv, exit, stderr
from workbook.gen.chapter import Chapter


class Workbook:
    def __init__(self, root_dir, out_dir, out_format='md'):
        self.root_dir = root_dir
        self.out_dir = out_dir
        self.out_format = out_format
        xml = osp.join(root_dir, "workbook.xml")
        root = ET.parse(xml).getroot()
        self.root = root

        self.title = root.find("title").text
        chapter_names = [c.attrib["name"] for c in root.findall("chapter")]
        self.chapters = []
        for name in chapter_names:
            try:
                self.chapters.append(Chapter(osp.join(root_dir, name), osp.join(out_dir, name), out_format))
            except FileNotFoundError:
                print("[!] Couldn't find chapter", osp.join(root_dir, name), file=stderr)
                print("    Continuing without this chapter", file=stderr)

    def generate_workbook(self):
        """
        Write this workbook to the output location
        """

        makedirs(self.out_dir)
        lines = []
        lines.append(f"# {self.title}")
        lines.append("## Table of Contents")

        for i, chapter in enumerate(self.chapters):
            file_location = chapter.generate_chapter().replace('\\', '/')
            rel_location = osp.relpath(file_location, self.out_dir).replace('\\', '/')
            lines.append(f"### Chapter {i+1}: [{chapter.title}]({rel_location})")
        
        file_location = f"{self.out_dir}/gto-workbook.md"
        with open(file_location, "w+") as f:
            f.write('\n'.join(lines))
        return file_location