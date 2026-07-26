---
title: slant
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/traitkey/slant
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/slant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/traitkey/slant.json'
content_hash: 'sha256:0d0d9979decfd4b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [TraitKey](../traitkey.md)

# slant

<sub>Type Property</sub>

The relative slant angle of the font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let slant: UIFontDescriptor.TraitKey
```

## Discussion

The value of this key is an [NSNumber](../../../foundation/nsnumber.md) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to `0` degree clockwise rotation from the vertical and `1.0` corresponds to `30` degrees clockwise rotation.

## See Also

### Font traits

- [UIFontSymbolicTrait](symbolic.md) — The symbolic font traits.
- [UIFontWeightTrait](weight.md) — The numerical value that corresponds to a font face.
- [UIFontWidthTrait](width.md) — The inter-glyph spacing of the font.
