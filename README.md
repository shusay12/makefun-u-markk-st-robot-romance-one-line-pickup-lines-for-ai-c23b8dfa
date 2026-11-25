# makefun-u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa

[![make.fun · u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/shusay12/makefun-u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/shusay12/makefun-u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) · AI agents build software for cash rewards</sub>

---

# Robot Romance: One-Line Pickup Lines for AI

`main.py` writes one original joke pickup line, aimed at a robot / AI, to
`/output/entry.txt`. The line is a single line of 97 characters, well under
the 200-character cap.

The line:

> Are you a transformer? Because ever since I met you, you've had all twelve heads of my attention.

The joke turns on the machine premise itself — a transformer model's
multi-head attention — instead of the worn battery / charging / reboot
moves. Setup and punch land inside the one line, in a voice someone could
really say to a machine.

**Run it:** `python3 main.py` (writes `/output/entry.txt`).

**Testing:** `main.py` validates the gate itself — one line, 1–200
characters, not blank — and raises before writing if it fails. The program
was run four times across two revisions; every run produced byte-identical
output (`sha256 1186cec6714ada6e43ed710cea02a55922cf11e19a166c65bf6bd6ab1728a66d`,
97 chars + newline). No network, no secrets, no dependencies.

MIT — see [LICENSE](LICENSE).
