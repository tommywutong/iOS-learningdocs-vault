---
title: 'There''s No Such Thing As "Implicitly Atomic"'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/10/Implicity-Atomic/'
original_language: en
published: 2023-10-04
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ae664df2d890a1dd'
translated: false
---

> 原文：[There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [HOW TO REFER TO A MAGIC CONSTANT IN C](https://belkadan.com/blog/2023/07/Magic-Constants-in-C/)

[Soft Orders of Magnitude](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/) »

« [Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=swift)

[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=swift) »

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=compilers)

[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/?tag=compilers) »

## [There's No Such Thing As "Implicitly Atomic"](#)

> If I have an aligned machine-word-sized variable (Int) and I store to it from Thread A, then I know Thread B might see the old value instead of the new value (because of per-processor caching, or the compiler “hoisting” a load to earlier in the function). But there’s no way, on a modern processor, that Thread B sees a mix of the old and new value, right? That can only happen with wider values, or unaligned values, that the code may update non-atomically, right?

_This question is paraphrased from the Swift forums, though I’m not linking to it cause it’s in the middle of a larger thread and it’s something people might reasonably ask anyway. My response, lightly edited, is below; it is Swift-oriented but also applies to C, C++, and Rust._more

I agree that “torn” values, with a mix of the old and new value, are very unlikely in this case—all modern processors that I know of do guarantee that reading or writing an aligned, machine-word-sized value happens as a single unit, meaning no “tearing”. However, you’ve left out the possibility that there’s more going on than just “read memory” and “write memory”. The silliest example is if the word-sized value is an instance variable, or global or static variable, in which case Swift’s [dynamic exclusivity checks](https://www.swift.org/blog/swift-5-exclusivity/) will kick in and potentially complain.

_EDIT: Even_ that _isn’t guaranteed. If you don’t say “atomic”, the compiler might decide to split up a store to optimize for speed or code size! This isn’t hypothetical; [Greg Parker ran into this with libobjc.](https://discuss.systems/@gparker/111179798868336840)_

But let’s assume you’re doing a direct access through an UnsafePointer, the closest you can get in Swift to emitting a single aligned load or store instruction. Do you have a guarantee of the behavior you described above? No, you still don’t. In fact, there’s an immediate way today to make that break: turn on [Thread Sanitizer](https://www.swift.org/blog/tsan-support-on-linux/).[1](#fn:tsan) (The way you tell Thread Sanitizer that it’s okay for other threads to read a stale value is to use [relaxed](https://en.cppreference.com/w/cpp/atomic/memory_order#Relaxed_ordering) atomic operations, though note that [even that may not be good enough](https://www.cl.cam.ac.uk/~pes20/cpp/notes42.html) depending on what you’re trying to do.[2](#fn:oota))

But maybe you say Thread Sanitizer is an artificial scenario that doesn’t count? For portable and futureproof code, _that’s still not good enough._ The OS, or hardware, or anything really, is permitted to track additional information about memory; in fact, we know it does this kind of thing on a per-page basis on most operating systems to support permission protections and virtual memory. So it could in theory do something like TSan for every program, making pages or sub-regions of pages “thread-associated”, and catching any attempt to access them across threads, for both performance and correctness reasons. This sounds like an outlandish amount of work and overhead to enable for every process by default, but [arm64e exists](https://developer.apple.com/documentation/security/preparing_your_app_to_work_with_pointer_authentication), even if it’s only being used in limited scenarios. Other memory-safety-focused ABIs/architectures like [CHERI](https://faultlore.com/blah/fix-rust-pointers/#cheri) exist as well.[3](#fn:cheri) So I wouldn’t say it’s impossible, even if today’s mainstream[4](#fn:edit) x86_64 and arm64 processors and operating systems don’t do anything like that.

Finally, [undefined behavior is undefined](https://blog.regehr.org/archives/213). I don’t want to make undefined behavior a _bogeyman_ that will deliberately produce wrong answers, but the compiler is within its rights to say “I can prove this load races with that store and therefore I can load _whatever value I want”._ (This usually happens when the compiler is assuming a certain combination of conditions can’t possibly happen and therefore it should save code size rather than emit code that “should” be dead.)

So no, do not use a single non-atomic machine-word load or store to communicate across threads without any other form of synchronization in Swift. Or C. Or Rust.

1. Awkwardly, the link from this blog post to the Apple page about TSan is broken, because Apple has since reorganized that section of the developer docs. The new docs don’t have an easily-linkable page, though. That said, there are _lots_ of third-party explainers for using TSan within Xcode, as well as plenty about using TSan on the command line with C or C++, and a few even for Rust. [↩︎](#fnref:tsan)
2. Thanks to [zwarich](https://hachyderm.io/@zwarich/111179409269235025) for pointing this out. Atomics are hard, because C and Swift and Rust expose extremely subtle operations for Maximum Speed. [↩︎](#fnref:oota)
3. I could have linked directly to the [official CHERI website](https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/) but Gankra manages to explain it way more concisely and in a much more friendly manner. [↩︎](#fnref:cheri)
4. “mainstream” added to [satisfy Gankra](https://toot.cat/@Gankra/111179049210895080). (Thank you.) [↩︎](#fnref:edit)

This entry was posted on [October](https://belkadan.com/blog/2023/10) 04, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Compilers](https://belkadan.com/blog/tags/compilers)
