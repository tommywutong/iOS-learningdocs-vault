---
title: mutableSpan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/contiguousarray/mutablespan
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/mutablespan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/mutablespan.json'
content_hash: 'sha256:3e231e0d613e67f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# mutableSpan

<sub>Instance Property</sub>

A mutable span over the elements of this array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableSpan: MutableSpan<Element> { mutating get }
```

## Return Value

A `MutableSpan` over the elements of this array.

## Discussion

> [!abstract] Complexity
> O(1) when the array’s storage is uniquely referenced, O(_n_) otherwise.
