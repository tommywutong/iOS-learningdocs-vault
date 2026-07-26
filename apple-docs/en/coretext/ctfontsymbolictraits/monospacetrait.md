---
title: monoSpaceTrait
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coretext/ctfontsymbolictraits/monospacetrait
source_url: 'https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/monospacetrait'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontsymbolictraits/monospacetrait.json'
content_hash: 'sha256:addc739f4af0a8bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontSymbolicTraits](../ctfontsymbolictraits.md)

# monoSpaceTrait

<sub>Type Property</sub>

The font uses fixed-pitch glyphs if available.

> [!warning] Deprecated
> Use [kCTFontTraitMonoSpace](traitmonospace.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var monoSpaceTrait: CTFontSymbolicTraits { get }
```

## Discussion

The font may have multiple glyph advances (many CJK glyphs contain two spaces).

## See Also

### Deprecated Constants

- [kCTFontItalicTrait](italictrait.md) — The font typestyle is italic. _(deprecated)_
- [kCTFontBoldTrait](boldtrait.md) — The font typestyle is boldface. _(deprecated)_
- [kCTFontExpandedTrait](expandedtrait.md) — The font typestyle is expanded. _(deprecated)_
- [kCTFontCondensedTrait](condensedtrait.md) — The font typestyle is condensed. _(deprecated)_
- [kCTFontVerticalTrait](verticaltrait.md) — The font uses vertical glyph variants and metrics. _(deprecated)_
- [kCTFontUIOptimizedTrait](uioptimizedtrait.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary. _(deprecated)_
- [kCTFontColorGlyphsTrait](colorglyphstrait.md) — The font contains color glyphs. _(deprecated)_
- [kCTFontCompositeTrait](compositetrait.md) — The font is in Composite Font Reference format. _(deprecated)_
- [kCTFontClassMaskTrait](classmasktrait.md) — Mask for the font class. _(deprecated)_
