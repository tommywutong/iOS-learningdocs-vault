---
title: width
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/traitkey/width
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/width'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/traitkey/width.json'
content_hash: 'sha256:fa98cc61cf59bb7a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [TraitKey](../traitkey.md)

# width

<sub>Type Property</sub>

The inter-glyph spacing of the font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let width: UIFontDescriptor.TraitKey
```

## Discussion

The value of this key is an [NSNumber](../../../foundation/nsnumber.md) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to the regular glyph spacing.

## See Also

### Font traits

- [UIFontSlantTrait](slant.md) — The relative slant angle of the font.
- [UIFontSymbolicTrait](symbolic.md) — The symbolic font traits.
- [UIFontWeightTrait](weight.md) — The numerical value that corresponds to a font face.
