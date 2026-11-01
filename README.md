<picture>
  <source media="(prefers-color-scheme: dark)" srcset="art/banner-dark.svg">
  <img alt="Sweax — independent developer at Sweax Studios, Türkiye. I build Windows apps, audio plugins, Roblox games and web apps, and ship each one all the way." src="art/banner-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://sweaxstudios.xyz"><b>sweaxstudios.xyz</b></a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Sweax3169/sweaxmorph">SweaxMorph</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Sweax3169/sweaxclip">SweaxClip</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/Sweax3169/sweaxcut">SWEAXCUT</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://discord.gg/vGZ2DZZsrf">Discord</a>
</p>

<br>

I'm an independent developer from Türkiye, working as **Sweax Studios**. I build native Windows software, audio plugins, Roblox games and web platforms, and I take each one all the way to release — code, interface, installer, tests and documentation. I also produce rap beats, which is why some of my tools are about sound.

<br>

## Featured

<a href="https://github.com/Sweax3169/sweaxdrop">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxdrop-dark.svg">
    <img alt="SweaxDrop: your files, on parallel lanes. Files, photos, folders and text between Windows, Android and iPhone." src="art/sweaxdrop-light.svg" width="100%">
  </picture>
</a>

**[SweaxDrop](https://github.com/Sweax3169/sweaxdrop)** sends files, photos, videos, whole folders, text and the clipboard between a PC and phones over your own Wi-Fi. Devices find each other, every transfer runs on parallel TLS 1.3 lanes and is checked chunk by chunk with BLAKE3, and a dropped connection resumes from the last verified chunk. Windows, Android and iPhone share one Rust core and one interface; an iPhone without the app scans a QR code and uses it in the browser.

<p align="center">
  <img alt="SweaxDrop on Windows: three files dropped on an iPhone, twelve photos accepted from it, the speed curve in history." src="art/sweaxdrop-demo.gif" width="680">
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- One Rust core: discovery (multicast, broadcast, mDNS), mutual TLS 1.3 pinned by Ed25519 key, SPAKE2 PIN and QR pairing
- Up to 16 lanes pulling 4 MiB chunks from one queue, no request per file, reads, hashes and writes on their own threads
- Windows app in Tauri (tray, Send to, drag and drop), Android in Kotlin over JNI, iPhone in Swift over a C ABI
- A browser client served by the PC for phones without the app

</td>
<td width="50%" valign="top">

**Shipped with**
- Measured against the official LocalSend 1.18.2 on the same PC and files: 4.8× faster with 200 photos, 3.0× with 10 000 small files, 3.4× with 300 small files, and a tie on one 4 GiB file, where the disk is the limit
- Tests for transfers, resume after a cut connection, wrong keys, PIN and QR pairing
- Android checked on the emulator in both directions, byte-identical; iOS built on a macOS runner
- A [website](https://sweax3169.github.io/sweaxdrop/) with the real interface running on a pretend network

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxdrop/releases/latest) · [Website](https://sweax3169.github.io/sweaxdrop/) · [Source](https://github.com/Sweax3169/sweaxdrop)

<br>

<a href="https://github.com/Sweax3169/sweaxiris">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxiris-dark.svg">
    <img alt="SweaxIris: a screen recorder for Windows that opens like a lens. A screen, a window or a region you draw, with system sound and microphone." src="art/sweaxiris-light.svg" width="100%">
  </picture>
</a>

**[SweaxIris](https://github.com/Sweax3169/sweaxiris)** is a screen recorder for Windows. Record a whole monitor, one window or a region you draw with a screenshot-style picker, with system sound and your microphone, each with its own switch, volume and meter. Pause and resume carry on in the same file, and every action has a shortcut you set by pressing it, macro keys included. The record button is a camera iris: it opens when you record and stops down with each second of the countdown.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxiris-demo-dark.gif">
    <img alt="The SweaxIris studio: the iris counts down 3-2-1, records with live sound meters, pauses, resumes and saves a take." src="art/sweaxiris-demo-light.gif" width="680">
  </picture>
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- Windows.Graphics.Capture with a ring of timestamped frames, so each tick takes the frame composed at its moment (24–240 fps)
- Direct3D 11 video engine for scaling and NV12; NVENC and AMF read straight from video memory, Quick Sync and x264 through staging
- Own WASAPI capture (speakers, microphone, one app) and a mixer that places sound by time and absorbs clock drift
- One timeline for picture and sound that stops while paused

</td>
<td width="50%" valign="top">

**Shipped with**
- A self-test that records only its own test pattern and tone and checks every frame and every flash against every tone
- No dropped frames from 1080p60 to 4K60 HEVC and 1440p144 on NVENC; sound and picture within a frame across pauses
- README films drawn by the app itself, frame by frame, with a made-up game and desktop
- A [website](https://sweax3169.github.io/sweaxiris/) with a working iris button and a macro-key tester

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxiris/releases/latest) · [Website](https://sweax3169.github.io/sweaxiris/) · [Source](https://github.com/Sweax3169/sweaxiris)

<br>

<a href="https://github.com/Sweax3169/sweaxmorph">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxmorph-dark.svg">
    <img alt="SweaxMorph — drop any file on Morph, pick a format, done. 126 formats, 229 extensions, offline." src="art/sweaxmorph-light.svg" width="100%">
  </picture>
</a>

**[SweaxMorph](https://github.com/Sweax3169/sweaxmorph)** is a file converter for Windows that lives one shortcut away. Morph, a little gel creature, opens its mouth when you carry files near it, swallows them, takes on their colour and grows a ring of petals: the formats they can become. Press <kbd>Win</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>, tap <kbd>Space</kbd> while dragging in Explorer, or right-click a file. Images, video, audio, documents, slides, PDF, e-books, data, archives, subtitles and fonts: 126 formats, all offline.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxmorph-demo-dark.gif">
    <img alt="A photo is dragged onto Morph; Morph swallows it, AVIF is picked and a file 91% smaller appears." src="art/sweaxmorph-demo-light.gif" width="680">
  </picture>
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- A route planner over 14 converters: when no tool goes straight there, it chains up to three (PowerPoint → PDF → PNG)
- ImageMagick, FFmpeg, Pandoc, Office and LibreOffice, Windows PDF and OCR
- WOFF/WOFF2 fonts, archives and JSON/YAML/TOML/XML/CSV/Excel written in-house
- Morph is drawn by hand every frame on a spring-physics gel body

</td>
<td width="50%" valign="top">

**Shipped with**
- A self-test that makes sample files and runs about a hundred real conversions
- README media recorded by the app itself, frame by frame
- English and Turkish, light and dark
- A [website](https://sweax3169.github.io/sweaxmorph/) where a live Morph reacts to files you drop on the page

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxmorph/releases/latest) · [Website](https://sweax3169.github.io/sweaxmorph/) · [Source](https://github.com/Sweax3169/sweaxmorph)

<br>

<a href="https://github.com/Sweax3169/sweaxclip">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxclip-dark.svg">
    <img alt="SweaxClip — everything you copy, kept. Press Win + V and it is right where you type." src="art/sweaxclip-light.svg" width="100%">
  </picture>
</a>

**[SweaxClip](https://github.com/Sweax3169/sweaxclip)** replaces <kbd>Win</kbd> + <kbd>V</kbd> on Windows with a history that never forgets. Everything you copy — text, links, code, colours, images, screenshots, files — is kept on your own disk and comes back as a timeline right under your text cursor. Screenshots are searchable by the words inside them through the Windows OCR engine, and the whole thing waits in the tray at about 10 MB.

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- Native C# / WPF on .NET 9, talking to Win32 directly
- SQLite in WAL mode with an FTS5 trigram index
- Low-level keyboard hook and accessibility caret lookup
- Spring physics for every movement in the panel

</td>
<td width="50%" valign="top">

**Shipped with**
- Self-contained single-file build from GitHub Actions
- English and Turkish, light and dark
- README media rendered by the app itself
- A [website](https://sweax3169.github.io/sweaxclip/) with a working copy of the panel

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxclip/releases/latest) · [Website](https://sweax3169.github.io/sweaxclip/) · [Source](https://github.com/Sweax3169/sweaxclip)

<br>

<a href="https://github.com/Sweax3169/sweaxcut">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxcut-dark.svg">
    <img alt="SWEAXCUT: video editor for Windows. Automatic captions, one-click edits and a WebGL2 timeline, all running on your PC." src="art/sweaxcut-light.svg" width="100%">
  </picture>
</a>

**[SWEAXCUT](https://github.com/Sweax3169/sweaxcut)** is a timeline video editor for Windows, made for people who cut gameplay clips, Shorts and YouTube videos. Version 3 was redrawn from scratch. Drop clips on a recipe and the edit builds itself: a beat-cut montage, a talking video with captions, game highlights. Captions are written word by word on your own PC, edited like a document and restyled live, and the preview and the export are drawn by the same WebGL2 compositor.

<p align="center">
  <img alt="SWEAXCUT 3: the home screen, a beat-cut montage built from a recipe, word-by-word captions restyled live, the command palette and the export window." src="art/sweaxcut-demo.gif" width="680">
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- Six one-click recipes, an eight-step "Polish" and eight looks; Ctrl+K reaches every tool
- whisper.cpp captions you can split, merge, retime and restyle, with 45 styles plus your own
- 197 transitions, 161 effects, 93 colour filters and 137 clip animations, all GLSL
- Keyframes with a bezier curve editor, colour scopes, and hardware export (NVENC, AMF, Quick Sync)

</td>
<td width="50%" valign="top">

**Shipped with**
- 777 stickers, 126 text templates and 101 fonts that all contain the Turkish letters
- 22 music tracks and 102 sound effects synthesised by the app
- An installer that carries every third-party licence, with source links in the release notes
- A [website](https://sweax3169.github.io/sweaxcut/) with a small editor that runs the app's own transition shaders

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxcut/releases/latest) · [Website](https://sweax3169.github.io/sweaxcut/) · [Source](https://github.com/Sweax3169/sweaxcut)

<br>

<a href="https://github.com/Sweax3169/sweaxterrain">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxterrain-dark.svg">
    <img alt="Sweax Terrain: generate, erase and build worlds in Roblox Studio. 9 biomes, 8 worlds, 54 structures, Ctrl+Z on every step." src="art/sweaxterrain-light.svg" width="100%">
  </picture>
</a>

**[Sweax Terrain](https://github.com/Sweax3169/sweaxterrain)** is a terrain plugin for Roblox Studio. Nine biomes blend into each other by weight, with lakes, rivers, an ocean edge and caves; a brush or a two-corner box erases any terrain in the place; 44 structures and 10 landforms drop onto the ground behind a see-through preview. Every step is one <kbd>Ctrl</kbd> + <kbd>Z</kbd>, and the panel speaks English and Turkish.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxterrain-demo-dark.gif">
    <img alt="A world is generated parcel by parcel, a brush carves a path across river plains, then ten structures are placed one by one." src="art/sweaxterrain-demo-light.gif" width="680">
  </picture>
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- A two-pass generator: a domain-warped height map, then materials, rock outcrops and caves per voxel, written in 24 × 24 column parcels
- 2048 × 2048 studs in one run; 512 × 512 takes 0.30 s
- 54 structures and landforms built from plain parts, so there is nothing to upload

</td>
<td width="50%" valign="top">

**Shipped with**
- A JavaScript port of the generator that matches Studio column for column (238,848 columns checked)
- README art drawn from real plugin output: voxels read back from Studio and rendered in Blender
- A [website](https://sweax3169.github.io/sweaxterrain/) where the plugin's own panel and generator run in the browser

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxterrain/releases/latest) · [Website](https://sweax3169.github.io/sweaxterrain/) · [Source](https://github.com/Sweax3169/sweaxterrain)

<br>

<a href="https://github.com/Sweax3169/sweaxbrush">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxbrush-dark.svg">
    <img alt="Sweax Brush: details, props and parts on any surface in Roblox Studio. A real scatter stroke seen from above, objects landing along the brush ring." src="art/sweaxbrush-light.svg" width="100%">
  </picture>
</a>

**[Sweax Brush](https://github.com/Sweax3169/sweaxbrush)** is a detailing brush for Roblox Studio. Pick Models or Parts in the Explorer and put them on any surface: one at a time behind a see-through preview, scattered under a brush ring with spacing and random turns and sizes, drawn to the size you drag, or stacked on a block grid. The eraser removes only what the brush placed, every click or drag is one <kbd>Ctrl</kbd> + <kbd>Z</kbd>, and the panel speaks English and Turkish.

<p align="center">
  <img alt="The brush scatters rocks, grass, flowers and mushrooms across a slope and a lawn; crates, barrels and lamps are placed on the floor, on a wall and under a ledge; blocks stack into stairs." src="art/sweaxbrush-demo.gif" width="680">
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- 22 Luau modules: surface rules for floors, walls and ceilings, disc sampling with a minimum spacing, a block grid that stacks, drawing on any surface plane
- One undo step per click, drag, draw or clear; no web requests and no assets
- A cutting-mat panel with ruler sliders that follows Studio's light or dark theme

</td>
<td width="50%" valign="top">

**Shipped with**
- README clips drawn from real plugin output: a test place dressed by the plugin's own controllers, read back part by part and rendered in Blender
- A [website](https://sweax3169.github.io/sweaxbrush/) where the plugin's panel and placement math run in the browser on a board dumped from Studio
- An import of presets from Detail Brush, the plugin's earlier private name

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxbrush/releases/latest) · [Website](https://sweax3169.github.io/sweaxbrush/) · [Source](https://github.com/Sweax3169/sweaxbrush)

<br>

<a href="https://github.com/Sweax3169/sweaxnext">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="art/sweaxnext-dark.svg">
    <img alt="SweaxNext: a vocal mix plug-in for rap. It hears the take first, then fixes only what needs fixing. VST3 for Windows." src="art/sweaxnext-light.svg" width="100%">
  </picture>
</a>

**[SweaxNext](https://github.com/Sweax3169/sweaxnext)** is a VST3 plug-in that mixes rap vocals. Put it on the vocal channel, press analyse and play the verse. It measures every phrase and names what is wrong (mic pops, harsh esses, room noise, hum, lines recorded at different levels), builds a chain for one of 16 styles, renders that chain offline on what it heard, measures again, and then hands you the result as ordinary parameters you can tweak, automate and undo.

<p align="center">
  <img alt="SweaxNext drawing itself: the role is picked, the vocal is analysed while it plays, the mix is ready, original and processed are compared and the tabs are opened." src="art/sweaxnext-demo.gif" width="680">
</p>

<table>
<tr>
<td width="50%" valign="top">

**Inside**
- 20 modules in C++ on JUCE, from a gate and a true-peak limiter to spectral resonance smoothing and formant shift
- 22 problem checks, a rule-based planner with its own chain order per style, and an offline render-and-measure loop
- An audio thread that never waits, locks or allocates; analysis and planning run on their own threads
- Latency fixed per quality mode and reported to the host

</td>
<td width="50%" valign="top">

**Shipped with**
- 159 automated tests and pluginval at strictness 10
- A demo take built from scratch (synthetic voice, synthesised beat) rendered through all 16 styles
- README pictures and videos drawn by the plug-in itself, off-screen
- A [website](https://sweax3169.github.io/sweaxnext/) where you switch styles and A/B the real renders over a beat

</td>
</tr>
</table>

[Download](https://github.com/Sweax3169/sweaxnext/releases/latest) · [Website](https://sweax3169.github.io/sweaxnext/) · [Source](https://github.com/Sweax3169/sweaxnext)

<br>

## Selected work

<table>
<tr>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxmorph"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxmorph-dark.svg"><img alt="SweaxMorph — drop any file on Morph, pick a format. 126 formats for Windows, offline. C#, .NET 9, WPF. Open source." src="art/card-sweaxmorph-light.svg" width="100%"></picture></a>
</td>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxclip"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxclip-dark.svg"><img alt="SweaxClip — permanent, searchable clipboard history for Windows. C#, .NET 9, WPF, SQLite FTS5. Open source." src="art/card-sweaxclip-light.svg" width="100%"></picture></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxcut"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxcut-dark.svg"><img alt="SWEAXCUT 3 — an offline video editor for Windows with one-click edits and word-by-word captions you can restyle. Electron, React, WebGL2, FFmpeg, whisper.cpp. Open source." src="art/card-sweaxcut-light.svg" width="100%"></picture></a>
</td>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxnext"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxnext-dark.svg"><img alt="SweaxNext — vocal mix plug-in for rap: hears the take first, 16 styles, 159 tests, pluginval strictness 10. C++, JUCE, VST3. Open source." src="art/card-sweaxnext-light.svg" width="100%"></picture></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxbeacon"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxbeacon-dark.svg"><img alt="SweaxBeacon — Minecraft Java powers, items and world controls on a server, a LAN world or single-player, with no login. Electron, React, C#. Open source." src="art/card-sweaxbeacon-light.svg" width="100%"></picture></a>
</td>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxterrain"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxterrain-dark.svg"><img alt="Sweax Terrain — Roblox Studio plugin: worlds from 9 blended biomes, a brush and box eraser, 54 structures. Luau, WebGL2 demo. Open source." src="art/card-sweaxterrain-light.svg" width="100%"></picture></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxbrush"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxbrush-dark.svg"><img alt="Sweax Brush — Roblox Studio plugin: place, scatter, draw and erase details on any surface, English and Turkish. Luau, three.js demo. Open source." src="art/card-sweaxbrush-light.svg" width="100%"></picture></a>
</td>
<td width="50%">
<a href="https://sweax3169.github.io/roblox-games/"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-robloxgames-dark.svg"><img alt="Roblox Games — the Sweax Studios games on Roblox, two released and one in development, each with its own page and play link. English and Turkish." src="art/card-robloxgames-light.svg" width="100%"></picture></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxiris"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxiris-dark.svg"><img alt="SweaxIris — screen recorder for Windows: a region in two keys, pause into the same file, GPU encoding. C#, .NET 9, WPF, Direct3D 11, FFmpeg. Open source." src="art/card-sweaxiris-light.svg" width="100%"></picture></a>
</td>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxdrop"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxdrop-dark.svg"><img alt="SweaxDrop — files between a PC and phones on parallel encrypted lanes, resumes after a drop. Rust, Tauri, Kotlin, Swift. Open source." src="art/card-sweaxdrop-light.svg" width="100%"></picture></a>
</td>
</tr>
</table>

<details>
<summary><b>More projects</b></summary>
<br>

| Project | What it is | Built with | Status |
| --- | --- | --- | --- |
| Sweax Rhythm Trainer | Metronome, tap tempo and auto-quantize for practising timing | C++, JUCE | VST3 |

</details>

<br>

## How I work

- **All the way to release.** A project isn't done when it runs on my machine. It is done when it has an installer, a page that explains it and a build anyone can check.
- **Measured, not guessed.** SWEAX NEXT runs 159 automated tests and passes pluginval at its strictest level; SweaxMorph converts about a hundred real sample files before a release; SweaxClip's memory use is measured on a real machine before a number goes in its README.
- **Interfaces with their own character.** Each product gets a look that comes from what it is — SweaxClip's panel is a timeline of your clips, SweaxMorph is a creature that eats files.

<br>

## Tools

<p>
  <img alt="C#" src="https://img.shields.io/badge/C%23-23201D?style=flat-square&logo=dotnet&logoColor=white">
  <img alt=".NET" src="https://img.shields.io/badge/.NET%209-512BD4?style=flat-square&logo=dotnet&logoColor=white">
  <img alt="WPF" src="https://img.shields.io/badge/WPF%20%C2%B7%20Win32-23201D?style=flat-square&logo=windows&logoColor=white">
  <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white">
  <img alt="JUCE" src="https://img.shields.io/badge/JUCE%20%C2%B7%20VST3-8DC63F?style=flat-square&logoColor=white">
  <img alt="Luau" src="https://img.shields.io/badge/Luau%20%C2%B7%20Roblox-23201D?style=flat-square&logo=roblox&logoColor=white">
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white">
  <img alt="Electron" src="https://img.shields.io/badge/Electron-2B2E3A?style=flat-square&logo=electron&logoColor=9FEAF9">
  <img alt="Cloudflare" src="https://img.shields.io/badge/Cloudflare%20Workers-F38020?style=flat-square&logo=cloudflare&logoColor=white">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Blender" src="https://img.shields.io/badge/Blender-E87D0D?style=flat-square&logo=blender&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white">
</p>

<br>

<p align="center"><sub>Sweax Studios · Türkiye · <a href="https://sweaxstudios.xyz">sweaxstudios.xyz</a></sub></p>
