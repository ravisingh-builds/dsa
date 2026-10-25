# One coding phone + 45-minute clock

## What it is

The **first live coding interview**, before the long loop.

- **Google Meet** + their editor (**VIP**; some geos still use a doc).
- **~45 minutes** (sometimes 45–60).
- **DSA**, usually **one** medium problem (a follow-up if you finish).
- You **type**; you often **cannot Run**. **No Copilot / ChatGPT / Cursor.**
- “Phone” is a leftover name. It is **video coding**, not voice-only.

If this is a **yes** → they book the 3 DSA + Googliness.  
If it is **weak** → they may add a **second** coding phone. That is the only time there are two phones.

Language: **Python** is fine if you can write it without an IDE. Practice `range`, lists, loops in a plain editor.

## 45-minute split (talk the whole time)

Silence on video looks like stuck.

| Minutes | What you do |
|--------:|-------------|
| **0–5** | Restate **input / output**. One tiny example. Ask constraints if they have them. |
| **5–12** | A **correct** method first (complete search). Say time. Then: “If `n` is huge I need a skip **with a proof**.” |
| **12–30** | **Type** that method. Clear names. Narrate. |
| **30–38** | **Dry run** *your* code on the example (variables, not “the picture says 6”). Then **1–2 edges**. |
| **38–45** | Time / space. A **proven** faster idea only if you have one. ~1 min for their questions. |

If correct code is done at minute 25: edges + proven skip — don’t invent a second random problem.

## Dry run vs edges (same as this repo)

- **Dry run:** walk your loops on a **small list that holds water / has a real answer**.
- **Edges:** break an **assumption** (code shape: `n=1`; story: no valley). Wrong number = bug. Right number = that edge passed.

## Practice

Re-code a locked problem from a **blank file**, phone timer on this table, **no AI**.
