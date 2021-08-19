#!/usr/bin/python

"""
document.py: represent a question generation document.
"""

import xml.etree.ElementTree as ET
import random
import os.path as osp
from os import makedirs
from workbook.range import Range, expand_combo
from workbook.gen.worksheet_generator import MarkdownWorksheetGenerator, WorksheetGenerator, suit_to_html

class Player:
    """
    Represent a player in the document, either "Hero" or "Villain".
    This has the following fields:

    :field self.is_hero: a boolean determining if this player is Hero
    :field self.table_position: the position of the player (lj, hj, co, bn, sb, bb)
    :field self.has_position: a boolean determining if this player has position or not
    :field self.range: a Range object describing this player's range
    """
    def __init__(self, elem):
        self.is_hero = elem.tag == 'hero'
        self.table_position = elem.attrib['pos']
        self.has_position = bool(elem.attrib['ip'])
        self.range = Range(elem.find('range').text.strip())
        self.range_title = elem.attrib['title']
    
    def __str__(self):
        return "Player[{}({})|range='{}']".format(
            self.table_position.upper(),
            "Hero" if self.is_hero else "Villain",
            self.range)


class Section:
    def __init__(self, xml_file, out_dir, parent=None):
        self.xml_file = xml_file
        self.parent = parent
        root = ET.parse(xml_file).getroot()
        self.root = root
        self.title = root.find("title").text.strip()
        self.name = root.find('name').text.strip()
        self.description = root.find('description').text.strip()
        self.hero = Player(root.find('./config/hero'))
        self.villain = Player(root.find('./config/villain'))
        self.flops = [f.text for f in root.find('flops')]
        self.flop_questions = [q.text.strip() for q in root.find('flop-questions')]
        self.hand_questions = [q.text.strip() for q in root.find('hand-questions')]
        self.out_dir = osp.join(out_dir, self.name)
        
    def __str__(self):
        return str(self.worksheet_gen)

    def as_markdown(self) -> str:
        '''
        Generate this section as markdown text and return a string containing
        that text. Other files, such as flop files, are generated and written to
        disk. Handles to these files are not returned.
        '''
        return self.generate_section(MarkdownWorksheetGenerator())

    def as_text(self):
        return self.generate_section(WorksheetGenerator())

    def generate_section(self, g: WorksheetGenerator) -> str:
        '''
        Generate this section using a WorksheetGenerator and return the text
        file's contents.  Other files, such as flop files, are written as
        needed.
        '''

        def hash_flop(f: str):
            '''
            For security reasons, Python's built-in `hash` function isn't
            consistent between invocations. This function implements a dummy
            hash by multiplying the ords of the chars in a string
            '''
            ords = [ord(c) for c in f.strip()]
            hash = 5381
            for x in ords:
                hash = (hash << 5) + hash + x
            return hash

        img_dir = osp.join(self.out_dir, "img")
        g.add_section(self.title, self.description)
        if isinstance(g, MarkdownWorksheetGenerator):
            g.add_range_subsection()
            hero_range_title = f"{self.name}-hero-range.jpg"
            villain_range_title = f"{self.name}-villain-range.jpg"
            self.hero.range.as_image(output_file=osp.join(img_dir, hero_range_title))
            self.villain.range.as_image(output_file=osp.join(img_dir, villain_range_title))
            g.add_player_range(title="Hero's {} Range".format(self.hero.range_title),
                                range_table="![Hero's Range]({})".format(f"img/{hero_range_title}"))

            g.add_player_range(title="Villain's {} Range".format(self.villain.range_title),
                                range_table="![Villain's Range]({})".format(f"img/{villain_range_title}"))


            for f in self.flops:
                flop_list = [f[i:i+2] for i in range(0, len(f), 2)]
                combos = self.hero.range.combos()

                # We want to make hands for each flop deterministic.  To do this
                # we hash the flop to produce a seed and use this seed to seed
                # random. This is robust to perterbations in in flop ordering,
                # number of flops, and number of hands per flop.

                assert isinstance(f, str)
                SEED = hash_flop(f)
                random.seed(SEED)
                random.shuffle(combos)
                g.add_flop_entry(f)
                g._flop_generator.add_player_range(title="Hero's {} Range".format(self.hero.range_title),
                                    range_table="![Hero's Range]({})".format(f"img/{hero_range_title}"))

                g._flop_generator.add_player_range(title="Villain's {} Range".format(self.villain.range_title),
                                    range_table="![Villain's Range]({})".format(f"img/{villain_range_title}"))
                # Enumerate flop-level questions
                for question in self.flop_questions:
                    g.add_flop_question(question)

                g.add_hands_subsection(f"Hands for flop {suit_to_html(f)}")
                for combo in  combos[:10]:
                    hands = expand_combo(combo, deadcards=flop_list)
                    random.shuffle(hands)
                    hand = hands[0]
                    g.add_hand(hand)
                    for question in self.hand_questions:
                        g.add_hand_question(question)
        for fg in g._flop_generators:
            with open(osp.join(self.out_dir, fg.basename()), 'w') as f:
                f.write(str(fg))
        return str(g)

    def to_text_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.as_text())
        
    def to_markdown_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.as_markdown())
