---
title: classSymbolic
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/classsymbolic
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/classsymbolic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/classsymbolic.json'
content_hash: 'sha256:8aecb92ec0f8ebb8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [SymbolicTraits](../symbolictraits-swift.struct.md)

# classSymbolic

<sub>Type Property</sub>

The font’s characters consist mainly of symbols rather than letters and numbers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var classSymbolic: UIFontDescriptor.SymbolicTraits { get }
```

## Discussion

This trait is suitable for special characters like icons, dingbats, technical symbols, and others that work equally well with any font.

## See Also

### Font traits

- [UIFontDescriptorTraitItalic](traititalic.md) — The font’s style is italic.
- [UIFontDescriptorTraitBold](traitbold.md) — The font’s style is boldface.
- [UIFontDescriptorTraitExpanded](traitexpanded.md) — The font’s characters have an expanded width.
- [UIFontDescriptorTraitCondensed](traitcondensed.md) — The font’s characters have a condensed width.
- [UIFontDescriptorTraitMonoSpace](traitmonospace.md) — The font’s characters all have the same width.
- [UIFontDescriptorTraitVertical](traitvertical.md) — The font uses vertical glyph variants and metrics.
- [UIFontDescriptorTraitUIOptimized](traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as in control titles, if necessary.
- [UIFontDescriptorTraitTightLeading](traittightleading.md) — The font uses a leading value that’s less than the default.
- [UIFontDescriptorTraitLooseLeading](traitlooseleading.md) — The font uses a leading value that’s greater than the default.
- [UIFontDescriptorClassMask](classmask.md) — The font family class mask that you use to access font descriptor values.
- [UIFontDescriptorClassOldStyleSerifs](classoldstyleserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 15th to 17th centuries.
- [UIFontDescriptorClassTransitionalSerifs](classtransitionalserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 18th to 19th centuries.
- [UIFontDescriptorClassModernSerifs](classmodernserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 20th century.
- [UIFontDescriptorClassClarendonSerifs](classclarendonserifs.md) — The font’s characters include variations of old style and transitional serifs.
- [UIFontDescriptorClassSlabSerifs](classslabserifs.md) — The font’s characters use square transitions, without brackets, between strokes and serifs.
