---
title: Const Correctness
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/03/Const-Correctness/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2334e9ffd495ae47'
translated: false
---

> 原文：[Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/)

[Hacking Safari 4...for Great Convenience](https://belkadan.com/blog/2009/04/Hacking-Safari-4-for-Great-Convenience/) »

« [Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/?tag=programming-languages)

[C++ Templates are Turing-Complete](https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/?tag=programming-languages) »

[C++ Templates are Turing-Complete](https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/?tag=cxx) »

## [Const Correctness](#)

I’m slipping a little on my promise to do once-a-week posts. Wait, it was biweekly, originally. Am I still good?

I’ve been working in C++ lately, which is one of those programming languages that resembles a [Hutt](http://starwars.wikia.com/wiki/Hutt): bloated, immobile, yet still greedy. And can be very, very powerful.

One of the core ideas of C++ was [const correctness](http://en.wikipedia.org/wiki/Const-correctness). This is one of those ideas I completely agree with in theory, but find hard to deal with in practice.

I’d love to say “this method will not modify the external state of the object”. I’d like “this collection is immutable, so you can treat it as a collection of a more generic content” (this is a [covariance/contravariance](http://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)) problem for mutable collections). And I’d really like to say “this part of the object will never be modified”.

The trouble is, there have been multiple times in this project where what I really need is “this part of the object will be modified _once_…but after it’s constructed.” Now, the _correct_ way to do this is to make the getter method public, the setter method private, and the function that needs to make that change a [friend](http://en.wikipedia.org/wiki/Friend_function).

But because these are mostly information-holding objects, we’ve been using them like structs. (WHAT‽) Forgoing a complete OO design, it’s a lot easier (and less code) to just use direct variable access. Changing this in one place would be an inconsistency. Changing the entire program would be a pain and a mess. For this project, it’s _simply not worth it_ to go back and go completely OO. (Particularly since it’s an academic project and will not be subjected to rigorous security/correctness testing.)

At this point I’ve alienated the pure OO crowd. The trouble is, C++ doesn’t make it easy to write these things correctly, as opposed to easily. They don’t follow the Uniform Access Principle. If accessing a variable directly and accessing it through a getter looked the same, well, then, fine! (C# and now Objective-C allow this, though it’s still controversial among old-hand developers for the latter.) But I don’t want to write getters for EVERY ivar in the project; most of them don’t need them. It’s easier to cheat a little…as long as you still play by the rules of your contract. (Eiffel formalizes this sort of thing with contract-based programming. But Eiffel is not quick to write, either.)

C++ is a hodgepodge language, and it’s uphill work to make it pure OO at all, let alone const-correct. (Look at the [`virtual`](http://www.cplusplus.com/doc/tutorial/polymorphism.html#virtual) keyword, and the fact that you need _both_ an `iterator()` and a `const_iterator()` method to be a const-correct collection.) In some cases, it’s easier just to cheat, and promise yourself (and your team members) that you’ll “follow the contract”.

But I wish they had a `once` keyword. “This variable can be initialized once; any attempt to access it before is an error, as is setting its value a second time.” Easy enough to do in code? Perhaps, but then I’d have to type it.

This entry was posted on [March](https://belkadan.com/blog/2009/03) 27, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Programming languages](https://belkadan.com/blog/tags/programming-languages), [C++](https://belkadan.com/blog/tags/cxx)
