---
title: Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/'
original_language: en
published: 2022-02-21
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2a7dca0bec4ebfd7'
translated: false
---

> 原文：[Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/)

[UnsafeMutableRawBufferPointer](https://belkadan.com/blog/2022/03/UnsafeMutableRawBufferPointer/) »

« [Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/?tag=linking)

## [Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps](#)

[A recent question on the Swift forums](https://forums.swift.org/t/exported-and-fixing-import-visibility/9415/63) prompted me to actually write this blog post I’ve been idly thinking about for a long time. These days, it’s common for apps to have external dependencies, but both statically linking and dynamically linking those dependencies comes with drawbacks. (This is the same thing as the title, only less provocative.) Why is there this tension and what can be done about it?more

> UPDATE: At WWDC 2023, Apple announced “[mergeable libraries](https://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries)”: dynamic libraries with sufficient metadata to be statically linked into a client that chooses to do so. I’m super excited about this because they seem to address nearly all the trade-offs I discuss here. You can learn more about them in [an excellent presentation by engineer Cyndy Ishida](https://developer.apple.com/videos/play/wwdc2023/10268). I’ll talk more about them at the end of this post, but let’s summarize it as “Mergeable Libraries Are Meant For Apps”!

---

There are four kinds of libraries your app can use:

1. Libraries that come with the OS (or at least from your OS vendor)
2. Libraries that come from someone else that get installed into a shared location, so many apps can share them
3. Libraries that you ship alongside your app that are only used by the app
4. Libraries that are loaded dynamically by the app (often “plug-ins”)

This post is going to focus on the third category; maybe I’ll come back to talk about the others in the future. (The second one’s not really allowed on iOS or Android anyway.) I’m also only going to talk about compiled native code, not VMs/bytecode, even though some of the same issues apply.

### Dynamic linking is for flexibility

The names hint at what’s different: static linking means the library is merged into your app ahead of time (when the app is built); dynamic linking means the library will be loaded into the process when the app is launched. This means not only allocating memory for the code in the dynamic library (and loading any of _its_ dependencies), but also fixing up the places where the main app tries to use APIs from the library so that they point to where the code is being loaded, not to mention just the baseline work of reading from additional files on disk.[1](#fn:aslr)

What’s all this for? Flexibility…that the app probably isn’t using. With libraries in categories 1 and 2, dynamic linking allows apps to keep working even when libraries get updated for bug fixes and performance improvements. It can even be used to _replace_ a dependency, say, with a version of a library that does extra checks for debugging purposes, or one from a _different vendor_ that provides a compatible implementation of the public interface.[2](#fn:swift)

But for category 3, all this flexibility is wasted. The libraries are shipped with the app; if you want to update the libraries, you can ship an update to the app. (I’m glad _that’s_ a solved problem in 2022.)

For category 4 the purpose of dynamic loading is different: it can be about _not_ loading functionality until it’s needed, or perhaps adding functionality without changing the base app, possibly functionality from outside vendors. It’s a very different problem space that’s fundamentally dynamic, but where _linking_ is only one option compared to cross-process communication.

### Static linking costs disk space

Static linking doesn’t have any of this wasted work. You’re taking a library and shoving it into your executable ahead of time, as if it were part of the main app all along. When it comes time to run the app, the loader can’t tell that it wasn’t. Sounds great, right?

The problem is that this only works nicely if you have exactly one executable. In a modern iOS app, like, oh, let’s say [Signal](https://twitter.com/UINT_MIN/status/1310718499719794688), there are usually several: the main app, but also _extensions_ that the OS can spin up for specific purposes. In Signal’s case, there’s a “share extension” (to work with the standard system share sheet), and a “notification service extension” (to handle push notifications without having to launch the whole app). Both of these use only a subset of the libraries that the main app uses, and indeed iOS _requires_ that with strict limits on processing time and memory usage. But they also share a lot with the main app.

If we static-linked everything, there’d be three copies of the common code, wasting space on the user’s phone. (Not to mention increasing build times.) We can’t even static-link a single mega-library and then dynamically load that, because that would use too many resources in those limited extension contexts.[3](#fn:busybox)

### They don’t mix

Things get even worse if you try to mix static and dynamic linking: you can end up with multiple copies of a library in the _same app_. Say your app uses two libraries: FooKit and BarKit, and they both depend on a third, libCore. If FooKit and BarKit are statically linked, then everything’s fine: the app “just” links to libCore as well. Similarly, if libCore is dynamically linked, then it doesn’t matter how the app uses FooKit and BarKit: it will have external references to a single libCore either way. But if libCore is statically linked and FooKit and BarKit are dynamically linked, then the code for libCore will be incorporated into _both_ FooKit and BarKit, wasting disk space and possibly causing problems at run time.

A variation of this is when there’s only _one_ intermediate library FooKit, but the _app_ also depends on libCore. In this case there are two options: have FooKit include _all_ parts of libCore, instead of just what it uses, and tell the app to find libCore’s symbols in FooKit; or do the same thing as above: statically link libCore into FooKit and then link it _again_ into the main app.

Sometimes people do this on purpose, because libCore is just an implementation detail of FooKit and BarKit. Maybe FooKit and BarKit come prebuilt, possibly from separate vendors. Maybe they even rely on different, incompatible versions of libCore! This is a valid idea, but not always well-supported: anything that expects to have global uniqueness in the program (like, say, Objective‑C class names, or Swift mangled type names) is now in danger of not working correctly. On the other hand, Rust’s Cargo does this deliberately to support the “incompatible versions” use case, and since Rust provides very few “global uniqueness” language features it usually works out in practice.

But if you can’t rely on that, the rule of thumb is that you can only use static linking within a subset of the build graph that has a single dynamic client (a dynamic library or an executable). That is, as soon as a dependency is used by multiple dynamic clients, it too must be treated as dynamic to avoid duplication.

(Swift’s initial implementation didn’t really plan for static libraries because of this. Like, we didn’t make them impossible or anything, but we kind of went in with the assumption that everyone would use dynamic libraries because they always work without this weird build limitation that already applied to Objective‑C, and static libraries would be for more specialized use cases. At the same time, though, our (Apple’s) linker people were trying to get external developers to use fewer dylibs in their apps because they really do affect load time. Oops. I don’t know exactly what we would have done differently, but we should have talked with the linker folks more than we did.)

### The static archive format is also bad

Dynamic libraries have an actual format. Static libraries are a bunch of object files glued together, at least on Unixy systems like iOS _and_ Android. [Seriously!](https://en.wikipedia.org/wiki/Ar_(Unix)) The standard extension is `.a`, for “archive”. The base format is so old it predates today’s more common `tar` (and forget about `zip`). And, like, old doesn’t mean bad, so instead I’ll complain about how this approach wastes a bunch of space: any functions that are copied into more than one object file are going to preserve all the copies instead of deduplicating them like proper linking does.[4](#fn:copied)

But it’s not just about file size. Swift’s `fileprivate`, `internal`, and `public` correspond, ish, to access levels supported by linkers: “only available in this file”, “only available in this library”, and “available to clients”. But because static libraries are just object files glued together, there’s no distinction between the “internal” and “public” parts. This isn’t just about preventing people from using some non-public symbol; it’s how dead-code stripping works across compilation units. Although that’s most useful when you link a static library into a larger program…

It’s easy to turn a static library into a dynamic library: you link it with no other files. But then you can’t statically link it anymore. (I can’t think of an inherent reason why you couldn’t write a tool to turn dynamic libraries back into object files either, but I don’t think anyone has, and it would certainly be a pain.)

### Conclusions

What I want is a format that behaves like an object file or static library, but which has already gone through a round of linking: deduplication, removing non-public symbols, dead-code stripping, maybe even some link-time optimization. I don’t think there’s any reason you couldn’t build such a tool today even _without_ a new format, but if you _did_ have a new format you could do more preparation to make later linking steps more efficient, not to mention making the archive format smaller.

[Keith Smiley reminded me that `ld -r` exists.](https://twitter.com/SmileyKeith/status/1495864637241184257) This is a mode of `ld`, the dynamic linker, that produces a single object file instead of a static archive or dynamic library, which would do a lot of what I said above! (The `-x` option hides the non-public symbols, for example.) This isn’t perfect, and I don’t know enough about this option to know if there are additional drawbacks, but it’s something that does exist today!

I do want to point out that this ought to be a client-side problem, rather than a library-side problem; the split isn’t between static or dynamic _libraries_ as much as static or dynamic _linking._ If you distributed your code in New Super Library Format DX, a client could statically link it as an implementation detail and hide all your public symbols (assuming it’s safe to do so), or they could statically link it and _re-export_ all your public symbols, or they could leave it up to the build system to statically link if it’s safe and dynamically link otherwise, or they could package it in a dynamically-loadable wrapper and use it from multiple executables, or as a plug-in.

This doesn’t fix the fundamental “two copies” problem with static linking, though. The only way I can think of to deal with that is to use dynamic linking, but make it less dynamic: if you link a dynamic library that you _know_ is shipped with the app, you don’t have to search the filesystem for the right library, or match symbols by name at runtime. And the (build-time) linker and (run-time) loader should be able to take that into account.[5](#fn:dyld3)

But we’re never going to get dynamic libraries down to being as fast to load as static linking, and static linking will always make two copies of a library’s code if there are two executables.

~~P.S. I didn’t talk to any of the Apple linker folks before writing this post. They very well could be working on improvements here. Same goes for every platform, really. But this is the current state of things.~~

> UPDATE: Apple’s Mergeable Libraries really do seem to be New Super Library Format DX. You can dynamically link against them, or have them “merged” into the client binary, which is effectively static linking. The only remaining tradeoff here is about when you leave the library dynamic because it has multiple dependencies, and that’s hopefully something Apple continues to address in other ways.[5](#fn:dyld3)
> 
> Unfortunately, Apple’s new linker isn’t open source. I haven’t seen anyone discussing bringing the format to [lld](https://lld.llvm.org) or [mold](https://github.com/rui314/mold)/[sold](https://github.com/bluewhalesystems/sold), or to experiment with it for ELF (Linux, Android) as well. And I don’t know enough about Windows to know whether the approach translates at all, though I suspect Windows apps don’t have the same launch time pressures that mobile apps do. (Android has of course merged the _Java_ classes from all your dependencies ahead of time for several years, but to my knowledge those classes’ native dependencies are still second-class citizens.)

### Appendix: Other trade-offs between static and dynamic linking

- Static linking is generally slower at build time, which can be annoying in an edit-build-debug cycle. _Mergeable libraries behave like dynamic libraries in debug mode._
- Static linking allows for more optimization: not just dead-code stripping but also any sort of “smart” cross-object-file optimizations (“link-time optimization”) can be applied across library boundaries. _I assume mergeable libraries work with LTO, but I haven’t verified._
- Static linking lets you distribute all your code as a single executable instead of needing multiple files on disk.
- Having code in a single binary allows for the use of [relative references](https://duriansoftware.com/joe/optimizing-global-constant-data-structures-using-relative-references) instead of absolute pointers, which avoids those launch time “fix-ups”. Static linking theoretically allows relative references across library boundaries, though either you’d have to promise this when compiling the client or have a smart enough linker to change an absolute reference to a relative one in a way the program will understand. _I assume mergeable libraries behave like static libraries here when merged._
- For the same reason, though, ASLR only works on dynamic libraries. If you have all your code in one executable, it all moves around the address space together, and the security benefit of ASLR is lessened.
- Dynamic libraries have an identity even at run time, so you can do things like “find resource file X.svg relative to FooKit”. Apple OSs use this as a way to namespace resources, so FooKit, BarKit, and the main app can all have resources named “X.svg” without worrying about them colliding. This was useful enough that [the same basic functionality was added to SwiftPM](https://github.com/apple/swift-evolution/blob/master/proposals/0271-package-manager-resources.md#resources-bundle), but based on auto-generated unique names rather than the actual dynamic library file. _Mergeable libraries apparently account for this by recording the original library name, but it_ is _a little extra indirection._
- Dynamic libraries can have code that’s run when they are loaded, and this is guaranteed by the loader to be run in dependency order. Static libraries don’t have that guarantee without extra synchronization work. But you should avoid doing work at launch/load time anyway. _I assume mergeable libraries preserve dependency order._
- Historically static libraries couldn’t specify the libraries they depend on as part of the format, only the symbols. But many environments work around that by putting in extra metadata, such as Swift’s “autolinking” info, so I didn’t include it as a format drawback above. This sort of thing does get in the way of changing where symbols are located, though.

1. Due to [address space layout randomization](https://www.howtogeek.com/278056/what-is-aslr-and-how-does-it-keep-your-computer-secure/), modern apps _always_ have to do this kind of “fix-up”, because the library won’t be loaded at the same address every time the app is launched. [↩︎](#fnref:aslr)
2. Swift uses the dynamic nature of dynamic library loading for backwards-deployment purposes. On Apple platforms that have the Swift stdlib in the OS, the dynamic linker finds libswiftCore.dylib inside /usr/lib; on older OSs, it can’t find it there and falls back to the copy inside the app bundle. This ensures that the OS version always wins while still supporting backwards-deployment, one way to turn a category 3 library into a category 1 library. [↩︎](#fnref:swift)
3. A twist on this approach is to build a single executable that changes what it does based on how it’s invoked. As a simple example, `clang++` is a symbolic link to `clang` on Apple platforms, but when you use `clang++` Clang activates a bunch of C++ options automatically. (The [BusyBox](https://en.wikipedia.org/wiki/BusyBox) project takes this much much further, with a single executable providing _hundreds_ of commands.) But symbolic links to executables may not be allowed in all use cases, and it’s a bit brittle anyway because someone might resolve the symbolic link ahead of time. Hard links wouldn’t have _that_ problem, but often aren’t preserved in archiving and copying. Plus, combining executables and _plug-ins_ this way usually isn’t supported, and it still doesn’t solve the problem if you _don’t_ want to load all the same libraries. [↩︎](#fnref:busybox)
4. Why would functions be copied into more than one file? If they don’t have a particular object file to call home. `static` C functions defined in header files, instantiations of C++ templates and Rust generics, and the implicit helper functions Swift generates to smooth over interoperation with Objective‑C are all examples of such functions. [↩︎](#fnref:copied)
5. Apple’s [dyld3](https://developer.apple.com/videos/play/wwdc2017/413/) project was about precomputing a bunch of this information at app install time, or at first launch if the app wasn’t installed from the store. This really can help, and harkens back to the pre-ASLR days of [prebinding](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/FrameworkBinding.html#//apple_ref/doc/uid/20002256-106894-BAJDCHID). But it’s also very after-the-fact, and doesn’t directly work for plug-in-style library loading while the program is already running. (They might have found a way to do some of the same optimizations here too; it’s just trickier.)

  They’re up to [dyld4](https://github.com/apple-oss-distributions/dyld/blob/dyld-940/doc/dyld4.md) now, by the way. [↩︎](#fnref:dyld3) [↩︎2](#fnref:dyld3:1)

This entry was posted on [February](https://belkadan.com/blog/2022/02) 21, [2022](https://belkadan.com/blog/2022) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Linking](https://belkadan.com/blog/tags/linking)
