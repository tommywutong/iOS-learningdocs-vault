---
title: 'Article updates, 2018 edition | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/updating-for-2018.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:c325a693b26ef980'
translated: false
---

> 原文：[Article updates, 2018 edition | Cocoa with Love](https://www.cocoawithlove.com/blog/updating-for-2018.html)　·　Cocoa with Love (Matt Gallagher)

Over the last month or two, I’ve been slowly updating Cocoa with Love Swift projects and articles to Swift 4.2, Xcode 10, iOS 12 and mac OS 10.14. In a year without any massive new features or obvious changes to Swift, it’s been a lot of work.

After a quick look at pain points in moving to Xcode 10’s new build system, this article will largely be a log of changes to Cocoa with Love content, in reverse chronological order, as I go back through all my Swift articles and make sure everything’s in order.

## Xcode 10’s “new build system”

Xcode’s “new build system” was quietly included with Xcode 9 but in Xcode 10, it becomes the default build system. This means that it can’t really be ignored anymore.

Unfortunately, there are enough new requirements in the new build system that it has caused issues with most non-trivial projects I work on.

> **I don’t want to know that there is a build system**: I want to create a project from a template, write code, hit Command-R and immediately see the program I wrote. Any time I become aware that there is a “build system”, it’s because my wishes have been denied and I’m already frustrated and angry.

My builds are not complex but most of my projects have build products that require inclusion/exclusion/modification based on the selected build scheme (mock service and debug testing frameworks, release configuration files). And most open source projects have to play nicely with multiple package managers – changing paths or other settings based on environment variables. Unfortunately, these situations require “script” build steps – and suddenly, I’m acutely aware of my build system and everything that isn’t working.

### Aspects of the build system that frustrate me

A few points about the “new build system” (does it have a catchier name?) stand out since they’ve caused multiple problems:

1. Input xcfilelists can’t be missing on first run
2. No two build phases in the entire workspace may generate the same output file
3. further modify the file
4. It’s important to be accurate when specifying input and output files of a build phase
5. Xcode implicitly and aggressively creates folders in the products directory if a build step declares a subpath as an output
6. on the command-line to build to the same directory as an Xcode build that may have triggered it
7. If any input files are touched during a build, the build is cancelled

I’m not saying that these rules don’t make sense – most of them do make some sense – but they are all new requirements or rules and not all of them produce clear errors; you might just get stale or partially processed data appearing in your products directory.

The one that feels the most frustrating – because it seems so unnecessary – is point 1. I want to be able to dynamically generate the list of input or output files for some build steps but it can’t be cleanly done. The input and output files must exist before any build step has run, so you can’t dynamically generate it (even though you can dynamically _update_ it).

Point 2 – no two build phases in the entire workspace may generate the same output file – might seem like a minor problem but it has broken many of my own projects and my dependencies. I previously had multiple targets – dynamically selected – that generated the same file in different ways based on build conditions but it’s no longer allowed. I’ve also had projects that built outputs using custom build script phases but also included their project files for editing and debugging ease but this no longer works.

Points 3, 4 and 5 break a surprising number of build script steps. The new build system may overwrite and replace files in the build products directory without warning. Any modifications should be made in the intermediates directory. Get the dependencies wrong though and any output that needs multiple processing step will go subtly wrong on a regular basis.

Points 6 and 7 might not matter to anyone but me but they eventually led to me giving up on some of my more elaborate build shenanigans. In particular, see the [Package Manager Fetch](#package-manager-fetch-deprecated) section, below.

## CwlViews

While it might seem strange to have an update for a library I haven’t yet released, the reality is that I’ve already written two articles using this library:

- Model-View-Controller without the Controller
- A view construction syntax

I’ve updated both of these articles to reflect the latest builds of CwlViews. In fact, the code for each article now includes full implementations of the iOS CwlViews code in a “concatenated” arrangement (the code for CwlViews is concatenated into 4 files which are dropped into the projects instead of requiring frameworks or dependencies).

I’m still working on some project templates for CwlViews (so starting quick projects is simpler) and I’m trying to set up some integration testing in library itself (refactoring passes have broken my old code for this) and once that’s in place, I’ll release the the whole project.

## CwlLayout

I first released the CwlLayout code as a Swift playground in [CwlLayout: a Swift wrapper around Auto Layout](https://www.cocoawithlove.com/blog/cwllayout.html).

Since its initial release, I’ve updated the CwlLayout to fix a range of bugs and potential layout problems, simplify the syntax slightly and improve the flexibility of views constrained to have the same length. I’ve also added basic animation support so that you can animate to layouts instead of merely applying them.

I’ve updated the playground and the article with these changes. Moving forward, the official location for this code will be as part of the CwlViews library (this playground will receive only periodic updates).

## compactMap

My article titled [Statements, message and reducers](https://www.cocoawithlove.com/blog/statements-messages-reducers.html) used the old `flatMap` function – the one that got renamed in Swift 4.1 to `compactMap`. Obviously I updated that article but the _next_ article, previously titled “An aside about flatMap” no longer made sense since it was entirely about how one `flatMap` in the standard library was not like the others.

So I’ve gone and done something weird and almost totally rewritten an old article. The new version is named [About flatMap, compactMap and monads](https://www.cocoawithlove.com/blog/an-aside-about-flatmap-and-monads.html).

I don’t know if anyone’s going to read a rewritten article but I’m really happen with it. Where the old article had clunky diagrams and rushed its explanation, I think the new article looks really good, takes its time and manages the make all the important points about unwrapping, abstractions, side-effects and information hiding.

## MVC

There was no code in my [Looking at Model-View-Controller in Cocoa](https://www.cocoawithlove.com/blog/mvc-and-cocoa.html) article but I updated all of the diagrams.

Previously, diagrams on Cocoa with Love haven’t had any particular theme or aesthetic. My diagrams were drawn in a range of different programs using a range of different styles. I’ve been trying to tidy things up so while redoing the diagrams for the `compactMap` article, I also redid the diagrams in this and other articles.

Not that these things matter to anyone else but sometimes, I need a little personal pride in my work.

## Package manager fetch (deprecated)

I’ve [previously written about using `swift package fetch`](https://www.cocoawithlove.com/blog/package-manager-fetch.html), later `swift package resolve`, in build script steps to dynamically resolve project dependencies and build them using `xcodebuild` without requiring a separate package manager. While I was able to migrate this approach to Xcode 10 – [see the Sep 30 commit for CwlSignal](https://github.com/mattgallagher/CwlSignal/tree/3d6c6d11171f93dd52d6b827da2775c9c79ba64d) – the increased fragility, the constant effort and the compromises required made me abandon the whole approach.

The biggest point that frustrated me was that it is not really possible for a project like CwlSignal to build a dependency, like CwlUtils, using a custom build script phase and also include the CwlUtils project file. The new build system will complain that CwlUtils.framework can be built two different ways (through the project file and through the build script phase) even though only one of those approaches is directly referenced.

Without project inclusion, debug symbols are difficult to maintain, jump to definition never works at all and maintaining both a dependency and a depender is an annoying process.

For this reason, I’ve reverted the interdependent Cocoa with Love projects CwlSignal, CwlUtils, CwlPrecondition (and the upcoming CwlViews) to using git subtrees for their dependencies.

If you don’t know about git subtrees, you can [read about subtree merging in the git book](https://git-scm.com/book/en/v2/Git-Tools-Advanced-Merging) but basically, you check out a completely separate repository into a separate branch and subfolder of a parent repository then merge its latest state into the parent repository’s master branch. Subtrees have an advantage that submodules and third party dependency managers don’t have: everything works seamlessly for the user with little more than a zip file of the git repository. Since you can reference your dependencies directly in the checkout, you can also build an Xcode project where debugging and definition symbols work smoothly.

It’s a little fussier to update repositories without help from additional tools. And it is a very _bad_ idea to perform a git rebase across a subtree merge (the subtree changes may get merged at the root of the repository instead of in the subtree’s directory). But until Xcode integrates properly with the Swift Package Manager (it’s shameful how long this is taking) it’s the least terrible option.

## Mines (obsoleted)

I wrote an article about [Compiling a Mac OS 8 application on macOS Sierra](https://www.cocoawithlove.com/blog/porting-from-macos8-to-sierra.html). With i386 deprecated in Xcode 10, this project doesn’t compile anymore. I don’t feel any need to port this code to 64-bit – it was momentary nostalgia and isn’t really practical for anyone moving forward.

## Key-Value Observing (deprecated)

**Ouch**, three deprecated or obsoleted articles in a row. Better to clean things out and make way for new stuff! 😁

While my [key value observing wrapper](https://www.cocoawithlove.com/blog/key-value-observing-wrapper.html) still works, I’m deprecating it in CwlUtils. My original motivation for this class was to provide observation handling through closures and provide automatic lifecycle management.

Swift 4 changes to key-value observing provided handling through closures and automatic lifecycle management at the observer end. More importantly though, Swift 4 replaced string-based key-paths with type-checked key-paths. Suddenly, my string-based approach ceased to have much appeal.

While I liked the `reason` parameter that my class offered for notifying whether the path broke, the target deallocated or the value truly changed, this isn’t enough to justify continuing to use string key-paths. Use Swift `KeyPath` instead.

## Reactive programming

My article [What is reactive programming and why should I use it?](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html) was similarly affected by changes to Swift’s key value observing. I had an entire example that showed the old key-value observing callback function and talked about how clunky it was.

Swift’s new key-value observing is aesthetically much better so I had to refactor the example to highlight the other advantages of reactive programming.

I had never previously shared the code for the non-reactive examples. This makes it harder for people to perform one-to-one comparisons. So I’ve added all the non-reactive code to a playground in the [Cocoa with Love Playgrounds project](https://github.com/mattgallagher/CocoaWithLovePlaygrounds). The three pages in this playground implement the same logic that the CwlSignal playground pages implement and run the same example scenarios.

## CwlSignal

I’ve continually worked on CwlSignal [since its original release](https://www.cocoawithlove.com/blog/cwlsignal.html). I’ve recently tagged the repository with a version 2.0.0 tag and I’ll try a little harder to avoid breaking changes in the near future.

### Interface and feature changes

Since version 1, there have been lots of bug fixes, refactoring and improvements, including:

1. improved Rx operator compatibility
2. for easier input and output construction in a single expression
3. to

  (for symmetry with

  )
4. to

I’ve added `withLatestFrom` implementations, matched the on-error behaviors of Rx a little more closely and added `just`, `empty` and a couple other common transforms from Rx. I have no intention of making CwlSignal into an RxSwift clone – they are based on some very different principles – but I would like the _transformations_ between stages of the two to be comprehensible between users of both frameworks.

The `SignalChannel` type is an extremely handy way to declare a `SignalInput` a full transformation pipeline and the `SignalOutput` all on a single line:

```swift
// without `SignalChannel`
let (input, signal) = Signal<Int>.create()
let output = signal.map { $0 * 2 }.subscribeValues { print($0) }

// with `SignalChannel`
let (input, output) = Signal<Int>.channel().map { $0 * 2 }.subscribeValues { print($0) }
```

The `SignalChannel` type is literally just a pair of `input` and `signal` values that you can transform like it’s just a `signal` until you get to a `subscribe` at which point, the both ends are returned.

Renaming `SignalEndpoint` to `SignalOutput` is intended to clarify its role. I originally avoided the `SignalOutput` name and used `SignalEndpoint` instead because the implementation is so different to `SignalInput` so I didn’t think a symmetrical name was appropriate. However, a signal pipeline has a start, middle and end:

- at the start
- and transformation closures
- values are emitted at the end of the graph through…

…the `SignalOutput`.

Renaming `Cancellable` to `Lifetime` is a bit more experimental. In either case, the name is used for implementations of the [Dispose pattern](https://en.wikipedia.org/wiki/Dispose_pattern). I could call it `Disposable`, like C# and other libraries. However, to me, `Disposable` is too tightly associated with garbage collection and `C#`’s memory management, so I’d rather use a different name. The protocol requires just one function – `cancel()` – so the old `Cancellable` name seemed appropriate. However, the protocol _implies_ much more than the existence of the function. Most importantly, holding onto the instance preserves the _lifetime_ of an ongoing asynchronous task, hence the name change. It is not without president in Swift since `withExtendedLifetime` operates on the same “lifetime” premise for scoped values. Oh, and `Cancellable` is really cumbersome to pronounce.

### Build and performance

The first release of CwlSignal included copies of Result, ExecutionContext and Cancellable in the same project. I’ve since moved these files into the CwlUtils framework. I think this more modular approach is cleaner, and better for most use cases but it is 30-50% _slower_ in narrow test cases that hammer the core “send” functions since Swift doesn’t inline between frameworks.

As an alternative, to the default build arrangement, you can build the CwlSignalConcat target in the CwlSignal project, open the the build products directory and copy the contents of the “Concat_internal” folder (a CwlUtils.swift and CwlSignal.swift file) directly into your project. Since this approach places all the code directly in your project’s module, it is heavily inlined and up to 50% faster in some cases. Of course, this runtime performance comes at the cost of slower Release compilation speed.

## CwlUtils.DebugContextCoordinator

The [Testing actions over time](https://www.cocoawithlove.com/blog/testing-actions-over-time.html) article contained variations on a `TimeoutService` that had fallen badly out-of-date. I’d been maintaining a version of this code in the CwlSignal playground but I had never propagated these changes back to the original.

I rewrote the core example and then a lot of the article required minor text changes to reflect the updated code.

## CwlUtils.Deque

In my article [Optimizing a copy-on-write double-ended queue in Swift](https://www.cocoawithlove.com/blog/2016/09/22/deque.html), I looked at trying to optimize a collection using `ManagedBuffer`.

All of the timing values had changed in this article. I reran them. I also checked to see if Swift had fixed the annoying closure capture that forced an ugly work around for performance reasons (no, it hasn’t).

## CwlWhitespacePolicing

[Updated the project for this article](https://www.cocoawithlove.com/blog/2016/06/25/policing-whitespace.html) to Swift 4.2. The compiler pointed out a number of `switch` cases that couldn’t be reached. Better diagnostics. Neat!

## CwlUtils.PThreadMutex

I’ve changed computers so [all the numbers have changed in this article](https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html) but that’s not the only thing that has happened.

While everything runs 30-50% faster on my MacBookPro15,1 versus my old MacPro4,1 – the `DispatchQueue.sync` performance has gotten 5% _worse_. I don’t know why but I guess it is due to additional priority handling (which none of the other mutexes handle).

The article includes a number of different variants (sync_2, sync_3, sync_4) that pass parameters to the mutex in different ways, trying to avoid closure capture. In the original article, these parameter passing variants were slightly slower as passing parameters incurred reference counting overheads. In Swift 4.2, all of these overheads appear to be gone. Somewhere between Swift 3 and Swift 4.2, reference type parameter overheads have _vastly_ decreased as the compiler is able to avoid reference counting in more cases.

## CwlUtils.RandomNumberGenerator

Since I originally wrote [this article](https://www.cocoawithlove.com/blog/2016/05/19/random-numbers.html), Swift has incorporated its own `RandomNumberGenerator` protocol, rendering my very similar `RandomGenerator` unnecessary. So I’ve rewritten the article to omit discussion of the protocol itself.

I’ve replaced the xoroshiro128 algorithm with the xoshiro256 algorithm since some potential issues with the former have been discovered.

I’ve rerun all the performance tests. Most tests are 30-50% faster on my MacBookPro15,1 but curiously, the new `arc4random` implementation, Swift’s `SystemRandomNumberGenerator`, is **4 times slower**. I don’t really know what’s going on there but I assume it’s due to a switch in the internal algorithm that happened in macOS Sierra.

## CwlDemangle

[Brought the implementation for this article](https://www.cocoawithlove.com/blog/2016/05/01/swift-name-demangling.html) up to date with all the latest Swift 4.2 demangling test cases. There will definitely be more work as Swift 5 approaches and then this little library might finally see some stability.

I’ve previously added a note to that article that the comparison between Swift and C++ involved the 2016 version of the Demangle.cpp file. Since then, the C++ version has slightly improved performance and started incorporating more C++11 syntax and less C macros (both significant changes for the better). I choose to believe that my criticism encouraged the refactoring – although, frankly, the old C++ `demangleImplConvention` function was bizarre enough and bug prone enough that it likely encouraged refactoring on its own.

## CwlUtils.Sysctl

I’ve made a number of updates to [my Sysctl wrapper](https://www.cocoawithlove.com/blog/2016/03/08/swift-wrapper-for-sysctl.html) over time. The original interface, while better than using `sysctl` directly, was clunky if you had to use the raw data functions. The updated `data(for:)` and `string(for:)` functions are a lot nicer – although this is a breaking change.

I’ve also tidied up a few properties that were not truly available on iOS (even though they succeeded in the simulator).

## Conclusion

Scorecard:

- 28 out of 39 Swift articles updated
- 1 article entirely rewritten
- 23 diagrams redrawn
- 11 different git repositories updated
- 2 articles were deprecated
- 1 article was obsoleted

Code maintenance is a drag but with all this out of the way, maybe I’ll finally get some new development done. Maybe?
