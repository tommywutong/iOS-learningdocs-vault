---
title: max()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncthrowingstream/max()
source_url: 'https://developer.apple.com/documentation/swift/asyncthrowingstream/max()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncthrowingstream/max%28%29.json'
content_hash: 'sha256:77dbc50f68947712'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncThrowingStream](../asyncthrowingstream.md)

# max()

<sub>Instance Method</sub>

Returns the maximum element in an asynchronous sequence of comparable elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func max() async rethrows -> Self.Element?
```

## Return Value

The sequence’s maximum element. If the sequence has no elements, returns `nil`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `max()` method returns the max value of the sequence.

```swift
let max = await Counter(howHigh: 10)
    .max()
print(max ?? "none")
// Prints "10"
```

## See Also

### Finding Elements

- [contains(_:)](<contains(__).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.
- [contains(where:)](<contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
