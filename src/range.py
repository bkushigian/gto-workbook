import re
import cards

def is_pair(combo):
    return len(combo) == 2 and combo[0] == combo[1]

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
    for suit in cards.SUITS:
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
    for suit1 in cards.SUITS:
        for suit2 in cards.SUITS:
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
    for suit1, suit2 in cards.SUIT_PAIRS:
        if suit1 == suit2: continue
        c1, c2 = r + suit1, r + suit2
        if c1 in deadcards or c2 in deadcards: continue
        hands.add(c1+c2)
    return list(hands)

def get_ranks_range(low='2', high='A', exclusive=False):
    if exclusive:
        return cards.RANKS[cards.RANKS.index(low):cards.RANKS.index(high)]
    else:
        return cards.RANKS[cards.RANKS.index(low):cards.RANKS.index(high)+1]

def enforce_combo_format(c1, c2=None):
    '''
    Make sure that a combo is well formated. Optionally, enforce that a second combo
    is also well formatted and that a dash-combo class c1-c2 is well formed.
    '''
    assert len(c1) in (2, 3), "Invalid combo length: " + c1
    assert c1[0] in cards.RANKS and c1[1] in cards.RANKS, "Invalid rank in combo: " + c1
    if len(c1) == 2:
        assert c1[0] == c1[1], "Combo with no suitedness specifier must be a pocket pair: " + c1
    if len(c1) == 3:
        assert c1[0] != c1[1], "Combo class with suitedness specifier must be a non pocket pair: " + c1
        assert c1[0] in cards.RANKS and c1[1] in cards.RANKS, "Invalid rank: " + c1
        assert c1[2] in "os", "Invalid suitedness specifier (must be 'o' or 's'): " + c1
        assert cards.RANKS.index(c1[0]) > cards.RANKS.index(c1[1]), "The first card of an unpaired combo class must have the greatest rank: " + c1
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
    if cards.RANKS.index(high[1]) < cards.RANKS.index(low[1]):
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

    def range_rows(self):
        rows = []

        for i,c1 in enumerate("AKQJT98765432"):
            row = []
            rows.append(row)
            for j,c2 in enumerate("AKQJT98765432"):
                suitedness_class = "suited"
                if i > j:
                    combo = f"{c2}{c1}o"
                    suitedness_class = "offsuit"
                elif i == j:
                    combo = f"{c1}{c2}"
                    suitedness_class = "pair"
                else:
                    combo = f"{c1}{c2}s"
                weight = int(self[combo])
                row.append((combo, weight, suitedness_class))
        return rows

    html_range_id_num = 1

    def as_image(self,
                 output_file="range.jpg",
                 range_id=None,
                 width="40px",
                 height="40px",
                 pair_rgb="0072ef",
                 suited_rgb="cc0000",
                 offsuit_rgb="ffff22",
                 max_color_weight=100,
                 min_color_weight=30):
        import imgkit
        html = "<!doctype html>" 
        html += self.as_html_table(range_id=range_id, width=width, height=height, pair_rgb=pair_rgb, suited_rgb=suited_rgb,
                                   offsuit_rgb=offsuit_rgb, max_color_weight=max_color_weight, min_color_weight=min_color_weight)
        print(output_file)
        imgkit.from_string(html, output_file)


    def as_html_table(self,
                      range_id=None,
                      width="40px",
                      height="40px",
                      text_align="center",
                      vertical_align="middle",
                      # pair_rgb="aaff9f",
                      pair_rgb="0072ef",
                      # suited_rgb="e37fd7",
                      suited_rgb="ee0000",
                      # offsuit_rgb="bbced3",
                      offsuit_rgb="ffff22",
                      max_color_weight=100,
                      min_color_weight=30):

        def weighted_color_str(weight, color_str):
            def weight_color(color):
                multiplier = (min_color_weight + (weight / 100) * (max_color_weight - min_color_weight)) / 100.0
                return int(color * multiplier)

            rgb = color_str[:2], color_str[2:4], color_str[4:6]
            rgb = [int(c, base=16) for c in rgb]
            rgb  = ['{0:0{1}x}'.format(weight_color(c), 2) for c in rgb]
            return "".join(rgb)

        def wb_contrast(rgb):
            rgb = rgb[:2], rgb[2:4], rgb[4:6]
            
            brightness = ( int(rgb[0], base=16) * 299
                         + int(rgb[1], base=16) * 587
                         + int(rgb[2], base=16) * 114) / 1000

            return '111' if (brightness > 125)  else 'eee'
            
        class_to_colors = {'pair': pair_rgb, 'suited': suited_rgb, 'offsuit': offsuit_rgb}

        if range_id is None:
            range_id = "styled_range_{}".format(self.html_range_id_num)
            self.html_range_id_num += 1
        elements = []
        elements.append(
            f"""<style>
            .range {{
                border: 3px solid black;
                width: auto;
            }}
            #{range_id} td {{
                width: {width};
                height: {height};
                text-align: {text_align};
                vertical-align: {vertical_align};
            }}
            #{range_id} td.pair {{
                background: #{pair_rgb};
                border: 1px solid black;
            }}
            #{range_id} td.offsuit {{
                background: #{offsuit_rgb};
                border: 1px solid black;
            }}
            #{range_id} td.suited {{
                background: #{suited_rgb};
                border: 1px solid black;
            }}
            </style>""")
        elements.append(f"<table id=\"{range_id}\" class=\"range\">")
        for row in self.range_rows():
            elements.append("<tr>")
            for combo, weight, clss in row:
                color = class_to_colors[clss]
                color = weighted_color_str(weight, color)
                foreground = wb_contrast(color)
                elements.append(f"<td class=\"{clss}\" style=\"background:#{color}; color:#{foreground}\">{combo}<br><small>{weight}</small></td>".format(clss, weight))
            elements.append("</tr>")


        elements.append("</table>")
        return ''.join(elements)

    def __getitem__(self, combo):
        enforce_combo_format(combo)
        return self.combos_to_weights.get(combo) or 0.0

    def __str__(self):
        return "Range[{}]".format(self.range_str)

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    import sys
    import imgkit
    html = "<!doctype html>" + Range("AA-22,AKs-A2s,KQs-K2s,QJs-Q5s,JTs-J6s,T9s-T6s,98s-96s,87s-85s,76s-75s,65s-64s,54s,43s,AKo-A6o,KQo-K8o,QJo-Q9o,JTo-J9o,T9o,98o,[50.0000]Q4s-Q2s,J5s-J2s,T5s-T2s,95s-92s,84s-82s,74s-72s,63s-62s,53s-52s,42s,32s,A5o-A2o,K7o,Q8o,J8o,T8o,97o,87o,76o[/50.0000]").as_html_table()
    imgkit.from_string(html, sys.argv[1])
