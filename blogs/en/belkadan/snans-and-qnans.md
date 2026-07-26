---
title: sNaNs and qNaNs
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/04/SNaNs-and-QNaNs/'
original_language: en
published: 2023-04-01
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:363e0c67a23d8094'
translated: false
---

> 原文：[sNaNs and qNaNs](https://belkadan.com/blog/2023/04/SNaNs-and-QNaNs/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Setting up GoToSocial](https://belkadan.com/blog/2023/02/Setting-up-GoToSocial/)

[HOW TO REFER TO A MAGIC CONSTANT IN C](https://belkadan.com/blog/2023/07/Magic-Constants-in-C/) »

## [sNaNs and qNaNs](#)

If you find yourself in the unfortunate position of having to think about the difference between IEEE 754 floating-point sNaNs and qNaNs, and keep getting mixed up about which one interrupts execution, here’s a handy way to remember: **They’re definitely not “silent” and “querulous”.** Because no standards body would name something “querulous”.

This was a quip I made on Twitter years ago. I never got them mixed up again.

(The actual two types of NaNs are “quiet” and “signaling”.)

This entry was posted on [April](https://belkadan.com/blog/2023/04) 01, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical).
