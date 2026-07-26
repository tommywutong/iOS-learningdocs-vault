---
title: kCTLigatureAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctligatureattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctligatureattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctligatureattributename.json'
content_hash: 'sha256:8314b1a7e7a071ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTLigatureAttributeName

<sub>Global Variable</sub>

The type of ligatures to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTLigatureAttributeName: CFString
```

## Discussion

The value associated with this attribute must be a [CFNumber](../corefoundation/cfnumber.md) object. Default is an integer value of `1`. The ligature attribute determines what kinds of ligatures should be used when displaying the string. A value of `0` indicates that only ligatures essential for proper rendering of text should be used. A value of `1` indicates that standard ligatures should be used, and `2` indicates that all available ligatures should be used. Which ligatures are standard depends on the script and possibly the font. Arabic text, for example, requires ligatures for many character sequences but has a rich set of additional ligatures that combine characters. English text has no essential ligatures, and typically has only two standard ligatures, those for “fi” and “fl”—all others are considered more advanced or fancy.

## See Also

### Constants

- [kCTCharacterShapeAttributeName](kctcharactershapeattributename.md) — Controls glyph selection. _(deprecated)_
- [kCTFontAttributeName](kctfontattributename.md) — The font of the text to which this attribute applies.
- [kCTKernAttributeName](kctkernattributename.md) — The amount to kern the next character.
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
- [kCTBaselineOffsetAttributeName](kctbaselineoffsetattributename.md) — Vertical offset for text position.
