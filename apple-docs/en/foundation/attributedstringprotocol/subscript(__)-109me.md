---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/subscript(_:)-109me'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(_:)-109me'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/subscript%28_%3A%29-109me.json'
content_hash: 'sha256:573a5188cda02ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a substring of the attributed string using a range to indicate the substring bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<R>(bounds: R) -> AttributedSubstring where R : RangeExpression, R.Bound == AttributedString.Index { get }
```

## Default Implementations

### AttributedStringProtocol Implementations

- [subscript(_:)](<subscript(__)-67hgv.md>) — Returns a discontiguous substring of this attributed string using a set of ranges to indicate the discontiguous substring bounds.
