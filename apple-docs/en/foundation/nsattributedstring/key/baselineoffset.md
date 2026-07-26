---
title: baselineOffset
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/baselineoffset
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/baselineoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/baselineoffset.json'
content_hash: 'sha256:0c1e23bb2f406fe5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# baselineOffset

<sub>Type Property</sub>

The vertical offset for the position of the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let baselineOffset: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing a floating point value indicating the character’s offset from the baseline, in points. The default value is `0`.

> [!important] Important
> This attribute is different from [kCTBaselineOffsetAttributeName](../../../coretext/kctbaselineoffsetattributename.md); you need to use [kCTBaselineOffsetAttributeName](../../../coretext/kctbaselineoffsetattributename.md) if you are writing code for [Core Text](../../../coretext.md).

## See Also

### Related Documentation

- [kCTBaselineOffsetAttributeName](../../../coretext/kctbaselineoffsetattributename.md) — Vertical offset for text position.

### Getting rendering attribute keys

- [backgroundColor](backgroundcolor.md) — The color of the background behind the text.
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
- [underlineStyle](underlinestyle.md) — The underline style of the text.
