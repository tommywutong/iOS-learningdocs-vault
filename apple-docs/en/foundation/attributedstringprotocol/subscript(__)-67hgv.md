---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/subscript(_:)-67hgv'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(_:)-67hgv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/subscript%28_%3A%29-67hgv.json'
content_hash: 'sha256:53902d034bcddaf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a discontiguous substring of this attributed string using a set of ranges to indicate the discontiguous substring bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(indices: RangeSet<AttributedString.Index>) -> DiscontiguousAttributedSubstring { get }
```

## Parameters

- `indices` — A set of ranges that indicate the bounds of the discontiguous substring to return.
