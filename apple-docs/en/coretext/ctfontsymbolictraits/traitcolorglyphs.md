---
title: traitColorGlyphs
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontsymbolictraits/traitcolorglyphs
source_url: 'https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitcolorglyphs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontsymbolictraits/traitcolorglyphs.json'
content_hash: 'sha256:f37d8c09a7d8436c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontSymbolicTraits](../ctfontsymbolictraits.md)

# traitColorGlyphs

<sub>Type Property</sub>

The font contains color glyphs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var traitColorGlyphs: CTFontSymbolicTraits { get }
```

## Discussion

Possible font tables that can contain color glyphs include ‘[sbix](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6sbix.html)’, ‘`COLR`’, and ‘`SVG_`’.

## See Also

### Symbolic Traits

- [kCTFontTraitItalic](traititalic.md) — The font typestyle is italic.
- [kCTFontTraitBold](traitbold.md) — The font typestyle is boldface.
- [kCTFontTraitExpanded](traitexpanded.md) — The font typestyle is expanded.
- [kCTFontTraitCondensed](traitcondensed.md) — The font typestyle is condensed.
- [kCTFontTraitMonoSpace](traitmonospace.md) — The font uses fixed-pitch glyphs if available.
- [kCTFontTraitVertical](traitvertical.md) — The font uses vertical glyph variants and metrics.
- [kCTFontTraitUIOptimized](traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [kCTFontTraitComposite](traitcomposite.md) — The font is in Composite Font Reference format.
- [kCTFontTraitClassMask](traitclassmask.md) — Mask for the font class.
