---
title: weight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/traitkey/weight
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/weight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/traitkey/weight.json'
content_hash: 'sha256:b516d4b7389ffbea'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [TraitKey](../traitkey.md)

# weight

<sub>Type Property</sub>

The numerical value that corresponds to a font face.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let weight: UIFontDescriptor.TraitKey
```

## Discussion

The value of this key is an [NSNumber](../../../foundation/nsnumber.md) object. The valid value range is from `-1.0` to `1.0`, where `0.0` corresponds to the [UIFontWeightRegular](../../uifont/weight/regular.md) weight constant. The negative side of the value range indicates that the font is light or thin; the positive side means the font is heavier or bolder. For example, the font face [UIFontWeightUltraLight](../../uifont/weight/ultralight.md) has the approximate value of `-0.8`, and [UIFontWeightBlack](../../uifont/weight/black.md) has the approximate value of `0.62`. When providing a weight that doesn’t precisely match a font face in the family, the system locates an available face that represents the closest match.

You can use a font face constant to specify a weight; for a list of constants, see [Weight](../../uifont/weight.md).

To access the weight of a font, first retrieve the font’s [UIFontDescriptorTraitsAttribute](../attributename/traits.md) dictionary information:

```swift
let font = UIFont.systemFont(ofSize: 21, weight: .bold)
if let traits = font.fontDescriptor.object(forKey: .traits) as? [UIFontDescriptor.TraitKey: Any]{
    let weightValue = traits[.weight]
}
```

## See Also

### Font traits

- [UIFontSlantTrait](slant.md) — The relative slant angle of the font.
- [UIFontSymbolicTrait](symbolic.md) — The symbolic font traits.
- [UIFontWidthTrait](width.md) — The inter-glyph spacing of the font.
