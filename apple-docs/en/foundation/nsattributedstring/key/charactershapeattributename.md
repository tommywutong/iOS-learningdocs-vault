---
title: characterShapeAttributeName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsattributedstring/key/charactershapeattributename
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/charactershapeattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/charactershapeattributename.json'
content_hash: 'sha256:17ab8dbbf9688441'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# characterShapeAttributeName

<sub>Type Property</sub>

The character shape attribute.

> [!warning] Deprecated
> This attribute is bound to a specific implementation of ATS feature and not generically supported by wide range of fonts. The majority of characters accessed through this API are now encoded in the Unicode standard. Use the CTFont feature API for fine control over character shape choices.

<sub>macOS</sub>

```swift
static let characterShapeAttributeName: NSAttributedString.Key
```

## Discussion

An integer value. The value is interpreted as Apple Type Services `kCharacterShapeType selector + 1`.

The character shape feature type (`kCharacterShapeType`) is used when a single font contains different appearances for the same character shape, and these shapes are not traditionally treated as swashes. It is needed for languages such as Chinese that have both traditional and simplified character sets.

The default value is 0 (disable). 1 is `kTraditionalCharactersSelector,` and so on. Refer to `<ATS/SFNTLayoutTypes.h>` and Font Features in ATSUI Programming Guide for additional information.

## See Also

### Deprecated Keys

- [expansion](expansion.md) — The expansion factor of the text. _(deprecated)_
- [obliqueness](obliqueness.md) — The obliqueness of the text. _(deprecated)_
- [verticalGlyphForm](verticalglyphform.md) — The vertical glyph form of the text. _(deprecated)_
- [usesScreenFontsDocumentAttribute](usesscreenfontsdocumentattribute.md) — The screen fonts attribute. _(deprecated)_
