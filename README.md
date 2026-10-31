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
  <a href="https://discord.gg/vGZ2DZZsrf">Discord</a>
</p>

<br>

I'm an independent developer from Türkiye, working as **Sweax Studios**. I build native Windows software, audio plugins, Roblox games and web platforms, and I take each one all the way to release — code, interface, installer, tests and documentation. I also produce rap beats, which is why some of my tools are about sound.

<br>

## Featured

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
<a href="https://github.com/Sweax3169/sweaxcut"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxcut-dark.svg"><img alt="SWEAXCUT 2 — a full timeline video editor for Windows that works offline. Electron, React, WebGL2, FFmpeg. Open source." src="art/card-sweaxcut-light.svg" width="100%"></picture></a>
</td>
<td width="50%">
<picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxnext-dark.svg"><img alt="SWEAX NEXT — vocal mixing plugin for rap with 12 vocal chains, 159 automated tests, passes pluginval at strictness 10. C++, JUCE. VST3." src="art/card-sweaxnext-light.svg" width="100%"></picture>
</td>
</tr>
<tr>
<td width="50%">
<picture><source media="(prefers-color-scheme: dark)" srcset="art/card-popit-dark.svg"><img alt="+1 Speed POP IT — Roblox game with session-locked saves and a phone-friendly world of 70,000+ parts. Luau. Released." src="art/card-popit-light.svg" width="100%"></picture>
</td>
<td width="50%">
<a href="https://github.com/Sweax3169/sweaxpanel"><picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxpanel-dark.svg"><img alt="SweaxPanel — desktop control panel for your own Minecraft server over RCON. Electron, React. Open source." src="art/card-sweaxpanel-light.svg" width="100%"></picture></a>
</td>
</tr>
<tr>
<td width="50%">
<picture><source media="(prefers-color-scheme: dark)" srcset="art/card-adana-dark.svg"><img alt="Adana Mücadele — website and member platform for an MMA club. Cloudflare Workers, D1, R2. Live." src="art/card-adana-light.svg" width="100%"></picture>
</td>
<td width="50%">
<picture><source media="(prefers-color-scheme: dark)" srcset="art/card-sweaxterrain-dark.svg"><img alt="Sweax Terrain — Roblox Studio plugin that paints terrain: 9 biomes and 8 ready-made worlds. Luau. Plugin." src="art/card-sweaxterrain-light.svg" width="100%"></picture>
</td>
</tr>
</table>

<details>
<summary><b>More projects</b></summary>
<br>

| Project | What it is | Built with | Status |
| --- | --- | --- | --- |
| Sweax Rhythm Trainer | Metronome, tap tempo and auto-quantize for practising timing | C++, JUCE | VST3 |
| RNG Zombie Defense | Roblox wave-defense game: 40 waves, 11 themes, 17 languages | Luau | In development |
| Maden Farm | Roblox mining tycoon with client-side ore physics at 60 FPS | Luau | In development |

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
