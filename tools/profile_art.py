# Artwork for the Sweax3169 GitHub profile: a banner and project cards, dark + light, as animated SVG.
# usage: python tools/profile_art.py art
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from art import T, FONT, MONO, defs, STYLE, mark

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)


def tile_windows(c, x, y):
    rows = ''.join(f'<circle cx="{x+30}" cy="{y+50+i*22}" r="3" fill="{h}"/><rect x="{x+42}" y="{y+46+i*22}" width="{w}" height="7" rx="3.5" fill="{c["bar2"] if i == 0 else c["bar"]}"/>'
                   for i, (h, w) in enumerate([(c['accent'], 120), (c['link'], 90), (c['shot'], 110), (c['code'], 70)]))
    return f'''<g class="f1"><g filter="url(#sh2)"><rect x="{x}" y="{y}" width="190" height="150" rx="14" fill="url(#pf)" stroke="{c['edge']}"/></g>
<rect x="{x+16}" y="{y+16}" width="90" height="8" rx="4" fill="{c['bar']}"/><line x1="{x+30}" y1="{y+40}" x2="{x+30}" y2="{y+140}" stroke="{c['rail']}"/>
<rect x="{x+38}" y="{y+40}" width="140" height="20" rx="6" fill="{c['sel']}" stroke="{c['accent']}" stroke-opacity=".35"/>{rows}</g>'''


def tile_audio(c, x, y):
    knobs = ''
    for i, (hue, a) in enumerate([(c['accent'], 220), (c['code'], 150), (c['link'], 260)]):
        cx = x + 40 + i * 55
        knobs += f'<circle cx="{cx}" cy="{y+60}" r="19" fill="{c["slate"]}" stroke="{c["edge"]}"/><path d="M{cx} {y+60} L{cx} {y+44}" stroke="{hue}" stroke-width="3" stroke-linecap="round" transform="rotate({a-200} {cx} {y+60})"/>'
    meter = ''.join(f'<rect x="{x+22+i*11}" y="{y+128-h}" width="7" height="{h}" rx="2" fill="{c["code"] if h < 30 else c["accent"]}" class="m" style="animation-delay:{i*.09}s"/>' for i, h in enumerate([18, 26, 34, 22, 14, 30, 38, 20, 12, 28, 16, 24, 32, 18]))
    return f'''<g class="f2"><g filter="url(#sh2)"><rect x="{x}" y="{y}" width="190" height="150" rx="14" fill="url(#pf)" stroke="{c['edge']}"/></g>{knobs}{meter}</g>'''


def tile_game(c, x, y):
    cubes = ''
    for i, (dx, dy, col) in enumerate([(0, 0, '#5CB85C'), (1, 0, '#5CB85C'), (2, 0, '#8B5A2B'), (0, 1, '#8B5A2B'), (1, 1, '#E4572E'), (2, 1, '#8B5A2B'), (1, 2, '#7DA8FF')]):
        px, py = x + 60 + dx * 26 - dy * 0, y + 90 - dy * 26
        cubes += f'<rect x="{px}" y="{py}" width="24" height="24" rx="4" fill="{col}" opacity=".92"/>'
    return f'''<g class="f3"><g filter="url(#sh2)"><rect x="{x}" y="{y}" width="190" height="150" rx="14" fill="url(#pf)" stroke="{c['edge']}"/></g>
<rect x="{x+14}" y="{y+14}" width="54" height="16" rx="5" fill="{c['accent']}" opacity=".85"/><rect x="{x+150}" y="{y+14}" width="26" height="16" rx="5" fill="{c['bar2']}"/>
{cubes}<rect x="{x+20}" y="{y+130}" width="150" height="6" rx="3" fill="{c['bar']}"/><rect x="{x+20}" y="{y+130}" width="96" height="6" rx="3" fill="{c['code']}" class="xp"/></g>'''


