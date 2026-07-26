---
title: matrix
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/attributename/matrix
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename/matrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/attributename/matrix.json'
content_hash: 'sha256:8c5ca375f90d12d8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [AttributeName](../attributename.md)

# matrix

<sub>Type Property</sub>

The font’s transformation matrix attribute.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let matrix: UIFontDescriptor.AttributeName
```

## Discussion

The value is a [CGAffineTransform](../../../corefoundation/cgaffinetransform.md) instance that specifies the font’s transformation matrix. The default value is the identity matrix.

Because the system applies the matrix to the text matrix at rendering time, translation isn’t available. The rendering engine determines the translation independently.

## See Also

### Constants

- [UIFontDescriptorCascadeListAttribute](cascadelist.md) — The cascading list attribute.
- [UIFontDescriptorCharacterSetAttribute](characterset.md) — The character set attribute.
- [UIFontDescriptorFaceAttribute](face.md) — The font face attribute.
- [UIFontDescriptorFamilyAttribute](family.md) — The font family attribute.
- [UIFontDescriptorFeatureSettingsAttribute](featuresettings.md) — The font feature settings attribute.
- [UIFontDescriptorFixedAdvanceAttribute](fixedadvance.md) — The glyph advancement attribute.
- [UIFontDescriptorNameAttribute](name.md) — The font name attribute.
- [UIFontDescriptorSizeAttribute](size.md) — The font size attribute.
- [UIFontDescriptorTextStyleAttribute](textstyle.md) — The text style attribute.
- [UIFontDescriptorTraitsAttribute](traits.md) — The font traits dictionary attribute.
- [UIFontDescriptorVisibleNameAttribute](visiblename.md) — The font’s visible name attribute.
