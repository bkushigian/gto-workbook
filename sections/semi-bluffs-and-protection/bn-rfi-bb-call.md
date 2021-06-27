# Section 1: Semi-Bluffs and Protection

## Scenario 1: BB Calls BN Open
_Blinds are $0.05/$0.10. Effective stacks are $10.00. You're on the button and action folds to you. You open for $0.30 (3bb), SB folds, and BB calls. You go to the flop with $9.70 behind and a pot of $0.65, and BB checks to you._
### Player Ranges

#### Hero's Button Opening Range Range

<style>
            .range {
                border: 3px solid black;
            }
            #styled_range_1 td {
                width: 40px;
                height: 40px;
                text-align: center;
                vertical-align: middle;
            }
            #styled_range_1 td.pair {
                background: #0072ef;
                border: 1px solid black;
            }
            #styled_range_1 td.offsuit {
                background: #ffff22;
                border: 1px solid black;
            }
            #styled_range_1 td.suited {
                background: #ee0000;
                border: 1px solid black;
            }
            </style>
<table id="styled_range_1" class="range">
<tr>
<td class="pair" style="background:#0072ef; color:#eee">AA<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">AKs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">AQs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">AJs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">ATs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A5s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A4s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A3s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A2s<br><small>100</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">AKo<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">KK<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">KQs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">KJs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">KTs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K5s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K4s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K3s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K2s<br><small>100</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">AQo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">KQo<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">QQ<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">QJs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">QTs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q5s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">Q4s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">Q3s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">Q2s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">AJo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">KJo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">QJo<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">JJ<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">JTs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J6s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">J5s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">J4s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">J3s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">J2s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">ATo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">KTo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">QTo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">JTo<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">TT<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T6s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">T5s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">T4s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">T3s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">T2s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A9o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">K9o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">Q9o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">J9o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">T9o<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">99<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">98s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">97s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">96s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">95s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">94s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">93s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">92s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A8o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">K8o<br><small>100</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">Q8o<br><small>50</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">J8o<br><small>50</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">T8o<br><small>50</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">98o<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">88<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">87s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">86s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">85s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">84s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">83s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">82s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A7o<br><small>100</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">K7o<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T7o<br><small>0</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">97o<br><small>50</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">87o<br><small>50</small></td>
<td class="pair" style="background:#0072ef; color:#eee">77<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">76s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">75s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">74s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">73s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">72s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A6o<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">K6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">96o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">86o<br><small>0</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">76o<br><small>50</small></td>
<td class="pair" style="background:#0072ef; color:#eee">66<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">65s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">64s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">63s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">62s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#cccc1b; color:#111">A5o<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">K5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">95o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">85o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">75o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">65o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">55<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">54s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">53s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">52s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#cccc1b; color:#111">A4o<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">K4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">94o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">84o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">74o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">64o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">54o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">44<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">43s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">42s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#cccc1b; color:#111">A3o<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">K3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">93o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">83o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">73o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">63o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">53o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">43o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">33<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">32s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#cccc1b; color:#111">A2o<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">K2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">92o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">82o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">72o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">62o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">52o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">42o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">32o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">22<br><small>100</small></td>
</tr>
</table>

#### Villain's Big Blind Calling Range vs Button Range

<style>
            .range {
                border: 3px solid black;
            }
            #styled_range_1 td {
                width: 40px;
                height: 40px;
                text-align: center;
                vertical-align: middle;
            }
            #styled_range_1 td.pair {
                background: #0072ef;
                border: 1px solid black;
            }
            #styled_range_1 td.offsuit {
                background: #ffff22;
                border: 1px solid black;
            }
            #styled_range_1 td.suited {
                background: #ee0000;
                border: 1px solid black;
            }
            </style>
