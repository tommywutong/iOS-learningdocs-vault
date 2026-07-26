---
title: Swift 4.1
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/04/swift-4-1/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:72751f67a486db7e'
translated: false
---

> 原文：[Swift 4.1](https://oleb.net/blog/2018/04/swift-4-1/)　·　Ole Begemann

# Swift 4.1

[Swift 4.1](https://swift.org/blog/swift-4-1-released/) has been out for a month, so I’m late to the party with this, but I wanted to point out what a significant step forward this release is for Swift.

# Conditional conformance

Even if you never write a [conditional protocol conformance](https://swift.org/blog/conditional-conformance/) yourself, having a more powerful type system is a huge deal for the standard library and other libraries. Users of these libraries don’t have to know or care about conditional conformance — for them, it simply means less frustration because more things that inexplicably didn’t work before now work as expected.

For example, you can now assert that two sets are equal in a unit test:

```
let intersection = Set(5...15).intersection(0..<10)
XCTAssertEqual(intersection, Set(5..<10))
```

This is how it always should have been. In fact, this stuff is so fundamental that in a few months we’ll probably wonder how we could get any work done in a language which didn’t support the most basic things.

# Recursive constraints on associated types

The same goes for the second new generics feature, [recursive constraints on associated types](https://github.com/apple/swift-evolution/blob/master/proposals/0157-recursive-protocol-constraints.md). _Of course_ the [subsequence](https://developer.apple.com/documentation/swift/sequence/1641117-subsequence) of a [`Sequence`](https://developer.apple.com/documentation/swift/sequence) should itself be a `Sequence` (and have the same element type). But until now, this constraint could not be expressed in the type system.

For example, this simple method for dropping the first and last element of a sequence wouldn’t compile in Swift 4.0:

```
extension Sequence {
    func dropFirstAndLast() -> SubSequence {
        // error: Value of type 'Self.SubSequence' has no member 'dropLast'
        return dropFirst().dropLast()
    }
}
```

![Screenshot of Xcode 9.2 (Swift 4.0) showing a compile error](https://oleb.net/media/swift-4-0-extension-error-missing-constraint.png)

<sub>Error in Swift 4.0 because the compiler doesn’t know that the `SubSequence` returned by `dropFirst` is a `Sequence`.</sub>

Only when you explicitly constrain the extension to sequences whose subsequence is also a sequence _and_ whose subsequence’s subsequence type _is_ the subsequence type (another thing which is also valid for all sequences, but the compiler didn’t know that) is the compiler satisfied:

```
extension Sequence
    where SubSequence: Sequence, SubSequence == SubSequence.SubSequence
{
    func dropFirstAndLast() -> SubSequence {
        return dropFirst().dropLast()
    }
}
```

![Screenshot of Xcode 9.2 (Swift 4.0) compiling successfully after adding explicit constraints](https://oleb.net/media/swift-4-0-extension-explicit-constraint.png)

<sub>After adding explicit constraints it compiles in Swift 4.0.</sub>

As of Swift 4.1, the definition of the `Sequence` protocol in the standard library already includes these constraints (and others), so the first version compiles just fine.

Again, this is how it should have been all along.

## The `Collection` documentation is finally complete

Incidentally, the recursive constraints implementation also improves how the Swift documentation works in Xcode and on Apple’s website. If you ever (unsuccessfully) tried to find the documentation for [`Collection`’s](https://developer.apple.com/documentation/swift/collection) associated [`Index`](https://developer.apple.com/documentation/swift/collection/2943866-index) type or the [`index(after:)`](https://developer.apple.com/documentation/swift/collection/2943746-index) method in the Swift 4.0 days, you can rejoice now.

The reason these and others were missing was that they were defined on the semi-private `_Indexable` protocol (a crutch the standard library used to work around the missing recursive constraints) and Apple chose to hide underscored members from the documentation. In Swift 4.1, `_Indexable` is gone because it’s no longer needed. Its requirements have been merged into `Collection`.

# `IndexDistance` is gone

Taken together with a third change — [the associated `IndexDistance` type has been removed from `Collection`](https://github.com/apple/swift-evolution/blob/master/proposals/0191-eliminate-indexdistance.md) — Swift 4.1 massively simplifies the writing of generic collection algorithms.

Up until Swift 4.0, extending `Sequence` or `Collection` with a new algorithm was too often an exercise in frustration. Deciphering the compiler’s error messages and adding the right missing constraints required a lot of knowledge of the generics system’s limitations.

With Swift 4.1, most extensions should now be a lot more straightforward to write. If you’ve added your own collection algorithms directly on [`Array`](https://developer.apple.com/documentation/swift/array) until now in order to not have to deal with `Collection`, I encourage you to try again. Even better, if you have a collection algorithm that you think is universally useful, [pitch it on the Swift forums](https://forums.swift.org/c/evolution/pitches) for inclusion in the standard library!

# Wrap-up

Swift’s generics system makes a big step forward with Swift 4.1. That doesn’t mean it’s finished though. In fact, there’s at least one more pesky error that I’d love to never see again:

> ‘X’ can only be used as a generic constraint because it has Self or associated type requirements

The associated generics feature is called [_generalized existentials_](https://github.com/apple/swift/blob/master/docs/GenericsManifesto.md#generalized-existentials).

## Doug Gregor and Ben Cohen on Swift Unwrapped

This post is more or less a rehash of things said by Swift team members [Doug Gregor](https://twitter.com/dgregor79) and [Ben Cohen](https://twitter.com/AirspeedSwift) on the [Swift Unwrapped podcast](https://spec.fm/podcasts/swift-unwrapped). Doug and Ben were guests on the podcast for two episodes in March 2018 and discussed Swift 4.1. It’s a great conversation and you should listen to it: [part 1](https://spec.fm/podcasts/swift-unwrapped/125759), [part 2](https://spec.fm/podcasts/swift-unwrapped/125760) (50 minutes in total).

I leave you with a quote from Ben (paraphrased):

> With Swift 4.1 the generics system has reached its first important plateau. A lot of the generics features that have been anticipated since the very beginning of Swift are now coming into the language. And that’s been really important for the standard library because a lot of the standard library _has been designed with these features in mind from the very beginning_.
