---
title: traitCondensed
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontsymbolictraits/traitcondensed
source_url: 'https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitcondensed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontsymbolictraits/traitcondensed.json'
content_hash: 'sha256:86d63ad077cc0247'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontSymbolicTraits](../ctfontsymbolictraits.md)

# traitCondensed

<sub>Type Property</sub>

The font typestyle is condensed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var traitCondensed: CTFontSymbolicTraits { get }
```

## Discussion

Additional detail is available via [kCTFontWidthTrait](../kctfontwidthtrait.md).

> [!important] Important
> [kCTFontExpandedTrait](expandedtrait.md) and [kCTFontCondensedTrait](condensedtrait.md) are mutually exclusive.

## See Also

### Related Documentation

- [kCTFontWidthTrait](../kctfontwidthtrait.md) — The normalized proportion (width condense or expand) trait from the font traits dictionary.

### Symbolic Traits

- [kCTFontTraitItalic](traititalic.md) — The font typestyle is italic.
- [kCTFontTraitBold](traitbold.md) — The font typestyle is boldface.
- [kCTFontTraitExpanded](traitexpanded.md) — The font typestyle is expanded.
- [kCTFontTraitMonoSpace](traitmonospace.md) — The font uses fixed-pitch glyphs if available.
- [kCTFontTraitVertical](traitvertical.md) — The font uses vertical glyph variants and metrics.
- [kCTFontTraitUIOptimized](traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [kCTFontTraitColorGlyphs](traitcolorglyphs.md) — The font contains color glyphs.
- [kCTFontTraitComposite](traitcomposite.md) — The font is in Composite Font Reference format.
- [kCTFontTraitClassMask](traitclassmask.md) — Mask for the font class.
