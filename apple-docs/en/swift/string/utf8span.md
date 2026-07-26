---
title: utf8Span
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/utf8span
source_url: 'https://developer.apple.com/documentation/swift/string/utf8span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/utf8span.json'
content_hash: 'sha256:3914b9b1548ad8f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# utf8Span

<sub>Instance Property</sub>

A UTF-8 span over the code units that make up this string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var utf8Span: UTF8Span { get }
```

## Return Value

A `UTF8Span` over the code units of this `String`.

## Discussion

> [!note] Note
> On Apple platforms, this property transcodes the code units of bridged UTF-16 `String` instances on first access and caches the result. Subsequent calls can reuse the cached buffer.

> [!abstract] Complexity
> O(1) for native UTF-8 strings, amortized O(1) for bridged UTF-16 strings.
