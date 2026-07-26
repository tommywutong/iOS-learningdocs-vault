---
title: foregroundColor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/foregroundcolor
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/foregroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/foregroundcolor.json'
content_hash: 'sha256:932bd22269645129'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# foregroundColor

<sub>Type Property</sub>

The color of the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let foregroundColor: NSAttributedString.Key
```

## Discussion

In macOS, the value of this attribute is an [NSColor](../../../appkit/nscolor.md) instance. In iOS, tvOS, watchOS, and Mac Catalyst, the value of this attribute is a [UIColor](../../../uikit/uicolor.md) instance. Use this attribute to specify the color of the text during rendering. If you don’t specify this attribute, the text renders in black.

## See Also

### Getting rendering attribute keys

- [backgroundColor](backgroundcolor.md) — The color of the background behind the text.
- [baselineOffset](baselineoffset.md) — The vertical offset for the position of the text.
- [font](font.md) — The font of the text.
- [glyphInfo](glyphinfo.md) — The name of a glyph info object.
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
