---
title: UIFontDescriptor.Class
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/class
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/class.json'
content_hash: 'sha256:fc85e3811b2c79c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# UIFontDescriptor.Class

<sub>Type Alias</sub>

Constants that classify certain stylistic qualities of the font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
typealias Class = Int
```

## Discussion

These values correspond closely to the font class values in the OpenType OS/2 table. The class values are bundled in the upper four bits of the [SymbolicTraits](symbolictraits-swift.struct.md) and can be accessed through [UIFontDescriptorClassMask](symbolictraits-swift.struct/classmask.md). For additional information about the specific meaning of each identifier, refer to the OpenType specification.

## See Also

### Constants

- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
- [SystemDesign](systemdesign.md) — Constants that describe the system-defined typeface designs.
- [SymbolicTraits](symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [AttributeName](attributename.md) — Constants that describe font attributes.
- [FeatureKey](featurekey.md) — Keys for retrieving feature settings.
- [TraitKey](traitkey.md) — Keys for retrieving the font descriptor’s trait information.
- [Weight](../uifont/weight.md) — Constants that represent standard typeface styles.
- [Width](../uifont/width.md)
