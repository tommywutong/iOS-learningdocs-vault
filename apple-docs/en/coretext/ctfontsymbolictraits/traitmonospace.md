---
title: traitMonoSpace
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontsymbolictraits/traitmonospace
source_url: 'https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitmonospace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontsymbolictraits/traitmonospace.json'
content_hash: 'sha256:e9c9faadf85500a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontSymbolicTraits](../ctfontsymbolictraits.md)

# traitMonoSpace

<sub>Type Property</sub>

The font uses fixed-pitch glyphs if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var traitMonoSpace: CTFontSymbolicTraits { get }
```

## Discussion

The font may have multiple glyph advances (many CJK glyphs contain two spaces).

## See Also

### Symbolic Traits

- [kCTFontTraitItalic](traititalic.md) — The font typestyle is italic.
- [kCTFontTraitBold](traitbold.md) — The font typestyle is boldface.
- [kCTFontTraitExpanded](traitexpanded.md) — The font typestyle is expanded.
- [kCTFontTraitCondensed](traitcondensed.md) — The font typestyle is condensed.
- [kCTFontTraitVertical](traitvertical.md) — The font uses vertical glyph variants and metrics.
- [kCTFontTraitUIOptimized](traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [kCTFontTraitColorGlyphs](traitcolorglyphs.md) — The font contains color glyphs.
- [kCTFontTraitComposite](traitcomposite.md) — The font is in Composite Font Reference format.
- [kCTFontTraitClassMask](traitclassmask.md) — Mask for the font class.
