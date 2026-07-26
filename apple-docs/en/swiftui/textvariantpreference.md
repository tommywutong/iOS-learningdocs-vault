---
title: TextVariantPreference
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textvariantpreference
source_url: 'https://developer.apple.com/documentation/swiftui/textvariantpreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textvariantpreference.json'
content_hash: 'sha256:8dd150990101967c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextVariantPreference

<sub>Protocol</sub>

A protocol for controlling the size variant of text views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TextVariantPreference
```

## Relationships

- **Conforming Types**: [FixedTextVariant](fixedtextvariant.md), [SizeDependentTextVariant](sizedependenttextvariant.md)

## Topics

### Type Properties

- [fixed](textvariantpreference/fixed.md) — The default text variant preference. It always chooses the largest available variant.
- [sizeDependent](textvariantpreference/sizedependent.md) — The size dependent preference allows the text to take the available space into account when choosing the size variant to display.

## See Also

### Adjusting text size

- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [DynamicTypeSize](dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](scaledmetric.md) — A dynamic property that scales a numeric value.
- [FixedTextVariant](fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
