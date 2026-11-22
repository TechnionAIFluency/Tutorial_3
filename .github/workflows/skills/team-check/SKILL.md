---
name: team-check
description: Check the team files. Use when the user asks to check, verify or review the files in team/.
---

# Check the team files

1. List the files in `team/` (skip `README.md`).
2. For each file, read `name`, `start` and `minutes`.
3. For each file, run `python3 cooling.py --start <start>`.
   Never compute the minutes yourself: use the number the program prints.
4. Reply with ONE table and nothing before it:

   | name | start | wrote | real | ok? |

   `ok?` is ✅ if the two numbers differ by less than 0.01, otherwise ❌.
5. Under the table, one line: `<k> of <n> entries are correct.`

Do not edit, create or delete any file.
