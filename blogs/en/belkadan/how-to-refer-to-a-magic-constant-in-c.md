---
title: HOW TO REFER TO A MAGIC CONSTANT IN C
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/07/Magic-Constants-in-C/'
original_language: en
published: 2023-07-15
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:28ee57a38c83819d'
translated: false
---

> 原文：[HOW TO REFER TO A MAGIC CONSTANT IN C](https://belkadan.com/blog/2023/07/Magic-Constants-in-C/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [sNaNs and qNaNs](https://belkadan.com/blog/2023/04/SNaNs-and-QNaNs/)

[There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/) »

« [My Little (String) Optimization, Part 2](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/?tag=cxx)

« [Queue, Queeu, Quuee](https://belkadan.com/blog/2019/09/Queue-Queeu-Quuee/?tag=humor)

[XZ Gon' Give It To Ya](https://belkadan.com/blog/2024/04/XZ-Gon-Give-It-To-Ya/?tag=humor) »

## [HOW TO REFER TO A MAGIC CONSTANT IN C](#)

|  | **Lawful** | **Neutral** | **Chaotic** |
|---|---|---|---|
| **Good** | `LIBUUID_UUID_LENGTH` | `sizeof(uuid_t)` | `sizeof(UUID_NULL)` |
| **Neutral** | `UUID_LENGTH` | `16` | `uuidLength` |
| **Evil** | `NUMBER_``OF_``OCTETS_``IN_``RFC_4122_``UNIVERSALLY_``UNIQUE_``IDENTIFIER` | `128 / CHAR_BIT` | `SIXTEEN` |

_Originally posted [for the Fediverse](https://social.belkadan.com/@jrose/statuses/01H5DE77Z64324VQ61CJT6MS19)._

This entry was posted on [July](https://belkadan.com/blog/2023/07) 15, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx), [Humor](https://belkadan.com/blog/tags/humor), [Social media import](https://belkadan.com/blog/tags/social-media-import)
