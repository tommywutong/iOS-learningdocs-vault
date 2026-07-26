---
title: ROSE-8 on Mac OS 9
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/'
original_language: en
published: 2020-05-24
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6045ba216066f83a'
translated: false
---

> 原文：[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/)

[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/) »

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=swift)

[Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=swift) »

« [Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/?tag=mac-os-classic)

[Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=mac-os-classic) »

« [Introducing the Game 'by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/?tag=rose-8)

## [ROSE-8 on Mac OS 9](#)

[![](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/meme.png)](https://knowyourmeme.com/memes/ah-shit-here-we-go-again)

It’s been nearly two months since my April Fools’ project this year (not a prank!) where I managed to [get a Swift program to run on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/). I’m still proud of both the technical achievement _and_ the blog post there. But when I finished it…I didn’t want to _stop._

There were a few things I wanted to do. First of all, there’s the small bit of all this that’s useful work: to get to my minimum viable C-interoperating product, I chopped down the Swift standard library quite a bit. That’s something that’s still useful to people who want to write Swift in constrained environments, like embedded code, and I’ve been encouraged to write about my findings there. (And plan to.) But moreover, while [BitPaint](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-the-goal) was a great proof-of-concept, it didn’t really use that much Swift. It really _was_ just C interop. So, what could I do that would actually feel like a _Swift_ project?

Well, how about my _other_ useless project from this year, [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/) and the [Game ’by Color](https://belkadan.com/blog/2020/02/ROSE-8-Game-by-Color/)? A fictional game system I designed, running on the OS I learned to program on? _Perfect._

This turned out to be, um, quite a bit of work.

### Runtime requirements

ROSE-8 doesn’t actually use too many complicated Swift features…but of course, it depends on the standard library, and specifically Swift’s plain old resizable, copy-on-write Array. Handling Array means properly handling

- class allocation and retain counting
- generic types
- generic implementations that aren’t fully optimized away

All of this needs actual _runtime_ support.^[1](#fn:runtime) With normal Swift, the runtime is written in C++ and linked in to the standard library. While I had [gotten Clang to emit code for Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#modern-compiler-classic-linker), C++ has its _own_ standard library, and I didn’t want to try to get _that_ working on Mac OS 9. (And of course, the C++ standard library provided on Mac OS 9 is too old to support many of the features the Swift runtime needs.) So one way or another I was going to have to do some implementing from scratch, not just copying from the real version like I’d done for the standard library.

But wait, why is the Swift runtime implemented in C++ anyway? Why not write it in Swift?

1. The runtime was needed pretty early on in the bring-up of Swift, so the oldest bits of it couldn’t have been written in Swift. That’s not going to apply here.
2. The runtime usually needs to be able to access platform functionality, but Swift has “overlay” libraries that augment the usual platform functionality when you do something like `import Darwin` (or in this case, `import MacTypes`). So you’d have a circular dependency between the runtime (usually linked in with the stdlib) and the platform overlays. _However,_ if I’m always going to use static linking, the linker can handle these circular dependencies.^[2](#fn:circular)
3. There are still some things C++ can do that Swift can’t do, the most important being declaring globals with particular names and declaring complex globals with compile-time constant values. The Swift compiler expects to be able to reference certain things directly, such as the type metadata for basic integer types. This one’s still a problem for me, but maybe I can limit my C++ use to that.

I had avoided taking any dependencies on the runtime before, but maybe it’d be a good learning experience for me. Even when I worked on Swift at Apple, I mostly worked on the user-facing parts of the _compiler,_ with only a few short jaunts into the runtime and standard library. So I decided to forge ahead with a runtime written in Swift (mostly). It may not be the fastest or prettiest, and it certainly wasn’t going to support everything the real runtime does, but I could make it work. Right?

### Breaking it down

Like [last time](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#modern-compiler-classic-linker), I decided to start with an easier goal: getting enough of the runtime working to support an ‑Onone build of BitPaint. As I said above, BitPaint really isn’t so complicated from a Swift perspective, in that it’s mostly just pushing integers and pointers around. With optimizations on, it inlines everything it needs, and doesn’t even need to link against the built stdlib. However, quite a few of the integer and pointer operations in Swift are implemented generically, relying on the compiler to optimize them down to machine-provided operations! So right off the bat I had to handle a bunch of the generics model.

Aside: This post isn’t going to be a discussion of the Swift runtime—the real one _or_ the tiny one I made. I’ve been encouraged to write a post on that too in the future, but for now I’m going to stick to a narrative about how I got the Mac OS 9 Game ’by Color app running.

My approach was basically “compile BitPaint at ‑Onone, try to link, and see what runtime functionality is missing”. There was a fair bit of it at the beginning!^[3](#fn:unresolved)

```
#  Unresolved external references:
#    $sBi16_WV
#    $sBi32_WV
#    $sBi64_WV
#    $sBi8_WV
#    $sytN
#    $sytWV
#    $syXlN
#    $syycWV
#    .swift_allocateGenericValueMetadata
#    .swift_allocObject
#    .swift_checkMetadataState
#    .swift_deallocObject
#    .swift_getAssociatedConformanceWitness
#    .swift_getAssociatedTypeWitness
#    .swift_getForeignTypeMetadata
#    .swift_getGenericMetadata
#    .swift_getTupleTypeLayout2
#    .swift_getTupleTypeMetadata
#    .swift_getTupleTypeMetadata2
#    .swift_getTupleTypeMetadata3
#    .swift_getWitnessTable
#    .swift_initEnumMetadataSinglePayload
#    .swift_initStructMetadata
#    .swift_release
#    .swift_retain
#    .swift_slowAlloc
#    .swift_slowDealloc
#    .truncf
#    .__divdi3
#    .__fixdfdi
#    .__fixsfdi
#    .__fixunsdfdi
#    .__fixunssfdi
#    .__floatdidf
#    .__floatdisf
#    .__moddi3
#    .__mulodi4
#    .__udivdi3
#    .__umoddi3
```

You can mostly group these into four categories:

1. Those global objects I mentioned earlier (the ones that start with `$s`)
2. Metadata, layout, and associated type utilities
3. Object allocation and reference counting
4. Some low-level numeric operations that weren’t implemented in the PowerPC of the day

And I ended up having to deal with each of these in a different way:

1. This is the one piece I borrowed most of from the real runtime. It _is_ implemented in C++ but for any complicated code I called back into Swift.
2. This was the bulk of the work. A lot of what the runtime does is manage generic metadata, which has to be allocated and filled out for every set of generic arguments if the use can’t be optimized away. It’s also easy to get it wrong.
3. Object allocation is actually pretty simple if you don’t support unowned and weak references! But wait, why do I need it at all for BitPaint, which only does numbers and pointers? Turns out Swift uses objects behind the scenes to implement both existentials and the captures stored for a closure, and besides, I’m going to need them anyway for Array’s storage. (Also, [this way my Swift can use ARC to manage CF objects](https://twitter.com/UINT_MIN/status/1248154940318482432).)
4. Most of these numeric operations, the ones with underscores, come from LLVM itself. LLVM knows that not every platform implements all these operations, so it provides the [compiler‑rt](https://compiler-rt.llvm.org) project to implement them in software. With not too much trouble I was able to get the compiler‑rt “builtins” I needed to build for PPC32.

  `truncf` was the one exception, since it’s normally part of the C standard library, but Mac OS 9 didn’t actually provide it. Why? Probably because C converts between `float`s and `double`s anyway, and the operation is going to have the same result if you round-trip through `double`. But LLVM wanted it to be there, and trying to _trick_ it into calling the double-precision `trunc` wasn’t working, so in the end I just took a detour and [implemented it myself](https://belkadan.com/source/ppc-swift-project/blob/refs/heads/dev:/stdlib/_Runtime/Truncf.swift), as a refresher on the IEEE 754 format.

### Debugging

…was a challenge. Without real string formatting, I made good use of a little `dump` utility that I tweeted:

> ```
> withUnsafePointer(to: v) {
>   let p = UnsafeRawPointer($0)
>   var i = 0
>   while i < MemoryLayout.size(ofValue: v) {
>     let nextByte = (p + i).load(as: UInt8.self)
>     putchar(hexToASCII(nextByte >> 4))
>     putchar(hexToASCII(nextByte & 0xF))
>     putchar(0x20)
>     i += 1
>   }
> }
> ```
> 
> — Jordan Rose (@UINT_MIN) [May 13, 2020](https://twitter.com/UINT_MIN/status/1260696630677757953?ref_src=twsrc%5Etfw)

But this only goes so far. It’s not so helpful when a pointer points to the wrong thing, or when some memory is left uninitialized, or when everything is offset by 4 from its correct address. My debugging techniques ranged from placemarker calls to `puts` (“did we get this far?”), to trying to compile minimal programs that would still crash in the same way (what I called a “playground” app), to early-exiting or even intentionally breaking things to see if they still crashed. These are all fairly standard debugging techniques, but the most powerful ones are missing: directly inspecting memory and stepping through instructions until you find a crash or misbehavior. No backtraces and no live debugging on Mac OS 9, at least not without more specialized tools I didn’t have!^[4](#fn:MacsBug)

The most mysterious problem was one where BitPaint would _appear_ to work, but crash after several seconds of user interaction. What was going on? Want to guess?

.

.

.

.

.

.

It took me _days_ to think of running out of memory; worse, this was _after_ it had already been suggested to me in bouncing ideas off a friend. (Did you know that in Mac OS 9, an application had to specify the maximum amount of memory it would ever use up front?) To be fair, the code that was causing the problem _shouldn’t have been allocating any memory,_ and the only metadata being allocated in the runtime was when a new generic type was instantiated. Why wasn’t the cache working?

It turned out to be a _compiler_ bug, though fortunately not one that’s gone out in any shipping version of Swift.^[5](#fn:master-next) The symptom was that global variables with constant initializers were considered to never change, and therefore the cache for generic metadata was getting allocated from scratch, empty, with every call. The fix ended up being pulling the latest updates for the compiler and merging in my changes once more. That’s it.

The _second_ most mysterious bug was another one I tweeted:

> Last few days' debugging:  
> `a != a`  
> → == for two Optionals uses a tuple [https://bugs.swift.org/browse/SR-12829](https://bugs.swift.org/browse/SR-12829)  
> → Runtime thinks tuple is half the size it should be  
> → All tuples using the same metadata  
> → Cache key is a CFData  
> → All cache keys are 0-length  
> → Forgot [https://developer.apple.com/documentation/corefoundation/1542375-cfdatasetlength](https://developer.apple.com/documentation/corefoundation/1542375-cfdatasetlength)
> 
> — Jordan Rose (@UINT_MIN) [May 19, 2020](https://twitter.com/UINT_MIN/status/1262609197411098624?ref_src=twsrc%5Etfw)

Anyway, with a lot of trial and error, “[psychic debugging](https://devblogs.microsoft.com/oldnewthing/?s=psychic+debugging&submit=%EE%9C%A1)”, and re-reading whatever code I _guessed_ was causing the problem, I eventually got a runtime that would work with an unoptimized BitPaint. And not too long after, with Array as well, and then the Game ’by Color.

### Rewards and Plans

Overall, it took me [a month or so](https://twitter.com/UINT_MIN/status/1253740850049191936) to do the original project, and maybe a month and a _half_ to do this part. In retrospect, I should have expected that: the original project was mostly hooking up pieces that worked and chopping out things that didn’t, while this one was porting a good chunk of a moderately complicated project (the Swift runtime) without being able to use tests or a debugger. But I got some things out of it:

- [A version of the Game ’by Color that runs on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/GameByColor.hqx). (Here’s the [game](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/super-maze.gbyc) I’ve been testing with.)
- An implementation of (some of) the Swift runtime, and more of the standard library, that runs on Mac OS 9. You can check this out in the [ppc-swift-project repository](https://belkadan.com/source/ppc-swift-project/). (The Game ’by Color sources are also available there.)
- A feature-flag-guarded version of the Swift standard library, which I plan to discuss on the actual Swift forums in case embedded developers are interested.
- A better understanding of the Swift runtime, which I hope to put in future blog posts.

I’ll finish off with a photo of the Game ’by Color running on an actual PowerPC Mac, once again courtesy of my friend Nadine:

[![Mac OS 9.2.2 on a Power Mac G4, running the Game ’by Color, running super-maze](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/running.jpg)](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/running.jpg)

1. The word “runtime” is a funny one these days. Originally it would have just meant “at the time when the program is run”, but these days it can also mean “a library that provides support for features that aren’t just compiled to plain machine code”. The simplest example of this is the automatic reference counting used by Swift classes; rather than directly manipulate reference count data in each object, the compiler emits calls to the `swift_retain` and `swift_release` functions. To keep these meanings clear, I tend to use “run-time” for the general “when the program is run” adjective, and “runtime” for the support library or things relating to it. [↩︎](#fnref:runtime)
2. Circular dependencies are normally not just a linking problem, but a conceptual problem: if something changes, what gets rebuilt? Does everything get rebuilt? _Does everything cause everything to get rebuilt, resulting in building everything in a cycle forever?_

  *cough*

  Anyway, in this case, there’s not really a circular dependency, even if we _were_ using dynamic linking for everything, _if_ you separate the interface and the implementation:

    1. Build Swift.swiftmodule (no dependencies)
    2. Build MacTypes.swiftmodule (depends on Swift.swiftmodule)
    3. Build _Runtime.dylib (depends on Swift.swiftmodule and MacTypes.swiftmodule)
    4. Build Swift.dylib (depends on Runtime.dylib)
    5. Build MacTypes.dylib (depends on Swift.dylib and Runtime.dylib)

  This logic only works because the runtime is optimized and doesn’t have any link-time dependencies on the standard library or overlays itself. Without that, this would still work, but it wouldn’t be _completely_ clean. In practice, the runtime is always statically linked into the stdlib, even when the stdlib is a dylib, so the only thing that strictly has to be optimized out is the overlay usage.

  Does this mean it’s worth doing this for the real runtime? Probably not, at least not immediately. The real runtime is a lot more complicated and makes use of a number of C++ features, and a bunch of its logic is shared with the debugger. Trying to share logic across C++ and Swift would be pain, so it’d be hard to just write _new_ code in Swift too. And detangling the build dependencies would be a pain. But maybe it’d be worth it to convert everything over, someday. [↩︎](#fnref:circular)
3. This isn’t even all of it, because I `#if`‘d out a number of things in the standard library that I didn’t need once I saw they had runtime dependencies. [↩︎](#fnref:unresolved)
4. There was a standard debugger distributed by Apple called [MacsBug](https://en.wikipedia.org/wiki/MacsBug), but I could not get it to work in my emulator. [↩︎](#fnref:MacsBug)
5. I’m working from the `master-next` branch because I need IBM’s latest work on AIX; after the next LLVM rebranch, I’ll pin this project to Swift 5.3 or 5.4 or whatever and leave it there. [↩︎](#fnref:master-next)

This entry was posted on [May](https://belkadan.com/blog/2020/05) 24, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [ROSE-8](https://belkadan.com/blog/tags/rose-8)
