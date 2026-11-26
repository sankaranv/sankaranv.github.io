#!/usr/bin/env python3
"""Generate assets/img/kolam-tile.svg: a seamless tile of a pulli (sikku) kolam, shown faintly in
the side margins as a CSS mask (so its colour comes from the theme).

The kolam is a mirror curve on a torus: one line runs diagonally between dots and turns in a
quarter circle around a dot wherever it meets a mirror. Mirrors are placed with reflection (D4)
symmetry only, so the pattern never forms a rotational pinwheel. Run from the repo root:

    python3 bin/kolam.py
"""
import math
from pathlib import Path

OUT = Path("assets/img/kolam-tile.svg")


def svg(width, height, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">{body}</svg>\n'


KOLAM_N = 6  # dots per side of the repeating tile
KOLAM_MIRRORS = [  # edge midpoints (half-cell units) where the line turns back; D4-symmetric
    (2, 3), (2, 9), (3, 2), (3, 4), (3, 8), (3, 10), (4, 3), (4, 5), (4, 7), (4, 9), (5, 4), (5, 8),
    (7, 4), (7, 8), (8, 3), (8, 5), (8, 7), (8, 9), (9, 2), (9, 4), (9, 8), (9, 10), (10, 3), (10, 9),
]


def kolam_tile(n=KOLAM_N, mirrors=frozenset(KOLAM_MIRRORS), s=10):
    m = 2 * n

    def out_dir(x, y, dx, dy):
        if (x % m, y % m) in mirrors:
            if x % 2 == 0:
                dx = -dx
            else:
                dy = -dy
        return dx, dy

    # trace every closed strand on the torus as (x, y, outgoing dx, dy) per edge midpoint
    seen, strands = set(), []
    for x in range(m):
        for y in range(m):
            if (x + y) % 2 == 0:
                continue
            for idx in (1, -1):
                for idy in (1, -1):  # incoming direction
                    if (x, y) + out_dir(x, y, idx, idy) in seen:
                        continue
                    pts, cx, cy, dx, dy = [], x, y, idx, idy
                    while True:
                        dx, dy = out_dir(cx, cy, dx, dy)
                        key = (cx % m, cy % m, dx, dy)
                        if key in seen:
                            break
                        seen.update({key, ((cx + dx) % m, (cy + dy) % m, -dx, -dy)})
                        pts.append((cx % m, cy % m, dx, dy))
                        cx, cy = cx + dx, cy + dy
                    if pts:
                        strands.append(pts)

    # straight runs between midpoints; quarter-circle (radius = half a diagonal step) round the dot at turns
    r, d = math.sqrt(0.5) * s, []
    for pts in strands:
        for i, (x, y, dx, dy) in enumerate(pts):
            ax, ay = pts[i - 1][2:]
            ndx, ndy = pts[(i + 1) % len(pts)][2:]
            turn, next_turn = (ax, ay) != (dx, dy), (dx, dy) != (ndx, ndy)
            start = (x + dx * 0.5, y + dy * 0.5) if turn else (x, y)
            end = (x + dx * 0.5, y + dy * 0.5) if next_turn else (x + dx, y + dy)
            pieces = [("L", start, end)] if start != end else []
            if turn:
                sweep = 1 if ax * dy - ay * dx > 0 else 0
                pieces.append((f"A{r:.2f},{r:.2f} 0 0 {sweep} ", (x - ax * 0.5, y - ay * 0.5), start))
            for cmd, (x1, y1), (x2, y2) in pieces:
                # repeat pieces that cross the tile edge on the opposite side, so the tile is seamless
                offs_x = [0] + ([m] if min(x1, x2) < 1 else []) + ([-m] if max(x1, x2) > m - 1 else [])
                offs_y = [0] + ([m] if min(y1, y2) < 1 else []) + ([-m] if max(y1, y2) > m - 1 else [])
                for ox in offs_x:
                    for oy in offs_y:
                        d.append(f"M{(x1 + ox) * s:.1f},{(y1 + oy) * s:.1f}{cmd}{(x2 + ox) * s:.1f},{(y2 + oy) * s:.1f}")
    dots = "".join(f'<circle cx="{(2 * j + 1) * s}" cy="{(2 * i + 1) * s}" r="1.3"/>' for i in range(n) for j in range(n))
    body = f'<path d="{"".join(d)}" fill="none" stroke="#000" stroke-width="1" stroke-linecap="round"/><g>{dots}</g>'
    return svg(m * s, m * s, body)


if __name__ == "__main__":
    OUT.write_text(kolam_tile())
