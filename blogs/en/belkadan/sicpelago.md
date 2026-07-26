---
title: SICPelago
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2025/04/SICPelago/'
original_language: en
published: 2025-04-01
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c5c517204cfdc297'
translated: false
---

> 原文：[SICPelago](https://belkadan.com/blog/2025/04/SICPelago/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [ROSE-8 in customasm](https://belkadan.com/blog/2025/01/ROSE-8-in-customasm/)

[What's in a Button?](https://belkadan.com/blog/2025/11/Whats-in-a-Button/) »

« [“Pretty Good, Pretty Good”](https://belkadan.com/blog/2025/01/Pretty-Good-Pretty-Good/?tag=games)

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=april-fools)

## [SICPelago](#)

SICPelago is a randomized Scheme environment where you unlock core capabilities by solving carefully selected exercises adapted from _[Structure and Interpretation of Computer Programs](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html)._ Starting only with your trusty `lambda` and the supporting `quote`, climb your way to the top of the textbook, exploring math puzzles, composite data structures, and infinite sequences. Happy [April Prototypes Day](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/)!more

## Where?

[Check out the source](https://belkadan.com/source/sicpelago/) (and install instructions). You can also download an [apworld](https://belkadan.com/blog/2025/04/SICPelago/sicp.apworld) for use with Archipelago directly (updated `2025-05-19`), though note that I’ve only tested it with from-source builds of Archipelago.

```
Welcome to SICPelago!

Your goal is to solve problems and collect the 7 sacred relics.
At the start of the game, you only have access to `lambda` and `quote`.
Use the commands below to guide you on your way:

  (#help) - show this message
  (#progress) - show how many relics you have collected
  (#inventory) - list all abilities you have access to
  (#list) - list all problems
  (#show "1.1") - print the prompt for a specific problem
  (#solve "1.1" (lambda (x) x)) - attempt to solve a problem
      All problem solutions take the form of a single function.
  (#unlock 'cons) - unlock an ability directly (i.e. cheat)

Good luck!

scm> (#show "1.41")

# 1.41 Again, Again!

Define a procedure double that takes a procedure of one argument
as an argument and returns a procedure that applies the original
procedure twice. For example, if inc is a procedure that adds 1 to
its argument, then (double inc) should be a procedure that adds 2.

scm> (#solve "1.41" (lambda (f) (lambda (x) (f (f x)))))
You unlocked:
- cdar
- number?
scm>
```

## Why?

> **@jrose@belkadan.com,** on [Feb 06, 2025](https://social.belkadan.com/@jrose/statuses/01JKD69SNWEPECAN3WKTFEE8W):
> 
> Programming Language Archipelago Randomizer World
> 
> - checks: coding puzzles (e.g. past Advents of Code)
> - items: language features and library functions
> - logic: recursion (vs having to use a Y combinator), parsing (vs having to write your own), etc
> 
> (Context: [https://archipelago.gg/](https://archipelago.gg/))

This year was my first time participating in an [Archipelago](https://archipelago.gg) multi-world randomizer—my game of choice being [Tunic](https://rando.tunic.run). (Due to knowing some awesome people, this was also one of the first trials of [ToxicFrog’s randomizer for gzDoom](https://github.com/ToxicFrog/doom-mods/tree/main/gzap)!) Randomizers force you to look at old challenges with fresh eyes as you take them on with less (or more!) at your disposal, or perhaps see them for the first time if you previously bypassed them. They’re a great way to continue enjoying a game you’ve already played before. A _multi-world_ randomizer, one where my items can be found in your world and vice versa, makes the whole thing a collaborative experience even when playing single-player games…though it can certainly be frustrating if the item you really need is placed just out of reach in someone else’s game.

A programming language isn’t a game, but it still can have challenges and capabilities and that means it’s randomizer-shaped.

### Why Scheme?

Scheme is a Lisp dialect, a language family famous for relatively straightforward implementation and an extremely regular surface syntax. With Swift or Python, providing new capabilities would pretty much only come in the form of what library functions you can use, or require surgery on the compiler/parser to reject certain forms. But in Scheme, all I have to do is check the name of the function or special form being used and see if it’s been unlocked, in one place in the code.

### Why SICP?

In my original post I mentioned Advent of Code as a source of puzzles. However, I figured it would make more sense to adapt from a course or textbook, since those tend to build up what they expect you to know over time, and _that_ means that, like a game, there will be at least some exercises that can be done without relying on having everything in the language at your disposal. SICP is even more rigorous and spartan than some other options, which make it a less welcoming textbook but an easier fit here. As a bonus, it’s CC-BY-SA, so I can copy and adapt the exercises without any legal concerns.

…Also, nostalgia. I TA’d a course based on SICP and Scheme for two years back in college, and so I know it pretty well.

(That said, this game is not a good way to learn Scheme, due to the need to solve things out of order!)

### Why Python?

The traditional choice would be to implement the host program in Scheme itself, or perhaps its modern offshoot Racket. But then there’d be an additional dependency for people who wanted to play, and for all I think it’s a good teaching language I _don’t_ actually like making even medium-sized programs in Scheme.

The next choices would be my two usual work/project languages these days, Swift and Rust. These are great languages for building fast and correct compiled programs. But because they _are_ compiled, I wouldn’t be able to say “just download this and run it”. I’d need separate builds for Mac, Windows, and Linux, and sorry to anyone not running one of those; or you’d have to build it from source yourself, and that’s again an extra step.[1](#fn:wasm)

So, Python. Many developers have a Python or several installed, so it was a less burdensome requirement than some of the other options. It’s also the language of both Archipelago and the course that replaced the one I TA’d, including its own little Scheme interpreter I could use as a starting point. And as a bonus, I got garbage collection for free.

## How?

A usual Scheme interpreter sets up a single global environment frame. SICPelago, on the other hand, sets up _three:_ the base environment with the full standard library and game-related built-ins, then an overlay that shadows all the things you need to unlock with special marker values the interpreter understands, and finally a plain environment the user can play in. That way all the utilities and solution-testing code have access to everything, while the player is limited.

To keep things uniform, “special forms” are looked up in the environment just like normal procedures. I assume this is how macros work in a real Scheme interpreter, so it’s not too farfetched, but it does mean a user can accidentally box themselves in by shadowing the name `lambda`. To counter that, I added a number of `#`-prefixed helper procedures, including `#undef`, that the user could not shadow. This also included the `#solve` procedure for submitting solutions.

Most of what’s left is just tweaks on the standard REPL and selectively modifying the environment when the user unlocks something. And of course I _did_ have to write a set of unit tests for every single puzzle…except I cheated and skipped a bunch of the trickier ones. If you find a solution that shouldn’t pass but does, congratulations! I believe that’s called a “sequence break” in speedrunning parlance.

## Archipelago!

(I ran out of question words.)

I was really worried I was going to run out of time on this one—I could only do so much each week. [RSI stinks.](https://belkadan.com/blog/2021/07/Keyboard-Pants/) But I couldn’t shake the dream of someone opening a chest in Tunic to send me `cons`, so one weekend I dedicated to the two parts of adding a game to Archipelago: first, describing the “world” of the game (its “items” and “locations”, in my case operations and exercises), and second, connecting a client to the server that handles syncing between games. And I got far enough to join a game and manually send myself `cons`! So with that I committed to finishing the rest of it before “launch day”, or at least enough to make it playable. There’s some quality of life stuff that would be worth fixing given infinite time, but hey, I’m happy it works at all.

(The Archipelago docs on how to set up a new “world” are pretty good. The docs on how to use their client to make your own are _not,_ even though there’s not that much to it. I might write up more on that later.)

## But Jordan…

A part of me feels guilty spending time on something so frivolous when the real world is falling apart. The USA is transforming into an authoritarian government before our eyes, or completing a transformation a long time in process, depending on who you ask. There are protests nearly every week in my home city of San Francisco. And here I am making a toy that’ll probably be used by exactly one person: me.

My defense has been that everyone needs respite, and that includes entertainment and personal projects. I hope this is entertainment for at least some of you as well! But I’ll also add that if you enjoyed this post and are in a reasonable position to do so…

- Hands Off

  ” this Saturday
- Trans Lifeline

  or

  Rainbow Railroad
- take Covid and the flu seriously, and wear a mask whenever you’re indoors with other people, or on public transit

(If you didn’t enjoy this post, you sure spent a lot of time on it to get to this part! Pick your own charity to donate to.)

## Whither?

If you end up trying this out, let me know! Not that I really expect anyone to; mostly this was just a neat project to show that it was possible. But I’m absolutely going to get my friends together to play an Archipelago rando again soon, and perhaps we’ll have one player in Tunic, one in Doom, and one—for the first time—in Scheme.

[![(Archipelago logo)](https://belkadan.com/blog/2025/04/SICPelago/archipelago.png)](https://archipelago.gg)

1. Another option would have been to compile to WebAssembly and wrap it in a website. That would probably work! But then I would have had to do a _lot_ more manual steps to make a REPL-friendly environment _and_ talk to the Archipelago server, and the result would be a website that takes a long time to load rather than “just” something you run locally. And I’m less familiar with wasm, so I don’t think I would have finished in time! [↩︎](#fnref:wasm)

This entry was posted on [April](https://belkadan.com/blog/2025/04) 01, [2025](https://belkadan.com/blog/2025) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Games](https://belkadan.com/blog/tags/games), [April Fools](https://belkadan.com/blog/tags/april-fools)
