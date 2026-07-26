---
title: 'symmetricDifference(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangeset/symmetricdifference(_:)'
source_url: 'https://developer.apple.com/documentation/swift/rangeset/symmetricdifference(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangeset/symmetricdifference%28_%3A%29.json'
content_hash: 'sha256:6463407c6a5a259a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeSet](../rangeset.md)

# symmetricDifference(_:)

<sub>Instance Method</sub>

Returns a new range set representing the values in this range set or the given range set, but not both.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func symmetricDifference(_ other: RangeSet<Bound>) -> RangeSet<Bound>
```

## Parameters

- `other` — The range set to find a symmetric difference with.

## Return Value

A new range set.
