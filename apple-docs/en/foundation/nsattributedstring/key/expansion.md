---
title: expansion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/key/expansion
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/expansion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/expansion.json'
content_hash: 'sha256:447822e463e079a9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# expansion

<sub>Type Property</sub>

The expansion factor of the text.

> [!warning] Deprecated
> This attribute is not supported with TextKit 2

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let expansion: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing a floating point value indicating the log of the expansion factor to be applied to glyphs. The default value is `0`, indicating no expansion.

## See Also

### Deprecated Keys

- [obliqueness](obliqueness.md) — The obliqueness of the text. _(deprecated)_
- [verticalGlyphForm](verticalglyphform.md) — The vertical glyph form of the text. _(deprecated)_
- [characterShapeAttributeName](charactershapeattributename.md) — The character shape attribute. _(deprecated)_
- [usesScreenFontsDocumentAttribute](usesscreenfontsdocumentattribute.md) — The screen fonts attribute. _(deprecated)_