<table id="styled_range_1" class="range">
<tr>
<td class="pair" style="background:#00448f; color:#eee">AA<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">AKs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">AQs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">AJs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">ATs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">A9s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">A8s<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A6s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">A5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">A4s<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A3s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A2s<br><small>100</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">AKo<br><small>0</small></td>
<td class="pair" style="background:#00448f; color:#eee">KK<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">KQs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">KJs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">KTs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K9s<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K5s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K4s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K3s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K2s<br><small>100</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">AQo<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">KQo<br><small>0</small></td>
<td class="pair" style="background:#00448f; color:#eee">QQ<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">QJs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">QTs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q9s<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q5s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q4s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q3s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q2s<br><small>100</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">AJo<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">KJo<br><small>0</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">QJo<br><small>100</small></td>
<td class="pair" style="background:#00448f; color:#eee">JJ<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">JTs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J9s<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J5s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J4s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">ATo<br><small>0</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">KTo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">QTo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">JTo<br><small>100</small></td>
<td class="pair" style="background:#00448f; color:#eee">TT<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T9s<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T6s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A9o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">K9o<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q9o<br><small>0</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">J9o<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">T9o<br><small>100</small></td>
<td class="pair" style="background:#00448f; color:#eee">99<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">98s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">97s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">96s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">95s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">94s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">93s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">92s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A8o<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">K8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">98o<br><small>0</small></td>
<td class="pair" style="background:#00448f; color:#eee">88<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">87s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">86s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">85s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">84s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">83s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">82s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A7o<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">K7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">97o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">87o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">77<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">76s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">75s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">74s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">73s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">72s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">96o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">86o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">76o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">66<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">65s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">64s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">63s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">62s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">A5o<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">K5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">95o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">85o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">75o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">65o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">55<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">54s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">53s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">52s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">94o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">84o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">74o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">64o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">54o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">44<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">43s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">42s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">93o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">83o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">73o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">63o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">53o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">43o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">33<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">32s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">92o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">82o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">72o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">62o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">52o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">42o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">32o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">22<br><small>100</small></td>
</tr>
</table>
### Flop 1: <b>A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>J<span style="color:#008800;">&clubs;</span>T<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>K<span style="color:#000000;">&spades;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#0088ff;">&diams;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>7<span style="color:#008800;">&clubs;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>5<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>6<span style="color:#000000;">&spades;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#008800;">&clubs;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#008800;">&clubs;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>9<span style="color:#008800;">&clubs;</span>4<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 2: <b>A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>Q<span style="color:#000000;">&spades;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>9<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>J<span style="color:#008800;">&clubs;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>Q<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>K<span style="color:#000000;">&spades;</span>Q<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#0088ff;">&diams;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>Q<span style="color:#000000;">&spades;</span>T<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>Q<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 3: <b>A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>Q<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>J<span style="color:#0088ff;">&diams;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>K<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>Q<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>4<span style="color:#ff0000;">&hearts;</span>4<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>J<span style="color:#008800;">&clubs;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>6<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>Q<span style="color:#0088ff;">&diams;</span>T<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 4: <b>K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>8<span style="color:#0088ff;">&diams;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#0088ff;">&diams;</span>2<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>A<span style="color:#0088ff;">&diams;</span>7<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>8<span style="color:#000000;">&spades;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>T<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#0088ff;">&diams;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#000000;">&spades;</span>K<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 5: <b>K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>T<span style="color:#000000;">&spades;</span>8<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>8<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#0088ff;">&diams;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>4<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>4<span style="color:#000000;">&spades;</span>3<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>Q<span style="color:#ff0000;">&hearts;</span>T<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>T<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>Q<span style="color:#ff0000;">&hearts;</span>4<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>K<span style="color:#ff0000;">&hearts;</span>2<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 6: <b>K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>T<span style="color:#008800;">&clubs;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#008800;">&clubs;</span>2<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#000000;">&spades;</span>8<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#ff0000;">&hearts;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>Q<span style="color:#ff0000;">&hearts;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>Q<span style="color:#000000;">&spades;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>Q<span style="color:#000000;">&spades;</span>5<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>Q<span style="color:#ff0000;">&hearts;</span>T<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>7<span style="color:#ff0000;">&hearts;</span>6<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 7: <b>Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#008800;">&clubs;</span>2<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>7<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>7<span style="color:#ff0000;">&hearts;</span>7<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>8<span style="color:#008800;">&clubs;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>8<span style="color:#ff0000;">&hearts;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>Q<span style="color:#ff0000;">&hearts;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#000000;">&spades;</span>J<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>Q<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>K<span style="color:#000000;">&spades;</span>5<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>5<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 8: <b>Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>J<span style="color:#0088ff;">&diams;</span>7<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#000000;">&spades;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>K<span style="color:#ff0000;">&hearts;</span>7<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>A<span style="color:#0088ff;">&diams;</span>T<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#ff0000;">&hearts;</span>5<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>T<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>J<span style="color:#ff0000;">&hearts;</span>5<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>K<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>4<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 9: <b>Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>8<span style="color:#ff0000;">&hearts;</span>6<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>8<span style="color:#ff0000;">&hearts;</span>3<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#0088ff;">&diams;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>A<span style="color:#008800;">&clubs;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>T<span style="color:#000000;">&spades;</span>3<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>J<span style="color:#000000;">&spades;</span>8<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>Q<span style="color:#008800;">&clubs;</span>J<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>7<span style="color:#ff0000;">&hearts;</span>3<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 10: <b>J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#0088ff;">&diams;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>7<span style="color:#008800;">&clubs;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>Q<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>9<span style="color:#000000;">&spades;</span>5<span style="color:#000000;">&spades;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>J<span style="color:#008800;">&clubs;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>7<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>6<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>9<span style="color:#000000;">&spades;</span>8<span style="color:#000000;">&spades;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 11: <b>T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>8<span style="color:#008800;">&clubs;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>T<span style="color:#008800;">&clubs;</span>4<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>A<span style="color:#ff0000;">&hearts;</span>T<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>5<span style="color:#ff0000;">&hearts;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>K<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>T<span style="color:#ff0000;">&hearts;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#000000;">&spades;</span>K<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>7<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 12: <b>T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>T<span style="color:#ff0000;">&hearts;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>8<span style="color:#ff0000;">&hearts;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>Q<span style="color:#008800;">&clubs;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>4<span style="color:#0088ff;">&diams;</span>2<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>A<span style="color:#008800;">&clubs;</span>Q<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>J<span style="color:#ff0000;">&hearts;</span>5<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>8<span style="color:#000000;">&spades;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>T<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>T<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#008800;">&clubs;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 13: <b>9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>J<span style="color:#ff0000;">&hearts;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>T<span style="color:#008800;">&clubs;</span>8<span style="color:#000000;">&spades;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>7<span style="color:#000000;">&spades;</span>5<span style="color:#000000;">&spades;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>4<span style="color:#ff0000;">&hearts;</span>3<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>6<span style="color:#008800;">&clubs;</span>4<span style="color:#008800;">&clubs;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#000000;">&spades;</span>3<span style="color:#000000;">&spades;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>9<span style="color:#ff0000;">&hearts;</span>6<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#008800;">&clubs;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>J<span style="color:#0088ff;">&diams;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 14: <b>8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>6<span style="color:#008800;">&clubs;</span>4<span style="color:#008800;">&clubs;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>3<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>9<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>Q<span style="color:#0088ff;">&diams;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>6<span style="color:#ff0000;">&hearts;</span>2<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>9<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>Q<span style="color:#000000;">&spades;</span>J<span style="color:#000000;">&spades;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>Q<span style="color:#008800;">&clubs;</span>8<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 15: <b>7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>6<span style="color:#ff0000;">&hearts;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#0088ff;">&diams;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>Q<span style="color:#ff0000;">&hearts;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>K<span style="color:#ff0000;">&hearts;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#008800;">&clubs;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>3<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>K<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>7<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>J<span style="color:#ff0000;">&hearts;</span>5<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