def tile_web(c, x, y):
    return f'''<g class="f4"><g filter="url(#sh2)"><rect x="{x}" y="{y}" width="190" height="150" rx="14" fill="url(#pf)" stroke="{c['edge']}"/></g>
<circle cx="{x+18}" cy="{y+18}" r="4" fill="{c['accent']}"/><circle cx="{x+31}" cy="{y+18}" r="4" fill="{c['files']}"/><circle cx="{x+44}" cy="{y+18}" r="4" fill="{c['code']}"/>
<rect x="{x+58}" y="{y+12}" width="118" height="12" rx="6" fill="{c['field']}" stroke="{c['edge']}"/>
<rect x="{x+16}" y="{y+40}" width="158" height="44" rx="8" fill="{c['slate']}"/><rect x="{x+28}" y="{y+54}" width="80" height="8" rx="4" fill="#fff" opacity=".85"/><rect x="{x+28}" y="{y+68}" width="54" height="6" rx="3" fill="#fff" opacity=".4"/>
<rect x="{x+16}" y="{y+94}" width="74" height="40" rx="7" fill="{c['field']}" stroke="{c['edge']}"/><rect x="{x+100}" y="{y+94}" width="74" height="40" rx="7" fill="{c['field']}" stroke="{c['edge']}"/>
<rect x="{x+26}" y="{y+106}" width="40" height="6" rx="3" fill="{c['link']}"/><rect x="{x+110}" y="{y+106}" width="40" height="6" rx="3" fill="{c['accent']}"/></g>'''


PSTYLE = '''<style>
  .f1,.f2,.f3,.f4{animation:bob 7s ease-in-out infinite}
  .f2{animation-delay:-1.8s}.f3{animation-delay:-3.6s}.f4{animation-delay:-5.4s}
  @keyframes bob{50%{transform:translateY(-7px)}}
  .m{animation:lvl 1.2s ease-in-out infinite alternate;transform-box:fill-box;transform-origin:bottom}
  @keyframes lvl{from{transform:scaleY(.55)}to{transform:scaleY(1)}}
  .xp{animation:xp 4s ease-in-out infinite}
  @keyframes xp{0%{width:40px}70%,100%{width:150px}}
  @media (prefers-reduced-motion: reduce){.f1,.f2,.f3,.f4,.m,.xp{animation:none}}
</style>'''


def banner(theme):
    c = T[theme]
    W, H = 1280, 400
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Sweax — independent developer, Sweax Studios">
{PSTYLE}
{defs(c)}
<rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
<ellipse cx="1000" cy="80" rx="420" ry="260" fill="url(#g1)"/>
<ellipse cx="780" cy="420" rx="380" ry="200" fill="url(#g2)"/>
<ellipse cx="1240" cy="380" rx="260" ry="200" fill="url(#g3)"/>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="23.5" fill="none" stroke="{c['edge']}"/>
<text x="84" y="104" font-family="{FONT}" font-size="16" fill="{c['ink3']}">Independent developer · Sweax Studios · Türkiye</text>
<text x="80" y="186" font-family="{FONT}" font-size="76" font-weight="700" letter-spacing="-2" fill="{c['ink']}">Sweax</text>
<text x="84" y="240" font-family="{FONT}" font-size="22" fill="{c['ink2']}">I build Windows apps, audio plugins, Roblox games</text>
<text x="84" y="270" font-family="{FONT}" font-size="22" fill="{c['ink2']}">and web apps — and ship each one all the way.</text>
<g font-family="{FONT}" font-size="14" font-weight="600">
  <rect x="84" y="306" width="96" height="30" rx="9" fill="{c['field']}" stroke="{c['edge']}"/><circle cx="100" cy="321" r="4" fill="{c['link']}"/><text x="112" y="326" fill="{c['ink2']}">Windows</text>
  <rect x="190" y="306" width="78" height="30" rx="9" fill="{c['field']}" stroke="{c['edge']}"/><circle cx="206" cy="321" r="4" fill="{c['code']}"/><text x="218" y="326" fill="{c['ink2']}">Audio</text>
  <rect x="278" y="306" width="84" height="30" rx="9" fill="{c['field']}" stroke="{c['edge']}"/><circle cx="294" cy="321" r="4" fill="{c['accent']}"/><text x="306" y="326" fill="{c['ink2']}">Games</text>
  <rect x="372" y="306" width="64" height="30" rx="9" fill="{c['field']}" stroke="{c['edge']}"/><circle cx="388" cy="321" r="4" fill="{c['shot']}"/><text x="400" y="326" fill="{c['ink2']}">Web</text>
