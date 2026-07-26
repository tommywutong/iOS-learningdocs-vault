---
title: UIFontDescriptor.TraitKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 4.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/traitkey
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/traitkey.json'
content_hash: 'sha256:0f1a703337a4ac21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# UIFontDescriptor.TraitKey

<sub>Structure</sub>

Keys for retrieving the font descriptor’s trait information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct TraitKey
```

## Overview

Use these keys to fetch values from the dictionary associated with the [UIFontDescriptorTraitsAttribute](attributename/traits.md) key.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Font traits

- [UIFontSlantTrait](traitkey/slant.md) — The relative slant angle of the font.
- [UIFontSymbolicTrait](traitkey/symbolic.md) — The symbolic font traits.
- [UIFontWeightTrait](traitkey/weight.md) — The numerical value that corresponds to a font face.
- [UIFontWidthTrait](traitkey/width.md) — The inter-glyph spacing of the font.

### Initializer

- [init(rawValue:)](<traitkey/init(rawvalue_).md>) — Creates a font trait key with the specified raw value.

## See Also

### Constants

- [TextStyle](../uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
- [SystemDesign](systemdesign.md) — Constants that describe the system-defined typeface designs.
- [SymbolicTraits](symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [Class](class.md) — Constants that classify certain stylistic qualities of the font.
- [AttributeName](attributename.md) — Constants that describe font attributes.
- [FeatureKey](featurekey.md) — Keys for retrieving feature settings.
- [Weight](../uifont/weight.md) — Constants that represent standard typeface styles.
- [Width](../uifont/width.md)
