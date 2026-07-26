---
title: characters
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/characters
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/characters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/characters.json'
content_hash: 'sha256:f9f8044070215de0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# characters

<sub>Instance Property</sub>

The characters of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var characters: AttributedString.CharacterView { get set }
```

## Discussion

Use the [characters](characters.md) view when you want to look for specific string content. You can then use the resulting ranges to set attributes for specific parts of the [AttributedString](../attributedstring.md).

You can also use this property to mutate the attributed string, using [RangeReplaceableCollection](../../swift/rangereplaceablecollection.md) methods, such as `insert(_:at:)` and [append(_:)](<../../swift/rangereplaceablecollection/append(__).md>). Inserted characters inherit any attributes present at the insertion point.

## See Also

### Accessing Views into the Attributed String

- [CharacterView](characterview.md) — A view into the underlying storage of the attributed string, as Unicode characters.
- [unicodeScalars](unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
- [UnicodeScalarView](unicodescalarview.md) — A view into the underlying storage of the attributed string, as Unicode scalars.
- [runs](runs-swift.property.md) — The attributed runs of the attributed string, as a view into the underlying string.
- [Runs](runs-swift.struct.md) — An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.
