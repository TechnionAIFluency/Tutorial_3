# The team

Each file in this folder is one person, with three lines:

    name: Your Name
    start: <a number from 70 to 95>
    minutes: <your answer>

On the `develop` branch there is a file `student.txt` with three empty lines: fill it in.

- `start`: the temperature of your coffee, in degrees C. Pick any number from 70 to 95.
- `minutes`: how long until it cools to 60 C.

CI checks every file in this folder (`tests/test_team.py`): it computes
`minutes` with `cooling.py` and fails if your number is different.