## Scenario 2: BB Calls LJ Open
_Blinds are $0.05/$0.10. Effective stacks are $10.00. You're on the button and action folds to you. You open for $0.30 (3bb), SB folds, and BB calls. You go to the flop with $9.70 behind and a pot of $0.65, and BB checks to you._
### Player Ranges

#### Hero's Hijack Opening Range Range

<style>
            .range {
                border: 3px solid black;
            }
            #styled_range_1 td {
                width: 40px;
                height: 40px;
                text-align: center;
                vertical-align: middle;
            }
            #styled_range_1 td.pair {
                background: #0072ef;
                border: 1px solid black;
            }
            #styled_range_1 td.offsuit {
                background: #ffff22;
                border: 1px solid black;
            }
            #styled_range_1 td.suited {
                background: #ee0000;
                border: 1px solid black;
            }
            </style>
<table id="styled_range_1" class="range">
<tr>
<td class="pair" style="background:#0072ef; color:#eee">AA<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">AKs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">AQs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">AJs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">ATs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A9s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">A8s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">A7s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">A6s<br><small>50</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A5s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">A4s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">A3s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">A2s<br><small>50</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">AKo<br><small>100</small></td>
<td class="pair" style="background:#0072ef; color:#eee">KK<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">KQs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">KJs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">KTs<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">K9s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">K8s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K7s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">AQo<br><small>100</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">KQo<br><small>50</small></td>
<td class="pair" style="background:#0072ef; color:#eee">QQ<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">QJs<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">QTs<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">Q9s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q8s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q7s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#cccc1b; color:#111">AJo<br><small>50</small></td>
<td class="offsuit" style="background:#cccc1b; color:#111">KJo<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">QJo<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">JJ<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">JTs<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">J9s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J8s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J7s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#cccc1b; color:#111">ATo<br><small>50</small></td>
<td class="offsuit" style="background:#999914; color:#111">KTo<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">QTo<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">JTo<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">TT<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T9s<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">T8s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T7s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T9o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">99<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">98s<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">97s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">96s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">95s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">94s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">93s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">92s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">98o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">88<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">87s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">86s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">85s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">84s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">83s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">82s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">97o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">87o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">77<br><small>100</small></td>
<td class="suited" style="background:#be0000; color:#eee">76s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">75s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">74s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">73s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">72s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">96o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">86o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">76o<br><small>0</small></td>
<td class="pair" style="background:#005bbf; color:#eee">66<br><small>50</small></td>
<td class="suited" style="background:#be0000; color:#eee">65s<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">64s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">63s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">62s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">95o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">85o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">75o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">65o<br><small>0</small></td>
<td class="pair" style="background:#005bbf; color:#eee">55<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">54s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">53s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">52s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">94o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">84o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">74o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">64o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">54o<br><small>0</small></td>
<td class="pair" style="background:#005bbf; color:#eee">44<br><small>50</small></td>
<td class="suited" style="background:#8e0000; color:#eee">43s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">42s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">93o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">83o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">73o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">63o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">53o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">43o<br><small>0</small></td>
<td class="pair" style="background:#00448f; color:#eee">33<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">32s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">92o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">82o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">72o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">62o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">52o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">42o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">32o<br><small>0</small></td>
<td class="pair" style="background:#00448f; color:#eee">22<br><small>0</small></td>
</tr>
</table>

