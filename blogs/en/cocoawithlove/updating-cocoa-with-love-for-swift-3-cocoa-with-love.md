---
title: 'Updating Cocoa with Love for Swift 3 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/09/14/updating-cocoawithlove.html'
original_language: en
published: 2016-09-14
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:8c830aa5c9244948'
translated: false
---

> 原文：[Updating Cocoa with Love for Swift 3 | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/09/14/updating-cocoawithlove.html)　·　Cocoa with Love (Matt Gallagher)

[Swift 3 was officially released this week](https://swift.org/blog/swift-3-0-released/). That’s exciting, right?

Maybe it will be, eventually. In the short term, it means everything old is broken. I’ve gone back through all Cocoa with Love Swift articles and updated them all to Swift 3 and iOS 10/macOS 10.12 – both the article text and the code on github.

Hooray for tedious housekeeping! This is what it’s like to be a code owner.

> **NOTE**: This article documents the 2016 update from Swift 2 to 3 but I’m not going to update the update, even though, as of October 2018, all Swift articles on Cocoa with Love are updated to Swift 4.2.

## Introduction

This article is my response to the question of the week: “how much work is involved in migrating to Swift 3?”

I don’t precisely know how long I’ve spent on Cocoa with Love updates. Over successive Swift 3 betas, I’ve spent about a week updating the code in my own Swift projects (including Cocoa with Love and a half dozen other projects). It’s clear that the actual answer for a given project is that the time taken will depend on which APIs you’re using.

AppKit, UIKit and Foundation APIs that have simply been renamed are pervasive (30% of all lines changed is entirely possible) but Xcode will largely auto-convert to them to the new names so the amount of work involved is low.

Renaming your _own_ functions to match the new Swift naming conventions is a harder problem. It’s not mandatory at all but there’s potentially a lot of work involved here if, like me, you find traditional Objective-C naming is a difficult habit to break.

There have also been a few major APIs (Dispatch, pointers, strings) where the changes are more complex than simply a renaming. This may involve _redesigning_ and can take a while. It really depends how you previously used these APIs as to whether or not this ends up a large part of your time.

Then, of course, Swift 3 is hitting at the same time as iOS 10 and macOS Sierra. Moving to Xcode 8 will usually involve solving both compatibility problems at once.

The rest of this article is a look at the main changes I made to each article to bring Cocoa with Love up to date. If you’d prefer to look at the code diffs, you can look at the “Cwl*” projects on [my github page](https://github.com/mattgallagher) and compare the “master” branches (which are now merged with the “swift3-prelease” branches) with the “swift2.3” branches (I won’t be updating the “swift2.3” branches but they’re there if you need them).

## [A new era for Cocoa with Love](https://www.cocoawithlove.com/blog/2016/01/25/a-new-era-for-cocoa-with-love.html)

Off to an easy start: nothing to update in this one (it was really just a meta post and contained no code).

## [Partial functions in Swift, Part 1: Avoidance](https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html)

Some minor changes to the article but the biggest changes were voluntary so that the function parameters would be more aligned with [Swift API Design Guidelines: Argument Labels](https://swift.org/documentation/api-design-guidelines/#argument-labels).

As an example of this, I changed the following function:

```swift
func divideFiveBy(x: NonZeroInt) -> Int
```

to the more Swift 3 styled:

```swift
func divideFive(by x: NonZeroInt) -> Int
```

in accordance with the idea that the preposition “by” should be used as the parameter name, rather than part of the function name (and, of course, the Swift 3 change that first parameter names are included, by default).

There were a few minor changes to collection indexes due to [SE-0065 A New Model for Collections and Indices](https://github.com/apple/swift-evolution/blob/master/proposals/0065-collections-move-indices.md) but nothing major.

Sadly, despite the collection index changes Swift introduced, there remains a failure to check that `String.CharacterView.Index` is advanced using the correct `String.CharacterView`, so the totally invalid:

```swift
let characterView1 = "👿👿".characters
let invalidIndex = "Unrelated string".characters.index(after: characterView1.startIndex)
print(characterView1[invalidIndex])
```

still runs without a precondition failure and still produces invalid UTF garbage.

## [Partial functions in Swift, Part 2: Catching precondition failures](https://www.cocoawithlove.com/blog/2016/02/02/partial-functions-part-two-catching-precondition-failures.html)

Since this article involved a lot of C-style pointer manipulation, it was significantly affected by:

- [SE-0055 Make unsafe pointer nullability explicit using Optional](https://github.com/apple/swift-evolution/blob/master/proposals/0055-optional-unsafe-pointers.md)
- [SE-0107 UnsafeRawPointer API](https://github.com/apple/swift-evolution/blob/master/proposals/0107-unsaferawpointer.md)

The need to pass unsafe pointers through `withMemoryRebound(to:capacity:)` to recast them had a huge impact on this code. Initially, the code was significantly worse, until I created specialized pointer conversion extension functions on the underlying data structures. The result is much nicer than the original Swift 2 code but only because I was kicked into refactoring by an uncomfortable syntax change. I’d prefer to see a helper function that combines `withUnsafeMutablePointer` and `withMemoryRebound(to:capacity:)` into a single step, in future.

## [Use it or lose it: why safe C is sometimes unsafe Swift](https://www.cocoawithlove.com/blog/2016/02/16/use_it_or_lose_it_why_safe_c_is_sometimes_unsafe_swift.html)

As a follow up to the previous article, it’s unsurprising that the biggest changes here involved the same [SE-0107 UnsafeRawPointer API](https://github.com/apple/swift-evolution/blob/master/proposals/0107-unsaferawpointer.md) changes.

## [Tracking tasks with stack traces in Swift](https://www.cocoawithlove.com/blog/2016/02/28/stack-traces-in-swift.html)

In addition to the Swift renaming and pointer changes that every article so far has required, this one also saw changes from [SE-0016 Add initializers to Int and UInt to convert from UnsafePointer and UnsafeMutablePointer](https://github.com/apple/swift-evolution/blob/master/proposals/0016-initializers-for-converting-unsafe-pointers-to-ints.md).

The biggest difficulty here was that the automatic Xcode Swift 2 to 3 converter doesn’t seem to do a good job with `String.fromCString` to `String?(validatingUTF8:)` conversions, especially when the parameter in Swift 2 was a potentially `nil` `UnsafePointer<CChar>` which, in Swift 3, is an `UnsafePointer<CChar>?` and now needs to be unwrapped before passing as a parameter. It’s not a difficult change to make in code but when you don’t even know _why_ the conversion tool has made a mess out of a particular line of code (because you can’t remember what the line of code was supposed to do) then these things can stop you in your tracks for a few minutes.

## [Gathering system information in Swift with sysctl](https://www.cocoawithlove.com/blog/2016/03/08/swift-wrapper-for-sysctl.html)

More renaming, more pointer shenanigans. No surprises there.

The `case` names for `enum`s are all lowercase now. It’s a change that I fully understand but it’s amazing how automatic things become in programming with reuse. I still keep writing new code with uppercase `case` names and need to go back and change them.

## [Errors: unexpected, composite, non-pure, external.](https://www.cocoawithlove.com/blog/2016/03/17/non-pure-errors.html)

I included the following code sample in the Swift 2 version of this article:

```swift
func secondsSince(previous: NSDate) -> Double {
   let current = NSDate()
   let result = current.timeIntervalSinceDate(previous)
   return result
}
```

This is replaced by:

```swift
func secondsSince(previous: Date) -> Double {
   let current = Date()
   let result = current.timeIntervalSince(date: previous)
   return result
}
```

I want to highlight this example because it points out something that is non-obvious: the “Great Swift Renaming” is not just a renaming. `Date` is an example of a type affected by [SE-0069 Mutability and Foundation Value Types](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0069-swift-mutability-for-foundation.md). In reality, the whole type has changed. Where `NSDate` was an Objective-C wrapper around `CFDate`, the new type is a Swift wrapper, obeying slightly different semantics. You can see the new implementation in the [Date.swift file in the Swift repository](https://github.com/apple/swift/blob/master/stdlib/public/SDK/Foundation/Date.swift).

## [Breaking Swift with reference counted structs](https://www.cocoawithlove.com/blog/2016/03/27/on-delete.html)

So, this one’s a complete write-off.

I’ve added the following note to the top of this article:

> **OUT OF DATE AS OF SWIFT 3**: While it is still possible to have a heap allocated, reference counted struct with cleanup behaviors in Swift 3, it is no longer possible to capture a reference to `self` in a struct method as describedS in this article. The problems detailed in section 2 in this article have been fixed in Swift 3 and the remainder of this article is merely a historical artefact. Don’t worry: you’re better off as a result.

## [Indent with tabs or spaces? I wish I didn’t need to know.](https://www.cocoawithlove.com/blog/2016/04/01/neither-tabs-nor-spaces.html)

This article contained just 3 lines of Swift and didn’t require any updates.

## [Presenting unanticipated errors to users](https://www.cocoawithlove.com/blog/2016/04/14/error-recovery-attempter.html)

Lots of Cocoa renaming. Roughly half of all lines involved at least one change as part of this renaming. However, it was quick and easy: I barely remember doing it.

## [Comparing Swift to C++ for parsing](https://www.cocoawithlove.com/blog/2016/05/01/swift-name-demangling.html)

The most widespread changes were voluntary changes to bring function naming into line with the Swift API guidelines. Most prominently, I changed:

```swift
func matchString(_ string: String)
```

to:

```swift
func match(string: String)
```

There were also plenty of changes from uppercase `case` names to lowercase `case` names.

As a file with heavy use of `UnicodeScalar` there were some impacts from [SE-0130 Replace repeating Character and UnicodeScalar forms of String.init](https://github.com/apple/swift-evolution/blob/master/proposals/0130-string-initializers-cleanup.md).

The change that took the most time was updating the parser itself. Swift 3 adds new parsable elements to the mangled name grammar (including raw pointers and nested generics) and numerous items have changed name or representation (`protocol <>` becomes `Any.Type`, `protocol<A, B>` becomes `A & B`, `ErrorProtocol` becomes `Error`).

## [Random number generators in Swift](https://www.cocoawithlove.com/blog/2016/05/19/random-numbers.html)

This article required a number of updates but for quite different reasons to the other articles so far.

Swift 3 removed `jrand48` so I removed the implementation involving it entirely from the article. Not a big loss but I think it’s strange that Swift is choosing to wholly remove functions, not merely deprecate them.

Second: performance numbers changed across the board so I updated the table in the article. Some tests ran a couple percent faster in Swift 3 compared to Swift 2.3 (although I’m not convinced that the change in /dev/random or `arc4random` performance had anything to do with Swift) and some tests definitely ran slower.

|  | Swift 2.3 (Seconds) | Swift 3 (Seconds) |
|---|---|---|
| `DevRandom` | 123.50 | 113.250 |
| `Arc4Random` | 4.651 | 4.359 |
| `Lfsr258` | 0.872 | 0.717 |
| `MT19937_64` (before my changes) | 0.643 | 0.631 |
| `MersenneTwister` (and MT19937_64 after changes) | 0.517 | 0.533 |
| `Lfsr176` | 0.511 | 0.498 |
| `xoroshiro128plus` | 0.352 | 0.367 |
| `Xoroshiro` | 0.347 | 0.362 |
| `ConstantNonRandom` | 0.221 | 0.211 |

What I did notice is that Swift 3 is _much_ less aggressive about inlining. Where I had previously inlined the Mersenne Twister code into a `withUnsafeMutablePointer` closure as follows:

```swift
withUnsafeMutablePointer(&state_internal) { ptr in
   let state = UnsafeMutablePointer<UInt64>(ptr)
   
   // Mersenne twister "twist" code using `state` here
}
```

I needed to rewrite this with the “twist” code out-of-line to prevent significant performance problems. i.e.:

```swift
let state = withUnsafeMutablePointer(to: &state_internal) {
   $0.withMemoryRebound(to: UInt64.self, capacity: MersenneTwister.stateCount) { $0 }
}

// Mersenne twister "twist" code using `state` here
```

This is horribly memory unsafe, since we need to leak the `state` pointer outside the scope where it is correctly bound. Unfortunately, without this change, performance dropped to 0.622 seconds (more than 16% slower).

I don’t know if these inlining changes were a deliberate choice (inlining is a tradeoff, after all) or an accidental regression. In any case, as a closure-heavy language, I wish Swift offered the ability to _force_ closure inlining.

Even after fixing the inlining issues, my `MersenneTwister` slowed from 0.517 seconds to 0.533 seconds. Curiously, the C implementation that I modified to follow the same steps had exactly the same performance change on my computer. I don’t know what the underlying cause would be there but it might be due to changes in LLVM.

## [Mutexes and closure capture in Swift](https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html)

This article was significantly impacted by [SE-0088 Modernize libdispatch for Swift 3 naming conventions](https://github.com/apple/swift-evolution/blob/master/proposals/0088-libdispatch-for-swift3.md). Specifically, the `dispatch_queue_sync` function has become `DispatchQueue.sync`.

iOS 10 and macOS 10.12 have added a new locking primitive: `os_unfair_lock_t`. This fills the gap left by the problematic `OSSpinLock` so I’ve added mention of it to the article.

I’ve updated all the performance numbers for Swift 3 although they’re largely the same.

## [Parsing whitespace in an Xcode extension](https://www.cocoawithlove.com/blog/2016/06/25/policing-whitespace.html)

This was the first article I wrote using Swift 3 – since it only works with Xcode 8.

However, I’ve heavily updated the code for this article since I first wrote it. Not to fix Swift issues but to fix limitations in the parser itself. What was originally a 600 line parser is now over 900 lines where only a couple hundred lines remain from the original implementation. The approach is largely the same but it’s had some significant revisions to avoid problems policing whitespace across a wider range of code.

## [Exponential time complexity in the Swift type checker](https://www.cocoawithlove.com/blog/2016/07/12/type-checker-issues.html)

I really wish I could say anything in this article had changed but the compiler issues described all remain exactly as is.

The Swift developers have indicated to me that “rewriting the Swift type checker is on their To-Do list” but that list is _very_ long so I have no idea when we’ll see progress in this area.

## [Design patterns for safe timer usage](https://www.cocoawithlove.com/blog/2016/07/30/timer-problems.html)

The fourth Swift 3 beta, containing the new Dispatch API was released the day after I wrote this article. I radically overhauled it immediately to use the new API. However, those changes were made in haste and the parameter names I chose for my functions didn’t use the same nouns as similar concepts in Apple’s own APIs and the parameters were non-sensically ordered. I’ve gone back and made these changes so it all feels a little more coherent.

## [Values and errors part 1 & 2](https://www.cocoawithlove.com/blog/2016/08/21/result-types-part-one.html)

Both of these articles were written after Swift 3 beta 6 (the last major breaking change) and they remain fully functional in Xcode 8.

## Conclusion

One article is a complete write-off. Five articles required no changes at all. Twelve articles required updates ranging from a couple minor fixes to hundreds of fixes to bring them up-to-date for Swift 3. [Over on github](https://github.com/mattgallagher), all my “swift3-prerelease” branches are merged into “master”.

Looking at performance, Swift 3’s performance numbers aren’t dramatically changed for the few cases Cocoa with Love has tested. There are a number of cases that ended up slightly faster but function inlining seems to be reduced in numerous places for reasons I can’t totally understand or cleanly reproduce in simple test cases, and this significantly hurts cases where previously inlined code falls back to capturing closures.

Cocoa API renaming is the most prominent change in Swift 3 but it is mindless and simple – Xcode will do 75% or more of these automatically. Even if Swift 2 code gets included after the initial Swift 3 conversion, fixing is rarely more than “Next Issue” (Command-Apostrophe) followed by “Select” (Return) to choose the Xcode suggested fix.

A bigger burden is the desired (but not required) updating of your _own_ APIs to follow similar guidelines. There’s no help here. As verbose as Objective-C’s naming conventions were, I used them for so long (even in other languages) that I think I’ll require more practice before Swift’s will be instinctive for me.

The most difficult mandatory problem when converting to Swift 3 is when your code uses pointers, string constructors, Dispatch or another API that Swift has rethought, rather than renamed. You can’t ignore these problems, Xcode might not be able to suggest an automatic solution, and you’ll need to simply rewrite whole blocks of code. Best to get your tests in order before you start.

### Looking forward

I hope the goal of source compatibility for Swift 4 and beyond is largely realized but I have no doubt that there will be some minor changes.
