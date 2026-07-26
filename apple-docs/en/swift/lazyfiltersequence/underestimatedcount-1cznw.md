---
title: underestimatedCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazyfiltersequence/underestimatedcount-1cznw
source_url: 'https://developer.apple.com/documentation/swift/lazyfiltersequence/underestimatedcount-1cznw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazyfiltersequence/underestimatedcount-1cznw.json'
content_hash: 'sha256:ed53c9c9f93b3d7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazyFilterSequence](../lazyfiltersequence.md)

# underestimatedCount

<sub>Instance Property</sub>

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var underestimatedCount: Int { get }
```

## Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> [!abstract] Complexity
> O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.
