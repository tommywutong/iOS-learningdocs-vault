---
title: C++ Templates are Turing-Complete
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bb3aada53bdc934c'
translated: false
---

> 原文：[C++ Templates are Turing-Complete](https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [[Meme] How Many HTML Elements Can You Name in 5 Minutes?](https://belkadan.com/blog/2009/04/Meme--How-Many-HTML-Elements-Can-You-Name/)

[“Several New Features”](https://belkadan.com/blog/2009/05/Several-New-Features/) »

« [Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/?tag=cxx)

[Macromancy](https://belkadan.com/blog/2016/08/Macromancy/?tag=cxx) »

« [Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/?tag=programming-languages)

[Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/?tag=programming-languages) »

## [C++ Templates are Turing-Complete](#)

Apologies to anyone reading. These last few weeks are very busy and I do not have time for a legitimate post. Hopefully things will be more regular later…?

So meanwhile, I present this semi-formal [proof that the C++ template system is Turing-complete](http://ubiety.uwaterloo.ca/~tveldhui/papers/2003/turing.pdf), shown to me by a friend. This means that, among other things, a C++ program that uses templates can (theoretically) take both infinite time and infinite space to compile!

I am not a C++ fan, though it has a few features I appreciate. But give me a nice OO system, with a solid C-language interface…Objective-C does not quite fit, because you still have to live with the lingering bits of C. Ah, well…

This entry was posted on [May](https://belkadan.com/blog/2009/05) 05, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [C++](https://belkadan.com/blog/tags/cxx), [Programming languages](https://belkadan.com/blog/tags/programming-languages)
