---
title: Swift was always going to be part of the OS
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/10/Swift-in-the-OS/'
original_language: en
published: 2022-10-09
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a9d4098144ec35ef'
translated: false
---

> 原文：[Swift was always going to be part of the OS](https://belkadan.com/blog/2022/10/Swift-in-the-OS/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/)

[The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/) »

« [Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=swift)

[The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/?tag=swift) »

« [Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=apple)

## [Swift was always going to be part of the OS](#)

Recently on the Swift Forums, someone complained that putting Swift in the OS has only made things worse for developers. My immediate reaction is a snarky “welcome to the world of libraries shipped with the OS”, but that’s not helpful and also doesn’t refute their point. So here’s a blog post that talks about how we got where we did, covering time when I worked on Swift at Apple. But I’m going to have to start a lot earlier to explain the problem…more

### OS Dependencies

In my previous post “[Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/)”, I talked about how there’s a trade-off between static and dynamic linking for libraries you ship with your app. But what about libraries that are shipped with the OS? At that point, you are invoking the primary power and curse of dynamic linking: the library you build and test against may not be the library you run against, at which point you have to be much more careful about what you rely on.

At this point we can imagine a spectrum, where at one end you use _nothing_ from the host OS, and at the other you are entirely dependent on it:

- The starting point doesn’t really exist anymore unless you _are_ the operating system, but once upon a time personal computers worked by handing over control of the entire computer to the running process, which was allowed to do whatever it liked with the whole machine, memory, whatever. Even for these programs the OS might provide “library functions” that either got loaded with the program or were left in memory at known locations when the program was loaded, but you _could_ have a program that eschewed all of that and was basically just an OS of its own, with no dynamic dependencies at all.
- These days, even a program that is “statically linked” still isn’t “in charge” of the entire machine. The operating system _kernel_ is always running as well, providing basic OS services and exposing some sort of “system call” interface by which programs can request certain privileged operations (such as reading a file, or allocating more memory pages). ~~Most modern OSs allow you to produce programs that work this way, including Windows and Linux.~~ Linux is the best-known modern OS that allows programs that work this way, where the only thing you depend on is the set of system calls available to you.
- The most common way to program these days is to depend on at least _some_ libraries shipped with the OS, even if it’s just the C standard library and its minimal runtime. Today’s Apple OSs have this as the “minimum system API boundary”: the system call interface is _not_ stable across OS versions and so you are “required” to use the C/POSIX standard library and its extensions to do even basic primitive operations.[1](#fn:go) EDIT: Windows is similar, though its “stable” interface is the library _below_ the C standard library (thanks [Slava](https://twitter.com/slava_pestov/status/1579275297408499712) and [Kyle](https://twitter.com/optshiftk/status/1579283783563743232)).
- I don’t think you can _really_ claim that _any_ program is at the other extreme, with _all_ its behaviors coming from dependencies, except in certain trivial examples. But from a certain point of view, every _interpreted_ program works like this. A shell script does not directly execute _any_ machine instructions; it’s the shell that does that based on what the script says. (Bytecode runtimes and JIT compilers blur the line here too.)

So given this, we can see that programs can depend on their host OSs to varying degrees, and that Apple in particular goes all-in on the “libraries” model. Let’s take a closer look at that:

### Apple’s Model (pre-Swift)

Before Swift, nearly all of Apple’s public APIs were written in either C or Objective-C and provided in compiled form as native code, rather than some kind of bytecode (like [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) or [CIL](https://en.wikipedia.org/wiki/Common_Intermediate_Language)). New OS versions would include new binary-compatible versions of existing libraries, presenting a superset (in theory) of the previous version’s APIs. Thus old apps would continue to run, but new apps could take advantage of new features. “Weak linking” and the inherent name-based dispatch in Objective-C even allowed new apps to _conditionally_ take advantage of new APIs but still work on older OSs. This eventually became formalized as the [availability model](https://belkadan.com/blog/2021/10/Swift-Delight-Available/), but that’s jumping ahead.

The main downside of this model is that new features and new APIs are tied to the new OS version. If you have an app, and you want to use new API announced alongside OS v9 even when running on OS v7, well, you can’t. Apple of course wants everybody to move to the new OS promptly, but not everybody does; maybe the new OS doesn’t support their computer, or maybe it’s not compatible with an app they use, and so on. So app developers are stuck waiting for enough people to get on OS v9 that they can drop support for OS v7 and v8 without losing revenue, user goodwill, whatever. And on the other side, Apple can’t change the behavior of an existing library without potentially breaking existing apps, even if the existing behavior was buggy.

We’ll talk more about alternatives later, but for now this sets the stage: Swift was designed to not require changes to this model. Libraries would still be compiled native code; new releases would still be binary-compatible with old ones. We accepted those as design constraints, as well as interoperating tightly with Objective-C and not relying on a JIT.[2](#fn:jit)

### Swift “betas” 1..\<5

Between Swift 1 and Swift 5 there was a _massive_ amount of change, from shifting API design to changing ARC function conventions to adding missing optimizations to learning what was going to be practical and idiomatic in this new language. Looming over us the whole time was “ABI stability”, the point at which code using two different versions of Swift could interoperate. Why was this important, when so many other languages didn’t seem to bother? Because this was the very premise of Apple’s OS-based library distribution model: apps compiled for Swift 5 would work with an OS built on Swift 6; apps compiled with Swift 6 would still be able to “backwards-deploy” to an OS built on Swift 5. Without this, _Apple couldn’t use Swift in its own public APIs._

So this was always a goal for Swift. And developers complained too: everyone who used Swift had to bundle all its libraries in with their app, increasing the app size by quite a bit. In addition, those developers who made their own closed-source libraries had to release a separate version for every new version of Swift, because they weren’t necessarily binary-compatible. But at the same time, ABI stability means you can’t change things anymore! (There are inefficiencies in Swift’s enum layout to this day that can’t be improved because that would change the ABI.)

With Swift 5, we finally reached a point where _most_ things were pretty good, where we had worked out how to handle old apps running earlier versions of Swift, and where we were already maxing out on _ill_ will from source-breaking changes. Not to mention pressure from inside Apple: this project had been going on for years and yet there were still all sorts of restrictions.

### The Transition

When it came time to put Swift into the OSs, we had to figure out how to do it without breaking

- existing built apps, which embedded their own earlier version of Swift
- which wanted to continue to support earlier versions of iOS

The first problem was solved by _deliberately_ changing Swift’s ABI, so that Swift 5 wouldn’t collide with anything from Swift 1-4. In the few places where old and new Swift needed to interact—Objective-C—metadata for Swift 5 types was marked differently from Swift 1-4, so that the older Swift would see newer classes as weird Objective-C classes. This was a lot to work out but ultimately pretty straightforward.

The second problem couldn’t be solved the same way; we _wanted_ newer apps to interact with the system Swift APIs. So somehow we had to continue allowing shipping the Swift libraries with apps while _also_ avoiding having two copies of Swift on new enough OSs. Certainly we wouldn’t want an app’s embedded Swift 5 library to supersede the following year OS’s Swift 5.1! That would break parts of the next-year OS that depended on Swift 5.1.

We ended up (ab)using a feature called “[rpath](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html)”, or “runtime search path”, which allowed an executable to find its dynamic libraries not by hardcoded path but by searching a series of directories. By making the search order start with `/usr/lib/swift/` and following that with the app bundle, we could guarantee that apps would use the OS version of Swift if present and fall back to their embedded version otherwise.[3](#fn:usr)

![](https://belkadan.com/blog/2022/10/Swift-in-the-OS/rpath.png)

I want to be very clear here: this is a technique for backwards-deploying the **first** version of an OS library. You can’t play the same rpath trick with the _second_ version, because the first version will already be present on disk. This same technique was used just last year for Swift Concurrency, and then a serious bug was discovered in that first release…and it can’t be “fixed” in the backwards-deployment library because that wouldn’t help on the OSs that still contain libswiftConcurrency 1.0. Which in turn would create a discontinuity in support:

![](https://belkadan.com/blog/2022/10/Swift-in-the-OS/discontinuity.png)

…okay, bugs are introduced and then fixed in OS updates all the time, so maybe there would be times when this is worth it, but the main point is it’s not a 100% solution, and for _new_ APIs it breaks the availability model.

### What we lost

So, Swift is now in the OS! Apps no longer need to embed Swift! A bunch of performance improvements can be made now that the Swift and Objective-C runtimes ship together! And finally, finally, Apple can ship Swift APIs as part of the OS.

And pretty quickly, external Swift contributors found out what Apple’s framework engineers deal with every year:

- To a first approximation, you can never remove anything, only deprecate it, because otherwise existing apps might _fail to launch_ or _[lose user data](https://belkadan.com/blog/2021/11/Swift-Mangling-Regret-The-Old-Mangling/)._
- The release cycle is tied to the OS release cycle. (Swift’s release cycle had always been tied to Xcode’s, which was bad enough, but OSs are even bigger “vehicles” for change and so it’s harder to change their course even if you really think it’s necessary.)
- And the main prompt for this post, **new APIs are only present in the new OS.** (And to add insult to injury, they must therefore all be annotated with availability.)

This last is a problem that Go doesn’t have, that Rust doesn’t have, and that Swift 1-4 didn’t have, and it’s all for the same reason: these languages ship(ped) their standard libraries with the app that uses them. They’re not part of the OS, and consequently there’s way less motivation to have a stable ABI and support library evolution at all (and they don’t).

We (Apple) tried to [manage all these expectations](https://www.swift.org/blog/abi-stability-and-apple/) at the time of the changeover. But it really is a trade-off, and so in the years following Swift-in-the-OS Apple and the Swift team have come up with a few techniques that support some common backwards-deployment scenarios:

- Specific functions can be marked with a not-yet-supported attribute to have them copied into clients instead of referenced by symbol name, much like a C `static` function defined in a header file. This only works for things like functions, methods, etc that don’t need _identity,_ though; if the same implementation were used with a global stored variable, you’d end up with multiple copies of the global. And it also only works when the implementation is compatible with both past and future versions of the APIs it uses in turn. (There have been actual bugs around this.)
- Some Apple libraries are deliberately _not_ shipped with the OS; you can choose to embed them in your app like third-party dependencies. [ResearchKit](http://researchkit.org) was one of the earliest of these, made even before Swift was part of the OSs.
- In certain cases, the Swift team includes a “compatibility” library that’s linked in to the _main app only_ (so that there’s exactly one) to bring some of the older OS’s support up to date. These sometimes use “customization points” in the runtime where we knew things might change, and sometimes use awful hacks relying on implementation details of the older runtime or OS (a practice that’s _slightly_ better for Apple to do to itself rather than for external developers to do, because Apple can promise itself it won’t change an older OS version any further).

None of these are perfect, however. There’s no standard mechanism to “backwards-deploy-if-needed” additions to the standard library and other Swift libraries in the OS (something that could be tricky if multiple targets in your app tried to be responsible for it), and backporting _modifications_ may be even harder. What if your new feature is a generic function that depends on a protocol that didn’t exist last year? What if the protocol _did_ exist but some of the types you want to use with the new feature didn’t adopt it until this year?

Swift was _required_ to be a language that you can define OS libraries in, and that automatically makes a bunch of things harder. This is where that knee-jerk reaction comes from: being an OS library developer is harder than being a third-party library developer (or an OS-internal-only library developer!). But that’s something that should be understood as a trade-off, and it’s valid to weight the sides of the trade-off differently, especially when some of the negatives [show up nearly every year](https://forums.swift.org/t/build-time-sdk-availability-check/59679) given how Apple does things.

### Alternatives

There are some reasonable things Apple could have done, or still could do, to improve the situation for developers. _Will_ Apple do them? Maybe, maybe not.

#### Library Deduplication

When fifteen different apps on your phone all use the same open-source library, they’re all going to use it a little differently. Maybe they have different build settings, maybe they made local modifications. But if they all use the same _closed-source_ library, and it’s a _dynamic_ library, Apple could _in theory_ deduplicate those libraries on disk, saving the end user some space. Code signing makes this trickier, but I don’t think it’s impossible, since (if I recall correctly) the App Store already re-signs all the libraries in your app bundle. This _definitely_ applies to the Swift compatibility libraries, and I even remember vague discussions of implementing this, so it might even have happened. But it wouldn’t change the listed download size for any app in the store (because you wouldn’t want that to change based on what else you have installed, unless perhaps it’s from the same developer), and for first-party libraries it only ever applies when backwards-deploying, which automatically makes it less interesting to Apple.

This also doesn’t really work on macOS, where apps aren’t 100% managed by the OS, but macOS is also the Apple platform where you’re least likely to care about code size problems on a per-app basis.

#### Explicit “polyfill” support

“Polyfill” is a term that arose in the land of web development to backport features to earlier browsers as well as paper over differences between browsers. In JavaScript this is easier because you can check whether a feature is present before installing your own implementation, something that you can do in Objective-C a bit clunkily, and that you can’t do in Swift at all. (The difference between “compile time” and “run time” makes this all more complicated for ObjC and especially for Swift.)

More common in ObjC _and_ Swift is adding a method that looks like this:

```
func backportFoo() -> String {
  if #available(iOS 16, *) {
    return foo()
  }
  // Fallback implementation
  return "foo: \(self)"
}
```

This gets trickier when you’re wrapping a _type_ rather than an _operation,_ but it’s usually still possible with a protocol, or sometimes a base class where one implementation defers to the OS and the other is for backporting. It would be nice™ if Swift explicitly supported this, but it’s an _extremely_ tricky feature to design, very much subject to the “[what if two people did this](https://devblogs.microsoft.com/oldnewthing/20050607-00/?p=35413)” problem. When people do it ad hoc like this, it’s at least clear what the behavior is for users of this workaround, because the workaround doesn’t have anything to do with the non-backport API as far as the language is concerned.

#### Explicit backwards-deployment support

Rather than a third-party “polyfill” approach, or an explicit wrapper function, wrapper type, or abstracting protocol, Swift could just make it easier for _the standard library_ (and other Swift libraries that are part of the OS) to support backwards-deploying new features by bundling them with the app “as needed”, and similarly loading them “as needed”. This is tricky because it means any client code has to now work two different ways (again, we can’t play the rpath trick for new features in an existing library). I don’t want to make this sound straightforward or easy to implement because it wouldn’t be, but I believe it’s _possible._ (For a taste of what this would take, check out an older post of mine, “[Backwards-deployable Conformances](https://forums.swift.org/t/backwards-deployable-conformances/29876/10)”.)

Android actually does do this fairly often, at least with its Java APIs. It’s a bit easier to set up because its apps and libraries use an intermediate format rather than native code, and also because Java doesn’t have extensions and therefore there are fewer ways to modify existing types. They call this “[desugaring](https://developer.android.com/studio/write/java8-support)”.

#### ABI Stability without Swift-in-the-OS

A final possibility is that Apple could have committed to Swift’s ABI stability, but not actually put Swift in the OS. Any closed-source Swift libraries Apple wanted to ship would be made available for embedding in each app that wanted to use them, possibly augmented with the “deduplication” strategy mentioned above. But Apple _wants_ to be able to update their libraries as part of OS releases, as well as security updates. It’s this capability that allows them to do system-wide UI adjustments and redesigns without forcing everyone to publish new versions of their app ahead of time and with relatively minimal conditionalizing even after the fact. You can argue whether or not you think that’s a good thing, but it’s something Apple won’t ever give up.

### Conclusions

_Was_ Swift-in-the-OS a bad trade-off for app developers? Maybe, if you’re not pressed for code size.[4](#fn:code-size) But then Apple wouldn’t have been able to write system libraries in Swift, and that was never an option.

P.S. Swift on Windows is still a young project, and it doesn’t have the same OS library concerns that Apple platforms do…but Windows is also home to many more closed-source third-party libraries than Linux is. So there’s a possibility [we’ll have a platform with ABI stability but _without_ Swift-in-the-OS](https://forums.swift.org/t/question-is-swift-abi-stable-on-windows-how-far-are-we-from-there/59601) in the not-too-distant future.

#### EDIT: Little of this is new to Swift

A lot of what I’ve talked about is a consequence of _libraries being shipped with the OS._ Notably, Objective-C used “[ARCLite](https://bignerdranch.com/blog/illuminating-arclite/)”, a compatibility _static_ library “linked into the main app only” as described above, to carefully support backwards-deployment of several new language features, but some were still limited to the latest OS versions (thanks, [Nick](https://twitter.com/nicklockwood/status/1579354730807328770)). More generally, Apple has never supported backwards-deployment of new features added to _Foundation,_ effectively “the stdlib of Objective-C” on Apple platforms. People have never been happy about that either, but there was also no concerted push to “fix” it.

What changed with Swift? There’s a technical change, where the balance between “compile time” and “run time” is more on the “compile time” side compared to Objective-C. But I really think the biggest changes are social, not technical:

1. The Swift stdlib is part of an open source project, while Foundation isn’t.
2. There were several years where Swift behaved like a third-party dependency rather than an OS library, and thus had fewer constraints. (This is what most of this post focuses on, trying to convince you that there’s not much point in being nostalgic for that.) Swift on non-Apple platforms still works like this, so the sentiment never quite goes away.
3. Due to Apple’s OS release schedules, for the last several years there’s been an Xcode that contains a New Swift Compiler with an Old Mac SDK, and thus an Old Swift Stdlib. That’s a [compatibility hazard for the Apple Swift team](https://forums.swift.org/t/clarification-needed-on-unsafecontinuation-documentation/57803/16), because their compiler has to support both SDKs for a bit (maybe the old stdlib had bugs!), but it’s also frustrating for developers who now have to distinguish between Swift _language_ changes and Swift _stdlib_ changes. This could have happened with Objective-C as well, but Clang and Foundation don’t share version numbers, so it’s less in-your-face about it.

Is that convincing? That’s up to you. But supporting updateable OS libraries _and_ backwards-compatibility is Difficult, and it should come as no surprise that forward-looking, “everybody update to the latest OS” Apple prioritized the former over the latter.

1. When [Go](https://go.dev) first came out, it made direct system calls on macOS to avoid dynamic linking. Apple told the Go people that this was unsupported, and indeed, in the next major release of macOS the system call interfaces changed. The Go project had to quickly put out a new release that conditionalized their system calls based on the OS version, and eventually they switched to the Apple-recommended use of the C standard interfaces instead.

  Should Apple have changed course to match Linux here, knowing that changing their kernel interfaces would break existing programs? Hard to say. “Not all change is progress, but all progress is change”, and compatibility restricts change pretty much by definition.

  This is a larger discussion with no perfect answer, so I won’t get into it more here. [↩︎](#fnref:go)
2. iOS doesn’t allow JITs by default for security reasons; the built-in JavaScript JIT is the main exception. I didn’t see this as a huge downside because JITs _do_ have a battery life cost (remember the Swift project started more than ten years ago), but some of my coworkers were more optimistic about JITs than I was, in particular because a JIT can optimize across the OS library / app client boundary without having to worry about forwards- or backwards-compatibility. Maybe it’ll still happen someday, but I’m not holding my breath; more likely there will be other sorts of small targeted tricks that work across ABI boundaries. [↩︎](#fnref:jit)
3. The system team later got mad at us because they were trying to phase out subdirectories of `/usr/lib`. Oops. But I think we could have convinced them it was worth it, because we wouldn’t want an app’s rpath to find any _other_ libraries in `/usr/lib/` just because they depended on Swift.

  Also, I know I marked the releases as “iOS” in the diagram but used Finder icons for the OS library. It’s fine, don’t worry about it. [↩︎](#fnref:usr)
4. Swift also doesn’t always have the most compact native code, at least partly because of its very dynamic generics model that doesn’t require that values have a uniform representation, followed by compile-time specialization that can make an extra, more optimized copy of a function. Objective-C, by contrast, has uniform representations and very few compile-time optimization opportunities, so code size is chunkier than C might be but is otherwise pretty uniform. This is another case where Swift was very ambitious and achieved some extraordinary flexibility, but may have paid the price in other areas. Fortunately, there _are_ still improvements that can be and are being made here even without breaking ABI. [↩︎](#fnref:code-size)

This entry was posted on [October](https://belkadan.com/blog/2022/10) 09, [2022](https://belkadan.com/blog/2022) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Apple](https://belkadan.com/blog/tags/apple)
