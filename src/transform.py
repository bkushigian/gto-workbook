#!/usr/bin/python

"""
Transform an xml file into a formatted series of questions
"""

import xml.etree.ElementTree as ET
import textwrap
import re
import itertools
import random
import os.path as osp
import pathlib

SEED = 12345

ranks = "23456789TJQKA"
suits = "hsdc"
suit_pairs = list(itertools.combinations(suits, 2))

def is_pair(combo):
    return len(combo) == 2 and combo[0] == combo[1]

def suit_to_html(cardstring):
    cardstring = cardstring.replace("h", "H")
    cardstring = cardstring.replace("d", "D")
    cardstring = cardstring.replace("c", "C")
    cardstring = cardstring.replace("s", "S")
    cardstring = cardstring.replace("H", "<span style=\"color:#ff0000;\">&hearts;</span>")
    cardstring = cardstring.replace("D", "<span style=\"color:#0088ff;\">&diams;</span>")
    cardstring = cardstring.replace("C", "<span style=\"color:#008800;\">&clubs;</span>")
    cardstring = cardstring.replace("S", "<span style=\"color:#000000;\">&spades;</span>")
    return cardstring

def is_suited(combo):
    return len(combo) == 3 and combo[2] == 's'

def is_unsuited(combo):
    return len(combo) == 3 and combo[2] == 'o'

def expand_combo(combo, deadcards=None):
    if is_suited(combo):
        return expand_suited_combo(combo, deadcards)
    if is_unsuited(combo):
        return expand_unsuited_combo(combo, deadcards)
    if is_pair(combo):
        return expand_pair_combo(combo, deadcards)
    raise RuntimeError("Invalid combo, cannot expand: " + combo)

def expand_suited_combo(combo, deadcards=None):
    assert is_suited(combo)
    if deadcards is None:
        deadcards = set()
    hands = []
    r1, r2, _ = combo
    for suit in suits:
        c1, c2 = r1 + suit, r2 + suit
        if c1 in deadcards or c2 in deadcards: continue
        hands.append(c1+c2)
    return hands

def expand_unsuited_combo(combo, deadcards=None):
    assert is_unsuited(combo)
    if deadcards is None:
        deadcards = set()
    hands = []
    r1, r2, _ = combo
    for suit1 in suits:
        for suit2 in suits:
            if suit1 == suit2: continue
            c1, c2 = r1 + suit1, r2 + suit2
            if c1 in deadcards or c2 in deadcards: continue
            hands.append(c1+c2)
    return hands

def expand_pair_combo(combo, deadcards=None):
    assert is_pair(combo)
    if deadcards is None:
        deadcards = set()
    hands = set()
    r, _ = combo
    for suit1, suit2 in suit_pairs:
        if suit1 == suit2: continue
        c1, c2 = r + suit1, r + suit2
        if c1 in deadcards or c2 in deadcards: continue
        hands.add(c1+c2)
    return list(hands)

def get_ranks_range(low='2', high='A', exclusive=False):
    if exclusive:
        return ranks[ranks.index(low):ranks.index(high)]
    else:
        return ranks[ranks.index(low):ranks.index(high)+1]

def enforce_combo_format(c1, c2=None):
    '''
    Make sure that a combo is well formated. Optionally, enforce that a second combo
    is also well formatted and that a dash-combo class c1-c2 is well formed.
    '''
    assert len(c1) in (2, 3), "Invalid combo length: " + c1
    assert c1[0] in ranks and c1[1] in ranks, "Invalid rank in combo: " + c1
    if len(c1) == 2:
        assert c1[0] == c1[1], "Combo with no suitedness specifier must be a pocket pair: " + c1
    if len(c1) == 3:
        assert c1[0] != c1[1], "Combo class with suitedness specifier must be a non pocket pair: " + c1
        assert c1[0] in ranks and c1[1] in ranks, "Invalid rank: " + c1
        assert c1[2] in "os", "Invalid suitedness specifier (must be 'o' or 's'): " + c1
        assert ranks.index(c1[0]) > ranks.index(c1[1]), "The first card of an unpaired combo class must have the greatest rank: " + c1
    if c2:
        enforce_combo_format(c2)
        assert len(c1) == len(c2), "Matching combo classes must be the same length: " + c1 + "-" + c2
        if len(c1) == 3:
            assert c1[0] == c2[0], "Matching combo classes must start with the same card: " + c1 + "-" + c2
            assert c1[2] == c2[2], "Matching combo classes must have the same suitedness specifier: " + c1 + "-" + c2


