---
title: C++
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/cxx'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c67264ff061e00af'
translated: false
---

> 原文：[C++](https://belkadan.com/blog/tags/cxx)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [HOW TO REFER TO A MAGIC CONSTANT IN C](https://belkadan.com/blog/2023/07/Magic-Constants-in-C/?tag=cxx)

15 July 2023

|  | **Lawful** | **Neutral** | **Chaotic** |
|---|---|---|---|
| **Good** | `LIBUUID_UUID_LENGTH` | `sizeof(uuid_t)` | `sizeof(UUID_NULL)` |
| **Neutral** | `UUID_LENGTH` | `16` | `uuidLength` |
| **Evil** | `NUMBER_``OF_``OCTETS_``IN_``RFC_4122_``UNIVERSALLY_``UNIQUE_``IDENTIFIER` | `128 / CHAR_BIT` | `SIXTEEN` |

_Originally posted [for the Fediverse](https://social.belkadan.com/@jrose/statuses/01H5DE77Z64324VQ61CJT6MS19)._

[(Continue reading…)](https://belkadan.com/blog/2023/07/Magic-Constants-in-C/?tag=cxx)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx), [Humor](https://belkadan.com/blog/tags/humor), [Social media import](https://belkadan.com/blog/tags/social-media-import)

## [My Little (String) Optimization, Part 2](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/?tag=cxx)

22 March 2018

[Previously](https://belkadan.com/blog/2018/03/My-Little-Optimization/), I talked about how Clang is smart enough to optimize a series of comparisons against constant strings in C++ by starting out with a switch on the length. I left off with the idea that while this is good, you might be able to do better if your strings have a unique character at a certain offset. Today we’re going to see what that looks like.

[(Continue reading…)](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/?tag=cxx)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx)

## [My Little Optimization: The Compiler Is Magic](https://belkadan.com/blog/2018/03/My-Little-Optimization/?tag=cxx)

15 March 2018

Today I had the idea to play with a pretty simple optimization problem: you have a string, and you want to see if it matches one of a set of known strings (down to the same Unicode codepoints, not caring about [canonical equivalence](https://www.unicode.org/reports/tr15/#Canon_Compat_Equivalence)). The naive way to do this would be to walk through and simply check every single string:

[(Continue reading…)](https://belkadan.com/blog/2018/03/My-Little-Optimization/?tag=cxx)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx)

## Older Posts

1. 2016-08-21

  Macromancy, Part 2
2. 2016-08-07

  Macromancy
3. 2009-05-05

  C++ Templates are Turing-Complete
4. 2009-03-27

  Const Correctness

### Possibly Related Tags

- Humor
- Programming languages
- Social media import
