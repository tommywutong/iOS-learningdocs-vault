---
title: Categories and +load
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/03/Categories-and-load/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:360a450f63695bbe'
translated: false
---

> 原文：[Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Subversion Checksum Problems](https://belkadan.com/blog/2009/03/Subversion-Checksum-Problems/)

[Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/) »

« [Alerts Without Apps (or nibs)](https://belkadan.com/blog/2008/03/Alerts-Without-Apps/?tag=cocoa)

[Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=cocoa) »

« [Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/?tag=objective-c)

[Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=objective-c) »

## [Categories and +load](#)

If you’re a Cocoa plugin writer, sanctioned or otherwise, you’ve probably thought about categories. About how you can magically add methods to existing classes…and if you’re careful, you can replace existing methods as well. With a few caveats: you can’t call the original method, and if someone else is doing the same thing, only one of you will win. Which makes it a bad idea, at best.

Well, today I was absentmindedly reading through GCC extensions to the C languages, and came across [this tidbit](http://gcc.gnu.org/onlinedocs/gcc-4.3.3/gcc/Executing-code-before-main.html):

> The `+load` is a method that is not overridden by categories. If a class and a category of it both implement `+load`, both methods are invoked. This allows some additional initializations to be performed in a category.

!! Categories get their own `+load` methods? It’s just like every class getting its own `+initialize`! With this here, you can safely add functionality to existing methods using categories:

1. .
2. when it would be calling the original method.
3. , swap the implementations of the two methods (using something like

  JRSwizzle

  ).

Now if someone else comes along and does the same thing, the methods will chain together, eventually calling the original implementation as intended. Has anyone been using this before or has no one known about it? (And, will the alternative compiler [Clang/LLVM](http://clang.llvm.org/) offer the same functionality?)

Remember, you [can’t trust very much during `+load`](http://gcc.gnu.org/onlinedocs/gcc-4.3.3/gcc/What-you-can-and-what-you-cannot-do-in-_002bload.html#What-you-can-and-what-you-cannot-do-in-_002bload). But you can do enough, here. (And because this is a category in a plugin we’re talking about, you can probably assume the rest of the application and frameworks have loaded anyway.)

There are some interesting things in the GCC language extensions. Even if you don’t end up using them, they’re fun to take a look at.

This entry was posted on [March](https://belkadan.com/blog/2009/03) 19, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa), [Objective-C](https://belkadan.com/blog/tags/objective-c)
