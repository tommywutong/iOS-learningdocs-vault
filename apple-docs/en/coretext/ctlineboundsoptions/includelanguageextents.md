---
title: includeLanguageExtents
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctlineboundsoptions/includelanguageextents
source_url: 'https://developer.apple.com/documentation/coretext/ctlineboundsoptions/includelanguageextents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlineboundsoptions/includelanguageextents.json'
content_hash: 'sha256:cb6ac9f19bf548e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTLineBoundsOptions](../ctlineboundsoptions.md)

# includeLanguageExtents

<sub>Type Property</sub>

An option to include additional space based on common glyph sequences for various languages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var includeLanguageExtents: CTLineBoundsOptions { get }
```

## Discussion

Use the result of this option when drawing to avoid clipping that the typographic bounds may cause. This option doesn’t have an effect when you use it with [kCTLineBoundsUseGlyphPathBounds](useglyphpathbounds.md).

## See Also

### Line Bounds Options

- [kCTLineBoundsExcludeTypographicLeading](excludetypographicleading.md) — An option to exclude typographic leading.
- [kCTLineBoundsExcludeTypographicShifts](excludetypographicshifts.md) — An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [kCTLineBoundsUseGlyphPathBounds](useglyphpathbounds.md) — An option to use glyph path bounds rather than the default typographic bounds.
- [kCTLineBoundsUseHangingPunctuation](usehangingpunctuation.md) — An option to enable hanging punctuation.
- [kCTLineBoundsUseOpticalBounds](useopticalbounds.md) — An option to use optical bounds.
