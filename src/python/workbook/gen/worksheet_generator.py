"""
Used by a QuestionGenerationDocument to generate a worksheet in a particular
format.
"""

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


class WorksheetGenerator:
    def __init__(self):
        self._section_titles = []
        self._sections = {}
        self._lines = 0
        self._current_section = 0

        self._section_depth = 0

        self._section_num = 0
        self._flop_num = 0
        self._flop_question_num = 0
        self._hand_num = 0
        self._hand_question_num = 0
        self._in_hands_subsection = False
    
    def next_section_num(self):
        return self._section_num + 1

    def next_flop_num(self):
        return self._flop_num + 1

    def next_flop_question_num(self):
        return self._flop_question_num + 1

    def next_hand_num(self):
        return self._hand_num + 1

    def next_hand_question_num(self):
        return self._hand_question_num + 1

    def add_section(self, title, description):
        assert title not in self._sections
        self._section_titles.append(title)
        self._lines = []
        self._lines.append(title)
        self._lines.append(description)
        self._section_depth = 1
        self._sections[title] = self._lines
        self._section_num += 1
        self._flop_num = 0

    def add_flop_subsection(self, flop):
        if not self._section_num:
            raise RuntimeError("Cannot add a flop without a containing section")
        self._lines.append(flop)
        self._section_depth = 3
        self._flop_num += 1
        self._flop_question_num = 0
        self._hand_question_num = 0
        self._in_hands_subsection = False
    
    def add_flop_question(self, question):
        if not self._flop_num:
            raise RuntimeError("Cannot add a flop question without a containing flop")
        self._lines.append(question + '\n')
        self._flop_question_num += 1

    def add_hands_subsection(self, header):
        if not self._flop_num:
            raise RuntimeError("Cannot add a hands subsection without a containing flop subsection")
        if self._in_hands_subsection:
            raise RuntimeError("Cannot create a hands subsection: already in a hands subsection")
        self._hand_num = 0
        self._section_depth = 4
        self._in_hands_subsection = True
        self._lines.append(header)

    def add_hand(self, hand):
        if not self._in_hands_subsection:
            raise RuntimeError("Cannot add a hand: not in a hands subsection")
        self._hand_num += 1
        self._hand_question_num = 0
        self._lines.append(hand + '\n')

    def add_hand_question(self, question):
        if not self._hand_num:
            raise RuntimeError("Cannot add a hand: not in a hands subsection")
        self._lines.append(question + '\n')
        self._hand_question_num += 1

    def section_break(self):
        return "\n\n"

    def add_raw_content(self, content):
        self._lines.append(content)
    
    def __str__(self):
        lines = []
        for title in self._section_titles:
            lines += self._sections[title]
            lines.append(self.section_break())
        return '\n'.join(lines) 
    

class MarkdownWorksheetGenerator(WorksheetGenerator):
    def __init__(self):
        super().__init__()
        self.current_flop = ""

    def add_section(self, title, description):
        super().add_section("# Section {}: {}\n".format(self.next_section_num(), title), description)

    def add_flop_subsection(self, flop):
        self.current_flop = flop
        super().add_flop_subsection("### Flop {}: <b>{}</b>".format(self.next_flop_num(), suit_to_html(flop)))

    def add_flop_question(self, question):
        super().add_flop_question("{}. **{}**".format(self.next_flop_question_num(), question))

    def add_hands_subsection(self, hands=None):
        hands = hands or "Hands"
        super().add_hands_subsection(f"#### {hands}")

    def add_hand(self, hand):
        super().add_hand("{}. <b>{}</b>    (Flop: {})".format(self.next_hand_num(), suit_to_html(hand), suit_to_html(self.current_flop)))

    def add_hand_question(self, question):
        super().add_hand_question("    {}. **{}**".format(self.next_hand_question_num(), question))

    def add_range_subsection(self):
        self.add_raw_content("### Player Ranges")

    def add_player_range(self, title, range_table):
        self._lines.append(f"\n#### {title}\n\n{range_table}\n\n")
