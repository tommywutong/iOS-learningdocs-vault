---
title: traitLooseLeading
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/traitlooseleading
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/traitlooseleading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct/traitlooseleading.json'
content_hash: 'sha256:9866ccc082e863d2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [SymbolicTraits](../symbolictraits-swift.struct.md)

# traitLooseLeading

<sub>Type Property</sub>

The font uses a leading value that’s greater than the default.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var traitLooseLeading: UIFontDescriptor.SymbolicTraits { get }
```

## Discussion

For fonts that you create using [TextStyle](../../uifont/textstyle.md), loose leading adds 2 points to the current leading value.

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
- [UIFontDescriptorClassMask](classmask.md) — The font family class mask that you use to access font descriptor values.
- [UIFontDescriptorClassOldStyleSerifs](classoldstyleserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 15th to 17th centuries.
- [UIFontDescriptorClassTransitionalSerifs](classtransitionalserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 18th to 19th centuries.
- [UIFontDescriptorClassModernSerifs](classmodernserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 20th century.
- [UIFontDescriptorClassClarendonSerifs](classclarendonserifs.md) — The font’s characters include variations of old style and transitional serifs.
- [UIFontDescriptorClassSlabSerifs](classslabserifs.md) — The font’s characters use square transitions, without brackets, between strokes and serifs.
- [UIFontDescriptorClassFreeformSerifs](classfreeformserifs.md) — The font’s characters include serifs, and don’t generally fit within other serif design classifications.
