---
title: '"FIXME" Doesn''t Always Mean "Fix Me"'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/04/FIXME/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:4fed5f75c5739fe6'
translated: false
---

> 原文：["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [My Little (String) Optimization, Part 2](https://belkadan.com/blog/2018/03/My-Little-String-Optimization-2/)

[Misleading Metrics and UX Tradeoffs](https://belkadan.com/blog/2018/04/Misleading-Metrics/) »

« [Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/?tag=swift)

[Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=swift) »

« [“Skip the FFI”](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=llvm)

[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=llvm) »

## ["FIXME" Doesn't Always Mean "Fix Me"](#)

If you browse through the Swift (or LLVM) codebase for a while, you’ll see a comment like [this](https://github.com/apple/swift/blob/3ffbc41d075b362f160ba685ee192d430551d233/lib/Serialization/SerializedModuleLoader.cpp#L278-L279):

```
// FIXME: Dependencies should be de-duplicated at serialization time,
// not now.
```

or [this](https://github.com/apple/swift/blob/76c264e9a155b10c8ab74717379962a0b05b566e/lib/Sema/CSRanking.cpp#L121-L124):

```
// FIXME: This is a hack. What we really want is to have substituted the
// base type into the declaration reference, so that we can compare the
// actual types to which two type declarations resolve. If those types are
// equivalent, then it doesn't matter which declaration is chosen.
```

or [this](https://github.com/apple/swift/blob/4797fae9330b328fddd35e499cc6437b7f63b3c8/lib/Sema/NameBinding.cpp#L363):

```
// FIXME: This is inefficient.
```

And you might be wondering if anyone is tracking all of these things that supposedly need fixing. Is there a [JIRA](https://bugs.swift.org) for each one? No, doesn’t seem to be…

The answer is that “FIXME” doesn’t _really_ mean “this code needs fixing”, at least not in Swift and LLVM. It means “this code isn’t as good as it should be”.

- Maybe it’s using a slow algorithm, like a linear search through thousands of elements instead of a hashtable or binary search.
- Maybe it doesn’t handle some inputs that are unusual but not impossible.
- Maybe the code’s behavior is fine, but it’s really hard to understand and could benefit from some refactoring.

…or one of many other reasons why code might not be as good as it should be.

There’s an interesting consequence of this slightly different definition, though. Sure, the code isn’t as good as it should be, but _that doesn’t mean you should put effort into improving it,_ at least not right now. Why? Well, if the fix was easy, the original author probably would have done it.[1](#fn:time) That means that if you are trying to “fix” the code, it might end up being a non-trivial change, which means a non-trivial amount of your time writing and debugging and testing. Your efforts may be better spent elsewhere, where something is _actively_ causing a problem. (Perhaps a [starter bug](https://bugs.swift.org/issues/?jql=labels%20%3D%20StarterBug)…)

So FIXME comments tend to stick around for a long time. That’s not automatically a problem. It just means that whatever deficiencies the original code had, they weren’t so bad that someone had to rewrite them. And if someone ever _does_ come across a problem with the code, there’s a reasonable chance it’s related to whatever was called out in the FIXME. So that’s what it is: a note to future maintainers of the code if a problem _does_ come up.

P.S. That said, there are definitely some FIXMEs that probably would be easy to fix, including some that may not have been easy to fix in the _past_ but would be _now._ This was more a point about not _assuming_ that they’re easy to fix, or that they automatically indicate poor health in the codebase, or that they should all be tracked in a bug tracker.

P.P.S. Note that there’s one case where “FIXME” should _not_ be used, which is “this code _looks_ like it should be better, but there’s a reason why it’s the way it is”. Maybe you can’t use a hashtable because the elements don’t hash well. Maybe the unusual inputs are handled by the caller instead (add an assertion!). Maybe the obvious refactoring would violate library layering, making the project harder to build. In these cases, the code still deserves a comment, but instead of “FIXME” I’d go with a simple “Note”.

1. There are exceptions, usually when the original author of the code was working under time pressure, or was trying to make as small a change as possible so as not to disrupt other parts of the project. But that’s not the common case. [↩︎](#fnref:time)

This entry was posted on [April](https://belkadan.com/blog/2018/04) 03, [2018](https://belkadan.com/blog/2018) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [LLVM](https://belkadan.com/blog/tags/llvm)
