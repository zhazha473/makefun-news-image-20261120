#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news wire board (1024x1024 PNG).

Fresh code written in this session. Deterministic: same input always yields
the same PNG bytes (fixed fonts, fixed geometry, no timestamps).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
REG = FONT_DIR + "DejaVuSans.ttf"

NAVY = (13, 27, 46)
PANEL = (22, 50, 74)
PANEL2 = (18, 42, 63)
WHITE = (245, 247, 250)
MUTED = (159, 179, 200)
AMBER = (245, 179, 1)
TEAL = (45, 190, 190)
RED = (229, 72, 77)
GREEN = (74, 200, 120)
BLUE = (90, 160, 255)
INK = (10, 20, 32)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width."""
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def panel_box(draw, x, y, w, h, accent):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=PANEL)
    draw.rounded_rectangle([x, y, x + w, y + 6], radius=3, fill=accent)
    draw.rounded_rectangle([x, y + 3, x + w, y + 6], radius=0, fill=accent)


def headline_block(draw, x, y, w, head, body, tag, hsize=21, bsize=13,
                   max_body=2):
    hf, bf, tf = font(BOLD, hsize), font(REG, bsize), font(BOLD, 11)
    lines = wrap(draw, head, hf, w)
    yy = y
    for ln in lines[:2]:
        draw.text((x, yy), ln, font=hf, fill=WHITE)
        yy += hsize + 3
    yy += 2
    for ln in wrap(draw, body, bf, w)[:max_body]:
        draw.text((x, yy), ln, font=bf, fill=MUTED)
        yy += bsize + 4
    return yy


def tag_text(draw, x, y, text):
    tf = font(BOLD, 11)
    draw.text((x, y), text, font=tf, fill=AMBER)


# --- pictograms (simple geometric drawings, one per hero story) ---

def pic_cyclone(draw, x, y, s):
    # spiral of arcs + eye
    cx, cy = x + s // 2, y + s // 2
    for r, col in [(52, TEAL), (42, (90, 210, 210)), (32, (140, 225, 225)),
                   (22, (200, 240, 245))]:
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=20, end=300,
                 fill=col, width=7)
    draw.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=AMBER)
    for i in range(5):  # rain streaks
        rx = x + 12 + i * 18
        draw.line([rx, y + s - 22, rx - 6, y + s - 6], fill=BLUE, width=3)


def pic_taiz(draw, x, y, s):
    # mountains, city blocks, blast star
    draw.polygon([(x, y + s), (x + 55, y + 18), (x + 110, y + s)], fill=(38, 74, 104))
    draw.polygon([(x + 70, y + s), (x + 130, y + 4), (x + 190, y + s)],
                 fill=(30, 60, 88))
    for bx, bw, bh in [(x + 8, 26, 34), (x + 40, 20, 26), (x + 66, 30, 42),
                       (x + 102, 22, 30), (x + 130, 26, 38)]:
        draw.rectangle([bx, y + s - bh, bx + bw, y + s], fill=(120, 140, 165))
        draw.rectangle([bx + 4, y + s - bh + 5, bx + bw - 4, y + s - bh + 10],
                       fill=AMBER)
    cx, cy = x + s - 34, y + 26
    for dx, dy in [(0, -16), (11, -11), (16, 0), (11, 11), (0, 16),
                   (-11, 11), (-16, 0), (-11, -11)]:
        draw.line([cx, cy, cx + dx, cy + dy], fill=AMBER, width=4)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED)


def pic_gta(draw, x, y, s):
    # skyline + game controller
    for bx, bw, bh in [(x, 26, 44), (x + 30, 20, 62), (x + 54, 24, 50),
                       (x + 82, 18, 70), (x + 104, 26, 46)]:
        draw.rectangle([bx, y + s - bh, bx + bw, y + s], fill=(52, 92, 130))
        for wy in range(3):
            draw.rectangle([bx + 4, y + s - bh + 6 + wy * 12, bx + bw - 4,
                            y + s - bh + 10 + wy * 12], fill=AMBER)
    cx, cy = x + s // 2, y + s - 46
    draw.rounded_rectangle([cx - 78, cy - 22, cx + 78, cy + 22], radius=18,
                           fill=(200, 60, 90))
    draw.ellipse([cx - 58, cy - 4, cx - 38, cy + 16], fill=INK)
    draw.ellipse([cx + 38, cy - 16, cx + 58, cy + 4], fill=INK)
    draw.rectangle([cx - 18, cy - 14, cx - 6, cy + 10], fill=WHITE)
    draw.rectangle([cx - 24, cy - 8, cx, cy + 4], fill=WHITE)
    for ox, oy in [(26, -12), (38, -4), (26, 4), (14, -4)]:
        draw.ellipse([cx + ox - 4, cy + oy - 4, cx + ox + 4, cy + oy + 4],
                     fill=AMBER)


def pic_cricket(draw, x, y, s):
    # stumps, bat, ball
    for sx in (x + 30, x + 42, x + 54):
        draw.rectangle([sx, y + 20, sx + 6, y + s - 20], fill=AMBER)
    draw.rectangle([x + 30, y + 14, x + 60, y + 20], fill=AMBER)
    draw.rounded_rectangle([x + 110, y + 8, x + 132, y + s - 30], radius=8,
                           fill=(214, 178, 120))
    draw.rectangle([x + 118, y + s - 30, x + 124, y + s - 8], fill=(120, 90, 50))
    draw.ellipse([x + 150, y + s - 46, x + 178, y + s - 18], fill=RED)
    draw.arc([x + 150, y + s - 46, x + 178, y + s - 18], start=0, end=360,
             fill=(255, 255, 255), width=2)


def pic_envoy(draw, x, y, s):
    # EU circle of stars + embassy columns
    cx, cy = x + 52, y + s // 2
    draw.ellipse([cx - 46, cy - 46, cx + 46, cy + 46], fill=(30, 70, 160))
    import math
    for k in range(12):
        a = math.pi * 2 * k / 12 - math.pi / 2
        sx, sy = cx + 32 * math.cos(a), cy + 32 * math.sin(a)
        draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=AMBER)
    bx = x + 118
    draw.rectangle([bx, y + 18, bx + 76, y + 26], fill=(120, 140, 165))
    for cx2 in (bx + 6, bx + 26, bx + 46):
        draw.rectangle([cx2, y + 26, cx2 + 12, y + s - 14], fill=(150, 168, 190))
    draw.rectangle([bx, y + s - 14, bx + 76, y + s - 6], fill=(120, 140, 165))


def pic_summit(draw, x, y, s):
    # two flags + arrow between them
    draw.rectangle([x + 6, y + 14, x + 66, y + 62], fill=(30, 70, 160))
    for k in range(8):
        import math
        a = math.pi * 2 * k / 8 - math.pi / 2
        sx, sy = x + 36 + 16 * math.cos(a), y + 38 + 16 * math.sin(a)
        draw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=AMBER)
    # Union Jack (simplified): blue field, white saltire, red saltire,
    # white cross, red cross
    fx, fy, fw, fh = x + 128, y + 14, 60, 48
    draw.rectangle([fx, fy, fx + fw, fy + fh], fill=(30, 60, 140))
    draw.line([fx, fy, fx + fw, fy + fh], fill=WHITE, width=9)
    draw.line([fx + fw, fy, fx, fy + fh], fill=WHITE, width=9)
    draw.line([fx, fy, fx + fw, fy + fh], fill=(200, 40, 60), width=4)
    draw.line([fx + fw, fy, fx, fy + fh], fill=(200, 40, 60), width=4)
    draw.rectangle([fx, fy + fh // 2 - 7, fx + fw, fy + fh // 2 + 7],
                   fill=WHITE)
    draw.rectangle([fx + fw // 2 - 6, fy, fx + fw // 2 + 6, fy + fh],
                   fill=WHITE)
    draw.rectangle([fx, fy + fh // 2 - 3, fx + fw, fy + fh // 2 + 3],
                   fill=(200, 40, 60))
    draw.rectangle([fx + fw // 2 - 3, fy, fx + fw // 2 + 3, fy + fh],
                   fill=(200, 40, 60))
    draw.line([x + 74, y + 38, x + 120, y + 38], fill=AMBER, width=5)
    draw.polygon([(x + 120, y + 30), (x + 120, y + 46), (x + 132, y + 38)],
                 fill=AMBER)


HEROES = [
    # (pictogram, accent, headline, body, tag)
    (pic_cyclone, TEAL, "CYCLONE AKVAN DUE TO HIT ODISHA",
     "Landfall near Gopalpur ~noon IST; winds to 110 km/h; ~105,000 "
     "evacuated.",
     "ASIA \u00b7 IMD"),
    (pic_taiz, RED, "INSIDE BESIEGED TAIZ",
     "A mother tells her son the blasts are \u201cjust fireworks\u201d; 148 "
     "civilians killed since August.", "MIDDLE EAST \u00b7 BBC"),
    (pic_gta, (200, 60, 90), "GTA VI: 19M COPIES IN A DAY",
     "Day-one sales near 19.1m copies, about $1.84bn; streams peak at 7.9m.",
     "TECH \u00b7 SENSOR TOWER"),
]

ROW2 = [
    (pic_cricket, GREEN, "PHILLIPS TON LIFTS NZ TO 317-6",
     "Glenn Phillips 118, Nicholls 146* at lunch; a 216-run stand.",
     "SPORT \u00b7 AP"),
    (pic_envoy, BLUE, "EU SUMMONS RUSSIAN ENVOY",
     "Strikes damage Austrian and Dutch embassies in Kyiv; one killed, "
     "five hurt.", "EUROPE \u00b7 AFP"),
    (pic_summit, AMBER, "BURNHAM MEETS EU LEADERS TODAY",
     "Brussels talks on trade rules, carbon markets and youth visas.",
     "EUROPE \u00b7 TODAY"),
]

BRIEFS = [
    ("APEC AFTERMATH", "What Trump, Xi and Putin each got from the historic Shenzhen talks.", "BBC"),
    ("IRAN STILL ARMED", "US intel: Tehran still holds 2,500+ missiles after nine months of conflict.", "WSJ"),
    ("BAPCO RESTARTS", "Bahrain refinery nears full output after six conflict strikes.", "WIRE"),
    ("NATO TALKS", "NATO chief meets intelligence chiefs in Brussels.", "WIRE"),
    ("EU v AUSTRIA", "Commission takes Austria to court over arrest-warrant rules.", "WIRE"),
    ("GULF RAILWAY", "Six-nation rail link planned to cut reliance on the Strait of Hormuz.", "WIRE"),
    ("MERZ ON UKRAINE", "Berlin: sustained support for Kyiv; terms set for peace talks.", "WIRE"),
    ("ALASKA PROBE", "US Justice Dept. issues 200+ subpoenas in an Alaska election inquiry.", "WIRE"),
    ("SAUDI\u2013CENTCOM", "Crown prince and US CENTCOM chief talk defence ties.", "WIRE"),
    ("XI: TALK TO BOTH", "China\u2019s Xi: constructive engagement with Moscow and Washington is essential.", "WIRE"),
    ("HOCKEY OPENS", "Women\u2019s Asian Hockey Champions Trophy begins.", "WIRE"),
    ("CANADA\u2019S AI BET", "Canada embraces AI data centres as US states push back.", "BBC"),
    ("COP31", "Climate talks continue in T\u00fcrkiye; India presses finance for resilience.", "WIRE"),
]

REGIONS = [("ASIA", 4), ("EUROPE", 6), ("MIDDLE EAST", 5),
           ("OCEANIA", 1), ("AMERICAS", 3)]


def draw_board():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 100], fill=(8, 18, 32))
    d.rectangle([0, 100, W, 104], fill=AMBER)
    d.text((14, 10), "THE WORLD", font=font(BOLD, 58), fill=WHITE)
    d.text((14, 74), "WIRE BOARD  \u00b7  THE DAY SO FAR",
           font=font(BOLD, 15), fill=AMBER)
    right = "FRIDAY 20 NOVEMBER 2026"
    d.text((W - 14 - d.textlength(right, font=font(BOLD, 26)), 14), right,
           font=font(BOLD, 26), fill=WHITE)
    sub = "19 STORIES \u00b7 5 REGIONS \u00b7 AS REPORTED BY 01:00 UTC"
    d.text((W - 14 - d.textlength(sub, font=font(BOLD, 14)), 52), sub,
           font=font(BOLD, 14), fill=MUTED)

    # ---- hero row ----
    pw, ph, gap, y0 = 322, 260, 12, 116
    for i, (pic, accent, head, body, tag) in enumerate(HEROES):
        x = 12 + i * (pw + gap)
        panel_box(d, x, y0, pw, ph, accent)
        pic(d, x + 16, y0 + 14, 120)
        headline_block(d, x + 16, y0 + 140, pw - 32, head, body, tag, 21, 13)
        tag_text(d, x + 16, y0 + ph - 24, tag)

    # ---- second row ----
    y1 = 388
    ph2 = 200
    for i, (pic, accent, head, body, tag) in enumerate(ROW2):
        x = 12 + i * (pw + gap)
        panel_box(d, x, y1, pw, ph2, accent)
        pic(d, x + 16, y1 + 12, 84)
        headline_block(d, x + 16, y1 + 102, pw - 32, head, body, tag, 19, 13)
        tag_text(d, x + 16, y1 + ph2 - 24, tag)

    # ---- regions strip ----
    y2 = 600
    d.rounded_rectangle([12, y2, W - 12, y2 + 52], radius=10, fill=PANEL2)
    d.text((26, y2 + 16), "WHERE IT HAPPENED", font=font(BOLD, 15), fill=WHITE)
    cx = 240
    for name, n in REGIONS:
        chip = f"{name} {n}"
        wch = d.textlength(chip, font=font(BOLD, 14)) + 22
        d.rounded_rectangle([cx, y2 + 12, cx + wch, y2 + 40], radius=14,
                            fill=(38, 74, 104))
        d.text((cx + 11, y2 + 18), chip, font=font(BOLD, 14), fill=WHITE)
        cx += wch + 10

    # ---- wire briefs ----
    y3 = 668
    d.text((14, y3), "THE WIRE \u2014 13 MORE STORIES",
           font=font(BOLD, 16), fill=AMBER)
    d.line([14, y3 + 26, W - 14, y3 + 26], fill=(38, 74, 104), width=2)
    col_w = 488
    bf, lf, sf = font(REG, 13), font(BOLD, 13), font(BOLD, 10)
    row_h = 37
    for i, (lead, text, src) in enumerate(BRIEFS):
        col = i % 2
        row = i // 2
        bx = 14 + col * (col_w + 12)
        by = y3 + 36 + row * row_h
        d.ellipse([bx, by + 5, bx + 7, by + 12], fill=TEAL)
        lead_txt = f"{lead} \u2014 "
        lw = d.textlength(lead_txt, font=lf)
        d.text((bx + 12, by), lead_txt, font=lf, fill=WHITE)
        sw = d.textlength(src, font=sf)
        # first line must leave room for the source tag at the right edge
        first_w = col_w - 12 - lw - sw - 10
        rest_w = col_w - 12
        lines = wrap(d, text, bf, first_w)
        if lines:
            d.text((bx + 12 + lw, by), lines[0], font=bf, fill=MUTED)
            rest = " ".join(lines[1:])
            for j, ln in enumerate(wrap(d, rest, bf, rest_w)[:1]):
                d.text((bx + 12, by + 17), ln, font=bf, fill=MUTED)
        d.text((bx + col_w - sw, by), src, font=sf, fill=AMBER)

    # ---- footer ----
    y4 = 962
    d.rectangle([0, y4, W, H], fill=(8, 18, 32))
    d.text((14, y4 + 10),
           "LATER TODAY:  Akvan landfall ~06:30 UTC  \u00b7  Burnham\u2013EU talks in "
           "Brussels  \u00b7  Take-Two\u2019s official GTA VI figures expected",
           font=font(BOLD, 13), fill=WHITE)
    d.text((14, y4 + 34),
           "Sources: BBC \u00b7 Reuters \u00b7 AP \u00b7 AFP \u00b7 IMD \u00b7 Sensor Tower "
           "\u2014 all as reported 20 November 2026. Image drawn in code.",
           font=font(REG, 12), fill=MUTED)
    return img


if __name__ == "__main__":
    board = draw_board()
    board.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", board.size)
