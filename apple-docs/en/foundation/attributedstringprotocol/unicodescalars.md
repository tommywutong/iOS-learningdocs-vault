---
title: unicodeScalars
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringprotocol/unicodescalars
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/unicodescalars'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/unicodescalars.json'
content_hash: 'sha256:b533b7fc1566c033'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# unicodeScalars

<sub>Instance Property</sub>

The Unicode scalars of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unicodeScalars: AttributedString.UnicodeScalarView { get }
```

## Discussion

Use this property when you want to split the attributed string by Unicode scalar instead of grapheme cluster. This is useful when you need to carefully control insertion points or render the content.

You can also use this property to mutate the attributed string, using [RangeReplaceableCollection](../../swift/rangereplaceablecollection.md) methods, such as `insert(_:at:)` and [append(_:)](<../../swift/rangereplaceablecollection/append(__).md>). Inserted characters inherit any attributes present at the insertion point.

## See Also

### Accessing Views into the Attributed String

- [characters](characters.md) — The characters of the attributed string, as a view into the underlying string.
- [runs](runs.md) — The attributed runs of the attributed string, as a view into the underlying string.
