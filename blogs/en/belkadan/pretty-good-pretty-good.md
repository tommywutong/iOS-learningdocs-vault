---
title: “Pretty Good, Pretty Good”
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2025/01/Pretty-Good-Pretty-Good/'
original_language: en
published: 2025-01-06
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:17d88712c19c09d2'
translated: false
---

> 原文：[“Pretty Good, Pretty Good”](https://belkadan.com/blog/2025/01/Pretty-Good-Pretty-Good/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Trunic](https://belkadan.com/blog/2024/07/Trunic/)

[What I Didn't Know About Jury Duty](https://belkadan.com/blog/2026/07/What-I-Didnt-Know-About-Jury-Duty/) »

« [Trunic](https://belkadan.com/blog/2024/07/Trunic/?tag=games)

[SICPelago](https://belkadan.com/blog/2025/04/SICPelago/?tag=games) »

« [Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=mac-os-classic)

## [“Pretty Good, Pretty Good”](#)

As a kid, one of my first games was Maelstrom, a slick Asteroids clone for the Mac by Ambrosia Software (who later went on to publish the Escape Velocity series). I have childhood memories of the two-note soundtrack while playing the two simplest strategies (spin in place without accelerating, and zoom upwards in a straight line firing all the way), of the “You EEdiot” when you accidentally shot a power-up canister, and the “Pretty good, pretty good!” for when you score over 10,000 points in a single stage.

Except if I open up Maelstrom now, it says “Hot damn!” instead.^[1](#fn:now)

At some point in Maelstrom’s release history, they must have replaced this exact sound effect. In fact, I kind of remember getting a new version on the family computer and a few things being a little different. And yet somehow, when I went looking for it as an adult, every version I found had “Hot damn”, or some low-quality sound effects that I’d never heard before in the 1.0 release. I became convinced that we must have had some alternate build, maybe one with certain sound effects replaced to be more family friendly. (This wouldn’t have surprised me, especially if Ambrosia had been angling to get into some game collection CD or default-install deal.)

Until finally, [my friends Irenes posted this](https://adhd.irenes.space/@ireneista/statuses/01JGFVY7X1CSRJB1DZ85TBYG35):

> “I have a thirty-second video that’s been stuck in my head since I saw it when I was a kid, decades ago. It wasn’t a meme or anything, just a thing I liked. I will never be able to find it again.”
> 
> [True]  
>  [False]

I replied with this story, and on a whim went looking one last time. And this time I struck paydirt: someone had uploaded [several different releases of Maelstrom](https://archive.org/details/maelstrom-68k) to the Internet Archive, originally from [Macintosh Garden](https://macintoshgarden.org/games/maelstrom-13-original). And it was there, methodically going through the sound resources with [ResEdit](https://en.wikipedia.org/wiki/ResEdit) inside [SheepShaver](https://sheepshaver.cebix.net), that I found it: “Pretty good, pretty good” was added in v1.2 (or possibly earlier) and replaced in v1.4.1. I hadn’t found it because neither the oldest nor the newest version of the game had the clip I was looking for.

["Pretty good, pretty good"](https://belkadan.com/blog/2025/01/Pretty-Good-Pretty-Good/pretty-good.aiff)

(Extracting that was an extra effort. Nothing reads old Mac sound resources anymore, but I manually dumped the contents and followed [instructions](https://apple.stackexchange.com/questions/33108/extract-a-sound-from-a-classic-application-for-mac-os-x) to load the effect into Audacity. Then learned [more about the `snd` format](https://preterhuman.net/macstuff/techpubs-old/mac/Sound/Sound-60.html) to figure out why that didn’t sound right. Then kept going for a while after that because it _still_ wasn’t sounding like the playback in SheepShaver…but once I opened the resulting AIFF file from _within_ SheepShaver it did sound the same, so presumably it’s an OS-level or emulator-based difference and this is close enough.)

In the end…this was pretty easy! I probably could have done it years ago, if I had only thought to look at more versions of Maelstrom. But only because people had uploaded them. If only the newest version had survived, or even the newest and oldest, I never would have recovered this bit of my childhood.

I made a donation to both Internet Archive and Macintosh Garden.

| Version | “Pretty good, pretty good” | “You idiot” | Other effects |
|---|---|---|---|
| v1.0 | (lounge jamming) | “Ya pinhead!” | (rock/lounge riffs, mostly) |
| v1.2-1.4 | “Pretty good, pretty good” | “You EEdiot!” | Voice clips, normal sfx |
| v1.4.1-3.0 | “Hot damn!” | “You EEdiot!” | Slight changes from previous (maybe switching to royalty-free?) |

1. “Now?” Okay, not exactly. There’s an SDL-based implementation called “Maelstrom 3.0” that made Maelstrom available on Linux, Mac OS X, and even Windows. But the last build on the website doesn’t work for me anymore—not so surprising when it’s from 2009. So it’s more “if I check out the Maelstrom I loaded in [SheepShaver](https://sheepshaver.cebix.net)”, or “if I grab the assets from the 2009 build”. [↩︎](#fnref:now)

This entry was posted on [January](https://belkadan.com/blog/2025/01) 06, [2025](https://belkadan.com/blog/2025) and is filed under [Personal](https://belkadan.com/blog/personal). Tags: [Games](https://belkadan.com/blog/tags/games), [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic)
