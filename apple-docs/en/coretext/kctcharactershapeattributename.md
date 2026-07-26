---
title: kCTCharacterShapeAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.11 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coretext/kctcharactershapeattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctcharactershapeattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctcharactershapeattributename.json'
content_hash: 'sha256:3a475f07e6fe611f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTCharacterShapeAttributeName

<sub>Global Variable</sub>

Controls glyph selection.

> [!warning] Deprecated
> Use feature type kCharacterShapeType with the appropriate selector

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTCharacterShapeAttributeName: CFString
```

## Discussion

Value must be a [CFNumber](../corefoundation/cfnumber.md) object. Default is value is `0` (disabled). A non-zero value is interpreted as Apple Type Services `kCharacterShapeType` selector `+ 1` (see `<ATS/SFNTLayoutTypes.h>` for selectors). For example, an attribute value of `1` corresponds to `kTraditionalCharactersSelector`.

## See Also

### Constants

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
- [kCTBaselineOffsetAttributeName](kctbaselineoffsetattributename.md) — Vertical offset for text position.
