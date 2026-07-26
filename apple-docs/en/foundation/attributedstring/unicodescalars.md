---
title: unicodeScalars
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/unicodescalars
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/unicodescalars'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/unicodescalars.json'
content_hash: 'sha256:aee5b1b68fddc275'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# unicodeScalars

<sub>Instance Property</sub>

The Unicode scalars of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unicodeScalars: AttributedString.UnicodeScalarView { get set }
```

## Discussion

Use this property when you want to split the attributed string by Unicode scalar instead of grapheme cluster. This is useful when you need to carefully control insertion points or render the content.

You can also use this property to mutate the attributed string, using [RangeReplaceableCollection](../../swift/rangereplaceablecollection.md) methods, such as `insert(_:at:)` and [append(_:)](<../../swift/rangereplaceablecollection/append(__).md>). Inserted characters inherit any attributes present at the insertion point.

## See Also

### Accessing Views into the Attributed String

- [characters](characters.md) — The characters of the attributed string, as a view into the underlying string.
- [CharacterView](characterview.md) — A view into the underlying storage of the attributed string, as Unicode characters.
- [UnicodeScalarView](unicodescalarview.md) — A view into the underlying storage of the attributed string, as Unicode scalars.
- [runs](runs-swift.property.md) — The attributed runs of the attributed string, as a view into the underlying string.
- [Runs](runs-swift.struct.md) — An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
