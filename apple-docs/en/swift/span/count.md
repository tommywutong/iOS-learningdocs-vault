---
title: count
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/span/count
source_url: 'https://developer.apple.com/documentation/swift/span/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span/count.json'
content_hash: 'sha256:b85de6691e4a8878'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Span](../span.md)

# count

<sub>Instance Property</sub>

The number of elements in the span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get }
```

## Discussion

To check whether the span is empty, use its `isEmpty` property instead of comparing `count` to zero.

> [!abstract] Complexity
> O(1)
