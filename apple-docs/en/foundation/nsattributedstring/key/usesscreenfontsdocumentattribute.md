---
title: usesScreenFontsDocumentAttribute
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.8+（10.11 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/key/usesscreenfontsdocumentattribute
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/usesscreenfontsdocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/usesscreenfontsdocumentattribute.json'
content_hash: 'sha256:bb30a17ee058ab8e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# usesScreenFontsDocumentAttribute

<sub>Type Property</sub>

The screen fonts attribute.

<sub>macOS</sub>

```swift
static let usesScreenFontsDocumentAttribute: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing a Boolean; this attribute corresponds to the [usesScreenFonts](../../../appkit/nslayoutmanager/usesscreenfonts.md) method of [NSLayoutManager](../../../appkit/nslayoutmanager.md); if absent, follows the system default setting.

## See Also

### Deprecated Keys

- [expansion](expansion.md) — The expansion factor of the text. _(deprecated)_
- [obliqueness](obliqueness.md) — The obliqueness of the text. _(deprecated)_
- [verticalGlyphForm](verticalglyphform.md) — The vertical glyph form of the text. _(deprecated)_
- [characterShapeAttributeName](charactershapeattributename.md) — The character shape attribute. _(deprecated)_
