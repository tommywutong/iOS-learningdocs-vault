---
title: 'filter(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/filter(_:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/filter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/filter%28_%3A%29.json'
content_hash: 'sha256:1913b1024f0cff5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# filter(_:)

<sub>Instance Method</sub>

Creates an asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func filter(_ isIncluded: @escaping @Sendable (Self.Element) async -> Bool) -> AsyncFilterSequence<Self>
```

## Parameters

- `isIncluded` — A closure that takes an element of the asynchronous sequence as its argument and returns a Boolean value that indicates whether to include the element in the filtered sequence.

## Return Value

An asynchronous sequence that contains, in order, the elements of the base sequence that satisfy the given predicate.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `filter(_:)` method returns `true` for even values and `false` for odd values, thereby filtering out the odd values:

```swift
let stream = Counter(howHigh: 10)
    .filter { $0 % 2 == 0 }
for await number in stream {
    print(number, terminator: " ")
}
// Prints "2 4 6 8 10 "
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
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [map(_:)](<map(__)-58nrv.md>) — Creates an asynchronous sequence that maps the given error-throwing closure over the asynchronous sequence’s elements.
- [map(_:)](<map(__)-4a4ju.md>) — Creates an asynchronous sequence that maps the given closure over the asynchronous sequence’s elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
