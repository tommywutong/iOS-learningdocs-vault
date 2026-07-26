---
title: useOpticalBounds
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctlineboundsoptions/useopticalbounds
source_url: 'https://developer.apple.com/documentation/coretext/ctlineboundsoptions/useopticalbounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlineboundsoptions/useopticalbounds.json'
content_hash: 'sha256:df25d9de28a1c038'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTLineBoundsOptions](../ctlineboundsoptions.md)

# useOpticalBounds

<sub>Type Property</sub>

An option to use optical bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var useOpticalBounds: CTLineBoundsOptions { get }
```

## Discussion

This option overrides [kCTLineBoundsUseGlyphPathBounds](useglyphpathbounds.md).

## See Also

### Line Bounds Options

- [kCTLineBoundsExcludeTypographicLeading](excludetypographicleading.md) — An option to exclude typographic leading.
- [kCTLineBoundsExcludeTypographicShifts](excludetypographicshifts.md) — An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [kCTLineBoundsIncludeLanguageExtents](includelanguageextents.md) — An option to include additional space based on common glyph sequences for various languages.
- [kCTLineBoundsUseGlyphPathBounds](useglyphpathbounds.md) — An option to use glyph path bounds rather than the default typographic bounds.
- [kCTLineBoundsUseHangingPunctuation](usehangingpunctuation.md) — An option to enable hanging punctuation.
