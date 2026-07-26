---
title: SizeDependentTextVariant
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sizedependenttextvariant
source_url: 'https://developer.apple.com/documentation/swiftui/sizedependenttextvariant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sizedependenttextvariant.json'
content_hash: 'sha256:fdf02960e9748799'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SizeDependentTextVariant

<sub>Structure</sub>

The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SizeDependentTextVariant
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TextVariantPreference](textvariantpreference.md)

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [DynamicTypeSize](dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](scaledmetric.md) — A dynamic property that scales a numeric value.
- [TextVariantPreference](textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
