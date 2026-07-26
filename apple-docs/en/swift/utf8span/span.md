---
title: span
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/span
source_url: 'https://developer.apple.com/documentation/swift/utf8span/span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/span.json'
content_hash: 'sha256:3dc66e97a4798d59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# span

<sub>Instance Property</sub>

A span used to access the code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var span: Span<UInt8> { get }
```

## Return Value

A `Span` over the UTF-8 code units of this `UTF8Span`.

## Discussion

> [!abstract] Complexity
> O(1)
