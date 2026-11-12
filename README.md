# Tutorial 3: Pull Requests, CI, and Your First Agent

Practice repository for **AI Fluency and Agentic Methods for Engineers**
(00560413, Technion). Follow along with the slides on the
[course tutorials page](https://technionaifluency.github.io/www/tutorials/).

## Getting started

1. Fork this repository. Uncheck **Copy the main branch only** so your fork
   includes both `main` and `develop`.
2. Clone **your fork** in VS Code and open it.
3. Switch to `develop`. It contains `team/student.txt`, the file you will
   fill in during Part 1.

## 1. Pull requests and continuous integration

**On your own**

1. Open `team/student.txt` on `develop` and enter your name, a starting
   temperature from 70 to 95 °C, and a guess for how many minutes it takes
   the drink to cool to 60 °C.
2. Commit the file locally. Wait until the group is ready before pushing.

**Together**

1. In your fork, add the **Python application** workflow from the **Actions**
   tab and commit it to `main`.
2. Push `develop`. Open a pull request **within your fork**, with `main` as
   the base branch and `develop` as the compare branch.
3. Read the failed check, fix `minutes` in `team/student.txt`, and push the
   fix to `develop`. Use `python3 cooling.py --start <temperature>` to check
   the result for your chosen temperature.
4. When the checks pass, review **Files changed** and merge the pull request.
   Switch to `main` in VS Code and pull the merged changes.

## 2. Your first coding agent

Start GitHub Copilot CLI in the repository folder and follow the slides to
sign in. In **Interactive** mode, ask Copilot to explain
[`cooling.py`](cooling.py) in two sentences without editing any files.
See [`AGENTS.md`](AGENTS.md) for the repository's agent instructions.

## 3. Agent skills

On `main`, ask Copilot: “Check the team files.” Read the result, then copy
[`extras/skills/team-check/`](extras/skills/team-check/) into `.github/skills/`.
Run `/skills reload` and ask the same question again. Compare the steps
Copilot takes and the format of its answer.

## 4. Your first agent-assisted commit

Create a branch named `add-team-skill` and ask Copilot to commit the skill you
just copied. Review the file, the Git commands, and the commit message before
approving. Include `Assisted-by: GitHub Copilot CLI` in the message.
Check the finished commit with `git show --stat HEAD`, then publish the
branch yourself.