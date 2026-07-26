---
title: characters
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringprotocol/characters
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/characters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/characters.json'
content_hash: 'sha256:3c03315162d08ea0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# characters

<sub>Instance Property</sub>

The characters of the attributed string, as a view into the underlying string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var characters: AttributedString.CharacterView { get }
```

## Discussion

Use the [characters](characters.md) view when you want to look for specific string content. You can then use the resulting ranges to set attributes for specific parts of the [AttributedString](../attributedstring.md) or [AttributedSubstring](../attributedsubstring.md).

You can also use this property to mutate the attributed string, using [RangeReplaceableCollection](../../swift/rangereplaceablecollection.md) methods, such as `insert(_:at:)` and [append(_:)](<../../swift/rangereplaceablecollection/append(__).md>). Inserted characters inherit any attributes present at the insertion point.

## See Also

### Accessing Views into the Attributed String

- [unicodeScalars](unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
- [runs](runs.md) — The attributed runs of the attributed string, as a view into the underlying string.