</g>
{tile_windows(c, 720, 40)}
{tile_audio(c, 930, 74)}
{tile_game(c, 760, 214)}
{tile_web(c, 970, 236)}
</svg>'''


CARDS = [
    ('sweaxmorph', 'SweaxMorph', ['Drop any file on Morph, pick a format, done.', '126 formats for Windows, offline.'], 'C# · .NET 9 · WPF · FFmpeg · ImageMagick', 'Open source', 'shot', 'morph'),
    ('sweaxterrain', 'Sweax Terrain', ['Roblox Studio plugin that paints terrain:', '9 biomes and 8 ready-made worlds.'], 'Luau · Roblox Studio plugin', 'Plugin', 'code', 'T'),
    ('sweaxclip', 'SweaxClip', ['Permanent, searchable clipboard history for', 'Windows. Replaces Win + V; reads screenshots.'], 'C# · .NET 9 · WPF · SQLite FTS5', 'Open source', 'link', 'deck'),
    ('sweaxcut', 'SWEAXCUT 3', ['Offline video editor for Windows: one-click', 'edits, word-by-word captions you can restyle.'], 'Electron · React · WebGL2 · FFmpeg · whisper.cpp', 'Open source', 'accent', 'cut'),
    ('sweaxnext', 'SWEAX NEXT', ['Vocal mixing plugin for rap: 12 vocal chains,', '159 automated tests, pluginval strictness 10.'], 'C++ · JUCE · VST3', 'VST3', 'code', 'N'),
    ('sweaxbeacon', 'SweaxBeacon', ['Minecraft Java powers, items and world controls', 'on a server, a LAN world or single-player.'], 'Electron · React · C# · RCON', 'Open source', 'shot', 'beacon'),
    ('popit', '+1 Speed POP IT', ['Roblox game with session-locked saves and', 'a phone-friendly world of 70,000+ parts.'], 'Luau · Roblox Studio', 'Released', 'image', '+1'),
    ('adana', 'Adana Mücadele', ['Website and member platform for an MMA', 'club, live with real members.'], 'Cloudflare Workers · D1 · R2', 'Live', 'files', 'A'),
]


def morph_icon(cx, cy, r):
    """SweaxMorph's mascot, small: a lilac-to-pink gel drop with a face."""
    return f'''<defs><linearGradient id="mg" x1=".2" y1="0" x2=".8" y2="1"><stop offset="0" stop-color="#CDB8FF"/><stop offset="1" stop-color="#FF8FC1"/></linearGradient></defs>
