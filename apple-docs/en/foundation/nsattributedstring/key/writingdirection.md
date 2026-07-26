---
title: writingDirection
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/writingdirection
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/writingdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/writingdirection.json'
content_hash: 'sha256:ca1c84d3a3cd29ca'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# writingDirection

<sub>Type Property</sub>

The writing direction of the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let writingDirection: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSArray](../../nsarray.md) object containing [NSNumber](../../nsnumber.md) objects representing the nested levels of writing direction overrides, in order from outermost to innermost.

This attribute provides a means to override the default bidirectional text algorithm, equivalent to using the Unicode bidi control characters `LRE`, `RLE`, `LRO`, or `RLO` paired with `PDF`, but as a higher-level attribute. (See [Unicode Standard Annex #9](http://unicode.org/reports/tr9/) for information about the Unicode bidi formatting codes.) The `NSWritingDirectionAttributeName` constant is a character-level attribute that provides a higher-level alternative to the inclusion of explicit bidirectional control characters in text. It is the `NSAttributedString` equivalent of the HTML markup using `bdo` element with the `dir` attribute.

The values of the `NSNumber` objects should be `0`, `1`, `2`, or `3`, for `LRE`, `RLE`, `LRO`, or `RLO` respectively, and combinations of [NSWritingDirection.leftToRight](../../../appkit/nswritingdirection/lefttoright.md) and [NSWritingDirection.rightToLeft](../../../appkit/nswritingdirection/righttoleft.md) with [NSTextWritingDirectionEmbedding](../../../appkit/nstextwritingdirectionembedding.md) or `NSTextWritingDirectionOverride`, as shown in the following table.

| Array NSNumber Values | Unicode Control Characters | Writing Direction Constants |
|---|---|---|
| `0` | `LRE` | `NSWritingDirectionLeftToRight` \| `NSTextWritingDirectionEmbedding` |
| `1` | `RLE` | `NSWritingDirectionRightToLeft` \| `NSTextWritingDirectionEmbedding` |
| `2` | `LRO` | `NSWritingDirectionLeftToRight` \| `NSTextWritingDirectionOverride` |
| `3` | `RLO` | `NSWritingDirectionRightToLeft` \| `NSTextWritingDirectionOverride` |

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
