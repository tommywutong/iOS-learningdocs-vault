---
title: ROSE-8 in customasm
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2025/01/ROSE-8-in-customasm/'
original_language: en
published: 2025-01-12
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9cfd33e479f9cde4'
translated: false
---

> 原文：[ROSE-8 in customasm](https://belkadan.com/blog/2025/01/ROSE-8-in-customasm/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Shell is a Program](https://belkadan.com/blog/2024/12/The-Shell-is-a-Program/)

[SICPelago](https://belkadan.com/blog/2025/04/SICPelago/) »

« [ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=rose-8)

« [Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=assembly)

## [ROSE-8 in customasm](#)

Last week a friend shared the existence of hlorenzi’s [customasm](https://hlorenzi.github.io/customasm/), a tool that can serve as the assembler for arbitrary CPU architectures just by defining a mapping of instructions to encodings.

Hey, [I made a CPU once!](https://belkadan.com/blog/2020/01/ROSE-8/?tag=rose-8) How hard would it be to make a customasm definition for ROSE-8? Turns out…not very! I played around with it for about two hours, and by the end of it I’d translated an entire ROSE-8 program to customasm, with most of the definition file looking basically the same as the text reference for the ISA encoding.more

Okay, so programs written by hand in assembly aren’t _that_ long. But still, how long did it take me to write the original assembler? Probably more than two hours! (The commits are spaced over a few days, at least.) With customasm I could get something binary-identical to the original program output, and meanwhile I got expression syntax, custom functions, and everything else for free.

I spent some more time yesterday to prettify the [definition file](https://belkadan.com/source/ROSE-8/blob/refs/heads/dev:/rose8.asm) and make it more convenient (and played around some more with bigger ROSE-8 programs). I considered committing some of those bigger programs, but they didn’t really show anything interesting—the core instructions were all the same, only the syntax had changed a little! In a mostly automated way, even! (read: regex find/replace to do 90% of the translation work). The trickiest bit was actually that I had previously relied on literals being emitted little-endian and customasm defaults to big-endian—easy enough to fix once I realized it.

I’m not _really_ planning to be writing more ROSE-8 programs, and I _did_ have an assembler already. But while there were a few things I was missing, overall I was just very taken with the benefits of having all this infrastructure just _available._ And I have a sense that this isn’t _just_ a good format for _code,_ but really _many_ binary outputs you might want to write by hand, like [protoscope](https://github.com/protocolbuffers/protoscope) for protobuf-like formats. Not a common thing, but when you need it it’s invaluable.[1](#fn:protoscope)

P.S. If you want an instruction that _does not emit anything,_ you can use a zero-width literal, like `0`0`.

1. Unfortunately, one thing customasm doesn’t do well is length-prefixing, which is needed for both protobuf and IFF-like formats like mp4. You can manually do it by measuring distance to an end label, but that’s kind of annoying, especially for protobuf where the length to be emitted is itself variable-length. But hey, it’s an open-source project, if I _really_ needed it I could implement it myself. [↩︎](#fnref:protoscope)

This entry was posted on [January](https://belkadan.com/blog/2025/01) 12, [2025](https://belkadan.com/blog/2025) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [ROSE-8](https://belkadan.com/blog/tags/rose-8), [Assembly](https://belkadan.com/blog/tags/assembly)
