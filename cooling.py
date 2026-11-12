"""Coffee cooling simulator: Newton's law of cooling.

    T(t) = T_room + (T_start - T_room) * exp(-k * t)

It answers one question: how many minutes until a hot drink
cools down to a temperature you can drink?
"""
import argparse
import math
import sys

K = 0.045       # cooling constant k, in 1/min (a mug of coffee, no lid)
T_ROOM = 22.0   # room temperature, in degrees C


def minutes_to_cool(t_start, t_target, t_room=T_ROOM, k=K):
    """Minutes until a drink at t_start cools to t_target (all in degrees C).

    Spec:
      - If t_target >= t_start: return 0.0 (it is already cool enough).
      - If t_target <= t_room: raise ValueError (it never gets there).
      - If k <= 0: raise ValueError.
    """
    ratio = (t_target - t_room) / (t_start - t_room)
    return -math.log(ratio) / k


def main():
    parser = argparse.ArgumentParser(description="Minutes until your drink is cool enough.")
    parser.add_argument("--start", type=float, default=85.0, help="start temperature")
    parser.add_argument("--target", type=float, default=60.0, help="drinkable temperature")
    args = parser.parse_args()
    try:
        minutes = minutes_to_cool(args.start, args.target)
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    print(f"start = {args.start}")
    print(f"target = {args.target}")
    print(f"minutes = {minutes:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