<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * .96}" fill="url(#mg)"/>
<ellipse cx="{cx - r * .42}" cy="{cy - r * .5}" rx="{r * .28}" ry="{r * .13}" fill="#fff" opacity=".55" transform="rotate(-28 {cx - r * .42} {cy - r * .5})"/>
<ellipse cx="{cx - r * .31}" cy="{cy - r * .06}" rx="{r * .1}" ry="{r * .13}" fill="#2B2140"/><ellipse cx="{cx + r * .31}" cy="{cy - r * .06}" rx="{r * .1}" ry="{r * .13}" fill="#2B2140"/>
<path d="M{cx - r * .12} {cy + r * .16} Q{cx} {cy + r * .27} {cx + r * .12} {cy + r * .16}" stroke="#2B2140" stroke-width="{r * .07}" stroke-linecap="round" fill="none"/>'''


def cut_icon(x, y, size):
    """SWEAXCUT's mark: a frame cut on the diagonal, the red half slid along the cut (24-unit grid)."""
    k = size / 24
    P = lambda a, b: f"{x + a * k:.1f},{y + b * k:.1f}"
    left = f"M{P(6, 3)} L{P(13.7, 3)} L{P(8.7, 21)} L{P(6, 21)} Q{P(3, 21)} {P(3, 18)} L{P(3, 6)} Q{P(3, 3)} {P(6, 3)} Z"
    right = f"M{P(15.3, 3)} L{P(18, 3)} Q{P(21, 3)} {P(21, 6)} L{P(21, 18)} Q{P(21, 21)} {P(18, 21)} L{P(10.3, 21)} Z"
    return f'''<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="13" fill="#13161C"/><path d="{left}" fill="#F4F6FA"/><path d="{right}" fill="#FF4B3E" transform="translate({0.5 * k:.1f} {-1.3 * k:.1f})"/>'''


def beacon_icon(x, y, size):
    """SweaxBeacon's mark: a beacon on a three-step pyramid with its beam (32-unit grid)."""
    k = size / 32
    R = lambda a, b, w, h, f: f'<rect x="{x + a * k:.1f}" y="{y + b * k:.1f}" width="{w * k:.1f}" height="{h * k:.1f}" fill="{f}"/>'
    return (f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="13" fill="#120D1B"/>'
            + R(14, 3, 4, 10, '#8EF6FF') + R(4, 25, 24, 4, '#2B1F40') + R(4, 25, 24, 1, '#4A3870') + R(7, 21, 18, 4, '#3A2B57')
            + R(7, 21, 18, 1, '#5E4A8F') + R(10, 17, 12, 4, '#4D3A75') + R(10, 17, 12, 1, '#7A62B0') + R(12, 11, 8, 7, '#BFF3FA')
            + R(13, 12, 6, 5, '#5FD0E2') + R(14, 13, 4, 3, '#FFFFFF'))


def card(theme, key, name, lines, stack, status, hue, initial):
    c = T[theme]
    W, H = 600, 210
    icon = mark(26, 30, 0.19) if initial == 'deck' else morph_icon(51, 53, 23) if initial == 'morph' else cut_icon(28, 30, 46) if initial == 'cut' else beacon_icon(28, 30, 46) if initial == 'beacon' else f'<rect x="28" y="30" width="46" height="46" rx="13" fill="{c[hue]}"/><text x="51" y="61" text-anchor="middle" font-family="{FONT}" font-size="{19 if len(initial) > 1 else 22}" font-weight="700" fill="#fff">{initial}</text>'
    sw = 34 + 7.6 * len(status)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{name}">
{defs(c)}
<rect width="{W}" height="{H}" rx="18" fill="url(#pf)"/>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="17.5" fill="none" stroke="{c['edge']}"/>
<rect x="0" y="30" width="3" height="46" rx="1.5" fill="{c[hue]}"/>
{icon}
<text x="92" y="60" font-family="{FONT}" font-size="22" font-weight="650" fill="{c['ink']}">{name}</text>
<rect x="{W-28-sw}" y="36" width="{sw}" height="26" rx="8" fill="{c['field']}" stroke="{c['edge']}"/>
<circle cx="{W-28-sw+13}" cy="49" r="3.5" fill="{c[hue]}"/>
<text x="{W-28-sw+22}" y="54" font-family="{FONT}" font-size="12.5" font-weight="600" fill="{c['ink2']}">{status}</text>
<text x="28" y="116" font-family="{FONT}" font-size="16" fill="{c['ink2']}">{lines[0]}</text>
<text x="28" y="140" font-family="{FONT}" font-size="16" fill="{c['ink2']}">{lines[1]}</text>
<text x="28" y="184" font-family="{MONO}" font-size="12.5" fill="{c['ink3']}">{stack}</text>
</svg>'''


for theme in ('dark', 'light'):
    open(os.path.join(OUT, f'banner-{theme}.svg'), 'w', encoding='utf-8').write(banner(theme))
    for key, name, lines, stack, status, hue, initial in CARDS:
        open(os.path.join(OUT, f'card-{key}-{theme}.svg'), 'w', encoding='utf-8').write(card(theme, key, name, lines, stack, status, hue, initial))
print('ok')
