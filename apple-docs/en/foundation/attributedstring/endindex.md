---
title: endIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/endindex
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/endindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/endindex.json'
content_hash: 'sha256:249f5657c6b531b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# endIndex

<sub>Instance Property</sub>

The string’s past-the-end position — the position one greater than the last valid subscript argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var endIndex: AttributedString.Index { get }
```

## Discussion

In an empty string, `endIndex` is equal to `startIndex`.
