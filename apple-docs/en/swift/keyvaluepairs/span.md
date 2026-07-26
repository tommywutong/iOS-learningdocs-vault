---
title: span
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyvaluepairs/span
source_url: 'https://developer.apple.com/documentation/swift/keyvaluepairs/span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyvaluepairs/span.json'
content_hash: 'sha256:e4e18c84ff4cb435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyValuePairs](../keyvaluepairs.md)

# span

<sub>Instance Property</sub>

A span over the key-value pairs of this collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var span: Span<KeyValuePairs<Key, Value>.Element> { get }
```

## Return Value

A `Span` over the elements of this collection.

## Discussion

> [!abstract] Complexity
> O(1)
