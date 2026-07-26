---
title: hasPointerRepresentation
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticstring/haspointerrepresentation
source_url: 'https://developer.apple.com/documentation/swift/staticstring/haspointerrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticstring/haspointerrepresentation.json'
content_hash: 'sha256:80cab11227702fca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticString](../staticstring.md)

# hasPointerRepresentation

<sub>Instance Property</sub>

A Boolean value that indicates whether the static string stores a pointer to a null-terminated sequence of UTF-8 code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hasPointerRepresentation: Bool { get }
```

## Discussion

If `hasPointerRepresentation` is `false`, the static string stores a single Unicode scalar value.
