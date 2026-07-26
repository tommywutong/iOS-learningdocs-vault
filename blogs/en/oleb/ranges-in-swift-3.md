---
title: Ranges in Swift 3
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/09/swift-3-ranges/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:6efc209d44640242'
translated: false
---

> 原文：[Ranges in Swift 3](https://oleb.net/blog/2016/09/swift-3-ranges/)　·　Ole Begemann

# Ranges in Swift 3

_This is a short excerpt from the Collections chapter in [_Advanced Swift_](https://www.objc.io/books/advanced-swift/), slightly amended for the blog. [Chris Eidhof](http://chris.eidhof.nl) and I are almost done updating the book for Swift 3 (and improving it in the process). It will be out soon._

A range is an interval of values, defined by its lower and upper bounds. You create ranges with the two range operators: `..<` for half-open ranges that do not include their upper bound, and `...` for closed ranges that include both bounds:

```
// 0 to 9, 10 is not included
let singleDigitNumbers = 0..<10

// "z" is included
let lowercaseLetters = Character("a")...Character("z")
```

Ranges seem like a natural fit to be sequences or collections, so it may surprise you to learn that they _are neither_. At least not all of them are.

In Swift 2, ranges were closely connected to collections. A range’s element type had to be an index type, and ranges themselves were also collections. This model underwent significant changes in Swift 3 as part of [the new collection indexing model](https://github.com/apple/swift-evolution/blob/master/proposals/0065-collections-move-indices.md). Because the old index protocols no longer exist, the only constraint on a range’s element type is now [`Comparable`](https://developer.apple.com/reference/swift/comparable) conformance. And since the range elements now can no longer advance themselves, it follows that `Range` can’t be a [`Collection`](https://developer.apple.com/reference/swift/collection) anymore, at least not without additional constraints. As a matter of fact, the [`Range`](https://developer.apple.com/reference/swift/range) type in Swift 3 is closer in concept to what used to be called intervals in Swift 2.[1](#fn:1)

## Range types

There are now four range types in the standard library. They can be classified in a 2-by-2 matrix as follows:

|  | Half-open range | Closed range |
|---|---|---|
| Elements are [`Comparable`](https://developer.apple.com/reference/swift/comparable) | [`Range`](https://developer.apple.com/reference/swift/range) | [`ClosedRange`](https://developer.apple.com/reference/swift/closedrange) |
| Elements are [`Strideable`](https://developer.apple.com/reference/swift/strideable) (with integer steps) | [`CountableRange`](https://developer.apple.com/reference/swift/countablerange) | [`CountableClosedRange`](https://developer.apple.com/reference/swift/countableclosedrange) |

The columns correspond to the two range operators we saw above, which create a `[Countable]Range` (half-open) or a `[Countable]ClosedRange` (closed), respectively. Half-open and closed ranges both have their place:

- can represent

  (when the lower and upper bounds are equal, as in

  ).
- can contain the

  its element type can represent (e.g.

  ). A half-open range always requires at least one representable value that is greater than the highest value in the range.

## Countable vs. non-countable

The rows in the matrix distinguish between “normal” ranges whose element type only conforms to the [`Comparable`](https://developer.apple.com/reference/swift/comparable) protocol (which is the minimum requirement), and ranges over types that are [`Strideable`](https://developer.apple.com/reference/swift/strideable) _and_ use integer steps between elements. Only the latter ranges are random-access collections, inheriting all the great functionality of the [`Sequence`](https://developer.apple.com/reference/swift/sequence) and [`Collection`](https://developer.apple.com/reference/swift/collection) protocols.

Swift calls these more capable ranges [_countable_](https://en.wikipedia.org/wiki/Countable_set) because only they can be iterated over. Valid bounds for countable ranges include integer and pointer types, but not floating-point types because of the integer constraint on the type’s `Stride`. If you need to iterate over consecutive of floating-point values, you can use the [`stride(from:to:by)`](https://developer.apple.com/reference/swift/1641347-stride) and [`stride(from:through:by)`](https://developer.apple.com/reference/swift/1641347-stride) functions to create such a sequence.

This means that you can iterate over some ranges but not others. For example, the range of `Character` values we defined above is not a sequence, so this won’t work:

```
for char in lowercaseLetters {
    // ...
}
// Error: Type 'ClosedRange<Character>' does not conform to protocol 'Sequence'
```

(You might expect that this should work because stepping through some simple ASCII characters is straightforward. But as we saw in the [article about strings](https://oleb.net/blog/2016/08/swift-3-strings/), Swift’s `Character` type can actually hold complete grapheme clusters and not just a single code point. And that means a character does not necessarily have a well-defined successor anymore. Thanks Unicode.)

Whereas the following is no problem because an integer range is a countable range and thus a collection:

```
singleDigitNumbers.map { $0 * $0 }
// → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Conditional protocol conformance

The standard library currently has to have separate types for countable ranges, [`CountableRange`](https://developer.apple.com/reference/swift/countablerange) and [`CountableClosedRange`](https://developer.apple.com/reference/swift/countableclosedrange). Ideally, these would not be distinct types but rather extensions on `Range` and `ClosedRange` that added [`RandomAccessCollection`](https://developer.apple.com/reference/swift/randomaccesscollection) conformance on the condition that the generic parameters meet the required constraints. It would look like this:

```
// Invalid in Swift 3
extension Range: RandomAccessCollection
    where Bound: Strideable, Bound.Stride: SignedInteger
{
    // Implement RandomAccessCollection
}
```

Alas, Swift 3’s type system cannot express this idea, so separate types are needed. Support for [conditional conformance](https://github.com/apple/swift/blob/master/docs/GenericsManifesto.md#conditional-conformances-) is one of the main goals for Swift 4 (or earlier?), and `CountableRange` and `CountableClosedRange` will be folded into `Range` and `ClosedRange` when it lands.

## Converting between half-open and closed ranges

The distinction between the half-open [`Range`](https://developer.apple.com/reference/swift/range) and the closed [`ClosedRange`](https://developer.apple.com/reference/swift/closedrange) will likely remain, and it can sometimes make working with ranges harder than it used to be. Say you have a function that takes a `Range<Character>` and you want to pass it the closed character range we created above:

```
func doSomething(with range: Range<Character>) {
    // ...
}

doSomething(with: lowercaseLetters)
// Error: Cannot convert value of type 'ClosedRange<Character>'
// to expected argument type 'Range<Character>'
```

Not only isn’t there an automatic conversion between closed and half-open ranges, there appears to be no way to do this at all! But why? Well, to turn a closed range into an equivalent half-open range, you would have to find the element that comes after the original range’s upper bound. And that is simply not possible unless the element is `Strideable`, which is only guaranteed for countable ranges (and countable ranges do provide initializers to convert between the two).

This means the caller of such a function will have to provide the correct type. If the function expects a `Range`, you can’t use the `...` operator to create it. We’re not sure how big of a limitation this is in practice since most ranges are likely integer-based. But it definitely is unintuitive.

1. Please refer to my earlier article about [Ranges and Intervals in Swift 2](https://oleb.net/blog/2015/09/swift-ranges-and-intervals/) to learn more about the distinction between ranges and intervals in Swift 2. [↩︎](#fnref:1)
2. In Swift 2, all ranges were technically half-open, even if they were created with the `...` operator. As a result, no range could contain a value like `Int.max`. The standard library used to have additional types, [`HalfOpenInterval`](http://swiftdoc.org/v2.2/type/HalfOpenInterval/) and [`ClosedInterval`](http://swiftdoc.org/v2.2/type/ClosedInterval/), to remedy this. They have been removed in Swift 3. [↩︎](#fnref:2)
