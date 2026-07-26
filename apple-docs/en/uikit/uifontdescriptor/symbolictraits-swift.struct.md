---
title: UIFontDescriptor.SymbolicTraits
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/symbolictraits-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct.json'
content_hash: 'sha256:be1a10f9b43b9e7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# UIFontDescriptor.SymbolicTraits

<sub>Structure</sub>

Constants that describe the stylistic aspects of a font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct SymbolicTraits
```

## Overview

The lower 16 bits represent the typeface, and the upper 16 bits describe appearance of the font. The font appearance information represented by the upper 16 bits of [NSFontSymbolicTraits](../../appkit/nsfontsymbolictraits.md) can be used for stylistic font matching. [Class](class.md) constants classify certain stylistic qualities of the font.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Font traits

- [UIFontDescriptorTraitItalic](symbolictraits-swift.struct/traititalic.md) — The font’s style is italic.
- [UIFontDescriptorTraitBold](symbolictraits-swift.struct/traitbold.md) — The font’s style is boldface.
- [UIFontDescriptorTraitExpanded](symbolictraits-swift.struct/traitexpanded.md) — The font’s characters have an expanded width.
- [UIFontDescriptorTraitCondensed](symbolictraits-swift.struct/traitcondensed.md) — The font’s characters have a condensed width.
- [UIFontDescriptorTraitMonoSpace](symbolictraits-swift.struct/traitmonospace.md) — The font’s characters all have the same width.
- [UIFontDescriptorTraitVertical](symbolictraits-swift.struct/traitvertical.md) — The font uses vertical glyph variants and metrics.
- [UIFontDescriptorTraitUIOptimized](symbolictraits-swift.struct/traituioptimized.md) — The font synthesizes appropriate attributes for user interface rendering, such as in control titles, if necessary.
- [UIFontDescriptorTraitTightLeading](symbolictraits-swift.struct/traittightleading.md) — The font uses a leading value that’s less than the default.
- [UIFontDescriptorTraitLooseLeading](symbolictraits-swift.struct/traitlooseleading.md) — The font uses a leading value that’s greater than the default.
- [UIFontDescriptorClassMask](symbolictraits-swift.struct/classmask.md) — The font family class mask that you use to access font descriptor values.
- [UIFontDescriptorClassOldStyleSerifs](symbolictraits-swift.struct/classoldstyleserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 15th to 17th centuries.
- [UIFontDescriptorClassTransitionalSerifs](symbolictraits-swift.struct/classtransitionalserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 18th to 19th centuries.
- [UIFontDescriptorClassModernSerifs](symbolictraits-swift.struct/classmodernserifs.md) — The font’s characters include serifs, and reflect the Latin printing style of the 20th century.
- [UIFontDescriptorClassClarendonSerifs](symbolictraits-swift.struct/classclarendonserifs.md) — The font’s characters include variations of old style and transitional serifs.
- [UIFontDescriptorClassSlabSerifs](symbolictraits-swift.struct/classslabserifs.md) — The font’s characters use square transitions, without brackets, between strokes and serifs.
- [UIFontDescriptorClassFreeformSerifs](symbolictraits-swift.struct/classfreeformserifs.md) — The font’s characters include serifs, and don’t generally fit within other serif design classifications.
- [UIFontDescriptorClassSansSerif](symbolictraits-swift.struct/classsansserif.md) — The font’s characters don’t have serifs.
- [UIFontDescriptorClassOrnamentals](symbolictraits-swift.struct/classornamentals.md) — The font’s characters use highly decorated or stylized character shapes.
- [UIFontDescriptorClassScripts](symbolictraits-swift.struct/classscripts.md) — The font’s characters simulate handwriting.
- [UIFontDescriptorClassSymbolic](symbolictraits-swift.struct/classsymbolic.md) — The font’s characters consist mainly of symbols rather than letters and numbers.

### Initializer

- [init(rawValue:)](<symbolictraits-swift.struct/init(rawvalue_).md>) — Creates a symbol traits structure with the specified raw value.

## See Also

### Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Adding a custom font to your app](../adding-a-custom-font-to-your-app.md) — Add a custom font to your app and use it in your app’s interface.
- [UIFont](../uifont.md) — An object that provides access to the font’s characteristics.
- [UIFontDescriptor](../uifontdescriptor.md) — A collection of attributes that describes a font.
- [UIFontMetrics](../uifontmetrics.md) — A utility object for obtaining custom fonts that scale to support Dynamic Type.
