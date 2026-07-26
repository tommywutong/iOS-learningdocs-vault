---
title: 'ROSE-8: Console Mode'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/01/ROSE-8-Console/'
original_language: en
published: 2020-01-28
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f08f45a32f50ec65'
translated: false
---

> 原文：[ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/)

[Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/) »

« [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/?tag=assembly)

[Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=assembly) »

« [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/?tag=source-code)

[Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/?tag=source-code) »

« [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/?tag=rose-8)

[Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/?tag=rose-8) »

## [ROSE-8: Console Mode](#)

A few weeks ago I got sucked into designing a toy 8-bit CPU, [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/), and got as far as writing an emulator for the machine that you could manually feed instructions to. At the end, I listed some future projects, the first of which was

> - for manually computing addresses and offsets, so I still want to get to this at some point.

This turned out to be quite the endeavor! I found out computing offsets and addresses is tricky in a program where not all instructions are the same length, and doubly so when certain parts of the program have to be located in certain parts of memory. It took me [about a week](https://belkadan.com/source/ROSE-8/shortlog/53a7984e4a9b3994165fbb15d2f02e9dd6c22d7c..ff92269b67a3c2bbd7e94929432b1a0306bb8667) to put together an assembler that had all the features I wanted.

The [readme](https://belkadan.com/source/ROSE-8) shows the architecture I eventually came up with

> - : Declares the basic representation for parsed instructions and such.
> - : Converting textual assembly code to an in-memory parsed representation.
> - : Converting the parsed representation to architecture instructions (and then encoding them to machine code).
> - : The final representation of an assembled program, which can be run directly or emitted to a file.

and the fact that I needed an “architecture” at all shows that it was more complicated than I expected going in! I’m pretty happy with what I came up with, though—it’s got a good separation of data and logic, and uses immutability and lots of helper types to make it clear what the invariants are at each step. You can [check it out](https://belkadan.com/source/ROSE-8) on my newly-set-up [gitweb](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/) instance. (Note that that URL is also a valid git “clone” URL if you want to play with ROSE-8 locally.)

This post also marks the “official” finalization of ROSE-8 v0.2.2, which comes with a handful of “new features”. You can check out the changelog in the [readme](https://belkadan.com/source/ROSE-8), but I want to focus in on one new instruction in particular: `WAIT`.

---

> ```
> WAIT spin or sleep until data1[it] > 0, then decrement data1[it] (for MMIO)
> ```

“MMIO” stands for “memory-mapped input/output”, and `WAIT` as the single primitive for this is the result of a [design discussion](https://twitter.com/UINT_MIN/status/1217193732597878784) between me and Cassie (the one who inspired the whole ROSE-8 project and who’s been providing contributions throughout). The simplest thing to do with this is to have a program that waits for (textual) input, instead of just running based on how it’s compiled. I’m not going to go into the details here, but the implementation was pretty straightforward ([other than one hiccup](https://twitter.com/UINT_MIN/status/1219855820067725312)), and it leads to actually-interactive programs!

> ```
> % swift run rose8-as Examples/greet.rose8 -o $TMPDIR/greet
> % swift run rose8-console $TMPDIR/greet
> What is your name?
> > JUNE EGBERT
> Pleasure to meet you, JUNE EGBERT!
> %
> ```

> The console extension provides a _poll address_ (default: segment 255, address 0) and an _input address_ (default: segment 255, address 1), which will be updated whenever a ROSE-8 program `WAIT`s for input. Reading a single byte looks something like this:
> 
> ```
> # Assuming 'data1' is already set to segment 255
> GETI 1
> SETR r0  # set up the address to read from (1)
> ZERO
> WAIT     # wait on address 0
> LD1R r0  # load the byte that was read
> BEZI eof # EOF is treated as a NUL byte
> # do something with the byte that was just read in
> ```

The “greet” example shown above is just the start; the [ROSE8Console](https://belkadan.com/source/ROSE8Console/) repository includes a full (tiny) maze game. It’s a game I could have written in C—or any more modern language. But this one’s written in an assembly I made up, for a CPU architecture I made, then put through an assembler I made, and run on an emulator I made. That’s a cool feeling.

---

But I’m not stopping here. In the original post I observed that the other 8-bit CPU I knew was the Game Boy, and to my brain that meant that I could make Game-Boy-like games based on ROSE-8. But was that just an idle dream?

![](https://belkadan.com/blog/2020/01/ROSE-8-Console/screen.png)

…You’ll have to find out next time.

This entry was posted on [January](https://belkadan.com/blog/2020/01) 28, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Assembly](https://belkadan.com/blog/tags/assembly), [Source code](https://belkadan.com/blog/tags/source-code), [ROSE-8](https://belkadan.com/blog/tags/rose-8)
