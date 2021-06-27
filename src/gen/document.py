#!/usr/bin/python

"""
document.py: represent a question generation document.
"""

import xml.etree.ElementTree as ET
import random
from range import Range, expand_combo
from gen.worksheet_generator import MarkdownWorksheetGenerator, WorksheetGenerator


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
    
    def __str__(self):
        return "Player[{}({})|range='{}']".format(
            self.table_position.upper(),
            "Hero" if self.is_hero else "Villain",
            self.range)

class Scenario:
    """
    A scenario to ask questions about. This corresponds to a <scenario> elem in
    the XML doc
    """
    def __init__(self, scenario_elem):
        t = scenario_elem
        self.name = t.attrib['name']
        self.title = t.find('title').text.strip()
        self.description = t.find('description').text.strip()
        self.hero = Player(t.find('./config/hero'))
        self.villain = Player(t.find('./config/villain'))


class QuestionGenerationDocument:
    def __init__(self, xml_file):
        # todo
        self.xml_file = xml_file
        root = ET.parse(xml_file).getroot()
        self.root = root
        self.title = root.find("title").text
        self.flops = [f.text for f in root.find('flops')]
        self.flop_questions = [q.text.strip() for q in root.find('flop-questions')]
        self.hand_questions = [q.text.strip() for q in root.find('hand-questions')]
        scenarios = root.find('scenarios')
        assert scenarios is not None
        scenarios = [Scenario(s) for s in scenarios.findall('scenario')]
        
        self.scenarios = scenarios

    def __str__(self):
        return str(self.worksheet_gen)

    def as_markdown(self):
        return self.generate_document(MarkdownWorksheetGenerator())

    def as_text(self):
        return self.generate_document(WorksheetGenerator())

    def generate_document(self, g: WorksheetGenerator):
        g.add_section(self.title)
        for scenario in self.scenarios:
            g.add_scenario_subsection(scenario.title, scenario.description)    

            for f in self.flops:
                flop_list = [f[i:i+2] for i in range(0, len(f), 2)]
                g.add_flop_subsection(f)
                # Enumerate flop-level questions
                for question in self.flop_questions:
                    g.add_flop_question(question)

                g.add_hands_subsection()
                combos = scenario.hero.range.combos()
                random.shuffle(combos)
                for combo in  combos[:10]:
                    hands = expand_combo(combo, deadcards=flop_list)
                    random.shuffle(hands)
                    hand = hands[0]
                    g.add_hand(hand)
                    for question in self.hand_questions:
                        g.add_hand_question(question)
        return str(g)

    def to_text_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.as_text())
        
    def to_markdown_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.as_markdown())
