---
title: mutableSpan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquearray/mutablespan
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/mutablespan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/mutablespan.json'
content_hash: 'sha256:d3fe99fc9ce45a1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# mutableSpan

<sub>Instance Property</sub>

A mutable span over the elements of this array, providing direct mutating access.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mutableSpan: MutableSpan<Element> { mutating get }
```

## Discussion

> [!abstract] Complexity
> O(1)
