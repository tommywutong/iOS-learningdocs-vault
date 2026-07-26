---
title: Assembly
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/assembly'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:06fd6714eecde38a'
translated: false
---

> 原文：[Assembly](https://belkadan.com/blog/tags/assembly)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [ROSE-8 in customasm](https://belkadan.com/blog/2025/01/ROSE-8-in-customasm/?tag=assembly)

12 January 2025

Last week a friend shared the existence of hlorenzi’s [customasm](https://hlorenzi.github.io/customasm/), a tool that can serve as the assembler for arbitrary CPU architectures just by defining a mapping of instructions to encodings.

Hey, [I made a CPU once!](https://belkadan.com/blog/2020/01/ROSE-8/?tag=rose-8) How hard would it be to make a customasm definition for ROSE-8? Turns out…not very! I played around with it for about two hours, and by the end of it I’d translated an entire ROSE-8 program to customasm, with most of the definition file looking basically the same as the text reference for the ISA encoding.

[(Continue reading…)](https://belkadan.com/blog/2025/01/ROSE-8-in-customasm/?tag=assembly)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [ROSE-8](https://belkadan.com/blog/tags/rose-8), [Assembly](https://belkadan.com/blog/tags/assembly)

## [Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=assembly)

14 May 2022

POV: You are a compiler targeting arm64[1](#fn:arm64), and you want some code to reference this global variable from the same library. The classic way to do this is to emit an instruction that loads “the address of X”, which will be [determined at run time by the dynamic loader](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/). But that’s not super efficient! For one thing, addresses are 64 bits long, and instructions are only 32 bits, so you can either break it up into multiple instructions, or load the address from some _other_ location. But more importantly, the global variable is _in the same library._ The dynamic loader isn’t going to break it up from this code[2](#fn:ios), and if we knew _how far away it was_ we could reference it that way.

That’s what the `adrp` instruction’s for.

[(Continue reading…)](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=assembly)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Assembly](https://belkadan.com/blog/tags/assembly), [Debugging](https://belkadan.com/blog/tags/debugging), [Objective-C](https://belkadan.com/blog/tags/objective-c)

## [ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=assembly)

28 January 2020

A few weeks ago I got sucked into designing a toy 8-bit CPU, [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/), and got as far as writing an emulator for the machine that you could manually feed instructions to. At the end, I listed some future projects, the first of which was

> - for manually computing addresses and offsets, so I still want to get to this at some point.

[(Continue reading…)](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=assembly)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Assembly](https://belkadan.com/blog/tags/assembly), [Source code](https://belkadan.com/blog/tags/source-code), [ROSE-8](https://belkadan.com/blog/tags/rose-8)

## Older Posts

1. 2020-01-13

  ROSE-8
2. 2016-05-23

  So You Want to Be a (Compiler) Wizard

### Possibly Related Tags

- Compilers
- Debugging
- Diversity in tech
- Objective-C
- Open source
- ROSE-8
- Source code
