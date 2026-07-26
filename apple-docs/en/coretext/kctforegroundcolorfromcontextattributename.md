---
title: kCTForegroundColorFromContextAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctforegroundcolorfromcontextattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctforegroundcolorfromcontextattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctforegroundcolorfromcontextattributename.json'
content_hash: 'sha256:bf1ed71701f5a38b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTForegroundColorFromContextAttributeName

<sub>Global Variable</sub>

Sets a foreground color using the context’s fill color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTForegroundColorFromContextAttributeName: CFString
```

## Discussion

Value must be a [CFBoolean](../corefoundation/cfboolean.md) object. Default is [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md). The reason this exists is because an [NSAttributedString](../foundation/nsattributedstring.md) object defaults to a black color if no color attribute is set. This forces Core Text to set the color in the context. This attribute allows developers to sidestep this, making Core Text set nothing but font information in the [CGContext](../coregraphics/cgcontext.md). If set, this attribute also determines the color used by [kCTUnderlineStyleAttributeName](kctunderlinestyleattributename.md), in which case it overrides the foreground color.

## See Also

### Constants

- [kCTCharacterShapeAttributeName](kctcharactershapeattributename.md) — Controls glyph selection. _(deprecated)_
- [kCTFontAttributeName](kctfontattributename.md) — The font of the text to which this attribute applies.
- [kCTKernAttributeName](kctkernattributename.md) — The amount to kern the next character.
- [kCTLigatureAttributeName](kctligatureattributename.md) — The type of ligatures to use.
- [kCTForegroundColorAttributeName](kctforegroundcolorattributename.md) — The foreground color of the text to which this attribute applies.
- [kCTParagraphStyleAttributeName](kctparagraphstyleattributename.md) — The paragraph style of the text to which this attribute applies.
- [kCTStrokeWidthAttributeName](kctstrokewidthattributename.md) — The stroke width.
- [kCTStrokeColorAttributeName](kctstrokecolorattributename.md) — The stroke color.
- [kCTSuperscriptAttributeName](kctsuperscriptattributename.md) — Controls vertical text positioning.
- [kCTUnderlineColorAttributeName](kctunderlinecolorattributename.md) — The underline color.
- [kCTUnderlineStyleAttributeName](kctunderlinestyleattributename.md) — The style of underlining, to be applied at render time, for the text to which this attribute applies.
- [kCTVerticalFormsAttributeName](kctverticalformsattributename.md) — The orientation of the glyphs in the text to which this attribute applies.
- [kCTGlyphInfoAttributeName](kctglyphinfoattributename.md) — The glyph info object to apply to the text associated with this attribute.
- [kCTRunDelegateAttributeName](kctrundelegateattributename.md) — The run-delegate object to apply to an attribute range of the string.
- [kCTBaselineOffsetAttributeName](kctbaselineoffsetattributename.md) — Vertical offset for text position.