def expand_combo_class(cc):
    if cc.endswith("+"):
        return expand_plus_combo_class(cc)
    if "-" in cc:
        return expand_dash_combo_class(cc)
    return [cc] 

def expand_plus_combo_class(cc):
    cc = cc.strip('+')
    enforce_combo_format(cc)
    assert len(cc) >= 2
    if cc[0] == cc[1]:
        return ['{}{}'.format(c, c) for c in get_ranks_range(cc[0])]
    else:
        s = cc[2]
    return ['{}{}{}'.format(cc[0], c, s) for c in get_ranks_range(cc[1], cc[0], exclusive=True)]

def expand_dash_combo_class(cc):
    high, low = cc.split('-')
    enforce_combo_format(high, low)
    if ranks.index(high[1]) < ranks.index(low[1]):
        high, low = low, high
    if len(high) == 2:
        return ['{}{}'.format(c, c) for c in get_ranks_range(low=low[0], high=high[0])]
    elif len(high) == 3:
        s = high[2]
        return ['{}{}{}'.format(low[0], c, s) for c in get_ranks_range(low[1], high[1])]
    else:
        raise RuntimeError("Invalid combo: " + high)

class Range:
    """
    Map hand combos to weights
    """
    def __init__(self, range_str):
        """Accepts a flopzilla format opening range string and parses it into a Range object"""
        self.range_str = range_str
        self.combos_to_weights = {}
        self.weights_to_combos = {}
        self._parse(range_str)
    
    def combos(self):
        return list(self.combos_to_weights.keys())

    def hands(self, deadcards=None):
        if deadcards is None:
            deadcards = set()
        combos = self.combos()
        hands = []
        for c in self.combos():
            hands += expand_combo(c, deadcards)
        return hands
    
    def _parse(self, s):
        tokens = re.findall("[^\[,]+|\[\d+\.\d+\]|\[/\d+.\d+\]", s)
        UNWEIGHTED = 0
        WEIGHTED = 1

        weight = 100.0
        state = UNWEIGHTED
        for token in tokens:
            if token.startswith("[/"):
                if state is UNWEIGHTED:
                    raise RuntimeError("closing tag " + token + " found when not in weighted section")
                state = UNWEIGHTED
                weight = 1.0
            elif token.startswith("["):
                if state is WEIGHTED:
                    raise RuntimeError("Nested weight token: " + token)
                weight = float(token.strip('[]'))
                state = WEIGHTED
            else:
                combo_class = expand_combo_class(token)
                for combo in combo_class:
                    assert combo not in self.combos_to_weights, "Redundant combo found: " + combo
                    self.combos_to_weights[combo] = weight
                    self.weights_to_combos.setdefault(weight, []).append(combo)
                self.combos_to_weights[combo] = weight

    def __getitem__(self, combo):
        enforce_combo_format(combo)
        return self.combos_to_weights.get(combo) or 0.0

    def __str__(self):
        return "Range[{}]".format(self.range_str)

    def __repr__(self):
        return str(self)

