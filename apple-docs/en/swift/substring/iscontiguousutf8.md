---
title: isContiguousUTF8
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/iscontiguousutf8
source_url: 'https://developer.apple.com/documentation/swift/substring/iscontiguousutf8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/iscontiguousutf8.json'
content_hash: 'sha256:9589dcc5a958c448'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# isContiguousUTF8

<sub>Instance Property</sub>

Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isContiguousUTF8: Bool { get }
```

## Discussion

Contiguous strings always operate in O(1) time for withUTF8, always give a result for Substring.UTF8View.withContiguousStorageIfAvailable, and always return a non-nil value from `Substring._utf8Span` and `Substring.UTF8View._span`. Contiguous strings also benefit from fast-paths and better optimizations.
