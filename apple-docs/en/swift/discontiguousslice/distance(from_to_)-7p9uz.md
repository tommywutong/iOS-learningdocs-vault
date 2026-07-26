---
title: 'distance(from:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/discontiguousslice/distance(from:to:)-7p9uz'
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/distance(from:to:)-7p9uz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/distance%28from%3Ato%3A%29-7p9uz.json'
content_hash: 'sha256:00e8cb8143da8ba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

# distance(from:to:)

<sub>Instance Method</sub>

Returns the distance between two indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from start: Self.Index, to end: Self.Index) -> Int
```

## Parameters

- `start` — A valid index of the collection.

- `end` — Another valid index of the collection. If `end` is equal to `start`, the result is zero.

## Return Value

The distance between `start` and `end`. The result can be negative only if the collection conforms to the `BidirectionalCollection` protocol.

## Discussion

Unless the collection conforms to the `BidirectionalCollection` protocol, `start` must be less than or equal to `end`.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the resulting distance.
