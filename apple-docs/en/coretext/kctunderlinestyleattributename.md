---
title: kCTUnderlineStyleAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctunderlinestyleattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctunderlinestyleattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctunderlinestyleattributename.json'
content_hash: 'sha256:4ebe60edae3d35d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTUnderlineStyleAttributeName

<sub>Global Variable</sub>

The style of underlining, to be applied at render time, for the text to which this attribute applies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTUnderlineStyleAttributeName: CFString
```

## Discussion

Value must be a [CFNumber](../corefoundation/cfnumber.md) object. Default is [kCTUnderlineStyleNone](ctunderlinestyle/kctunderlinestylenone.md). Set a value of something other than [kCTUnderlineStyleNone](ctunderlinestyle/kctunderlinestylenone.md) to draw an underline. In addition, the constants listed in  [CTUnderlineStyleModifiers](ctunderlinestylemodifiers.md) can be used to modify the look of the underline. The underline color is determined by the text’s foreground color.

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
- [kCTVerticalFormsAttributeName](kctverticalformsattributename.md) — The orientation of the glyphs in the text to which this attribute applies.
- [kCTGlyphInfoAttributeName](kctglyphinfoattributename.md) — The glyph info object to apply to the text associated with this attribute.
- [kCTRunDelegateAttributeName](kctrundelegateattributename.md) — The run-delegate object to apply to an attribute range of the string.
- [kCTBaselineOffsetAttributeName](kctbaselineoffsetattributename.md) — Vertical offset for text position.