#### Villain's Big Bling Calling Range vs Hijack Range

<style>
            .range {
                border: 3px solid black;
            }
            #styled_range_1 td {
                width: 40px;
                height: 40px;
                text-align: center;
                vertical-align: middle;
            }
            #styled_range_1 td.pair {
                background: #0072ef;
                border: 1px solid black;
            }
            #styled_range_1 td.offsuit {
                background: #ffff22;
                border: 1px solid black;
            }
            #styled_range_1 td.suited {
                background: #ee0000;
                border: 1px solid black;
            }
            </style>
<table id="styled_range_1" class="range">
<tr>
<td class="pair" style="background:#00448f; color:#eee">AA<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">AKs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">AQs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">AJs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">ATs<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A5s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A4s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A3s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">A2s<br><small>100</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">AKo<br><small>0</small></td>
<td class="pair" style="background:#00448f; color:#eee">KK<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">KQs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">KJs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">KTs<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K7s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K6s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">K5s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">K2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">AQo<br><small>0</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">KQo<br><small>100</small></td>
<td class="pair" style="background:#00448f; color:#eee">QQ<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">QJs<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">QTs<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">Q8s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q7s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">Q2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">AJo<br><small>100</small></td>
<td class="offsuit" style="background:#ffff22; color:#111">KJo<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">QJo<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">JJ<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">JTs<br><small>0</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">J8s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J7s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">J2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#ffff22; color:#111">ATo<br><small>100</small></td>
<td class="offsuit" style="background:#999914; color:#111">KTo<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">QTo<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">JTo<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">TT<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T9s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T8s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">T7s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T6s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T5s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T4s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T3s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">T2s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J9o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T9o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">99<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">98s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">97s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">96s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">95s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">94s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">93s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">92s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T8o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">98o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">88<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">87s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">86s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">85s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">84s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">83s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">82s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T7o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">97o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">87o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">77<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">76s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">75s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">74s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">73s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">72s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T6o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">96o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">86o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">76o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">66<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">65s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">64s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">63s<br><small>0</small></td>
<td class="suited" style="background:#8e0000; color:#eee">62s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T5o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">95o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">85o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">75o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">65o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">55<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">54s<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">53s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">52s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T4o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">94o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">84o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">74o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">64o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">54o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">44<br><small>100</small></td>
<td class="suited" style="background:#ee0000; color:#eee">43s<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">42s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T3o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">93o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">83o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">73o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">63o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">53o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">43o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">33<br><small>100</small></td>
<td class="suited" style="background:#8e0000; color:#eee">32s<br><small>0</small></td>
</tr>
<tr>
<td class="offsuit" style="background:#999914; color:#111">A2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">K2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">Q2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">J2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">T2o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">92o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">82o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">72o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">62o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">52o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">42o<br><small>0</small></td>
<td class="offsuit" style="background:#999914; color:#111">32o<br><small>0</small></td>
<td class="pair" style="background:#0072ef; color:#eee">22<br><small>100</small></td>
</tr>
</table>
### Flop 1: <b>A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>K<span style="color:#0088ff;">&diams;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>J<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>Q<span style="color:#0088ff;">&diams;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>6<span style="color:#0088ff;">&diams;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>A<span style="color:#ff0000;">&hearts;</span>K<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#008800;">&clubs;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>6<span style="color:#0088ff;">&diams;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>K<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#008800;">&clubs;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#ff0000;">&hearts;</span>A<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>5<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 2: <b>A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>7<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>6<span style="color:#0088ff;">&diams;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>A<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>7<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>Q<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#0088ff;">&diams;</span>2<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>Q<span style="color:#0088ff;">&diams;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#000000;">&spades;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>K<span style="color:#000000;">&spades;</span>J<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>4<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 3: <b>A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#008800;">&clubs;</span>T<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>6<span style="color:#0088ff;">&diams;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>7<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>J<span style="color:#ff0000;">&hearts;</span>J<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>J<span style="color:#0088ff;">&diams;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>9<span style="color:#000000;">&spades;</span>8<span style="color:#000000;">&spades;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>9<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>T<span style="color:#ff0000;">&hearts;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>K<span style="color:#ff0000;">&hearts;</span>Q<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>K<span style="color:#0088ff;">&diams;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span>2<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 4: <b>K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>8<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>9<span style="color:#008800;">&clubs;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>A<span style="color:#008800;">&clubs;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>K<span style="color:#0088ff;">&diams;</span>Q<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#008800;">&clubs;</span>K<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>K<span style="color:#ff0000;">&hearts;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>4<span style="color:#ff0000;">&hearts;</span>4<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#0088ff;">&diams;</span>K<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span>4<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 5: <b>K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#ff0000;">&hearts;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>K<span style="color:#ff0000;">&hearts;</span>Q<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>K<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#ff0000;">&hearts;</span>J<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>T<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>8<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>J<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>J<span style="color:#000000;">&spades;</span>T<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#ff0000;">&hearts;</span>A<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>7<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 6: <b>K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>5<span style="color:#000000;">&spades;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>K<span style="color:#008800;">&clubs;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#008800;">&clubs;</span>K<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#008800;">&clubs;</span>Q<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>K<span style="color:#008800;">&clubs;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>J<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>6<span style="color:#ff0000;">&hearts;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#008800;">&clubs;</span>7<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#ff0000;">&hearts;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: K<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 7: <b>Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>K<span style="color:#000000;">&spades;</span>K<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#008800;">&clubs;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>6<span style="color:#000000;">&spades;</span>5<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>T<span style="color:#000000;">&spades;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>K<span style="color:#000000;">&spades;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>J<span style="color:#0088ff;">&diams;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#ff0000;">&hearts;</span>A<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>Q<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 8: <b>Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>T<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#0088ff;">&diams;</span>8<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#0088ff;">&diams;</span>2<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>9<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>T<span style="color:#ff0000;">&hearts;</span>8<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>Q<span style="color:#008800;">&clubs;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>K<span style="color:#ff0000;">&hearts;</span>9<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#0088ff;">&diams;</span>K<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#000000;">&spades;</span>A<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#0088ff;">&diams;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>T<span style="color:#0088ff;">&diams;</span>7<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 9: <b>Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#008800;">&clubs;</span>6<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>K<span style="color:#ff0000;">&hearts;</span>8<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#008800;">&clubs;</span>Q<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>8<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>K<span style="color:#000000;">&spades;</span>K<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#ff0000;">&hearts;</span>2<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>K<span style="color:#008800;">&clubs;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>4<span style="color:#ff0000;">&hearts;</span>4<span style="color:#000000;">&spades;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>7<span style="color:#ff0000;">&hearts;</span>6<span style="color:#ff0000;">&hearts;</span></b>    (Flop: Q<span style="color:#000000;">&spades;</span>8<span style="color:#0088ff;">&diams;</span>6<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 10: <b>J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>T<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>J<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#ff0000;">&hearts;</span>5<span style="color:#ff0000;">&hearts;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>9<span style="color:#ff0000;">&hearts;</span>8<span style="color:#ff0000;">&hearts;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>A<span style="color:#ff0000;">&hearts;</span>Q<span style="color:#ff0000;">&hearts;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>8<span style="color:#ff0000;">&hearts;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>K<span style="color:#0088ff;">&diams;</span>J<span style="color:#0088ff;">&diams;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>K<span style="color:#000000;">&spades;</span>Q<span style="color:#ff0000;">&hearts;</span></b>    (Flop: J<span style="color:#000000;">&spades;</span>3<span style="color:#0088ff;">&diams;</span>2<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 11: <b>T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>T<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>T<span style="color:#ff0000;">&hearts;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>A<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>7<span style="color:#ff0000;">&hearts;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>A<span style="color:#008800;">&clubs;</span>K<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>8<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>Q<span style="color:#0088ff;">&diams;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>K<span style="color:#0088ff;">&diams;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>9<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 12: <b>T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#000000;">&spades;</span>J<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>K<span style="color:#ff0000;">&hearts;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#0088ff;">&diams;</span>6<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>4<span style="color:#0088ff;">&diams;</span>4<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>K<span style="color:#008800;">&clubs;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#000000;">&spades;</span>8<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#008800;">&clubs;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>8<span style="color:#0088ff;">&diams;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>8<span style="color:#000000;">&spades;</span>7<span style="color:#000000;">&spades;</span></b>    (Flop: T<span style="color:#000000;">&spades;</span>4<span style="color:#000000;">&spades;</span>2<span style="color:#000000;">&spades;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 13: <b>9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>K<span style="color:#000000;">&spades;</span>K<span style="color:#008800;">&clubs;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#000000;">&spades;</span>K<span style="color:#000000;">&spades;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>8<span style="color:#0088ff;">&diams;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#0088ff;">&diams;</span>Q<span style="color:#0088ff;">&diams;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>K<span style="color:#ff0000;">&hearts;</span>Q<span style="color:#000000;">&spades;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>T<span style="color:#ff0000;">&hearts;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>T<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>A<span style="color:#0088ff;">&diams;</span>2<span style="color:#0088ff;">&diams;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#008800;">&clubs;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#008800;">&clubs;</span>5<span style="color:#008800;">&clubs;</span></b>    (Flop: 9<span style="color:#000000;">&spades;</span>4<span style="color:#0088ff;">&diams;</span>3<span style="color:#008800;">&clubs;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 14: <b>8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>A<span style="color:#0088ff;">&diams;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>A<span style="color:#008800;">&clubs;</span>9<span style="color:#008800;">&clubs;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>T<span style="color:#008800;">&clubs;</span>8<span style="color:#008800;">&clubs;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>6<span style="color:#ff0000;">&hearts;</span>5<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>T<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#008800;">&clubs;</span>T<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>J<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>A<span style="color:#0088ff;">&diams;</span>7<span style="color:#0088ff;">&diams;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#ff0000;">&hearts;</span>J<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 8<span style="color:#000000;">&spades;</span>5<span style="color:#0088ff;">&diams;</span>3<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

