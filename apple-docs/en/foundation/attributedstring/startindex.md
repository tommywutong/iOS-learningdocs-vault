---
title: startIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/startindex
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/startindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/startindex.json'
content_hash: 'sha256:3dd13d593381b143'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# startIndex

<sub>Instance Property</sub>

The position of the first character in a nonempty attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startIndex: AttributedString.Index { get }
```

## Discussion

In an empty string, `startIndex` is equal to `endIndex`.
