---
title: underlineStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/underlinestyle
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/underlinestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/underlinestyle.json'
content_hash: 'sha256:9845788433959fe3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# underlineStyle

<sub>Type Property</sub>

The underline style of the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let underlineStyle: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing an integer. This value indicates whether the text is underlined and corresponds to one of the constants described in [NSUnderlineStyle](../../../uikit/nsunderlinestyle.md). The default value for this attribute is [NSUnderlineStyleNone](../../../uikit/nsunderlinestyle/nsunderlinestylenone.md).

## See Also

### Getting rendering attribute keys

- [backgroundColor](backgroundcolor.md) — The color of the background behind the text.
- [baselineOffset](baselineoffset.md) — The vertical offset for the position of the text.
- [font](font.md) — The font of the text.
- [foregroundColor](foregroundcolor.md) — The color of the text.
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
