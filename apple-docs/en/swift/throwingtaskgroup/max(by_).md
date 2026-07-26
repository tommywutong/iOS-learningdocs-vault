---
title: 'max(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/max(by:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/max(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/max%28by%3A%29.json'
content_hash: 'sha256:57bc4ab964d0db22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

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

## See Also

### Accessing an Asynchronous Sequence of Results

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [compactMap(_:)](<compactmap(__)-944nh.md>) — Creates an asynchronous sequence that maps an error-throwing closure over the base sequence’s elements, omitting results that don’t return a value.
- [compactMap(_:)](<compactmap(__)-7mgi5.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements, omitting results that don’t return a value.
- [contains(_:)](<contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [drop(while:)](<drop(while_).md>) — Omits elements from the base asynchronous sequence until a given closure returns false, after which it passes through all remaining elements.
- [dropFirst(_:)](<dropfirst(__).md>) — Omits a specified number of elements from the base asynchronous sequence, then passes through all remaining elements.
- [filter(_:)](<filter(__).md>) — Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [map(_:)](<map(__)-58nrv.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-4a4ju.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
