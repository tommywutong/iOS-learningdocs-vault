---
title: kCTParagraphStyleAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctparagraphstyleattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctparagraphstyleattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctparagraphstyleattributename.json'
content_hash: 'sha256:71f1dda95af23d8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTParagraphStyleAttributeName

<sub>Global Variable</sub>

The paragraph style of the text to which this attribute applies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTParagraphStyleAttributeName: CFString
```

## Discussion

A paragraph style object is used to specify things like line alignment, tab rulers, writing direction, and so on. Value must be a [CTParagraphStyle](ctparagraphstyle.md) object. Default is an empty [CTParagraphStyle](ctparagraphstyle.md) object.

## See Also

### Related Documentation

- [CTParagraphStyle](ctparagraphstyle.md) — Paragraph or ruler attributes in an attributed string.

### Constants

- [kCTCharacterShapeAttributeName](kctcharactershapeattributename.md) — Controls glyph selection. _(deprecated)_
- [kCTFontAttributeName](kctfontattributename.md) — The font of the text to which this attribute applies.
- [kCTKernAttributeName](kctkernattributename.md) — The amount to kern the next character.
- [kCTLigatureAttributeName](kctligatureattributename.md) — The type of ligatures to use.
- [kCTForegroundColorAttributeName](kctforegroundcolorattributename.md) — The foreground color of the text to which this attribute applies.
- [kCTForegroundColorFromContextAttributeName](kctforegroundcolorfromcontextattributename.md) — Sets a foreground color using the context’s fill color.
- [kCTStrokeWidthAttributeName](kctstrokewidthattributename.md) — The stroke width.
- [kCTStrokeColorAttributeName](kctstrokecolorattributename.md) — The stroke color.
- [kCTSuperscriptAttributeName](kctsuperscriptattributename.md) — Controls vertical text positioning.
- [kCTUnderlineColorAttributeName](kctunderlinecolorattributename.md) — The underline color.
- [kCTUnderlineStyleAttributeName](kctunderlinestyleattributename.md) — The style of underlining, to be applied at render time, for the text to which this attribute applies.
- [kCTVerticalFormsAttributeName](kctverticalformsattributename.md) — The orientation of the glyphs in the text to which this attribute applies.
- [kCTGlyphInfoAttributeName](kctglyphinfoattributename.md) — The glyph info object to apply to the text associated with this attribute.
- [kCTRunDelegateAttributeName](kctrundelegateattributename.md) — The run-delegate object to apply to an attribute range of the string.
- [kCTBaselineOffsetAttributeName](kctbaselineoffsetattributename.md) — Vertical offset for text position.