### Flop 15: <b>7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span></b>
1. **Approximate each player's equity. Who has the equity advantage?**

2. **What are the weakest hands that could go all in on the flop? Go for three streets of value on blank turns?**

3. **Which player has the nuts advantage?**

4. **How static or dynamic is this flop? What aspects of this flop make it more static or dynamic?  How do these aspects interact with one another?**

5. **On this flop do you prefer to bet small or large?  With what frequencies would you check and bet?**

6. **Say you adopt a strategy where you either bet with your preferred sizing or check. You choose to bet and villain calls. What are the best and worst turn cards for your range?**

#### Hands
1. <b>Q<span style="color:#ff0000;">&hearts;</span>T<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

2. <b>A<span style="color:#008800;">&clubs;</span>3<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

3. <b>J<span style="color:#0088ff;">&diams;</span>9<span style="color:#0088ff;">&diams;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

4. <b>K<span style="color:#008800;">&clubs;</span>J<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

5. <b>9<span style="color:#ff0000;">&hearts;</span>7<span style="color:#ff0000;">&hearts;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

6. <b>K<span style="color:#ff0000;">&hearts;</span>K<span style="color:#000000;">&spades;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

7. <b>A<span style="color:#0088ff;">&diams;</span>5<span style="color:#0088ff;">&diams;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

8. <b>T<span style="color:#0088ff;">&diams;</span>T<span style="color:#008800;">&clubs;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

9. <b>9<span style="color:#ff0000;">&hearts;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**

10. <b>A<span style="color:#000000;">&spades;</span>9<span style="color:#000000;">&spades;</span></b>    (Flop: 7<span style="color:#000000;">&spades;</span>6<span style="color:#000000;">&spades;</span>6<span style="color:#0088ff;">&diams;</span>)

    1. **If you bet this hand should you expect better hands to fold? If so, which hands?**

    2. **If you bet this hand should you expect worse hands to call? If so, which hands?**

    3. **Does this hand benefit from a protection bet? Explain.**

    4. **Does this hand benefit from growing the pot? How so?**

    5. **How is this hand doing if you bet and get called? What parts of villain's range are you ahead of? Behind?**

    6. **How is this hand doing against a check-raise?**

    7. **What are this hand's incentives on this flop? Does it want to bet or check? If it wants to bet, what sizing does it prefer? Do these incentives line up with the strategy you proposed for your range above?**

    8. **Suppose you take your preferred action from the last question (check or bet the preferred size). If this is a bet, suppose villain calls. What are the best and worst turn cards for this hand?**