class Player:
    def __init__(self, elem):
        self.is_hero = elem.tag == 'hero'
        self.pos = elem.attrib['pos']
        self.ip = bool(elem.attrib['ip'])
        self.range = Range(elem.find('range').text.strip())
    
    def __str__(self):
        return "Player[{}({})|range='{}']".format(
            self.pos.upper(),
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


class Transformer:
    def __init__(self, xml_file):
        # todo
        self.xml_file = xml_file
        root = ET.parse(xml_file).getroot()
        self.root = root
        self.flops = [f.text for f in root.find('flops')]
        self.flop_questions = [q.text.strip() for q in root.find('questions')]
        self.hand_questions = [q.text.strip() for q in root.find('hand-questions')]
        scenarios = root.find('scenarios')
        assert scenarios is not None
        scenarios = [Scenario(s) for s in scenarios.findall('scenario')]
        
        self.scenarios = scenarios

    def as_markdown(self):
        def format_card_str(s):
            return "<b>{}</b>".format(suit_to_html(s))
        lines = []
        for i, scenario in enumerate(self.scenarios):
            lines.append("# Semibluffs and Protection")
            lines.append("## Scenario {}: {}".format(i + 1, scenario.title))
            for l in textwrap.wrap(scenario.description, width=80):
                lines.append("{}".format(l))

            for fn, f in enumerate(self.flops):
                flop_list = [f[i:i+2] for i in range(0, len(f), 2)]
                lines.append("### Flop {}: {}".format(fn + 1, format_card_str(f)))
                # Enumerate flop-level questions
                for j, question in enumerate(self.flop_questions):
                    q = "{}. **{}**".format(j + 1, question)
                    q = textwrap.wrap(q, width=76)
                    lines.append(q[0])
                    for l in q[1:]:
                        lines.append("   {}".format(l))
                    lines.append("")
                lines.append("#### Hands")
                combos = scenario.hero.range.combos()
                random.shuffle(combos)
                for h, combo in  enumerate(combos[:10]):
                    hands = expand_combo(combo, deadcards=flop_list)
                    random.shuffle(hands)
                    hand = hands[0]
                    lines.append("{}. {} (Flop: {})".format(h+1, format_card_str(hand), suit_to_html(f)))
                    for j, question in enumerate(self.hand_questions):
                        q = "{}. **{}**".format(j + 1, question)
                        q = textwrap.wrap(q, width=76)
                        lines.append("    " + q[0])
                        for l in q[1:]:
                            lines.append("       {}".format(l))
        return '\n'.join(lines)

    def as_text(self):
        lines = []
        for i, scenario in enumerate(self.scenarios):
            lines.append("+" + ('-' * 78) + "+")
            lines.append("Scenario {}: {}".format(i + 1, scenario.title))
            lines.append("")
            lines.append("Description")
            lines.append("-----------")
            for l in textwrap.wrap(scenario.description, width=70):
                lines.append("    {}".format(l))
            
            lines.append("Flops")
            lines.append("-----")
            for fn, f in enumerate(self.flops):
                flop_list = [f[i:i+2] for i in range(0, len(f), 2)]
                hero_range_hands = scenario.hero.range.hands(deadcards=flop_list)
                lines.append('')
                lines.append("Flop {}: {}".format(fn + 1, f))
                # Enumerate flop-level questions
                for j, question in enumerate(self.flop_questions):
                    q = "({}) {}".format(j + 1, question)
                    for l in textwrap.wrap(q):
                        lines.append("    {}".format(l))
                    lines.append("")
                # TODO: Add specific hand questions
                hands = list(hero_range_hands)
                random.shuffle(hands)
                for h, hand in  enumerate(hands[:10]):
                    lines.append("    Hand {}: {} (Flop: {})".format(h+1, hand, f))
                    for j, question in enumerate(self.hand_questions):
                        q = "({}) {}".format(j + 1, question)
                        for l in textwrap.wrap(q):
                            lines.append("        {}".format(l))
                        lines.append("")

        return '\n'.join(lines)

    def to_text_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.as_text())
        
    def to_markdown_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.as_markdown())

file_format_extensions = {"md" : "md", "markdown": "md", "txt": "txt", "text": "txt"}

def main():
    from sys import argv, exit
    if len(argv) < 3 or len(argv) > 4:
        print("usage: transform.py file.xml format [output]")
        exit(1)
    file = argv[1]
    format = argv[2]

    if format not in file_format_extensions:
        raise RuntimeError("Unrecognized output format: " + format)

    if len(argv) == 4:
        output_file = argv[3]
    else:
        stem = pathlib.Path(file).stem + "-questions"
        output_file = stem + "." + file_format_extensions[format]

    random.seed(SEED)
    t = Transformer(file)

    if format == 'text' or format == 'txt':
        t.to_text_file(output_file)
    elif format == 'md' or format == 'markdown':
        t.to_markdown_file(output_file)
    else:
        print("Unknown format: " + format)
        exit(1)

if __name__ == '__main__':
    main()
