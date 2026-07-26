---
title: 'max(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncthrowingdropwhilesequence/max(by:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence/max(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingdropwhilesequence/max%28by%3A%29.json'
content_hash: 'sha256:ee8a8edfa98a88c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingDropWhileSequence](../asyncthrowingdropwhilesequence.md)

# max(by:)

<sub>Instance Method</sub>

Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func max(by areInIncreasingOrder: (Self.Element, Self.Element) async throws -> Bool) async rethrows -> Self.Element?
```

## Parameters

- `areInIncreasingOrder` — A predicate that returns `true` if its first argument should be ordered before its second argument; otherwise, `false`.

## Return Value

The sequence’s minimum element, according to `areInIncreasingOrder`. If the sequence has no elements, returns `nil`.

## Discussion

Use this method when the asynchronous sequence’s values don’t conform to `Comparable`, or when you want to apply a custom ordering to the sequence.

The predicate must be a _strict weak ordering_ over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are _incomparable_ if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

The following example uses an enumeration of playing cards ranks, `Rank`, which ranges from `ace` (low) to `king` (high). An asynchronous sequence called `RankCounter` produces all elements of the array. The predicate provided to the `max(by:)` method sorts ranks based on their `rawValue`:

```swift
enum Rank: Int {
    case ace = 1, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
}

let max = await RankCounter()
    .max { $0.rawValue < $1.rawValue }
print(max ?? "none")
// Prints "king"
```
