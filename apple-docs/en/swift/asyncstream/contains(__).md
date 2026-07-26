---
title: 'contains(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/asyncstream/contains(_:)'
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/contains%28_%3A%29.json'
content_hash: 'sha256:aeb5c19cd09e9b7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AsyncStream](../asyncstream.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the asynchronous sequence contains the given element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ search: Self.Element) async rethrows -> Bool
```

## Parameters

- `search` — The element to find in the asynchronous sequence.

## Return Value

`true` if the method found the element in the asynchronous sequence; otherwise, `false`.

## Discussion

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `contains(_:)` method checks to see whether the sequence produces the value `5`:

```swift
let containsFive = await Counter(howHigh: 10)
    .contains(5)
print(containsFive)
// Prints "true"
```

## See Also

### Finding Elements

- [contains(where:)](<contains(where_).md>) — Returns a Boolean value that indicates whether the asynchronous sequence contains an element that satisfies the given predicate.
- [allSatisfy(_:)](<allsatisfy(__).md>) — Returns a Boolean value that indicates whether all elements produced by the asynchronous sequence satisfy the given predicate.
- [first(where:)](<first(where_).md>) — Returns the first element of the sequence that satisfies the given predicate.
- [min()](<min().md>) — Returns the minimum element in an asynchronous sequence of comparable elements.
- [min(by:)](<min(by_).md>) — Returns the minimum element in the asynchronous sequence, using the given predicate as the comparison between elements.
- [max()](<max().md>) — Returns the maximum element in an asynchronous sequence of comparable elements.
- [max(by:)](<max(by_).md>) — Returns the maximum element in the asynchronous sequence, using the given predicate as the comparison between elements.
