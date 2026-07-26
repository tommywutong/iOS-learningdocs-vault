---
title: 'Introducing the Game ''by Color'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/'
original_language: en
published: 2020-02-04
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:251285a353fcc88c'
translated: false
---

> 原文：[Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/)

[Flexible Identities in git](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/) »

« [ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=source-code)

[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=source-code) »

« [ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=rose-8)

[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=rose-8) »

## [Introducing the Game 'by Color](#)

When designing [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/), I realized that the last 8-bit CPU architecture I had learned about was the Nintendo Game Boy, via Eevee’s [Cheezball Rising](https://eev.ee/blog/2018/06/19/cheezball-rising-a-new-game-boy-color-game/) series. That gave me a goal for ROSE-8: implement a system that could display graphics and receive real-time button presses, and thus play games. As I hinted [last time](https://belkadan.com/blog/2020/01/ROSE-8-Console/), I did indeed manage to achieve this! Introducing the Game ’by Color ([pronounced like “Game B Color”](https://en.wiktionary.org/wiki/enby)).more

![](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/screen.png)

```
% xcodebuild -scheme App
% swift run rose8-as Examples/super-maze.rose8 -o $TMPDIR/super-maze
% open -a "Game 'by Color" $TMPDIR/super-maze
```

TLDR: You can [check out the repository](https://belkadan.com/source/GameByColor/) and build this Mac app yourself. If you’re very enterprising, you can even write games for it. Non-games too, I suppose.

**EDIT:** I added an [X11](https://en.wikipedia.org/wiki/X_Window_System) implementation for Linux users as well, under `swift run xgamebycolor`.

There were several different pieces that went into this:

- The ROSE-8 “CPU” needed basically no changes from what was already needed for [console interaction](https://belkadan.com/blog/2020/01/ROSE-8-Console/), which was nice.
- The graphics system was the biggest piece. For this I basically copied what the Game Boy does, referring to a bevy of resources [which I linked in the readme](https://belkadan.com/source/GameByColor/). I did simplify it some, but the gist is still the same: there are color palettes, and tiles you can draw using those color palettes, and a background grid of tiles, and sprites that also use the tiles.
- A realtime system needs a timer, mainly for animation but also to avoid zipping across the screen if you hold down the “right” button too long. I went with a simple design I [discussed with ROSE-8 co-conspirator Cassie](https://twitter.com/UINT_MIN/status/1217193732597878784): there’s a counter in memory that goes up at a program-defined interval, and programs can `WAIT` on that counter to “consume” a “tick”. This works pretty well for what I’m doing, but I can see it being limiting in other instances.
- Of course, it’s not a game if you don’t have inputs. I wired up the keyboard to cause bits of memory inside the ROSE-8 to change when you press certain buttons. This is what I think of as “computer plumbing”: connecting two self-contained systems to make something work. It wasn’t hard. (Actually processing the input inside the ROSE-8 program was a bit trickier, though.)

If you’re interested in any of these pieces for one of your own projects, I suggest checking out the [revision history](https://belkadan.com/source/GameByColor/). I think it’s pretty clean, even if it comes in big chunks.

The screenshot at the top is of a maze game, the same game I used to demonstrate [console mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/). It really works! (Fun fact: the screenshot from [_last_ time](https://belkadan.com/blog/2020/01/ROSE-8-Console/) was the test pattern Eevee used during her own initial forays into Game Boy Color programming.)

I think this is about it for ROSE-8 adventures for me. While I do still have ideas for new instructions to make it easier to program (…in bare assembly…), I’ve accomplished all the basic things I thought about when first starting the project[1](#fn:compiler), and I have other projects and blog posts I’d like to get to. But it was a fun month’s diversion, and I appreciated both the challenge of operating under (virtual, self-imposed) limitations and the opportunity to learn about and make things I hadn’t before. If you have time, I highly recommend learning about and making things you haven’t before.

1. Except a compiler, cause oof, that would be a lot of work. [↩︎](#fnref:compiler)

This entry was posted on [February](https://belkadan.com/blog/2020/02) 04, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Source code](https://belkadan.com/blog/tags/source-code), [ROSE-8](https://belkadan.com/blog/tags/rose-8)
