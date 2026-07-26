---
title: traitExpanded
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontsymbolictraits/traitexpanded
source_url: 'https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitexpanded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontsymbolictraits/traitexpanded.json'
content_hash: 'sha256:1c8acb58decd28d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontSymbolicTraits](../ctfontsymbolictraits.md)

# traitExpanded

<sub>Type Property</sub>

The font typestyle is expanded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var traitExpanded: CTFontSymbolicTraits { get }
```

## Discussion

> [!important] Important
> [kCTFontExpandedTrait](expandedtrait.md) and [kCTFontCondensedTrait](condensedtrait.md) are mutually exclusive.

## See Also

### Symbolic Traits

- [kCTFontTraitItalic](traititalic.md) — The font typestyle is italic.
- [kCTFontTraitBold](traitbold.md) — The font typestyle is boldface.
- [kCTFontTraitCondensed](traitcondensed.md) — The font typestyle is condensed.
- [kCTFontTraitMonoSpace](traitmonospace.md) — The font uses fixed-pitch glyphs if available.
- [kCTFontTraitVertical](traitvertical.md) — The font uses vertical glyph variants and metrics.
- [kCTFontTraitUIOptimized](traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [kCTFontTraitColorGlyphs](traitcolorglyphs.md) — The font contains color glyphs.
- [kCTFontTraitComposite](traitcomposite.md) — The font is in Composite Font Reference format.
- [kCTFontTraitClassMask](traitclassmask.md) — Mask for the font class.
