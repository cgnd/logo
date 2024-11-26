# /// script
# dependencies = [
#   "svg.py",
# ]
# ///

"""
Python script to generate Common Ground Electronics logo in SVG format.

Usage:
    uv run cgnd_logo.py > cgnd_logo.svg
"""

import svg


def draw() -> svg.SVG:
    return svg.SVG(
        width=500,
        height=500,
        elements=[
            # 1st layer
            svg.Polygon(
                points=[
                    (211, 56),
                    (237, 56),
                    (237, 228),
                    (371, 228),
                    (371, 254),
                    (77, 254),
                    (77, 228),
                    (211, 228),
                ],
                stroke="#EAFA5F",
                fill="#EAFA5F",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (105, 298),
                    (343, 298),
                    (343, 324),
                    (105, 324),
                ],
                stroke="#EAFA5F",
                fill="#EAFA5F",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (133, 368),
                    (315, 368),
                    (315, 394),
                    (133, 394),
                ],
                stroke="#EAFA5F",
                fill="#EAFA5F",
                stroke_width=0,
            ),
            # 2nd layer
            svg.Polygon(
                points=[
                    (237, 56),
                    (263, 82),
                    (263, 228),
                    (237, 228),
                ],
                stroke="#FA6DE4",
                fill="#FA6DE4",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (77, 254),
                    (371, 254),
                    (371, 228),
                    (397, 254),
                    (397, 280),
                    (103, 280),
                ],
                stroke="#FA6DE4",
                fill="#FA6DE4",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (105, 324),
                    (343, 324),
                    (343, 298),
                    (369, 324),
                    (369, 350),
                    (131, 350),
                ],
                stroke="#FA6DE4",
                fill="#FA6DE4",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (133, 394),
                    (315, 394),
                    (315, 368),
                    (341, 394),
                    (341, 420),
                    (159, 420),
                ],
                stroke="#FA6DE4",
                fill="#FA6DE4",
                stroke_width=0,
            ),
            # 3rd layer
            svg.Polygon(
                points=[
                    (263, 82),
                    (289, 108),
                    (289, 228),
                    (263, 228),
                ],
                stroke="#00F0CA",
                fill="#00F0CA",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (103, 280),
                    (397, 280),
                    (397, 254),
                    (423, 280),
                    (423, 306),
                    (351, 306),
                    (343, 298),
                    (121, 298),
                ],
                stroke="#00F0CA",
                fill="#00F0CA",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (131, 350),
                    (369, 350),
                    (369, 324),
                    (395, 350),
                    (395, 376),
                    (323, 376),
                    (315, 368),
                    (149, 368),
                ],
                stroke="#00F0CA",
                fill="#00F0CA",
                stroke_width=0,
            ),
            svg.Polygon(
                points=[
                    (159, 420),
                    (341, 420),
                    (341, 394),
                    (367, 420),
                    (367, 446),
                    (185, 446),
                ],
                stroke="#00F0CA",
                fill="#00F0CA",
                stroke_width=0,
            ),
        ],
    )


if __name__ == "__main__":
    print(draw())
