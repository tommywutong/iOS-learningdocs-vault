---
title: useHangingPunctuation
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctlineboundsoptions/usehangingpunctuation
source_url: 'https://developer.apple.com/documentation/coretext/ctlineboundsoptions/usehangingpunctuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlineboundsoptions/usehangingpunctuation.json'
content_hash: 'sha256:fddc2a96e94950b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTLineBoundsOptions](../ctlineboundsoptions.md)

# useHangingPunctuation

<sub>Type Property</sub>

An option to enable hanging punctuation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var useHangingPunctuation: CTLineBoundsOptions { get }
```

## Discussion

The result of this option moves standard punctuation, such as periods, commas, hyphens, dashes, quotation marks, and asterisks, into the margin of either end of text, to give the appearance of a more uniform vertical alignment. Consider using this option when the text is fully justified.

## See Also

### Line Bounds Options

- [kCTLineBoundsExcludeTypographicLeading](excludetypographicleading.md) — An option to exclude typographic leading.
- [kCTLineBoundsExcludeTypographicShifts](excludetypographicshifts.md) — An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [kCTLineBoundsIncludeLanguageExtents](includelanguageextents.md) — An option to include additional space based on common glyph sequences for various languages.
- [kCTLineBoundsUseGlyphPathBounds](useglyphpathbounds.md) — An option to use glyph path bounds rather than the default typographic bounds.
- [kCTLineBoundsUseOpticalBounds](useopticalbounds.md) — An option to use optical bounds.
