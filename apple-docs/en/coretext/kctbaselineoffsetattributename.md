---
title: kCTBaselineOffsetAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctbaselineoffsetattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctbaselineoffsetattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctbaselineoffsetattributename.json'
content_hash: 'sha256:d3775ddf34632d58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTBaselineOffsetAttributeName

<sub>Global Variable</sub>

Vertical offset for text position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTBaselineOffsetAttributeName: CFString
```

## Discussion

The value of this attribute must be a [CFNumber](../corefoundation/cfnumber.md) float. The default is standard positioning, following the baselines of the fonts used.

The baseline offset attribute indicates how many points the characters should be shifted perpendicular to their baseline. For horizontal text, a positive baseline value indicates a shift above the text baseline, and a negative baseline value indicates a shift below the text baseline. For vertical text, a positive baseline value indicates a shift to the right of the text baseline, and a negative baseline value indicates a shift to the left of the text baseline. If this value is set to `0.0`, no baseline shift will be performed.

> [!important] Important
> This attribute is different from [baselineOffset](../foundation/nsattributedstring/key/baselineoffset.md). If you are writing code for [TextKit](../appkit/textkit.md), you need to use [baselineOffset](../foundation/nsattributedstring/key/baselineoffset.md).

## See Also

### Constants

- [kCTCharacterShapeAttributeName](kctcharactershapeattributename.md) — Controls glyph selection. _(deprecated)_
- [kCTFontAttributeName](kctfontattributename.md) — The font of the text to which this attribute applies.
- [kCTKernAttributeName](kctkernattributename.md) — The amount to kern the next character.
- [kCTLigatureAttributeName](kctligatureattributename.md) — The type of ligatures to use.
- [kCTForegroundColorAttributeName](kctforegroundcolorattributename.md) — The foreground color of the text to which this attribute applies.
- [kCTForegroundColorFromContextAttributeName](kctforegroundcolorfromcontextattributename.md) — Sets a foreground color using the context’s fill color.
- [kCTParagraphStyleAttributeName](kctparagraphstyleattributename.md) — The paragraph style of the text to which this attribute applies.
- [kCTStrokeWidthAttributeName](kctstrokewidthattributename.md) — The stroke width.
- [kCTStrokeColorAttributeName](kctstrokecolorattributename.md) — The stroke color.
- [kCTSuperscriptAttributeName](kctsuperscriptattributename.md) — Controls vertical text positioning.
- [kCTUnderlineColorAttributeName](kctunderlinecolorattributename.md) — The underline color.
- [kCTUnderlineStyleAttributeName](kctunderlinestyleattributename.md) — The style of underlining, to be applied at render time, for the text to which this attribute applies.
- [kCTVerticalFormsAttributeName](kctverticalformsattributename.md) — The orientation of the glyphs in the text to which this attribute applies.
- [kCTGlyphInfoAttributeName](kctglyphinfoattributename.md) — The glyph info object to apply to the text associated with this attribute.
- [kCTRunDelegateAttributeName](kctrundelegateattributename.md) — The run-delegate object to apply to an attribute range of the string.
