---
title: Swift’s Type System
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/07/swift-type-system/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5fa8dc87fa43a958'
translated: false
---

> 原文：[Swift’s Type System](https://oleb.net/blog/2015/07/swift-type-system/)　·　Ole Begemann

# Swift’s Type System

Brent Simmons in [Solving Problems I Don’t Have, Except that I Do Have Them](http://inessential.com/2015/07/19/solving_problems_i_dont_have_except_th):

> Swift’s type system solves a problem I don’t have.

I can relate to this, and I bet many other Objective-C developers can too.

When I started experimenting with Swift, the compiler seemed to fight me constantly.[1](#fn:1) It has gotten much better as I became more familiar with the language, but sometimes the compiler, with its often cryptic error messages, still reminds me of a petulant child that’s impossible to please.

In these situations, the benefit you get from Swift’s strict type-checking can seem small compared to the effort to make your code work. Even so, the type system has grown on me in the last year, to a point where I don’t want to miss it anymore.

# Swift is More Expressive

The biggest reason I like Swift much better than Objective-C is not its type system, though. It’s the more mundane features that I love the most:

- First-class value types. Being able to put an integer or a struct into an array without having to box them in an object is a big win, as is being able to extend these types.
- Enums with associated values. Tuples. Modeling data structures is so much cleaner in Swift.
- Pattern matching

  .
- Cleaner syntax and no header files.

In short, Swift is a modern language, and Objective-C clearly isn’t.

If Apple had released a true “Objective-C 3.0” last year, modernizing the language while keeping Obj-C’s dynamic nature intact[2](#fn:2), I would have been very happy and I’d probably never have argued for more static type-checking. After all, “I know what I’m doing and I’ve never shipped a bug where an array contained objects of an unexpected type.”

# Hole-Driven Development

But Apple gave us Swift, not Objective-C 3.0. The release of Swift motivated me to explore other languages with similar type systems, such as Haskell, ML, and Scala. One thing I learned in particular from those communities is the idea of [hole-driven (or compiler-driven) development](https://matthew.brecknell.net/post/hole-driven-haskell/): seeing the compiler not as an enemy you have to fight, but as a tool that guides you almost magically to a solution for your problem, one step at a time, using types.

Hole-driven development is a fantastic technique for modeling data structures and data transformations (exactly what Haskell and friends excel at), and it works really well in Swift too, though there’s still plenty of potential for improvement. The key difference between an annoying and a helpful compiler are easy-to-understand error messages, and many of Swift’s diagnostics have a rather mysterious quality.[3](#fn:3)

For typical GUI programming, compiler-driven development is probably less useful, although I think this is mainly due to the design of the Cocoa APIs and not an inherent limitation. Libraries like [ReactiveCocoa](http://reactivecocoa.io/) show what kind of API designs the type system (and, to some extent, the cleaner syntax) makes possible. A [complex signal transformation](https://github.com/ReactiveCocoa/ReactiveCocoa#making-network-requests) over multiple steps is much easier to get right when you can rely on the compiler thanks to generics. I now find code like this much harder to write (and understand later) in Objective-C because I have to keep more stuff in my head.

# Automatic Documentation

Another huge benefit of a strict type system is the automatic documentation it generates as a byproduct. As developers on Apple’s platforms, we don’t have access to the source code of the libraries we use the most, so we have to rely on the documentation. The more information the compiler enforces API designers to provide, the better for consumers of the API. Optional annotations alone have improved the Cocoa documentation significantly.[4](#fn:4) Imagine if all Cocoa APIs just used `id` for all method parameters and return values. The header files would be a lot less useful.

# Conclusion

By forcing me to think very carefully about types, I find that my Swift code is better designed and easier to maintain. I feel more confident in the correctness of my code, and for some strange reason writing it is also more fun!

Swift is still at the beginning of its journey. It can be frustrating, but over time the compiler will get better error messages, and it will help you even more to reason about your code. As an example of something we all struggle with, take concurrency: if the compiler could statically prove that your multithreaded code has no race conditions, that would be a huge win. Swift can’t do that at the moment, but [Rust can](https://doc.rust-lang.org/book/concurrency.html). I’m excited.

1. That’s one reason why I think Swift is decidedly not an easy language to learn (or teach). That, and the complexity of the standard library. [↩︎](#fnref:1)
2. We’ve had “Objective-C without the C” for decades, though, in the form of Smalltalk. [↩︎](#fnref:2)
3. At least partly due to my relative unfamiliarity with the language, no doubt. [↩︎](#fnref:3)
4. I should mention that the annotations themselves don’t enforce correctness, so strictly speaking they are no more reliable than header comments. One could argue that the mere presence of a strict compiler forced Apple to make their documentation more precise. [↩︎](#fnref:4)
