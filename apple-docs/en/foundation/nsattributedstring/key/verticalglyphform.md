---
title: verticalGlyphForm
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/key/verticalglyphform
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/verticalglyphform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/verticalglyphform.json'
content_hash: 'sha256:86146c0060da3629'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# verticalGlyphForm

<sub>Type Property</sub>

The vertical glyph form of the text.

> [!warning] Deprecated
> This attribute is not supported with TextKit 2

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let verticalGlyphForm: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing an integer. The value `0` indicates horizontal text. The value `1` indicates vertical text. In iOS, horizontal text is always used and specifying a different value is undefined.

## See Also

### Deprecated Keys

- [expansion](expansion.md) — The expansion factor of the text. _(deprecated)_
- [obliqueness](obliqueness.md) — The obliqueness of the text. _(deprecated)_
- [characterShapeAttributeName](charactershapeattributename.md) — The character shape attribute. _(deprecated)_
- [usesScreenFontsDocumentAttribute](usesscreenfontsdocumentattribute.md) — The screen fonts attribute. _(deprecated)_
