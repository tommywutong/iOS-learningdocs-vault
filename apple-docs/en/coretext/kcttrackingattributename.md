---
title: kCTTrackingAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kcttrackingattributename
source_url: 'https://developer.apple.com/documentation/coretext/kcttrackingattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kcttrackingattributename.json'
content_hash: 'sha256:c112136d953aafa9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTTrackingAttributeName

<sub>Global Variable</sub>

The tracking for the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTTrackingAttributeName: CFString
```

## Discussion

The value associated with this attribute must be a [CFNumber](../corefoundation/cfnumber.md) float. The default is `0` (no tracking).

Tracking adds space, in points, between the specified [character cluster](https://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries). A positive value increases the spacing between characters, while a negative value brings the characters closer together. For example, setting [kCTTrackingAttributeName](kcttrackingattributename.md) to 0.1 adds 0.1 point of spacing between each character of the text.

The effect of this attribute is similar to [kCTKernAttributeName](kctkernattributename.md), but it treats tracking as trailing whitespace and a nonzero amount disables nonessential ligatures, unless overridden by the presence of [kCTLigatureAttributeName](kctligatureattributename.md).

> [!important] Important
> If you apply both [kCTTrackingAttributeName](kcttrackingattributename.md) and [kCTKernAttributeName](kctkernattributename.md), [kCTTrackingAttributeName](kcttrackingattributename.md) supersedes [kCTKernAttributeName](kctkernattributename.md).

## See Also

### Related Documentation

- [kCTKernAttributeName](kctkernattributename.md) — The amount to kern the next character.
- [kCTLigatureAttributeName](kctligatureattributename.md) — The type of ligatures to use.

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
