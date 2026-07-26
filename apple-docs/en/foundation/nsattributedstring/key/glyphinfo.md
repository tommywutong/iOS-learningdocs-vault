---
title: glyphInfo
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/glyphinfo
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/glyphinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/glyphinfo.json'
content_hash: 'sha256:098e23172436a73b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# glyphInfo

<sub>Type Property</sub>

The name of a glyph info object.

<sub>macOS</sub>

```swift
static let glyphInfo: NSAttributedString.Key
```

## Discussion

The [NSLayoutManager](../../../appkit/nslayoutmanager.md) object assigns the glyph specified by this [NSGlyphInfo](../../../appkit/nsglyphinfo.md) object to the entire attribute range, provided that its contents match the specified base string, and that the specified glyph is available in the font specified by `NSFontAttributeName`.

## See Also

### Getting rendering attribute keys

- [backgroundColor](backgroundcolor.md) — The color of the background behind the text.
- [baselineOffset](baselineoffset.md) — The vertical offset for the position of the text.
- [font](font.md) — The font of the text.
- [foregroundColor](foregroundcolor.md) — The color of the text.
- [kern](kern.md) — The kerning of the text.
- [ligature](ligature.md) — The ligature of the text.
- [paragraphStyle](paragraphstyle.md) — The paragraph style of the text.
- [strikethroughColor](strikethroughcolor.md) — The color of the strikethrough.
- [strikethroughStyle](strikethroughstyle.md) — The strikethrough style of the text.
- [strokeColor](strokecolor.md) — The color of the stroke.
- [strokeWidth](strokewidth.md) — The width of the stroke.
- [superscript](superscript.md) — The superscript of the text.
- [tracking](tracking.md) — The amount to modify the default tracking.
- [underlineColor](underlinecolor.md) — The color of the underline.
- [underlineStyle](underlinestyle.md) — The underline style of the text.
